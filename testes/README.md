# Objetivo dos testes

Simular o envio de mensagens aleatórias com os tipos de dados (content-types) : XML, JSON, UL, HTML, indefinido, LoRa, Teros12. Receber essas mensagens em um algoritmo capaz de analisar o payload e enviá-lo para um agente (IoT Agent) responsável por gerenciar essas mensagens 

# Cenário dos testes

https://docs.google.com/spreadsheets/d/105WulcEI_N9G7DqwXDJvnhXg6a3PEYmjO1qWytULM5Q/edit#gid=0


# Arquitetura dos testes

![Defesa-Orquestrador-Final](https://user-images.githubusercontent.com/9336800/144167743-fa0f7c65-8feb-449f-9a88-e8bce570cbba.jpg)



O simulador irá gerar mensagens com 6 diferentes content-types: xml, html, json, ul, indefinido, teros. Uma amostra dessas mensagens pode ser visualizado na tabela abaixo:

![image](https://user-images.githubusercontent.com/9336800/144165519-5ab7b6f8-0389-484f-91b8-524fe9900fdf.png)


O SenSE[1] que também é um gerador de mensagens gera 1 tipo de content-type baseado no padrão LoRa. O conteúdo da mensagem está codificado em base 64. A mensagem gerada por esse simulador é dessa forma:

{applicationID:5,applicationName:mestrado_simulacao,deviceName:DHT11,devEUI:221597e4529df57d,rxInfo:[{gatewayID:000000ffff001000,name:ExpGW,rssi:-57,loRaSNR:7,location:{latitude:0,longitude:0,altitude:0}}],txInfo:{frequency:915000000,dr:5},adr:false,fCnt:0,fPort:1,data:dHN8MTYzODMyMTY2NjE4MHx0aXxsb3Jh}

Repare que no campo data o conteúdo está em base 64. Quando decodificamos a mensagem obtemos: 
ts|1638321666180|ti|lora

Na saída do redirecionar é realizado a persistência em um arquivo csv de log. Essa saída é comparada com a mensagem que foi redirecionada para o IoT Agent e persistida tanto no CrateDB quanto no MongoDb. Isso é realizado pelo Quantum Leap e pela API, respectivamente. 

## Referências Bibliográficas

[1]	C. K. Ivan Zyrianoff, Fabrizio Borelli, “SenSE – Sensor Simulation Environment: Uma ferramenta para geração de tráfego IoT em larga escala,” SBRC 2017 - Salão de Ferramentas, p. 9, 2017, [Online]. Available: https://www.researchgate.net/publication/316581014_SenSE_-_Sensor_Simulation_Environment_Uma_ferramenta_para_geracao_de_trafego_IoT_em_larga_escala
