## Para iniciar o sistema siga os passos abaixo:

Obs.: O nome do sistema é Heliot acrônimo para Heterogeneity less in IoT - obviamente é um nome muito ambicioso para o que o sistema se propõe mas ficou um nome legal...

    Abrir o prompt de comando e entrar na pasta C:\Angular\heliot digitar ng serve

    Abrir outro prompt entrar na pasta C:\Program Files\MongoDB\Server\4.4\bin digitar mongod --dbpath C:\javamongodb\data

    Abrir outro prompt e digitar C:\Program Files\MongoDB\Server\4.4\bin executar o comando mongo

    Executar o sistema heliot2 que fará a ligação do frontend com o backend no eclipse. Para isso procure a classe Application e clique com o botão direito run as Java Application. Para visualizar a página web acesse: http://localhost:4200/agentlogs


![Heliot](https://user-images.githubusercontent.com/9336800/144471224-c600bb23-588a-45ab-ac01-8ac3d4a06500.png)


    Logar nas vms: vm1: 177.104.61.126 em que está o servidor LoRA para geração de dados em formato base64

    comandos necessários: sudo su

    cd /home/ubuntu/lorac

    docker-compose up -d

    root@sense:/home/ubuntu/lorac# docker ps

![LoRa](https://user-images.githubusercontent.com/9336800/144471314-82250427-aaee-4928-9d99-356e2434df43.png)


vm2: 177.104.61.27 em que estão os IoT Agents LoRa, UL, Json, XML, etc

comandos necessários: sudo su

cd /home/ubuntu/testes/swamp-iot-agent

docker-compose up -d

root@renatoteste:/home/ubuntu/testes/swamp-iot-agent# docker ps

![IoTAgents](https://user-images.githubusercontent.com/9336800/144471368-8e257800-52f1-48de-8851-f270377b03a3.png)


    Executar o IoT Redirector. Entre no projeto paho-publish-subscribe-master e procure a classe Subscriber e execute como java application. Ao executar uma mensagem será mostrada: Subscriber is now listening to #

    Executar o Node-Red para simulação via docker. O fluxo utilizado pode ser encontrado em https://github.com/renatobdo/mestrado/blob/defesa/flows.json

    Estava utilizando o zabbix e o google para realizar o monitoramento, porém estou analisando o grafana: http://177.104.61.27:3003/login


# Arquitetura dos testes

![ArquiteturaDosTestes](https://user-images.githubusercontent.com/9336800/122453049-4d9f9680-cf80-11eb-88ac-abeacc6a8611.png)

São utilizadas 2 máquinas virtuais:
vm2: 177.104.61.27 em que estão os IoT Agents LoRa, UL, Json, XML, etc

docker-compose.yml está em https://github.com/renatobdo/heliot/blob/master/docker-compose.yml_vm1

vm1: 177.104.61.126 em que está o servidor LoRA para geração de dados em formato base64

docker-compose.yml https://github.com/renatobdo/heliot/blob/master/docker-compose.yml_vm3

2 notebooks foram utilizados um com Ubuntu e outro com o Windows 10. No Ubuntu foi instalado o Node-Red e no Windows 10 o Iot Redirector e o Heliot.


## Cenário dos testes

https://docs.google.com/spreadsheets/d/1NVP1pvPBCw29xQ5PDzMr0tMPG5Xhfww95qH1ZccwvqY/edit?usp=sharing

https://docs.google.com/spreadsheets/d/105WulcEI_N9G7DqwXDJvnhXg6a3PEYmjO1qWytULM5Q/edit#gid=0

## Passos para executar os testes

1) É necessário possuir os fluxos para geração dos dados: https://github.com/renatobdo/heliot/blob/master/flows.json
Os dados são de temperatura obtidos de uma API do openweather https://openweathermap.org/api
A partir desse dados de temperatura são gerados dados em diversos formatos: JSON, XML, HTML, UL, LoRa, etc.

2) Executar o software SenSE simultaneamento com o Node-Red. O SenSE pode ser baixado do seguinte endereço: https://github.com/ivanzy/SenSE-Sensor-Simulation-Environment 

Comando utilizado com 50 sensores em um tempo de 8 horas e 20s de envio entre cada dado.

java -jar SenSE.jar -sensor 50 -rep 1 -time 30000 - p 20 -h tcp://177.104.61.126:1883 -sensorType lora -temp -netkey 9c698235533b8865900aee3558dfc47b -appkey b73485bb9c5e29a2c8b6a330f0bf2ed3 -mac 000000ffff001000 -devAddress 00fb0bc1

Para um teste manual pode ser utilizado um publish via mosquitto. Eu estou usando a vm3 177.104.61.119 que possui o mosquitto:

mosquitto_pub -h 177.104.61.126 -t "application/5/device/221597e4529df57d/rx" -m "{\"applicationID\":\"5\",\"applicationName\":\"application\",\"deviceName\":\"device\",\"devEUI\":\"221597e4529df57d\",\"txInfo\":{\"frequency\":868300000,\"dr\":1},\"adr\":false,\"fCnt\":0,\"fPort\":1,\"data\":\"dHN8MTYyMjAzOTA1MDk4MQ==\"}"
ts|1622039050981 = dHN8MTYyMjAzOTA1MDk4MQ==

mosquitto_pub -h 177.104.61.126 -t "application/5/device/221597e4529df57d/rx" -m "{\ "applicationID\ ":\ "5\ ",\ "applicationName\ ":\ "application\ ",\ "deviceName\ ":\ "device\ ",\ "devEUI\ ":\ "221597e4529df57d\ ",\ "txInfo\ ":{\ "frequency\ ":868300000,\ "dr\ ":1},\ "adr\ ":false,\ "fCnt\ ":0,\ "fPort\ ":1,\ "data\ ":\ "dHN8MTYyMjAzOTA1MDk4MQ==\ "}"

ou

mosquitto_pub -h 177.104.61.27 -t "application/5/device/221597e4529df57d/rx" -m "{\"applicationID\":\"5\",\"applicationName\":\"application\",\"deviceName\":\"device\",\"devEUI\":\"221597e4529df57d\",\"txInfo\":{\"frequency\":868300000,\"dr\":1},\"adr\":false,\"fCnt\":0,\"fPort\":1,\"data\":\"dHN8MTYyMjAzOTA1MDY4MQ==\"}"
ts|1622039050681 = dHN8MTYyMjAzOTA1MDY4MQ==

obs.: Não se esqueça de retirar os espaços entre a barra e as aspas duplas

mosquitto_pub -h 177.104.61.27 -t "application/5/device/221597e4529df57d/rx" -m "{\ "applicationID\ ":\ "5\ ",\ "applicationName\ ":\ "application\ ",\ "deviceName\ ":\ "device\ ",\ "devEUI\ ":\ "221597e4529df57d\ ",\ "txInfo\ ":{\ "frequency\ ":868300000,\ "dr\ ":1},\ "adr\ ":false,\ "fCnt\ ":0,\ "fPort\ ":1,\ "data\ ":\ "dHN8MTYyMjAzOTA1MDY4MQ==\ "}"

mosquitto_sub -t "#" -h "177.104.61.121"
mosquitto_pub -h localhost -t test -m "hello world"
mosquitto_sub -h localhost -t test


3) Verificar os logs no frontend do Heliot ou no MongoDB Compass.

4) API para visualizar os dados notificados no ORION:
http://177.104.61.121:8080/ 
docker run -d -p 8080:3000 renatobdo/mestrado:api
