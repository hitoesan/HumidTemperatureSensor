#INTERNET DAS COISAS
import dht
import machine
import time
from wifi_lib import conecta
import urequests

d = dht.DHT11(machine.Pin(4))
r = machine.Pin(2, machine.Pin.OUT)

#Conecta à internet
print("Conectando...")
station = conecta("NET_2G3A151A", "")
if not station.isconnected():
    print("Não conectado!")
else:
    print("Conectado!")


while True:
        d.measure()            #Mede a temperatura e umidade
        temp = d.temperature() #Armazena a temperatura
        umid = d.humidity()    #Armazena a umidade
        
        if temp>31 or umid>70: #Condições para acender o relé
            r.value(1)
        else:
            r.value(0)
        
        #Envio de dados para o Thingspeak via internet
        resposta = urequests.get("https://api.thingspeak.com/update?api_key=0JGY1Z4W00USO8R9&field1={}&field2={}".format(temp, umid))
        resposta.text
    
        #Imprime a temperatura e umidade
        print("Temp={} Umid={}".format(temp, umid))
        
        #Repete o processo a cada 5s
        time.sleep(5)
