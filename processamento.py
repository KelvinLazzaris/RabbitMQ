import pika
import json

def registrar_pedido_no_banco_de_dados(pedido):
    print("Pedido registrado no banco de dados:", pedido)

def callback(ch, method, properties, body):
    pedido = json.loads(body)
    print(" [x] Pedido recebido:", pedido)
    registrar_pedido_no_banco_de_dados(pedido)

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='pedidos_da_loja_digital')

channel.basic_consume(queue='pedidos_da_loja_digital',
    on_message_callback=callback,
    auto_ack=True)

print(' [*] Aguardando pedidos. Para sair, pressione CTRL+C')
channel.start_consuming()
