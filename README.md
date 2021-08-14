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

* CrateDB
http://177.104.61.27:4200/
https://crate.io/docs/crate/tutorials/en/latest/generate-time-series/cli.html

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

* Fiware
https://fiware-tutorials.readthedocs.io/en/latest/time-series-data.html

* Grafana
https://grafana.com/
http://177.104.61.27:3003/login


## Para iniciar o sistema siga os passos abaixo:

1) Abrir o prompt de comando e entrar na pasta C:\Angular\heliot digitar ng serve

2) Abrir outro prompt entrar na pasta C:\Program Files\MongoDB\Server\4.4\bin digitar mongod --dbpath C:\javamongodb\data

3) Abrir outro prompt e digitar C:\Program Files\MongoDB\Server\4.4\bin executar o comando mongo

4) Executar o sistema heliot2 que fará a ligação do frontend com o backend no eclipse. Para isso procure a classe Application e clique com o botão direito run as Java Application. Para visualizar a página web acesse: http://localhost:4200/agentlogs

![Heliot](https://user-images.githubusercontent.com/9336800/126373749-b9eebe64-8561-47ae-a9ca-8f4a88b932c4.png)



5) Logar nas vms: 
 vm1: 177.104.61.126 em que está o servidor LoRA para geração de dados em formato base64
 
    comandos necessários: sudo su
    
    cd /home/ubuntu/lorac
    
    docker-compose up -d
    
    root@sense:/home/ubuntu/lorac# docker ps
    
    
![dockerPS](https://user-images.githubusercontent.com/9336800/126373347-31cad8a8-75ab-4147-862c-fb34bb68d39b.png)



 vm2: 177.104.61.27 em que estão os IoT Agents LoRa, UL, Json, XML, etc
 
   comandos necessários: sudo su
   
   cd /home/ubuntu/testes/swamp-iot-agent
   
   docker-compose up -d
   
   root@renatoteste:/home/ubuntu/testes/swamp-iot-agent# docker ps
   
   
![dockerPS2](https://user-images.githubusercontent.com/9336800/126373445-f6c9e7de-338e-45b0-9b24-ba2872bceda1.png)


6) Executar o IoT Redirector. Entre no projeto paho-publish-subscribe-master e procure a classe Subscriber e execute como java application. Ao executar uma mensagem será mostrada: Subscriber is now listening to #

7) Executar o Node-Red para simulação via docker. O fluxo utilizado pode ser encontrado em https://github.com/renatobdo/mestrado/blob/defesa/flows.json

8) Estava utilizando o zabbix e o google para realizar o monitoramento, porém estou analisando o grafana: http://177.104.61.27:3003/login

