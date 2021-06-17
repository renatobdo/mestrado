# Bem vindo ao sistema para redução da heterogeneidade de dados em aplicações IoT.

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
