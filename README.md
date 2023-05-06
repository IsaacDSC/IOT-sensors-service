# IOT-sensors-service


Requisitos:

1. Desenvolver um microsserviço para armazenar dados de sensores em um banco de dados PostgreSQL. Os dados devem ser enviados no formato de dicionário com os seguintes campos:
   - sensor_id (int)
   - timestamp (datetime)
   - variable (string)
   - value (float)
   - unit (string)

OK -> 2. Não permitir a gravação de dados duplicados no banco de dados.

3. Criar testes unitários e de integração para cada função do microsserviço, garantindo seu correto funcionamento.

OK -> 4. Desenvolver um sistema de watchdog para monitorar o status dos serviços e enviar alarmes, para um webhook do Discord, caso algum deles esteja fora do ar.

5. Implementar uma solução baseada em containers usando Docker para facilitar o deploy e a escalabilidade do sistema.

6. Criar um script para simular o envio de 5000 dados em 1 minuto, garantindo que o sistema suporte essa carga sem downtime.


### 

###### Command run application in development
uvicorn src.main:app --port 8000 --reload


###### Command build application Dockerfile
docker build . --rm -t fastapi:latest


###### Command start application with Dockerfile
 docker run --name fastapi -p 8080:8080 fastapi:latest