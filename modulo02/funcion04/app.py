def saludo():
    global nombre
    nombre = "John Doe"
    print(f'Hola {nombre}')

def despedido():
    global nombre
    print(f'Adios {nombre}')

saludo()
despedido()