# HumidTemperatureSensor

Programa para ESP32 e sensor de umidade e temperatura DHT11, escrito com MicroPython, que realiza:
1. Ligamento do relé sempre que a umidade for superior a 70 ou a temperatura for maior que 31.
2. Desligamento do relé caso contrário.

O intuito do ligamento/desligamento do relé é ativar/desativar um possível sistema de aquecimento e irrigação automaticamente, assim que as condições de temperatura e umidade detectadas pelo sensor não forem ideais.
Os dados são atualizados a cada 5 segundos e enviados ao ThingSpeak.
