https://docs.google.com/spreadsheets/d/105WulcEI_N9G7DqwXDJvnhXg6a3PEYmjO1qWytULM5Q/edit#gid=0

Cenário 1 - Caso de testes 3	(CT3)

## Descrição do teste
Simular o envio de 5000 sensores aleatórios com os tipos de dados (content-types) : XML, JSON, UL, HTML, dado aleatório, LoRa, Teros12. 

## propósito:
Com intervalo de tempo entre cada envio de 3 segundos.	
1) Analisar o tempo de parsing/ filtro do algoritmo para cada content type;
2) Obter a vazão ou a quantidade de Bits/s na saída do redirecionador
3) Analisar o comportamento do redirecionador com carga de sensores maior em menor tempo

## métricas
- Tempo de parsing, 
- utilização de cpu, 
- utilização de memória, 
- vazão	variedade, volume e velocidade	

## duração
10 min	

## resultado esperado
1) Tempo de parsing para cada content type;
2) vazão na saída do redirecionador em bits/s
3) Utilização de cpu e memória 

## Resultado obtido

abrir aba c1-ct3
https://docs.google.com/spreadsheets/d/105WulcEI_N9G7DqwXDJvnhXg6a3PEYmjO1qWytULM5Q/edit#gid=926317124

## Comandos do SenSE:
java -jar SenSE.jar -sensor 850 -rep 1 -time 600 - p 3 -h tcp://177.104.61.126:1883 -sensorType lora -temp -netkey 9c698235533b8865900aee3558dfc47b -appkey b73485bb9c5e29a2c8b6a330f0bf2ed3 -mac 000000ffff001000 -devAddress 00fb0bc1	"

## Comandos do Simulador java:
java -jar SimuladorComSleep.jar 5000 600000

## Comandos do Subscriber Redirector
java -jar SubscriberRedirector.jar 

## Pasta com documentos de testes
C:\Users\renat\OneDrive\Área de Trabalho\Renato\UFABC\2021-03\testes\Cenario1-ct3
