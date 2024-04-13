import pika
import json

def enviar_pedido_para_logistica(pedido):
    print("Pedido enviado para o sistema de envio/logística:", pedido)

def callback(ch, method, properties, body):
    pedido = json.loads(body)
    print(" [x] Pedido recebido para envio:", pedido)
    enviar_pedido_para_logistica(pedido)

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='pedidos_processados')

channel.basic_consume(queue='pedidos_processados',
    on_message_callback=callback,
    auto_ack=True)

print(' [*] Aguardando pedidos processados. Para sair, pressione CTRL+C')
channel.start_consuming()
