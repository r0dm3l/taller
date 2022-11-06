class Libro:
    #constructor
    def __init__(self,id,titulo,genero,isbn,editorial,autor):
        self.__id=id
        self.__titulo=titulo
        self.__genero=genero
        self.__isbn=isbn
        self.__editorial=editorial
        self.__autor=autor
        
    #Getters(métodos GET)
    
    def get_Id(self):
        return self.__id
    
    def get_Titulo(self):
        return self.__titulo
    
    def get_Genero(self):
        return self.__genero
    
    def get_Isbn(self):
        return self.__isbn
    
    def get_Editorial(self):
        return self.__editorial
    
    def get_Autor(self):
        return self.__autor
    
    #Setters(métodos Set)
    def set_Titulo(self,titulo):
        self.__titulo = titulo
    
    def set_Genero(self,genero):
        self.__genero = genero
    
    def set_Isbn(self, isbn):
        self.__isbn = isbn
    
    def set_Editorial(self,editorial):
        self.__editorial = editorial
    
    def set_Autor(self, autor):
        self.__autor = autor
    
biblioteca={}

#metodos

libro1=Libro(1,"troya",["fantacia","belico","mitologia"],"70378595","san marcas","homero")

libro2=Libro(2,"divina comedia","culto","74859623","san agustin","dhante aliguery")

#metodo ordenar libros por titulo
def ordenar_Titulo():
    df=pd.DataFrame(ListLibros,columns=['id','titulo','genero','isbn','editorial','autor_es'])
    print(df.sort_values('titulo',ascending=True))

#metodo buscar por Autor
def Buscar_Autor(autor):
    for i in ListLibros:
        for j in i:
            if autor in j:
                print(i)
                break
#buscar por editorial
def Buscar_Editorial(editorial):
    for i in ListLibros:
        if editorial in i[4]:
            print(i)

#buscar por genero
def Buscar_Genero(genero):
    for i in ListLibros:
        if genero in i[2]:
            print(i)
            
#Buscar por numero de autores            
def Buscar_Num_Autores(N):
    for i in ListLibros:
        if str(i[5].count(',')+1)==str(N):
            print(i)

#metodo actualizar libro            
def Actualizar_Libro(id):

    titulo = input("Actualizar titulo: ")
    genero = input("Actualizar genero")
    isbn = input("Actualizar ISBN")
    editorial = input("Actualizar editorial")
    autor = input("Actualizar autor")

    j=0
    
    for i in ObjetoLibros:        
        if i.get_Id()==str(id):
            ObjetoLibros[j].set_Titulo(titulo)
            ObjetoLibros[j].set_Genero(genero)
            ObjetoLibros[j].set_Isbn(isbn)
            ObjetoLibros[j].set_Editorial(editorial)
            ObjetoLibros[j].set_Autor(autor)
            ListLibros[j]=Objeto_list(ObjetoLibros[j])
            
            break
        else:
            j+=1

#metod Guardar libros en csv
def guardar_Libros_Csv():
    df=pd.DataFrame(ListLibros,columns=['id','titulo','genero','isbn','editorial','autor_es'])
    df.to_csv('/home/frank/Escritorio/Python/silabuz/trabajo_unidad1/libros/libroFinal.csv',sep=',',index=False)
    print("archivo csv creado con exito")
