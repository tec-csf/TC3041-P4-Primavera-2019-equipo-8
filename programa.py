from time import sleep
import numpy as np
from influxdb import InfluxDBClient
import datetime
import random


#Conexión a la base de datos
client = InfluxDBClient('localhost', 8086, 'root', 'root', 'oficina_IoT')

#Creación de una base de datos
client.create_database('oficina_IoT')

#aire acondicionado entre 23°C y 26°C


minTemp = 23
maxTemp = 26
for i in range(20000000):
    random1 = round(random.uniform(minTemp,maxTemp+1),2)
    random2 = random1 - round(random.uniform(1,7),2)
    temperatures = [{"measurement": "temperatura",
                   "tags":{"acondicionador": "No_1"},
                   "time":datetime.datetime.utcnow().isoformat(),
                   "fields": {"gradosCentigrados":random1}},
                   {"measurement": "temperatura",
                   "tags":{"acondicionador": "No_2"},
                   "time":datetime.datetime.utcnow().isoformat(),
                   "fields": {"gradosCentigrados":random2}}]
    client.write_points(temperatures)
print("Serie de temperatura")


#humedad entre 45% y 60%

minHumid = 45
maxHumid = 60
for i in range(20000000):
    humidity = round(random.uniform(minHumid,maxHumid+1),2)
    humidIndoors = humidity - round(random.uniform(20,25),2)
    humid_arr = [{'measurement': 'humedad',
                  'tags':{'humidificador': 'No_1'},
                  'time':datetime.datetime.utcnow().isoformat(),
                  'fields': {'porcentajeHumedad':humidIndoors}},
                  {'measurement': 'humedad',
                  'tags':{'humidificador': 'No_2'},
                  'time':datetime.datetime.utcnow().isoformat(),
                  'fields': {'porcentajeHumedad':humidity}}]
    client.write_points(humid_arr)
print("Serie de humedad")

#Cantidad de accesos

for i in range(20000000):
    TotalEntries = random.random()*100
    Entries_arr= [{'measurement': 'entradas',
                  'tags':{'control_de_seguridad': 'entradas'},
                  'time':datetime.datetime.utcnow().isoformat(),
                  'fields': {'Número_entradas':TotalEntries}},
                  {'measurement': 'salidas',
                  'tags':{'control_de_seguridad': 'salidas'},
                  'time':datetime.datetime.utcnow().isoformat(),
                  'fields': {'Número_salidas':TotalEntries}}]
    client.write_points(Entries_arr)
print("Serie de entradas y salidas")
