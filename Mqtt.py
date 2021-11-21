# Comunicação com Protocolo MQTT
# Internet das Coisas
Data: 01/11/2021 
Após ter baixado no celular o app no drive-->MQTT <br>
Versão: 1.0
#-----------------------------------------------
# Importar as bibliotecas( Colab usa "!"  no vc code tira)
! pip install paho-mqtt
#------------------------------------------------
# Importar as bibliotecas
import paho.mqtt.client as mqtt
import sys
#------------------------------------------------
# Configurações do MQTT :variaveis necessárias e suas senhas 
Broker = "test.mosquitto.org"
PortaBroker = 1883
#aqui é o tempo de conexão passou corta a conexão
KeepAliveBroker = 60
TopicoSubscribe = "roma15:21112021" 
#--------------------------------------------------
# Função para conexão com o broker------Não mudar nada(somente mensagem do print)
#nome da função é padrão,
def on_connect(client, userdata, flags, rc):
  print('[STATUS]  Conectando ao Broker. Resultado: ' + str(rc))
  # Inscrever no topico configurado
  client.subscribe(TopicoSubscribe)
#-----------------------------------------------
# Função para recebimento de mensagem------Não mudar nada(somente mensagem do print)
def on_message(client, userdata, msg):
  MensagemRecebida = str(msg.payload)
  print("[MSG RECEBIDA] Topico:"+msg.topic+" / Mesagem: "+MensagemRecebida)
#------------------------------------------------
# Programa Principal------Não mudar nada(somente mensagem do print)
try:
  print("[STATUS] Iniciando o MQTT...")

  client = mqtt.Client()
  client.on_connect = on_connect
  client.on_message = on_message

  # Conexão proriamente dita
  client.connect(Broker, PortaBroker, KeepAliveBroker)
  client.loop_forever()
except KeyboardInterrupt:
  print("Ctrl+C pressionado, encerrando a aplicação")
  sys.exit(0)