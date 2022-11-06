import pandas as pd
import _csv
from os import system
import time
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
    
ObjetoLibros=[]    
ListLibros=[]

#metodos
#creando objetos de tipo libro

libro1=Libro(1,"troya","fantacia","70378595","san marcas","homero, anonimo")

libro2=Libro(2,"divina comedia","culto","74859623","san agustin","dhante aliguery")


libro3=Libro(3,"aves sin nido","indigenismo","145897gh","coquito","clorinda mato de turner")


#creando listas utilizando los datos de los objetos
list1=[libro1.get_Id(),libro1.get_Titulo(),libro1.get_Genero(),libro1.get_Isbn(),libro1.get_Editorial(),libro1.get_Autor()]
list2=[libro2.get_Id(),libro2.get_Titulo(),libro2.get_Genero(),libro2.get_Isbn(),libro2.get_Editorial(),libro2.get_Autor()]
list3=[libro3.get_Id(),libro3.get_Titulo(),libro3.get_Genero(),libro3.get_Isbn(),libro3.get_Editorial(),libro3.get_Autor()]

#creando un archivo csv para luego cargarlo

with open('D:/libros01.csv','w',newline='')as csvData:
    writer=_csv.writer(csvData)
    writer.writerow(['Id','Titulo','Genero','ISBN','Editorial','Autor'])
    writer.writerow(list1)
    writer.writerow(list2)
    writer.writerow(list3)


#metodo para pasar un objeto libro a alista
def Objeto_list(a:Libro):
    list=[a.get_Id(),a.get_Titulo(),a.get_Genero(),a.get_Isbn(),a.get_Editorial(),a.get_Autor()]
    return list

#leer un archivo csv
def Cargar_archivoPC():
    with open('D:/libros01.csv') as File:
        data= _csv.reader(File,delimiter=',')
        next(data)
        for i in data:
            
            libro=Libro(i[0],i[1],i[2],i[3],i[4],(i[5]))
            ObjetoLibros.append(libro)
            ListLibros.append(Objeto_list(libro))

#metodo para listar todo los libros
def Listar_libros():
    for i in ListLibros:
        print(i)
        
#metodo para agregar un nuevo libro    
def Agregar_libro(L:Libro):
    ObjetoLibros.append(L)
    ListLibros.append(Objeto_list(L))

#metodo para eliminar un libro segun su id
def Eliminar_Libro(id):
    j=0
    for i in ObjetoLibros:
        
        if i.get_Id()==str(id):
            ObjetoLibros.pop(j)
            ListLibros.pop(j)
            break
        else:
            j+=1
#metodo buscar libro por ISBN
def Buscar_ISBN(isbn):
    for i in ListLibros:
        if i[3]==isbn:
            print(i)
        

#metodo buscar por titulo
def Buscar_Titulo(titulo):
    for i in ListLibros:
        if titulo in i[1]:
            print(i)
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

