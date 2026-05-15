# Importamos Flask, render_template y request desde el módulo flask
from flask import Flask, render_template, request

# Creamos la instancia de la aplicación Flask
app = Flask(__name__)

# ------------------------------------------------------------------
# USUARIOS PREREGISTRADOS — Ejercicio 2
# Lista con dos diccionarios, uno por cada usuario del sistema
# ------------------------------------------------------------------
usuarios = [
    {"nombre": "juan", "contrasena": "admin", "tipo": "Administrador"},
    {"nombre": "pepe", "contrasena": "user",  "tipo": "Usuario"},
]

# ------------------------------------------------------------------
# PRINCIPAL- muestra el menú con dos botones
# ------------------------------------------------------------------
@app.route('/')
def index():
    return render_template('index.html')

# ------------------------------------------------------------------
# EJERCICIO 1 — Cálculo de compras de pintura
# GET: muestra el formulario en blanco
# POST: recibe los datos, calcula y devuelve los resultados
# ------------------------------------------------------------------
@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    # Inicializa en None para que Jinja2 no muestre resultados en GET
    nombre         = None
    total_sin_desc = None
    descuento      = None
    total_pagar    = None

    if request.method == 'POST':
        # Obtener los valores enviados desde el formulario
        nombre   = request.form['nombre']
        edad     = int(request.form['edad'])
        cantidad = int(request.form['cantidad'])

        # Precio unitario fijo según enunciado
        precio_unitario = 9000

        # Calcular el total antes de cualquier descuento
        total_sin_desc = cantidad * precio_unitario

        # Tramos de descuento según edad (especificación del examen):
        # - Menor de 18        → sin descuento
        # - Entre 18 y 30 inclusive → 15%
        # - Mayor de 30        → 25%
        if edad < 18:
            porcentaje = 0
        elif 18 <= edad <= 30:
            porcentaje = 0.15
        else:
            porcentaje = 0.25

        # Monto descontado y total final
        descuento   = total_sin_desc * porcentaje
        total_pagar = total_sin_desc - descuento

    return render_template('ejercicio1.html',
                           nombre=nombre,
                           total_sin_desc=total_sin_desc,
                           descuento=descuento,
                           total_pagar=total_pagar)

# ------------------------------------------------------------------
# EJERCICIO 2 — Login con usuarios preregistrados
# GET: muestra el formulario en blanco
# POST: verifica credenciales y muestra mensaje
# ------------------------------------------------------------------
@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    mensaje = None

    if request.method == 'POST':
        nombre_ingresado     = request.form['nombre']
        contrasena_ingresada = request.form['contrasena']

        # Recorremos la lista buscando coincidencia de nombre Y contraseña
        usuario_encontrado = None
        for u in usuarios:
            if u['nombre'] == nombre_ingresado and u['contrasena'] == contrasena_ingresada:
                usuario_encontrado = u
                break

        # Mensaje según resultado — formato exacto del enunciado
        if usuario_encontrado:
            mensaje = f"Bienvenido {usuario_encontrado['tipo']} {usuario_encontrado['nombre']}"
        else:
            mensaje = "Usuario o contraseña incorrectos"

    return render_template('ejercicio2.html', mensaje=mensaje)

# ------------------------------------------------------------------
# EJECUTAR LA APLICACIÓN
# ------------------------------------------------------------------
if __name__ == '__main__':
    app.run(debug=True)