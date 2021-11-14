# Kafka Project: Sales and Reports
## A simple project to manage sales for carts and generate a daily report of sales with email notification
### Miguel Contreras - Lester Carrasco - Nicolas Poza

# Guide
First, clone this respository:
```
git clone https://github.com/mygeone/T2-SistDits.git
cd T2-SistDits
```
Install dependencies:
```
pip install -r requirements.txt
```
Second, you need to run Kafka service included in this repo.
Execute following commands in separate terminals.
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

* [newOrder](newOrder.md) : `POST /newOrder`
* [dailySummary](dailySummary.md) : `GET /dailySummary`

Emails are sended to registered emal in POST request.