# Diagrama de Classes
https://viewer.diagrams.net/?highlight=0000ff&edit=_blank&layers=1&nav=1&title=RedirecionadorUML#R7Vxtb9s2EP41ArYPKSRRku2PsduuHdItaDKs%2FTQwNm1plUSPopO4v36kSFpvlO3EopUEAoLAPJ1eeM8dj3c80gKz5PE3AtfhF7xAseXai0cLvLdcdxyM2X9O2AoCmABBWJFoIUhOQbiJfiJJtCV1Ey1QVmGkGMc0WleJc5ymaE4rNEgIfqiyLXFcfesarlCDcDOHcZP6d7SgoeyWbxf0TyhaherNji2v3MH5jxXBm1S%2BL8UpElcSqB4jWbMQLvBDiQQ%2BWGBGMKbiV%2FI4QzGXqpKYuO9jy9XdJxOU0mNuCGcX3%2F9ZeGhyje3b%2B4SG2Wp0EaiPo1slC7RgopFNTGiIVziF8YeCOs37i%2FhjbdYqeK4wXjOiw4j%2FIkq3Eme4oZiRQprE8mpGIaGXHDdGmMcwy6K5In%2BMYsWG0oViyuWaU%2BR1%2FuYFzML8Mziz6Af%2F%2BFb5SFKGN2SO9giFc%2BUqCMkK0T2MfrDDkVkGwgmiZMtuJCiGNLqvfgmUOrra8RVgsR8Srydgpz7zHsYb%2BaoblGaYfPty1UA1e4iSGOZCXOKUKoC55GAcrVIOBBMUIoxwjwiNmHFcyguUwzqdh1G8uIJbvOEiYVjNf6jWNMQk%2BskeCysIS%2FzdoMJxw%2B%2BUCBKUMZ5rhZFTI32BjxXGK5hRSZjjOIbrLLrbdSNhaEXpFFOKE8kk5cO6gx73a0UTQ3kDkAYiBzbHC0T7oRgmHGXhYWmIGAemUAcN1C13yrUVJWtEIN0QaIFLPgrGGNKGIjBR0Bwggn%2BgGY4xKcxryWyrRlLKEaMlbVWNbA3nUbq6ynneewXlqxQIJ2F2L%2Fskbs1htFigNB9JKKRQYMgBW%2BMopbnE%2FCn7Y3Kd2e98y2cfPmNtp2izP85O6AynrC8wyuFETEEeEFeS47DfY1dNjZAq4B6pAa4xDfA0GlBDOY5y9ATKyqU5z4I4YWDlw77E9DYf5C%2BcBu6giTvQYBzDOxRf4yyiEebPJ4K3hn1v8PrukQZuCl2%2Fxb6XmLC5DyLXcMsMe%2FHLrzspDNbdHfxqQtSfdQctXv3T7Qtz6%2FYrdutOUPXru0ikjDvwNWZvm8J9NPh1w5bfMltXKnCkBpiz%2FPHg183Bq5u4aw3cFLqTwa%2F3CL%2Fv9WzdXtOYz5BpYTIj22%2F8fgaAbH6Xj8sb7x8rra1sVTI0dzHmrr2Sn7GPyM9Y3aVkgMoKHkrJgLFeDY5OyeS3sm7BbYlBanjx5GtOKKYT9TSBPynry0F2Z2zv5Qcjfx8%2F%2ByE%2BuNDOXc9PUNhRHwr7ahXPA29Q8fzxafxuAMwrqt%2FzyFoeV50D42reukYkYp3mQdnrHmy9yRvU%2BcA%2Bjd%2B13TPoPOhV552yzpemFm9tNuG%2BxUHd8ffyG1JYf5hNKMU7VZ8OasAum6UeIRRd3lVA3a1imlEcZauNfKg1c63L5vJ1S0YUDBnR%2FRlRtxZiaLJhI00e3FGrUZ0HzKBtIYTfxfOgTDXRiuE45EqemitpG4b2ZEJ12BvLlTi2LhXKsU9hggT6N5Qw8Q%2Fgdw2%2BLk96VvCB24L9mokTs%2BEQDwpgUgFGbt8KoKtwGdZBOoJ3Mj4OXlPoBjq3HsS8zxH7sRKdb18YEazs1SVu%2FRBQigOOVYF89tVqrxwzHmNkYrrntA0zxrBzbM0qhtY2Ta1SO3YvWeFKpWclqJMi3xPTqbDPXFAnLepgNiHotVwUNOdUIpD6%2FebPP44No4Z60UP1ok49FNetO5%2BzYBS0LTwPhSVdedyWNcc9BaM6DTC39GwPEypz8OoKRrUGbgrdZoJsKCw5H%2Fy6gtHzWnczXBJ%2B%2Fa%2BXVS76mr26V1sy0abIzroNxNNtAhi8eod231bQ8VK2gXi6QHrw6h3B2%2Fc2EK%2B5DWDw6ueDv%2FdtIF5btH6Fv8LBr3fk14PG9k4N7r5u2dNxTQE%2FhOumTf%2Fp4bpOBYyZvj%2BE6wbh1Tl2HbymHLs%2FhOt9WrfOsZ%2FVuoO20oY5TvP%2BkinMUOAx%2FAfwOwZ%2F3PfQHjgNUM%2B8CWhklavV3znOodrdwxXrh5fgiiNeikW4xrKekEwnK3K%2BxO9wfW9PBeyjyqzTs89QgKvW%2FV%2Fh%2FrPnrvH2rl6T0YnqddpMo5lCYMJhzqOhCEP4%2BMzwsRo9gpFmchGcMyvsNw8RuBhCx%2B7mF20Hfu0JHXX4mwsdhyMEDMKrCx215m0K3T1HCCRMkEPkaBJ9XeR4VuMOdEsCohxyXcE6%2BG%2FDD5WUTk%2BM%2BPb60XKF27MF%2FSLHkF%2FzSte4mlxI8Pk16fd3zyyKLhs1mwFMuFLEzdZn%2FowlZJMqRa7eUnlitbRT0O5Ig6IIszhK4OX159Ltd3VmRlvXaSHhMlMnkaruOe09fZaMhfnshNx8NufFa5Q%2BIEhDPsEqlbbv67%2BuS2a%2B8LgvqI02%2BvGiNqiURoZlPmsXs09ZXevK9keYRDG3wU8ovkf8qdUQoxqj7E5ZFfPAhEedhW%2BZ7o5rrQ13dW94%2BtwQ1HdZHrmpRtE6Hz4mmgOm%2BBa6abSzTtacHmNzX3n8wubsWG90NV0oYdWBXMfVfWreRCNXRyNX35hcJ40ev%2FCK6LZ0TDlYB2OrkiiyC8JTEkVWh1G31N%2FDpxKY2WQLamdbgCM32XaVwNmdOd1fBsdzK0rxHIUwobe9KNmptfzPyhz6Tm30s8%2BwA9ux%2B85adzQYvRXdC04946rF37FmcRy90J7itH%2Fw4X8%3D

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




