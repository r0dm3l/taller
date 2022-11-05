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


print (biblioteca[1].get_Genero())
