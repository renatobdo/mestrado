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

C:\Program Files\MongoDB\Server\4.4\bin>mongod --dbpath C:\javamongodb\data
Caso não consiga clicar com o botão direito do mouse no relógio e em gerenciador de tarefas. Clicar na aba serviços e procurar pelo MongoDb. Iniciá-lo.
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

http://177.104.61.27:81/

8) Configurar um item para monitorar Zabbix:
https://www.zabbix.com/documentation/4.4/manual/config/hosts/host#configuration


# Passos para realização dos testes:

1) Verificar se todos os containeres estão no ar nas vms da UFABC: 
 
Comando executado para subir os containeres: docker-compose up -d
Comando executado para parar os containeres: docker-compose stop
Comando executado para restartar os containeres: docker-compose restart

vm1: 177.104.61.27 
- usada para os IoT Agents XML, JSON, LoRa, UL, etc. Para visualizar o docker-compose.yml acesse: https://github.com/renatobdo/heliot/blob/master/docker-compose.yml_vm1

vm2: 177.104.61.119 - usada para realizar testes manuais em que consigo executar um publish no mosquitto

Comando manual que pode ser executado para um teste simples na vm2: 

mosquitto_pub -h 177.104.61.27 -t "application/5/device/221597e4529df57d/rx" -m "{\"applicationID\":\"5\",\"applicationName\":\"application\",\"deviceName\":\"device\",\"devEUI\":\"221597e4529df57d\",\"txInfo\":{\"frequency\":868300000,\"dr\":1},\"adr\":false,\"fCnt\":0,\"fPort\":1,\"data\":\"dHN8MTYyMjAzOTA1MDk4MQ==\"}"
ts|1622039050981 = dHN8MTYyMjAzOTA1MDk4MQ== 

ou

mosquitto_pub -h 177.104.61.126 -t "application/5/device/221597e4529df57d/rx" -m "{\"applicationID\":\"5\",\"applicationName\":\"application\",\"deviceName\":\"device\",\"devEUI\":\"221597e4529df57d\",\"txInfo\":{\"frequency\":868300000,\"dr\":1},\"adr\":false,\"fCnt\":0,\"fPort\":1,\"data\":\"dHN8MTYyMjAzOTA1MDk4MQ==\"}"
ts|1622039050981 = dHN8MTYyMjAzOTA1MDk4MQ==

vm3: 177.104.61.126 - usada pelo servidor LoRa. https://github.com/renatobdo/heliot/blob/master/docker-compose.yml_vm3

Comando para o executar senSE com 50 sensores, durante 180s e intervalo de 20s entre os envios de dados. Isso dentro da pasta home/ubuntu/SENSE:

java -jar SenSE.jar -sensor 50 -rep 1 -time 180 - p 20 -h tcp://177.104.61.126:1883 -sensorType lora -temp -netkey 9c698235533b8865900aee3558dfc47b -appkey b73485bb9c5e29a2c8b6a330f0bf2ed3 -mac 000000ffff001000 -devAddress 00fb0bc1

2) Verificar se o NODE-Red está no ar. No caso estou executando no meu notebook via docker com o Ubuntu. Para visualizar todo o fluxo:
https://github.com/renatobdo/node-red/blob/master/flow_defesa_mestrado
para realizar a importação para o node-red siga os passos em: https://nodered.org/docs/user-guide/editor/workspace/import-export
Para executar o NODE-Red via docker: https://nodered.org/docs/getting-started/docker

3) Verificar se o software que chamei de Heliot está rodando. (Veja os passos 1 a 4 dos Passos para iniciar o sistema)

4) Verificar os logs. 
