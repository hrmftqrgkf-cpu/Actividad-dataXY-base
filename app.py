from flask import Flask, render_template, redirect, url_for
import serial
import time
from datetime import datetime

app = Flask(__name__)

# Configuración del puerto serial del ESP32
PUERTO_ESP32 = "/dev/ttyUSB0"
BAUDIOS = 115200

# Estado actual del estacionamiento
estado_actual = "Disponible"
control_usuario = True
historial = ["Sistema iniciado - Estado: Disponible"]

def enviar_estado(codigo, nombre_estado):
    global estado_actual

    try:
        with serial.Serial(PUERTO_ESP32, BAUDIOS, timeout=1) as esp32:
            time.sleep(2)
            esp32.write(f"{codigo}\n".encode())

        estado_actual = nombre_estado
        historial.append(f"{datetime.now().strftime('%H:%M:%S')} - {nombre_estado}")

    except Exception as e:
        historial.append(f"Error: {e}")
@app.route("/")
def index():
    return render_template(
        "index.html",
        estado=estado_actual,
        historial=historial[::-1]
    )
@app.route("/admin")
def admin():
    return render_template(
        "admin.html",
        estado=estado_actual,
        historial=historial[::-1]
    )


@app.route("/disponible")
def disponible():
    enviar_estado(0, "Disponible")
    return redirect(url_for("index"))

@app.route("/reservado")
def reservado():
    enviar_estado(1, "Reservado")
    return redirect(url_for("index"))

@app.route("/ocupado")
def ocupado():
    enviar_estado(2, "Ocupado")
    return redirect(url_for("index"))


@app.route("/admin/disponible")
def admin_disponible():
    enviar_estado(0, "Disponible")
    return redirect(url_for("admin"))

@app.route("/admin/reservado")
def admin_reservado():
    enviar_estado(1, "Reservado")
    return redirect(url_for("admin"))

@app.route("/admin/ocupado")
def admin_ocupado():
    enviar_estado(2, "Ocupado")
    return redirect(url_for("admin"))

@app.route("/admin/mantenimiento")
def admin_mantenimiento():
    enviar_estado(3, "Mantenimiento")
    return redirect(url_for("admin"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
