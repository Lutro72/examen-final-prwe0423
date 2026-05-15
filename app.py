# Se importan las herramientas de Flask que se van a usar
from flask import Flask, render_template, request

# Se crea la aplicación Flask
app = Flask(__name__)

# Lista con los dos usuarios del sistema

usuarios = [
    {"nombre": "juan", "contrasena": "admin", "tipo": "Administrador"},
    {"nombre": "pepe", "contrasena": "user",  "tipo": "Usuario"},
]

# Ruta principal muestra el menú con dos botones
# ------------------------------------------------------------------
@app.route('/')
def index():
    return render_template('index.html')

# Ruta del ejercicio 1, acepta GET y POST
@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    # Las variables empiezan en None hasta que se envie el formulario
    nombre         = None
    total_sin_desc = None
    descuento      = None
    total_pagar    = None

    if request.method == 'POST':
        # Obtener los valores enviados desde el formulario
        nombre   = request.form['nombre']
        edad     = int(request.form['edad'])
        cantidad = int(request.form['cantidad'])

        # Valor de cada tarro de pintura
        precio_unitario = 9000

        # Calcular el total antes de cualquier descuento
        total_sin_desc = cantidad * precio_unitario

        # Se aplica el descuento segun la edad ingresada:
        # - Menor de 18→ sin descuento
        # - Entre 18 y 30 inclusive → 15%
        # - Mayor de 30→ 25%
        if edad < 18:
            porcentaje = 0
        elif 18 <= edad <= 30:
            porcentaje = 0.15
        else:
            porcentaje = 0.25

        # Se calcula el descuento y total final
        descuento   = int(total_sin_desc * porcentaje)
        total_pagar = int(total_sin_desc - descuento)

    return render_template('ejercicio1.html',
                           nombre=nombre,
                           total_sin_desc=total_sin_desc,
                           descuento=descuento,
                           total_pagar=total_pagar)

# Ruta del ejercicio 2, acepta GET y POST
# ------------------------------------------------------------------
@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    mensaje = None

    if request.method == 'POST':
        nombre_ingresado     = request.form['nombre']
        contrasena_ingresada = request.form['contrasena']

        # Recorre la lista buscando si el usuario existe
        usuario_encontrado = None
        for u in usuarios:
            if u['nombre'] == nombre_ingresado and u['contrasena'] == contrasena_ingresada:
                usuario_encontrado = u
                break

        # Muestra el mensaje según si el usuario fue encontrado o no
        if usuario_encontrado:
            mensaje = f"Bienvenido {usuario_encontrado['tipo']} {usuario_encontrado['nombre']}"
        else:
            mensaje = "Usuario o contraseña incorrectos"

    return render_template('ejercicio2.html', mensaje=mensaje)

# Se ejecuta la aplicacion
# ------------------------------------------------------------------
if __name__ == '__main__':
    app.run(debug=True)