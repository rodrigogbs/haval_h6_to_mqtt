# custom_components/haval_h6_to_mqtt/__init__.py
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from .mqtt_client import MQTTClient

DOMAIN = "haval_h6_to_mqtt"

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    # Inicializar o cliente MQTT
    mqtt_client = MQTTClient(hass, entry.data)
    hass.data[DOMAIN] = mqtt_client

    # Conectar ao MQTT
    await mqtt_client.connect()
    
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    # Fechar a conexão MQTT ao descarregar
    mqtt_client = hass.data.pop(DOMAIN)
    await mqtt_client.disconnect()
    
    return True
