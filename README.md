# IOT-sensors-service


## Requisitos:

1. Desenvolver um microsserviço para armazenar dados de sensores em um banco de dados PostgreSQL. Os dados devem ser enviados no formato de dicionário com os seguintes campos:
   - sensor_id (int)
   - timestamp (datetime)
   - variable (string)
   - value (float)
   - unit (string)

2. Não permitir a gravação de dados duplicados no banco de dados.

3. Criar testes unitários e de integração para cada função do microsserviço, garantindo seu correto funcionamento.

4. Desenvolver um sistema de watchdog para monitorar o status dos serviços e enviar alarmes, para um webhook do Discord, caso algum deles esteja fora do ar.

5. Implementar uma solução baseada em containers usando Docker para facilitar o deploy e a escalabilidade do sistema.

6. Criar um script para simular o envio de 5000 dados em 1 minuto, garantindo que o sistema suporte essa carga sem downtime.


-------

## RUNNING APPLICATION
---
### CREATE ENVIRONMENT:
```sh
DATABASE_URL = 'postgresql://root:root@__INTERNAL_IP__:5432/iot'
WHOAMI_IP = '__INTERNAL_IP__'
WHOAMI_URL = 'http://__INTERNAL_IP__/'
TOKEN_DISCORD = '__DISCORD_TOKEN__'
SECRET_TOKEN_DISCORD = '__SECRET_TOKEN__'
```

---
### STARTUP APPLICATION:
###### 
*Command run application replicate 3 instance, database, traefik, manage_database*
```sh
sh scripts/docker-compose.start.sh
```
#### OR
*Command start application with Dockerfile*
```sh
docker build . --rm -t iot-service-sensors:latest
docker run --name service-sensor -p 8080:8080 iot-service-sensors:latest
```
#### OR
*Command run application in development*
```sh
uvicorn src.main:app --port 8000 --reload
```
----
### RUNNING TESTS:
*Execute tests with command*
```sh
pytest
```
----
### RUNNING SCRIPT FROM SEND CHARGE REQUEST:
*Execute with command*
```sh
python3 ./watchdog/monitoring.py
```
----
### RUNNING SCRIPT FROM HEALTH CHECK:
*Execute command the health check without lock thread to requests*
```sh
python3 charge-test/with-tread/charge.py
```
#### OR
*Execute command the health check with lock thread to requests*
```sh
python3 charge-test/not-thread/charge.py
```
---
## Observations:
   ### More application info:
   #### This simple application using traefik and docker-compose from balancing and facility integration with tools the observability.
   - Is Possible Simple Integration With Tools:
      - Grafana with prometheus
      - Elastic Stack
      - Datadog
      - Load Balancer (AWS, Google Cloud, Azure)
      - Kubernetes
---
## Recommended
   ### Security from not loss data:
   #### Integrate with tools the stream data and database with large power writer
   - Examples tools of streaming data possible integration
      - Apache Kafka
      - RabbitMQ
      - Apache Spark
      - Others

   - Example tools the database power writer possible integration
      - Cassandra
      - Elastic Search
      - Redis
      - Others

   - From to high availability database possible execution
      - Using multiple instances of database or nodes
      - Replication data
      - Separate Writer the Read
      - Implement CQRS from application

---
## About
### This project only example 
*Project implemented with principles the Solid, Clean Code, Clean Arch, and philosophy DDD, from large project more is possible be simpler adapter from best use case.*

*Software Engineer: Isaac DSC*