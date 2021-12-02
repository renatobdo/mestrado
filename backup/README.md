Para iniciar o sistema siga os passos abaixo:

Obs.: O nome do sistema é Heliot acrônimo para Heterogeneity less in IoT - obviamente é um nome muito ambicioso para o que o sistema se propõe mas ficou um nome legal...

    Abrir o prompt de comando e entrar na pasta C:\Angular\heliot digitar ng serve

    Abrir outro prompt entrar na pasta C:\Program Files\MongoDB\Server\4.4\bin digitar mongod --dbpath C:\javamongodb\data

    Abrir outro prompt e digitar C:\Program Files\MongoDB\Server\4.4\bin executar o comando mongo

    Executar o sistema heliot2 que fará a ligação do frontend com o backend no eclipse. Para isso procure a classe Application e clique com o botão direito run as Java Application. Para visualizar a página web acesse: http://localhost:4200/agentlogs

Heliot

    Logar nas vms: vm1: 177.104.61.126 em que está o servidor LoRA para geração de dados em formato base64

    comandos necessários: sudo su

    cd /home/ubuntu/lorac

    docker-compose up -d

    root@sense:/home/ubuntu/lorac# docker ps

dockerPS

vm2: 177.104.61.27 em que estão os IoT Agents LoRa, UL, Json, XML, etc

comandos necessários: sudo su

cd /home/ubuntu/testes/swamp-iot-agent

docker-compose up -d

root@renatoteste:/home/ubuntu/testes/swamp-iot-agent# docker ps

dockerPS2

    Executar o IoT Redirector. Entre no projeto paho-publish-subscribe-master e procure a classe Subscriber e execute como java application. Ao executar uma mensagem será mostrada: Subscriber is now listening to #

    Executar o Node-Red para simulação via docker. O fluxo utilizado pode ser encontrado em https://github.com/renatobdo/mestrado/blob/defesa/flows.json

    Estava utilizando o zabbix e o google para realizar o monitoramento, porém estou analisando o grafana: http://177.104.61.27:3003/login

