class publicaciones:
    def __init__(self, tipo, url,date,categoria, author):
        
        self.tipo = tipo
        self.url = url
        self.date = date
        self.categoria = categoria
        self.author = author
        


#=====================================
    def getTipo (self):
        return self.tipo

    def setTipo (self,tipo):
        self.tipo = tipo
#=====================================
    def getCategoria (self):
        return self.categoria

    def setCategoria (self,categoria):
        self.categoria = categoria
#=====================================
    def getUrl (self):
        return self.url

    def setUrl (self,url):
        self.url = url
#=====================================
    def getDate (self):
        return self.date

    def setDate (self,date):
        self.date = date
#=====================================
    def getAuthor (self):
        return self.author

    def setAuthor (self,author):
        self.author = author