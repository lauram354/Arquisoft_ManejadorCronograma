#!/usr/bin/env python
import time
import pika
from sys import path
from os import environ
import django

def run_producer():

   rabbit_host = '10.128.0.10'
   rabbit_user = 'losarquis_user'
   rabbit_password = '1234'
   exchange = 'cronogramas_pagos'
   topic = 'Cronograma'

   path.append('reportes/settings.py')
   environ.setdefault('DJANGO_SETTINGS_MODULE', 'reportes.settings')
   django.setup()



   from reportes.logic.logic_cronogramas import cronogramaPagos

   connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=rabbit_host, credentials=pika.PlainCredentials(rabbit_user, rabbit_password))
    )
    
   channel = connection.channel()
   channel.exchange_declare(exchange=exchange, exchange_type='topic')
   print('> Sending measurements. To exit press CTRL+C')

   while True:
     print('guayando')
     pagos = cronogramaPagos()
    
     for p in pagos:
        fecha_str = p.fecha.strftime("%Y-%m-%d")
        message =  p.nombre  +"," +  p.responsableF.correo  +"," + fecha_str  +"," + p.responsableF.nombre
        channel.basic_publish(exchange=exchange, routing_key=topic, body=message) 
    
        print(f"[x] Mensaje enviado: {message}")

     time.sleep(15)

   connection.close()

if __name__ == "__main__":
    run_producer()