#creando el menu
aux=1
while aux==1:
    system("cls")
    print(".............................................................")
    print("bien venido a este menu")
    print(".............................................................")
    print("elige una opcion que desea realizar(escriba un numero)/n")
    print("1:Leer archivo de disco duro que cargue 3 libros.")
    print("2: Listar libros.")
    print("3: Agregar libro")
    print("4: Eliminar libro")
    print("5: Buscar libro por ISBN o por título")
    print("6: Ordenar libros por título")
    print("7: Buscar libros por autor, editorial o género")
    print("8: Buscar libros por número de autores")
    print("9: Editar o actualizar datos de un libro")
    print("10: Guardar libros en archivo de disco duro")
    print("11:salir del menu")
    
    #menu opcion 1
    opp=input("escribe el numero elejido")
    if int(opp)==1:
        system("cls")
        print("------------------------------------------------------")
        print("CARGAR ARCHIVO")
        print("------------------------------------------------------")
        Cargar_archivoPC()
        print("archivo cargado correctamente")
        time.sleep(3)
    #menu opcion 2    
    elif int(opp)==2:
        system("cls")
        print("------------------------------------------------------")
        print("LISTA DE LIBROS")
        print("------------------------------------------------------")
        
        print("id,   titulo  genero,  isbn,   editorial,  autores")
        Listar_libros()
        time.sleep(6)
        
    #menu opcion 3
    elif int(opp)==3:
        system("cls")
        print("------------------------------------------------------")
        print("AGREGANDO UN LIBRO NUEVO")
        print("------------------------------------------------------")
        id=input("ingrese el id")
        titulo=input("ingrese el titulo del libro")
        genero=input("ingrese el genero al que pertenece el libro(ejem: fantasia,belico,etc.)")
        isbn=input("ingrese el isbn del libro")
        editorial=input("ingrese la editoria")
        autor=input("ingrese el autor o los autores del libro")
        libro=Libro(id,titulo,genero,isbn,editorial,autor)
        system("cls")
        Agregar_libro(libro)
        system("cls")
        print("------------------------------------------------------")
        print("LIBRO AGREGADO CORRECTAMENTE")
        print("------------------------------------------------------")
        
        print("id,   titulo  genero,  isbn,   editorial,  autores")
        print(Objeto_list(libro))
        time.sleep(4)
    #menu opcion 4
    elif int(opp)==4:
        system("cls")
        print("------------------------------------------------------")
        print("ELIMINAR LIBRO POR ID")
        print("------------------------------------------------------")
        id=input("ingrese el id del libro que decea eliminar")
        a=len(ListLibros)
        Eliminar_Libro(id)
        b=len(ListLibros)
        if a==b:
            print("no existe un libro con ese id")
        else:
            print("Libro eliminado con exito")
        time.sleep(3)
    elif int(opp)==5:
        system("cls")
        print("------------------------------------------------------")
        print("BUSCAR LIBRO POR ISBN O TITULO")
        print("------------------------------------------------------")
        print(" INGRESA:1  para buscar por ISBN")
        print(" INGRESA:2  para buscar por titulo")
        O=input("ingrese una respuesta")
        if int(O)==1:
            system("cls")
            print("------------------------------------------------------")
            print("BUSCAR LIBRO POR ISBN")
            print("------------------------------------------------------")
            O=input('Ingrese el ISBN del libro : ')
            Buscar_ISBN(O)
            time.sleep(3)
        elif int(O)==2:
            system("cls")
            print("------------------------------------------------------")
            print("BUSCAR LIBRO POR ISBN")
            print("------------------------------------------------------")
            O=input('Ingrese el titulo del libro : ')
            Buscar_Titulo(O)
            time.sleep(3)
        else:
            print("dato incorrecto...")
            print("saliendo al menu principal.")
            time.sleep(3)
        



    elif int(opp)==6:
        print("\nLIBROS ORDENADOS POR TITULO\n")
        ordenar_Titulo()
        print("\n")
        
    elif int(opp)==7:
        print("\n")
        print("1.Autor")
        print("2.Editorial")
        print("3.genero\n")
        option = input("elige una opcion: \n")
        while int(option) not in [1,2,3]:
            print("opción incorrecta")
        if int(option) == 1:
            autor = input("Ingrese autor: \n")
            while autor not in [libro[5] for libro in ListLibros if libro[5] == autor]:     
                print("Autor no encontrado en biblioteca")
                autor = input("Ingrese autor: ")
            print("\n")
            Buscar_Autor(autor)
            print("\n")
            time.sleep(2)
            print("\n")
        elif int(option) == 2:
            editorial = input("Ingrese editorial: \n")
            while editorial not in [libro[4] for libro in ListLibros if libro[4] == editorial]:     
                print("Editorial no encontrado en biblioteca")
                editorial = input("Ingrese editorial: ")
            print("\n")
            Buscar_Editorial(editorial)
            print("\n")
            time.sleep(2)
        elif int(option) == 3:
            genero = input("Ingrese genero: \n")
            while genero not in [libro[2] for libro in ListLibros if libro[2] == genero]:     
                print("Genero no encontrado en biblioteca")
                genero = input("Ingrese genero: ")
            print("\n")
            Buscar_Genero(genero)
            print("\n")
            time.sleep(2)

    elif int(opp)==8:
        numero = input("Ingrese el número de autores: ")
        print("\n")
        Buscar_Num_Autores(numero)
        print("\n")

    elif int(opp)==9:
        id = input("Ingrese ID del libro: ")
        Actualizar_Libro(id)
    
    elif int(opp)==10:
        guardar_Libros_Csv()
        time.sleep(3)

    else:
        print("opcion invalida")
