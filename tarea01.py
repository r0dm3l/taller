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
