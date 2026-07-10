# Smart Parking INACAP

Sistema de estacionamiento inteligente desarrollado como proyecto de la asignatura de Sistemas Embebidos.

## Descripción

El proyecto utiliza un ESP32 conectado a una aplicación web desarrollada con Flask para controlar el estado de un estacionamiento en tiempo real.

El sistema cuenta con un panel para usuarios y un panel de administración, permitiendo cambiar estados, bloquear usuarios y visualizar un historial de eventos.

---

## Funcionalidades

- Estado Disponible.
- Estado Reservado.
- Estado Ocupado.
- Estado Mantenimiento.
- Panel de administración.
- Panel de usuario.
- Bloqueo y desbloqueo de usuarios.
- Historial de cambios.
- Comunicación entre Flask y ESP32 mediante puerto serial.
- Detección de desconexión del ESP32.

---

## Tecnologías utilizadas

- Python
- Flask
- HTML
- CSS
- ESP32
- Arduino IDE
- Git y GitHub

---

## Ejecución

1. Conectar el ESP32 al computador.
2. Ejecutar:

```bash
python3 app.py
```

3. Abrir el navegador en:

```
http://127.0.0.1:5000
```

---

## Estructura del proyecto

```
.
├── app.py
├── templates
│   ├── index.html
│   └── admin.html
├── capturas
├── README.md
└── Código ESP32
```

---

## Capturas

Las capturas del funcionamiento se encuentran en la carpeta **capturas**. (Durante la carga de las capturas a GitHub desde un dispositivo móvil, varias imágenes tenían el mismo nombre (image.jpg). GitHub conservó únicamente la última imagen porque los archivos con el mismo nombre se sobrescriben. El funcionamiento completo del sistema fue verificado durante la demostración y las capturas representan el estado final del proyecto.) por lo cual dejare un link de youtube pàra que pueda ver todo

---

## Autor

Johanan Victor
Ingeniería Electrónica y Sistemas Inteligentes
INACAP
