# heliot - Heterogeneity less in IoT
Redução da heterogeneidade em IoT

Esse sistema está sendo desenvolvido como trabalho de mestrado em ciência da computação - UFABC.

# Ferramentas utilizadas

- Node js
- Angular
- Java
- MongoDb
- Zabbix para monitoramento: 
https://github.com/zabbix/zabbix-docker
https://www.zabbix.com/documentation/4.4/manual/quickstart/host

- Docker: https://docs.docker.com/get-started/
- Docker compose
- FIWARE

# Passos para iniciar o sistema

1) Abrir o prompt de comando e executar o NodeJs:
cd C:\Angular\heliot
ng serve

2) Em outro prompt executar o mongodb:

//executa o servidor mongodb

C:\Program Files\MongoDB\Server\4.4\bin>mongod

//executa o cliente do mongo e permite que digitemos comandos:

C:\Program Files\MongoDB\Server\4.4\bin>mongo

3) Abrir o Eclipse e procurar pelo projeto heliot2

4) Clicar com o botão direito do mouse em Application e em run as java aplication

5) Para visualizar a aplicação no browser digitar:
http://localhost:4200/agentlogs

Link com tutorial https://www.javaguides.net/2020/07/spring-boot-angular-10-crud-example-tutorial.html

6) Iniciar o Zabbix:
https://www.zabbix.com/documentation/3.4/manual/installation/containers
Se der pau no docker executar docker-machine restart

Dentro do docker 
docker run --name zabbix-appliance -t \
      -p 10051:10051 \
      -p 81:80 \
      -d zabbix/zabbix-appliance:latest

7) Executar o Zabbix no seguinte endereço:
http://192.168.99.100:81/ 
Usuário Admin
Senha zabbix


