# T2-SistDits
## An simple stream data implementation using Kafka 

# Guide
First of all, clone this respository:
```
git clone https://github.com/mygeone/T2-SistDits.git
cd T2-SistDits
```
Second, you need to run Kafka service, included in this repo.
Execute following commands in separate terminal tabs
```
kafka/bin/zookeeper-server-start.sh config/zookeeper.properties
```
```
kafka/bin/kafka-server-start.sh config/server.properties
```
 Third, run main.py
 ```
 python3 main.py
 ```
 ## Open Endpoints

Open endpoints require no Authentication.

* [newOrder](login.md) : `POST /newOrder`
* [dailySummary](login.md) : `GET /dailySummary`

Emails are sended to registered emal in POST request.
