#!/usr/bin/env python
import pika
import time
import os
import os.path

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

mypath="./"

fileSet=set() 
while True:
  time.sleep(2)
  for myfile in os.listdir(mypath):
      if myfile not in fileSet:
        fileSet.add(myfile)
        print(f"new file added: ${myfile}")
        channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
        print(" [x] Sent 'Hello World!'")
