import dht 
import machine
import urequests
import time
import math
import network
from machine import ADC, Pin, PWM


# Configuración de la red WiFi
SSID = "UNAL"
#SSID = "FLIA GARCIA GUERRERO"
#PASSWORD = "11150903"

# Configuración de Firebase
FIREBASE_URL = "https://smartpot-474b2-default-rtdb.firebaseio.com/"
FIREBASE_API_KEY = "8507dbcd2d2b6f5a69d49c6dbcebdafc9b4e44d3"

# Configuración del pin del sensor DHT11
DHT_PIN = 5  # Puedes cambiar el número de pin según tu configuración
soil = ADC(Pin(34))
soil.atten(ADC.ATTN_11DB)
sensor = ADC(Pin(32))
umbral = 1000

# Nombre de la clave en la base de datos
FIREBASE_KEY = "last_data"

def read_sl():
    hum_s = soil.read_u16()
    return hum_s

def connect_to_wifi():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print("Conectándose a WiFi...")
        sta_if.active(True)
        #Para una red abierta
        sta_if.connect(SSID)
        #Para una red con contraseña
        #sta_if.connect(SSID, PASSWORD)
        while not sta_if.isconnected():
            pass
        print("Conexión exitosa")
    else:
        print("Ya estás conectado a WiFi")

def read_dht11():
    dht_sensor = dht.DHT11(machine.Pin(DHT_PIN))
    dht_sensor.measure()
    temperature = dht_sensor.temperature()
    humidity_a = dht_sensor.humidity()
    return temperature, humidity_a



def read_light():
    valor = sensor.read()
    if valor < umbral:
        light = "yes"
    else:
        light = "no"
    
    return light

def send_to_firebase(temperature, humidity_a, humidity_s, light):
    data = {
        "temperature": temperature,
        "humidity ambient": humidity_a,
        "humidity soil" : humidity_s,
        "light" : light
    }
    url = f"{FIREBASE_URL}/{FIREBASE_KEY}.json?auth={FIREBASE_API_KEY}"
    response = urequests.patch(url, json=data)
    print("Respuesta de Firebase:", response.text)

def main():
    connect_to_wifi()
    
    while True:
        temperature, humidity_a = read_dht11()
        humidity_s = read_sl()
        light = read_light()
        print(f"Temperatura: {temperature}°C, Humedad ambiente: {humidity_a}%, Humedad suelo: {humidity_s}%, Presencia de luz: {light}")
        
        try:
            send_to_firebase(temperature, humidity_a, humidity_s, light)
        except Exception as e:
            print("Error al enviar datos a Firebase:", e)
        
        time.sleep(60)  # Esperar 60 segundos antes de tomar y enviar nuevos datos


#Bucle principal
while True:
    main()
#while True:
    #try:
        #main() # intenta ejecutar la función main
    #except:
        #print("Ocurrió un error, intentando de nuevo") # imprime un mensaje de error
        #continue # vuelve al inicio del while
