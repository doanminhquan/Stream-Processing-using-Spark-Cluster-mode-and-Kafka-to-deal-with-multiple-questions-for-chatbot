# Stream Processing using Spark and KafKa on cluster to deal with multiple questions for chatbot
[![python](https://img.shields.io/badge/python-3.10.14-green)](https://www.python.org/doc/)
[![python](https://img.shields.io/badge/kafka-3.7.0-yellow)](https://kafka.apache.org/documentation/)
[![python](https://img.shields.io/badge/spark-3.5.1-blue)](https://spark.apache.org/docs/latest/)

### Overview
The objective of this project is to create a module that can handle multiple questions at once for my organization's chatbot app, without being hindered by a sudden surge in the number of questions. The idea is to integrate Kafka and Spark Streaming on a Cluster for stream processing and distributed handling of questions across multiple workers simultaneously. Additionally, I have built a Flask module to create a POST request that serves the purpose of testing the increasing number of questions in this trial version. Feel free to upgrade this app and scale it up for your purposes
Tech stack: PySpark, Apache Kafka, Apache Spark, Python, Flask

# Architecture
![alt text](https://github.com/doanminhquan/Stream-Processing-using-Spark-Cluster-mode-and-Kafka-to-deal-with-multiple-questions-for-chatbot/blob/93bc465b1c3f71ebf8f77f3115b098cccbce3e8f/architecture.png)
# How to use

## 1.Install and config Apache Spark, Apache Kafka, Flask
```
https://spark.apache.org/downloads.html
https://kafka.apache.org/downloads
pip install flask
```
## 2.Pull git repo
```
git clone https://github.com/doanminhquan/Stream-Processing-using-Spark-Cluster-mode-and-Kafka-to-deal-with-multiple-questions-for-chatbot.git
```
## 3.Start the Kafka Environment
- Go to Kafka folder
```
- cd Your_Kafka_folder
```

```
# Start the ZooKeeper service
$ bin/zookeeper-server-start.sh config/zookeeper.properties
```
- Open another terminal session and run:
```
# Start the Kafka broker service
$ bin/kafka-server-start.sh config/server.properties
```
## 4. Create topics to store questions and answer
- Open another terminal session and run:
```
# Create topic chatbot_requests
$ bin/kafka-topics.sh --create --topic chatbot_requests --bootstrap-server localhost:9092 --partitions 3 --replication-factor 1
```
- Open another terminal session and run:
```
# Create topic chatbot_responses
$ bin/kafka-topics.sh --create --topic chatbot_responses --bootstrap-server localhost:9092 --partitions 3 --replication-factor 1
```

## 5. Start Spark on master node and worker node
- Run this on your master node:
```
$ /spark/sbin/start-master.sh
```
- SSH to worker nodes and run:
```
$ /spark/sbin/start-worker.sh
```
## 6. Run flask module and spark_kafka module on venv
```
# Run flask module to create POST api endpoint which receive question
python /home/dis/rag-chatbot/flask-app/flask_app.py
```
- Run this on master node to start spark_kafka module
- If you do not use venv, remove --archives parameter and venv-pack
```
source /home/dis/rag-chatbot/venv/bin/activate
venv-pack -o pyspark_venv.tar.gz
spark-submit --archives /home/dis/pyspark_venv.tar.gz --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.1 /home/dis/rag-chatbot/spark-kafka-app/spark_kafka.py
```
- Alternative script to run on global environment
```
python /home/dis/rag-chatbot/spark-kafka-app/spark_kafka.py
```

- Test with multiple question by sending multiple POST requests to http://localhost:5000/chat using Postman or any other api testing tool (forwarding port before sending if you use localhost)
```
{
    "user_question":"What is Computer Science?"
}
```
![alt text](https://github.com/doanminhquan/Stream-Processing-using-Spark-Cluster-mode-and-Kafka-to-deal-with-multiple-questions-for-chatbot/blob/93bc465b1c3f71ebf8f77f3115b098cccbce3e8f/answer.png)

- Enjoy! 🔥 🔥 🔥 
# Note
This repo is a demo version of spark + kafka module in a rag chatbot app of our organization, you could see more about our Rag module in this github: https://github.com/longcule/rag-chatbot-uet/tree/master or use your chatbot module by changing function generate_responses() in spark_kafka.py (currently using Gemini api)
# Contact for questions
- Email: quandoanminh.work@gmail.com
