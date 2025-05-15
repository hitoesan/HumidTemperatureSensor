# HumidTemperatureSensor

Program for the ESP32 and DHT11 temperature and humidity sensor, written in MicroPython, which performs the following:

1. Activates the relay whenever the humidity exceeds 70% or the temperature is higher than 31°C.
2. Deactivates the relay otherwise.

The purpose of turning the relay on or off is to automatically activate or deactivate a potential heating and irrigation system whenever the temperature and humidity conditions detected by the sensor are not ideal.
The data is updated every 5 seconds and sent to the ThingSpeak platform, where it can be viewed in real time through dashboards.

----------------------------------------------------------

Programa para ESP32 e sensor de umidade e temperatura DHT11, escrito com MicroPython, que realiza:
1. Ligamento do relé sempre que a umidade for superior a 70 ou a temperatura for maior que 31.
2. Desligamento do relé caso contrário.

O intuito do ligamento/desligamento do relé é ativar/desativar um possível sistema de aquecimento e irrigação automaticamente, assim que as condições de temperatura e umidade detectadas pelo sensor não forem ideais.
Os dados são atualizados a cada 5 segundos e enviados ao Thingspeak, no qual é possível visualizar os dados em tempo real através de dashboards.
