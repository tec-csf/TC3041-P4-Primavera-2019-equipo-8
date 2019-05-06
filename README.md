# TC3041-P4-Primavera-2019-equipo-8


La aplicación recopila datos cada segundo y los muestra en la interfaz de grafana cada 30. 
La información proviene de dos acondicionadores que regulan la temperatura junto con dos humidificadores que regulan la humedad 
en una oficina, así como de un control de acceso a ésta misma.

Según las normas promedio para la regulación de temperatura y humedad son entre 23°C y 26°C y entre 40% y 60% respectivamente. 
Para el acceso únicamente se mantiene un conteo por seguridad.

Mediciones: grados centígrados, porcentaje y enteros.
Etiquetas: Acondiconador_no1, Acondiconador_no2, Humidificador_no1, Humidificador_no2, Control_de_seguridad.
Los valores se generan aleatoriamente con funciones random de Python.


Visualización de la información disponible en la siguiente liga: http://localhost:3000/dashboard/db/new-dashboard
InfluxDB user: root password:root
Grafana user: admin  password:admin
