from flask import Flask, jsonify, request
from flask_cors import CORS
import json

from usuario import usuario
from publicaciones import publicaciones


app=Flask(__name__)
CORS(app)

Publicaciones = [] #listas xd 

usuarios = [] #listas xd

usuarios.append(usuario("Abner Cardona", "M", "admin", "admin@ipc1.com", "admin@ipc1")) #PARA QUE ESTE GUARDADO


@app.route('/Registrar' , methods = ['POST']) #RETORNAR
def registrarUsuarios(): #REGISTRAR POST
    global usuarios
    nombre = request.json['name']
    genero = request.json['gender']
    username = request.json['username']
    email = request.json['email']
    password = request.json['password']
    if verificarPassword(password)==True:
        usuarios.append(usuario(nombre,genero,username,email,password))
        return(jsonify({
            'Mensaje': 'Se ah registrado con éxito :3',
            'Entrar': 'SI'
        }))
    return(jsonify({
            'Mensaje': 'Ingrese una contraseña válida que contenga un número, un simbolo y tenga como mínimo 8 carácteres',
            'Entrar': 'NO'
        }))


        




def validarinfo(usernamexd,passwordxd):
    for usuario in usuarios:
        if usernamexd == usuario.getUsername():
            if passwordxd == usuario.getPassword():
                return True
    return False




    

def verificarPassword(verpass):
    
    if len(str(verpass)) >= 8:
        return True
    
@app.route('/VerUsuarios', methods = ['GET'])
def verUsuarios(): 
    global usuarios
    verusu = [] #lista xd 
    for usuario in usuarios:
        u = {
            'name':usuario.getNombre(),
            'gender':usuario.getGenero(),
            'username':usuario.getUsername(),
            'email':usuario.getCorreo(),
            'password':usuario.getPassword()
        }
        verusu.append(u)
    return(jsonify(verusu))

@app.route('/Iniciar', methods = ['POST'])
def login():
    username = request.json['user']
    contrasena = request.json['contras']
    if username == "admin" and contrasena == "admin@ipc1":
        return (jsonify({
            'Mensaje': 'Bienvenido' + username,
            'Tipo': 'Admin',
        }))
    elif validarinfo(username,contrasena) == True:
        return(jsonify({
            "Mensaje": "Bienvenido Usuario",
            "Tipo": "Usuario",
            "user": str(username)}))
    return (jsonify({
            'Mensaje': 'Sus credenciales son inválidas',
            'Tipo': 'Nadie',
        }))

@app.route('/CrearPublicacion', methods= ['POST'])
def CrearPublicacion():
    global Publicaciones
    
    tipo = request.json['type']
    url = request.json['url']
    date = request.json['date']
    categoria = request.json['category']
    
    nuevo2 = publicaciones(tipo, url, date, categoria,"Usuario")
    Publicaciones.append(nuevo2)
    return (jsonify({
        'Mensaje':'Se publico con exito'
    }))

@app.route('/VerPublicaciones', methods= ['GET'])
def VerPublicacion():
    global Publicaciones
    Datos = []
    for publicaciones in Publicaciones:
        objeto = {
            'type': publicaciones.getTipo(),
            'url': publicaciones.getUrl(),
            'date': publicaciones.getDate(),
            'category': publicaciones.getCategoria(),
            'author': publicaciones.getAuthor()
        }
        Datos.append(objeto)
    return(jsonify(Datos))












if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)