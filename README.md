# Gerenciamento de dados heterogêneos para aplicações IoT

   Bem vindo ao sistema para gerenciamento de dados de sensores heterogêneos. O objetivo desse sistema é simular o envio de dados através de diversos sensores de ambientes IoT, analisar o conteúdo/assinatura da mensagem, filtrá-la e redirecioná-la para um Iot Agent responsável pelo seu processamento. Um Agente genérico (redirecionador) é capaz de entender o dado com aplicação de filtros podendo encaminhar esse dado de forma inteligente. A diminuição da heterogeneidade em aplicações baseada em sensores IoT seria uma das consequências possibilitando maior integração e interoperabilidade entre sistemas. Desenvolvido como dissertação de mestrado em ciência da computação da Universidade Federal do ABC - UFABC com orientação do professor Dr. Carlos Alberto Kamienski.

![RedirecionadorUML-Fluxograma - visão geral](https://user-images.githubusercontent.com/9336800/130318257-c049071a-a01c-427f-8f97-8fb306f4c0bb.jpg)

## Palavras-chave: 
MQTT, REST, padrão publish/subscribe, FIWARE, IoT Agent, Interoperabilidade, Heterogeneidade

## Ferramentas necessárias:

Front end: 

* Angular: https://www.javaguides.net/2020/06/free-spring-boot-angular-open-source-projects-github.html

* Nodejs: https://www.youtube.com/watch?v=q-lUgFxwjEM
* http://177.104.61.121:8081/

Back end:

* Java
https://www.javaguides.net/2019/12/spring-boot-angular-mongodb-crud-example-tutorial.html
https://www.javaguides.net/2019/12/spring-boot-mongodb-crud-example-tutorial.html

* Maven
https://maven.apache.org/download.cgi
https://maven.apache.org/install.html

* Simulador SenSE
https://github.com/ivanzy/SenSE-Sensor-Simulation-Environment

Banco de dados:

* Mongodb

* Mongodb Compass
https://www.mongodb.com/products/compass

* CrateDB
http://177.104.61.121:4200/
https://crate.io/docs/crate/tutorials/en/latest/generate-time-series/cli.html

IDE

* Eclipse ou Visual Studio Code

* Postman
https://www.postman.com/


Infraestrutura

* Docker
https://docs.docker.com/engine/install/ubuntu/

* Docker-compose
https://docs.docker.com/compose/install/

* Node-Red
https://nodered.org/docs/getting-started/docker

* Fiware
https://fiware-tutorials.readthedocs.io/en/latest/time-series-data.html

* Grafana
https://grafana.com/
http://177.104.61.27:3003/login

Sistemas Operacionais:

* Ubuntu

* Windows 10


# Arquitetura do sistema

![ArquiteturaDosTestes](https://user-images.githubusercontent.com/9336800/122453049-4d9f9680-cf80-11eb-88ac-abeacc6a8611.png)

São utilizadas 4 máquinas virtuais:

![2021-12-02 (25)](https://user-images.githubusercontent.com/9336800/144474057-1c936918-f8dd-455f-8576-7152fce4a203.png)


docker-compose.yml está em https://github.com/renatobdo/heliot/blob/master/docker-compose.yml_vm1

vm1: 177.104.61.126 em que está o servidor LoRA para geração de dados em formato base64

docker-compose.yml https://github.com/renatobdo/heliot/blob/master/docker-compose.yml_vm3

2 notebooks foram utilizados um com Ubuntu e outro com o Windows 10. No Ubuntu foi instalado o Node-Red e no Windows 10 o Iot Redirector e o Heliot.






