# Heliot - Heterogeneity less in IoT

Bem vindo ao sistema para redução da heterogeneidade de dados em aplicações IoT. Esse sistema foi desenvolvido como tese de mestrado em ciência da computação na UFABC

## Ferramentas necessárias:

* Java
https://www.javaguides.net/2019/12/spring-boot-angular-mongodb-crud-example-tutorial.html
https://www.javaguides.net/2019/12/spring-boot-mongodb-crud-example-tutorial.html
https://www.javaguides.net/2020/06/free-spring-boot-angular-open-source-projects-github.html

* Mongodb

* Mongodb Compass
https://www.mongodb.com/products/compass

* Nodejs

* Angular

* Node-Red
https://nodered.org/docs/getting-started/docker

* Docker
https://docs.docker.com/engine/install/ubuntu/

* Docker-compose
https://docs.docker.com/compose/install/

* Eclipse

* Postman
https://www.postman.com/

## Para iniciar o sistema siga os passos abaixo:

1) Abrir o prompt de comando e entrar na pasta C:\Angular\heliot digitar ng serve

2) Abrir outro prompt entrar na pasta C:\Program Files\MongoDB\Server\4.4\bin digitar mongod --dbpath C:\javamongodb\data

3) Abrir outro prompt e digitar C:\Program Files\MongoDB\Server\4.4\bin executar o comando mongo

4) Executar o sistema heliot2 que fará a ligação do frontend com o backend no eclipse. Para isso procure a classe Application e clique com o botão direito run as Java Application

5) Executar o IoT Redirector. Entre no projeto paho-publish-subscribe-master e procure a classe Subscriber e execute como java application. Ao executar uma mensagem será mostrada: Subscriber is now listening to #

6) Executar o Node-Red para simulação via docker. O fluxo utilizado pode ser encontrado em 

7) Estava utilizando o zabbix e o google para realizar o monitoramento, porém estou analisando o grafana


# Arquitetura dos testes

![ArquiteturaDosTestes](https://user-images.githubusercontent.com/9336800/122453049-4d9f9680-cf80-11eb-88ac-abeacc6a8611.png)

São utilizadas 2 máquinas virtuais:
vm1: 177.104.61.27 em que estão os IoT Agents LoRa, UL, Json, XML, etc
vm2: 177.104.61.126 em que está o servidor LoRA para geração de dados em formato base64

2 notebooks foram utilizados um com Ubuntu e outro com o Windows 10. No Ubuntu foi instalado o Node-Red e no Windows 10 o Iot Redirector e o Heliot.

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

ou

mosquitto_pub -h 177.104.61.27 -t "application/5/device/221597e4529df57d/rx" -m "{\"applicationID\":\"5\",\"applicationName\":\"application\",\"deviceName\":\"device\",\"devEUI\":\"221597e4529df57d\",\"txInfo\":{\"frequency\":868300000,\"dr\":1},\"adr\":false,\"fCnt\":0,\"fPort\":1,\"data\":\"dHN8MTYyMjAzOTA1MDY4MQ==\"}"
ts|1622039050681 = dHN8MTYyMjAzOTA1MDY4MQ==

3) Verificar os logs no frontend do Heliot ou no MongoDB Compass.




