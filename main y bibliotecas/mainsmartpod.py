import dht 
import machine
import urequests
import time
import math
import network
import sh1106
from machine import ADC, Pin, PWM, I2C


# Configuración de la red WiFi
#SSID = "UNAL"
#SSID = "FLIA GARCIA GUERRERO"
#PASSWORD = "11150903"
SSID = "Redmi"
PASSWORD = "delunoalocho"

# Configuración de Firebase
FIREBASE_URL = "https://smartpot-474b2-default-rtdb.firebaseio.com/"
FIREBASE_API_KEY = "8507dbcd2d2b6f5a69d49c6dbcebdafc9b4e44d3"

# Configuración del pin del sensor DHT11
DHT_PIN = 5  # Puedes cambiar el número de pin según tu configuración
soil = ADC(Pin(34))
soil.atten(ADC.ATTN_11DB)
sensor = ADC(Pin(32))
umbral = 1000
i2c = I2C(0, scl=Pin(22), sda=Pin(21))
oled = sh1106.SH1106_I2C(128, 64, i2c)

# Nombre de la clave en la base de datos
FIREBASE_KEY = "last_data"

def read_sl():
    hum_s = int(((soil.read_u16() - 48000) * 100 / (65500 - 48000)) + 0)


    return hum_s

def connect_to_wifi():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print("Conectándose a WiFi...")
        sta_if.active(True)
        #Para una red abierta
        #sta_if.connect(SSID)
        #Para una red con contraseña
        sta_if.connect(SSID, PASSWORD)
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
        light = "1"
    else:
        light = "0"
    
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
        
        if light is "0":
                oled.fill(0)
                oled.ellipse(64, 32, 20, 14, 1)  # Elipse exterior del sol
                oled.line(64, 8, 64, 16, 1)  # Rayo vertical superior
                oled.line(64, 48, 64, 56, 1)  # Rayo vertical inferior
                oled.line(32, 32, 40, 32, 1)  # Rayo horizontal izquierdo
                oled.line(86, 32, 94, 32, 1)  # Rayo horizontal derecho
                oled.line(40, 12, 48, 20, 1)  # Rayo diagonal superior izquierdo
                oled.line(80, 42, 88, 50, 1)  # Rayo diagonal inferior derecho
                oled.line(88, 12, 80, 20, 1)  # Rayo diagonal superior derecho
                oled.line(44, 42, 36, 50, 1)  # Rayo diagonal inferior izquierdo
                oled.line(2,39,16,39,1)# signo menos
                oled.line(9,46,9,32,1)#rayita para signo más
                oled.text("Dame ", 0,8, 1)
                oled.text("luz", 0,16 , 1)
                oled.show()
                
        elif temperature < 8:
                oled.fill(0)
                oled.ellipse(64, 32, 30, 30, 1)  # Cara
                oled.ellipse(54, 25, 8, 12, 1)  # Ojo izquierdo
                oled.ellipse(74, 25, 8, 12, 1)  # Ojo derecho
                oled.ellipse(54, 25, 4, 6, 1)  # Pupila izquierda
                oled.ellipse(74, 25, 4, 6, 1)  # Pupila derecha
                oled.line(48, 38, 58, 43, 1)  # Ceja izquierda
                oled.line(70, 43, 80, 38, 1)  # Ceja derecha
                oled.line(54, 48, 74, 48, 1)  # Boca
                oled.text("(", 45, 15, 1)
                oled.text(")", 85, 15, 1)
                oled.text("(", 45, 35, 1)
                oled.text(")", 85, 35, 1)
                oled.text("(", 45, 55, 1)
                oled.text(")", 85, 55, 1)
                oled.text("Teno",0,1,1)
                oled.text("frio",0,8,1)
                oled.show()
                
        elif temperature > 35:
                oled.fill(0)
                oled.ellipse(64, 32, 30, 30, 1)  # Cara
                oled.ellipse(54, 25, 8, 12, 1)  # Ojo izquierdo
                oled.ellipse(74, 25, 8, 12, 1)  # Ojo derecho
                oled.ellipse(54, 25, 4, 6, 1)  # Pupila izquierda
                oled.ellipse(74, 25, 4, 6, 1)  # Pupila derecha
                oled.ellipse(64, 50, 10, 6, 1)  # Boca
                oled.ellipse(90, 25, 2, 5, 1)  # Gota de sudor
                oled.ellipse(90, 50, 3, 8, 1)  # Gota de sudor
                oled.text("Estoy ", 0,8, 1)
                oled.text("muy", 0,16 , 1)
                oled.text("hot!", 0, 24, 1)
                oled.show()
        
        elif humidity_a < 30:
                oled.fill(0)
                oled.text("La humedad aqui",0, 0,1)
                oled.text("es muy baja",0, 25,1)
                oled.text("ayudame :((((",0, 50,1)
                oled.show()
                
        elif humidity_a > 90:
                oled.fill(0)
                oled.ellipse(64, 32, 30, 30, 1)  # Cara
                oled.ellipse(54, 25, 8, 12, 1)
                oled.ellipse(74, 25, 8, 12, 1)
                oled.ellipse(54, 25, 4, 6, 1)
                oled.ellipse(74, 25, 4, 6, 1)
                oled.pixel(54, 25, 0)
                oled.pixel(74, 25, 0)
                oled.ellipse(64, 45, 8, 4, 1)  # Boca
                oled.ellipse(48, 40, 6, 3, 1)  # Mejilla izquierda
                oled.ellipse(82, 40, 6, 3, 1)# Mejilla derecha
                oled.text("me",0,1,1)
                oled.text("vuelvo ",0,8,1)
                oled.text("moho",0,15,1)
                oled.show()
                
        elif humidity_s < 25:
                oled.fill(0)
                oled.ellipse(64, 32, 30, 30, 1)  # Cara
                oled.line(54, 25, 62, 33, 1)  # Ojo izquierdo
                oled.line(54, 33, 62, 25, 1)  # Ojo izquierdo
                oled.line(70, 25, 78, 33, 1)  # Ojo derecho
                oled.line(70, 33, 78, 25, 1)  # Ojo derecho
                oled.ellipse(64, 45, 10, 6, 1)  # Boca
                oled.ellipse(70, 55, 3, 6, 1)
                oled.text("Tengo",0,1,1)
                oled.text("mucha",0,8,1)
                oled.text("sed",0,15,1)
                oled.show()
                
        elif humidity_s > 75:
                oled.fill(0)
                oled.ellipse(64, 32, 30, 30, 1)  # Cara
                oled.line(54, 25, 62, 33, 1)  # Ojo izquierdo
                oled.line(54, 33, 62, 25, 1)  # Ojo izquierdo
                oled.line(70, 25, 78, 33, 1)  # Ojo derecho
                oled.line(70, 33, 78, 25, 1)  # Ojo derecho
                oled.line(54, 45, 74, 45, 1)  # Boca
                oled.line(62, 50, 62, 60, 1)
                oled.line(66, 50, 66, 60, 1)
                oled.line(70, 50, 70, 60, 1)
                oled.text("Bebi",0,1,1)
                oled.text("mucha",0,8,1)
                oled.text("agua",0,15,1)
                oled.show()
        else:
                oled.fill(0)
                oled.ellipse(64, 32, 30, 24, 1)
                oled.ellipse(54, 25, 8, 12, 1)
                oled.ellipse(74, 25, 8, 12, 1)
                oled.ellipse(54, 25, 4, 6, 1)
                oled.ellipse(74, 25, 4, 6, 1)
                oled.pixel(54, 25, 0)
                oled.pixel(74, 25, 0)
                oled.text("Ando", 0,4,1)
                oled.text("feli!", 0,12,1)
                for x in range(20):
                      y = int(27 + math.sqrt(20**2 - (x-10)**2))
                      oled.pixel(55+x, y, 1)
                oled.show()
        
        try:
            send_to_firebase(temperature, humidity_a, humidity_s, light)
        except Exception as e:
            print("Error al enviar datos a Firebase:", e)
        






#Bucle principal
#while True:
    #main()
contador = 0 # definir una variable para llevar el conteo de los intentos
while True:
    try:
        main() # intenta ejecutar la función main
        problem()
        print (problem())
        contador = 0 # si se ejecuta sin errores, reinicia el contador
    except:
        contador += 1 # si hay un error, incrementa el contador en uno
        print("Ocurrió un error, intentando de nuevo") # imprime un mensaje de error
        if contador == 4: # si el contador llega a 3, se detiene el bucle
            print("Se alcanzó el máximo de intentos, deteniendo el programa")
            break # sale del bucle while
        continue # si no, vuelve al inicio del while
