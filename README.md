# Sistema de Processamento de Pedidos com RabbitMQ

Este repositório apresenta um sistema básico de processamento de pedidos em uma loja digital utilizando RabbitMQ para comunicação assíncrona entre componentes. O sistema é composto por três partes principais: produtor, processamento e logística.

## Funcionalidades

- **Produção de pedidos:** Envia pedidos simulados para a fila inicial.
- **Processamento de pedidos:** Registra os pedidos recebidos em um banco de dados (simulado).
- **Logística de pedidos:** Encaminha os pedidos processados para o sistema de envio/logística (simulado).
- **Mensageria:** Utiliza RabbitMQ para gerenciar filas e garantir comunicação entre os módulos.

## Implementação

- Criei um sistema de comunicação utilizando o RabbitMQ para facilitar a troca de informações entre os diferentes componentes de um sistema distribuído.
- Configurei duas filas para gerenciar os pedidos da loja online e os pedidos processados.
- Desenvolvi scripts em Python para simular a loja online e processar os pedidos, garantindo o envio correto para o sistema de envio/logística.

## Arquivos do Projeto

- **`produtor.py`:** Simula o envio de pedidos para a fila inicial.
- **`processamento.py`:** Consome os pedidos da fila inicial e realiza o processamento.
- **`logistica.py`:** Consome os pedidos processados e simula o envio para o sistema de logística.

## Como Executar o Projeto

### Pré-requisitos

- Python 3.6 ou superior
- RabbitMQ instalado e em execução
