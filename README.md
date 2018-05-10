

#  Cliente Basado en MQTT.

## Requisitos de Software

### Instalación de paho.mqtt
Este projecto requiere de la instalción de python y sus dependencias.
```batch
pip install paho-mqtt
```

### Clonar el repositorio:
Creamos una carpeta donde se desea almacenar el cliente de MQTT.


```batch
mkdir projects/ && cd projects/
```
Clonar el repositorio hospedado en GitHub

```batch
git clone https://github.com/CURSOS-TEC/python-mqtt-client.git
```   
### Configurar  el archivo defaults.json 
Para que el cliente envíe datos, se debe de configurar el siguiente archivo json

```json
	{
	"broker_address" : "xxx.yyyy.com",
	"serverPort" :00000,
	"user" : "*******",
	"password" : "*******",
	"topic": "soa/expo3",
	"clientId" :"*******",
	"auth": true

}
```


### Ejecutar el archivo test.py de paquetes
Para que el cliente envíe datos, se debe de utilizar el siguiente comando

```batch
	python test.py
```
