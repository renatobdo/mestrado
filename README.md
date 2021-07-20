# Heliot - Heterogeneity less in IoT

Bem vindo ao sistema para redução da heterogeneidade de dados em aplicações IoT. Esse sistema foi desenvolvido como dissertação de mestrado em ciência da computação na UFABC

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

4) Executar o sistema heliot2 que fará a ligação do frontend com o backend no eclipse. Para isso procure a classe Application e clique com o botão direito run as Java Application. Para visualizar a página web acesse: http://localhost:4200/agentlogs

5) Logar nas vms: 
 vm1: 177.104.61.126 em que está o servidor LoRA para geração de dados em formato base64
   # comandos necessários: sudo su
    cd /home/ubuntu/lorac
    docker-compose up -d
    root@sense:/home/ubuntu/lorac# docker ps
CONTAINER ID        IMAGE                              COMMAND                  CREATED             STATUS              PORTS                    NAMES
3ff37b3d2e87        loraserver/lora-geo-server:2       "./lora-geo-server"      3 months ago        Up 6 days                                    lorac_geoserver_1
e4b6b319ea97        redis:4-alpine                     "docker-entrypoint.s…"   3 months ago        Up 6 days           0.0.0.0:6379->6379/tcp   lorac_redis_1
d6abfabd879f        postgres:9.6-alpine                "docker-entrypoint.s…"   3 months ago        Up 6 days           5432/tcp                 lorac_postgresql_1
96933d9dd73b        loraserver/lora-gateway-bridge:2   "./lora-gateway-brid…"   3 months ago        Up 6 days           0.0.0.0:1700->1700/udp   lorac_gatewaybridge_1
e022bfce1f59        loraserver/lora-app-server:2       "./lora-app-server"      3 months ago        Up 6 days           0.0.0.0:8080->8080/tcp   lorac_appserver_1
cc902af52bd0        loraserver/loraserver:2            "./loraserver"           3 months ago        Up 6 days                                    lorac_loraserver_1

 vm2: 177.104.61.27 em que estão os IoT Agents LoRa, UL, Json, XML, etc
   # comandos necessários: sudo su
   cd /home/ubuntu/testes/swamp-iot-agent
   docker-compose up -d
   root@renatoteste:/home/ubuntu/testes/swamp-iot-agent# docker ps
CONTAINER ID        IMAGE                                    COMMAND                  CREATED             STATUS                      PORTS                                                                NAMES
37f8a860c2f3        grafana/grafana                          "/run.sh"                25 minutes ago      Up 24 minutes               0.0.0.0:3003->3000/tcp                                               swamp-iot-agent_grafana_1_2c7200c2ef30
5a2f1dafcd36        smartsdk/quantumleap                     "/bin/sh -c 'python …"   25 minutes ago      Up 24 minutes               0.0.0.0:8668->8668/tcp                                               fiware-quantum-leap
cc46f3e9d9ba        fiware/cygnus-ngsi:latest                "/cygnus-entrypoint.…"   25 minutes ago      Up 24 minutes               0.0.0.0:5050->5050/tcp, 0.0.0.0:5080->5080/tcp                       fiware-cygnus
4ceea007e45d        fiware/iotagent-ul:1.16.0-distroless     "/nodejs/bin/node ./…"   25 minutes ago      Up 24 minutes (healthy)     4061/tcp, 0.0.0.0:4043->4043/tcp, 0.0.0.0:7898->7898/tcp, 7896/tcp   fiware-iot-agentul
0bdcb19edcb4        fiware/orion:2.0.0                       "/usr/bin/contextBro…"   25 minutes ago      Up 24 minutes               0.0.0.0:1026->1026/tcp                                               fiware-orion
eb68b129d7c3        fiware/iotagent-json:1.17.0-distroless   "/nodejs/bin/node ./…"   25 minutes ago      Up 24 minutes (healthy)     4041/tcp, 0.0.0.0:4042->4042/tcp, 7896/tcp, 0.0.0.0:7897->7897/tcp   fiware-iot-agentjson
b7e5064e3050        fiware/iotagent-xml                      "docker-entrypoint.s…"   25 minutes ago      Up 24 minutes (unhealthy)   0.0.0.0:4041->4041/tcp, 0.0.0.0:7896->7896/tcp                       fiware-iot-agentxml
a749154ed156        crate/crate                              "/docker-entrypoint.…"   25 minutes ago      Up 24 minutes               0.0.0.0:4200->4200/tcp, 0.0.0.0:4300->4300/tcp, 5432/tcp             db-crate
7f32810fc644        swamp-iot-agent_iot-agent                "docker-entrypoint.s…"   25 minutes ago      Up 24 minutes               0.0.0.0:3456->3456/tcp                                               iot-agent-lora
3299f1055ecb        eclipse-mosquitto                        "/docker-entrypoint.…"   25 minutes ago      Up 25 minutes               0.0.0.0:1883->1883/tcp, 0.0.0.0:9001->9001/tcp                       mosquitto
4dbf02524085        mongo:3.6                                "docker-entrypoint.s…"   25 minutes ago      Up 25 minutes               0.0.0.0:27017->27017/tcp                                             db-mongo


6) Executar o IoT Redirector. Entre no projeto paho-publish-subscribe-master e procure a classe Subscriber e execute como java application. Ao executar uma mensagem será mostrada: Subscriber is now listening to #

7) Executar o Node-Red para simulação via docker. O fluxo utilizado pode ser encontrado em 

8) Estava utilizando o zabbix e o google para realizar o monitoramento, porém estou analisando o grafana: http://177.104.61.27:3003/login


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

3) Verificar os logs no frontend do Heliot ou no MongoDB Compass.




