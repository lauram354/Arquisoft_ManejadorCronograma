#!/usr/bin/env python
import time
import pika
from random import uniform

import json
from sys import path
from os import environ
import django

rabbit_host = '10.128.0.10'
rabbit_user = 'losarquis_user'
rabbit_password = '1234'
exchange = 'cronogramas_pagos'
topic = 'Cronograma'




from reportes.logic.logic_cronogramas import cronogramaPagos

connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=rabbit_host, credentials=pika.PlainCredentials(rabbit_user, rabbit_password))
    )
    
channel = connection.channel()
channel.exchange_declare(exchange=exchange, exchange_type='topic')
print('> Sending measurements. To exit press CTRL+C')

while True:
    pagos = cronogramaPagos()
    
    for p in pagos:
        message = "{'mensaje': %r, 'correo': %r, 'fecha': %r,'responsable': '%r'}" % (p.nombre, p.responsableF.correo, p.fecha, p.responsableF.nombre)
        channel.basic_publish(exchange=exchange, routing_key=topic, body=message) 
    
        print(f"[x] Mensaje enviado: {message}")

    time.sleep(15)

connection.close()

