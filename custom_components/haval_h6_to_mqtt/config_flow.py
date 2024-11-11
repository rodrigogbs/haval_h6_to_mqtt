# custom_components/haval_h6_to_mqtt/config_flow.py
import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import callback
from homeassistant.helpers import config_validation as cv
from .const import DOMAIN

class HavalH6ToMQTTConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Config flow for GWM Brasil Haval H6 with MQTT integration."""

    VERSION = 1
    CONNECTION_CLASS = config_entries.CONN_CLASS_LOCAL_PUSH

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        errors = {}

        if user_input is not None:
            # Se desejar, faça validações extras aqui.
            return self.async_create_entry(title="GWM Brasil Haval H6 com MQTT", data=user_input)

        # Defina o esquema de dados para o formulário de configuração
        data_schema = vol.Schema({
            vol.Required("haval_username"): str,
            vol.Required("haval_password"): str,
            vol.Required("haval_vin"): str,
            vol.Optional("haval_pin"): str,
            vol.Optional("mqtt_server", default="mqtt://homeassistant.local:1883"): str,
            vol.Optional("mqtt_user"): str,
            vol.Optional("mqtt_pass"): str,
            vol.Optional("refresh_time", default=30): int,
            vol.Optional("device_tracker_enabled", default=True): bool,
        })

        # Exibe o formulário de configuração para o usuário
        return self.async_show_form(
            step_id="user",
            data_schema=data_schema,
            errors=errors,
        )

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        """Define o fluxo de opções para modificar configurações após a configuração inicial."""
        return OptionsFlowHandler(config_entry)

class OptionsFlowHandler(config_entries.OptionsFlow):
    """Manipulador de fluxo de opções para a integração Haval H6."""

    def __init__(self, config_entry):
        """Inicializa o OptionsFlowHandler."""
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None):
        """Gerencia o fluxo de opções para atualização de configuração."""
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        # Preenche o formulário com os dados já fornecidos
        data_schema = vol.Schema({
            vol.Required("haval_username", default=self.config_entry.data.get("haval_username")): str,
            vol.Required("haval_password", default=self.config_entry.data.get("haval_password")): str,
            vol.Required("haval_vin", default=self.config_entry.data.get("haval_vin")): str,
            vol.Optional("haval_pin", default=self.config_entry.data.get("haval_pin", "")): str,
            vol.Optional("mqtt_server", default=self.config_entry.data.get("mqtt_server", "mqtt://homeassistant.local:1883")): str,
            vol.Optional("mqtt_user", default=self.config_entry.data.get("mqtt_user", "")): str,
            vol.Optional("mqtt_pass", default=self.config_entry.data.get("mqtt_pass", "")): str,
            vol.Optional("refresh_time", default=self.config_entry.data.get("refresh_time", 30)): int,
            vol.Optional("device_tracker_enabled", default=self.config_entry.data.get("device_tracker_enabled", True)): bool,
        })

        return self.async_show_form(step_id="init", data_schema=data_schema)
