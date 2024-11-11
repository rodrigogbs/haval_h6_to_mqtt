# custom_components/haval_h6_to_mqtt/mqtt_client.py
import asyncio
import paho.mqtt.client as mqtt

class MQTTClient:
    def __init__(self, hass, config):
        self.hass = hass
        self.config = config
        self.client = mqtt.Client()

    async def connect(self):
        # Configura o cliente MQTT e conecta ao broker
        self.client.username_pw_set(self.config['username'], self.config['password'])
        self.client.connect(self.config['broker'], self.config['port'])
        
        # Iniciar a conexão em um loop de asyncio
        loop = asyncio.get_event_loop()
        await loop.run_in_executor(None, self.client.loop_start)

    async def disconnect(self):
        # Desconecta o cliente MQTT
        self.client.loop_stop()
        self.client.disconnect()
