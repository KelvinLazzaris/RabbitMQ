import pika
import json

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='pedidos_da_loja_digital')

def enviar_pedido(pedido):
    channel.basic_publish(exchange='',
        routing_key='pedidos_da_loja_digital',
        body=json.dumps(pedido))
    print(" [x] Pedido enviado:", pedido)

# Simulação de envio de pedidos
pedido1 = {"cliente": "João", "produto": "Celular", "quantidade": 1}
pedido2 = {"cliente": "Maria", "produto": "Tablet", "quantidade": 2}

enviar_pedido(pedido1)
enviar_pedido(pedido2)

connection.close()
