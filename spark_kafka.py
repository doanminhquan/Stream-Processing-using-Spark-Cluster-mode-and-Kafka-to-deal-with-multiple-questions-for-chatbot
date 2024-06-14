import findspark
findspark.init()
from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StringType, StructType
from kafka import KafkaProducer
import json
import google.generativeai as gen_ai
print('Import Done')
import os
import time
from dotenv import load_dotenv

os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages org.apache.spark:spark-streaming-kafka-0-10_2.12:3.5.1,org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.1 pyspark-shell'
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
gen_ai.configure(api_key=GOOGLE_API_KEY)
print(GOOGLE_API_KEY)
load_dotenv()

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("KafkaSparkLLM") \
    .master("spark://10.10.28.40:7077") \
    .config("spark.executor.memory", "1g") \
    .config("spark.executor.cores", "1") \
    .getOrCreate()

print("SparkSS Done")
# Define the schema of the incoming Kafka messages
schema = StructType().add("user_id", StringType()).add("question", StringType())

print("schema done")
# Read from Kafka topic
kafka_stream = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "chatbot_requests") \
    .option("startingOffsets", "latest") \
    .option("failOnDataLoss", "false") \
    .load() 
    # \
    # .selectExpr("CAST(value AS STRING)")

print("Schema and Kafka stream done")
# Parse the JSON messages
# query = kafka_stream \
#     .selectExpr("CAST(value AS STRING)") \
#     .writeStream \
#     .outputMode("append") \
#     .format("console") \
#     .start()

# query.awaitTermination()



# parsed_stream = kafka_stream.select(from_json(col("value"), schema).alias("data")).select("data.*")
# print("-------parsed_stream:----------- ")

def generate_response(user_question):
    # Load your Gemini-Pro model
    model = gen_ai.GenerativeModel('gemini-pro')
    # Start chat session with empty history
    chat_session = model.start_chat(history=[])
    # Send user's question to Gemini-Pro and get the response
    gemini_response = chat_session.send_message(user_question)
    return gemini_response.text

# def process_batch(df, epoch_id):
#     # Chuyển DataFrame thành list và in từng giá trị
#     messages = df.select("message").collect()
#     for row in messages:
#         print(row["message"])

def process_batch(batch_df, batch_id):
    # Iterate over rows in the batch DataFrame
    for row in batch_df.collect():
        message = row.message
        response = generate_response(message)
        # Print the response to the console
        print(f"Question: {message}, Response: {response}")

query = kafka_stream \
    .selectExpr("CAST(value AS STRING) as message") \
    .writeStream \
    .foreachBatch(process_batch) \
    .start()

query.awaitTermination()
# # Function to process each row
# def process_row(row):
#     request = row.asDict()
#     user_input = request['question']

#     # Process request with LLM logic (simplified for this example)
#     response = generate_response(user_input)

#     # Send response to Kafka
#     response_message = {
#         'user_id': request['user_id'],
#         'response': response
#     }
#     send_to_kafka("chatbot_responses", json.dumps(response_message))

# def send_to_kafka(topic, message):
#     producer = KafkaProducer(bootstrap_servers='localhost:9092')
#     producer.send(topic, value=message.encode('utf-8'))
#     producer.flush()

# # Apply the processing function to each row in the stream
# parsed_stream.writeStream.foreach(process_row).start().awaitTermination()
