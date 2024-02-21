from flask import  Flask, jsonify, request
#TODO Crear una instancia de la aplicacion Flask 
app =Flask(__name__)

#Datos de ejemplo de Usuarios
usuarios =[{'id':1, 'nombre': 'Anderson'}, {'id':2, 'nombre': 'Davis'},{'id':3, 'nombre': 'Andercode'}]

#TODO definir una ruta para la pagina principal
@app.route('/')
def hola_mundo():
    return 'Hola Mundo'


#Definir una ruta para obtener la lista de usuarios
@app.route('/usuarios')
def obtener_usuarios(): 
    #Convertir la lista de usuarios a formato JSON y devolverlos como respuesta
    return jsonify({'usuarios':usuarios})


#TODO Definir una ruta para obtener un usuario por su ID
@app.route('/usuario/<int:id_usuario>')
def obtener_usuario(id_usuario):
    #TODO Buscar el usuario por ID en la lista de Usuarios
    usuario = next((user for user in usuarios if user['id']==id_usuario),None)
#TODO:     Verificar si se encontro el usuario y devolverlo de lo contrario  responder mensaje de no encontrado
    if usuario:
        return jsonify(usuario)
    else:
        return jsonify({'mensaje':'Usuario no encontrado'}),404


@app.route('/buscar')
def buscar_usuario():
    nombre = request.args.get('nombre')
    usuarios_encontrados = [user for user in usuarios if nombre.lower() in user['nombre'].lower()]
    
    if usuarios_encontrados:
        return jsonify({'usuarios':usuarios_encontrados})
    
    else: 
        return jsonify({'mensaje': 'Usuario no encontrado'}), 404
     

#TODO:  Iniciar la aplicacion si este escript es ejecutado directamente
if __name__ == '__main__':
    #TODO: Configuracion para ejecutar la aplicacion en modo depuracion
    app.run(debug=True)
    

    
    

