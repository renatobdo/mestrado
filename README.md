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

![Defesa-Orquestrador-19-Chirp Stack(1)](https://user-images.githubusercontent.com/9336800/144475643-184a1720-4640-4b8d-8dfa-2026b0f146ba.jpg)


São utilizadas 4 máquinas virtuais:

![2021-12-02 (25)](https://user-images.githubusercontent.com/9336800/144474057-1c936918-f8dd-455f-8576-7152fce4a203.png)


## Diagrama UML de classe do gerador de mensagens

![RedirecionadorUML-UML](https://user-images.githubusercontent.com/9336800/144477559-e7dc43d9-5f26-4b92-a17c-1ba5c852e3e3.jpg)

