from flask import Flask, request, jsonify
from kafka import KafkaProducer, KafkaConsumer
import threading
import json
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

# Initialize Kafka producer
producer = KafkaProducer(bootstrap_servers='localhost:9092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

def send_request_to_kafka(topic, message):
    try:
        producer.send(topic, value=message)
        producer.flush()
        app.logger.info(f"Sent message to {topic}: {message}")
    except Exception as e:
        app.logger.error(f"Failed to send message to {topic}: {e}")

@app.route('/chat', methods=['POST'])
def chat():
    # Lấy nội dung của request từ client
    user_question = request.json.get('user_question')
    
    # Send request to Kafka
    send_request_to_kafka('chatbot_requests', user_question)
    
    return jsonify({'status': 'Request received'}), 202

def consume_responses():
    consumer = KafkaConsumer('chatbot_responses',
                           bootstrap_servers='localhost:9092',
                             auto_offset_reset='earliest',
                             value_deserializer=lambda x: json.loads(x.decode('utf-8')))
    for message in consumer:
        response = message.value
        user_id = response['user_id']
        chatbot_response = response['response']
    app.logger.info(f"Response for user {user_id}: {chatbot_response}")

if __name__ == '__main__':
    threading.Thread(target=consume_responses).start()
    app.run(debug=True, port=5000)
