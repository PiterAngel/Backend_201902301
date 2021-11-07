class usuario:
    def __init__(self,nombre, genero, username, correo, password):
        self.nombre = nombre
        self.genero = genero
        self.username=username
        self.correo = correo
        self.password= password
        
#=============================================
    def getNombre(self):
        return self.nombre

    def setNombre(self,nombre):
        self.nombre = nombre
#=============================================
    def getGenero(self):
        return self.genero

    def setGenero(self,genero):
        self.genero = genero
#============================================= 
    def getUsername(self):
        return self.username

    def setUsername(self,username):
        self.username = username
#=============================================
    def getCorreo(self):
        return self.correo

    def setCorreo(self,correo):
        self.correo = correo
#=============================================
    def getPassword(self):
        return self.password

    def setPassword(self,password):
        self.password = password
#=====================================
  



        