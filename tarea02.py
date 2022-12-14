import requests
import pandas as pd
import pyshorteners
from os import system
import time

#funcion para acortar url
def Acortar_URL(url):
    s = pyshorteners.Shortener()
    newURL=s.tinyurl.short(url)
    return newURL


#metodo para ingresar al json 
    

def get_listar_pokemos(name):
    
    response=requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}")
        
    if response.status_code==200:
        payload = response.json()
        
        name=payload['name']
        id=payload['id']
        img=Acortar_URL(f'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/home/{id}.png')
                
        result=payload.get('abilities',[])
        habilidades=[]
        
        if result:
            for i in result:
                habilidades.append(i['ability']["name"])
                
    list_Pokemon=pd.DataFrame({"nombre":[name],"habilidad_es":[habilidades], "Url_img":[img]})    
                
    return list_Pokemon





#metodo listar por generacion

def Listar_generacion(l:int,N):
    list_Pokemon_gene=pd.DataFrame(columns=["nombre","habilidad_es", "Url_img"])
    response=requests.get(f"https://pokeapi.co/api/v2/generation/{N}")
    
    if response.status_code==200:
        payload = response.json()
        
        resultGen=payload.get('pokemon_species',[])
        
        if resultGen:
            j=0
            for i in resultGen:
                if j<=l:
                    list_Pokemon_gene=pd.concat([list_Pokemon_gene,get_listar_pokemos(i['name'])])
                    j+=1
                else:
                    break
    return list_Pokemon_gene     
                
#listar por tipo
def Listar_PorTipo(l:int,N):
    list_Pokemon_Tipo=pd.DataFrame(columns=["nombre","habilidad_es", "Url_img"])
    response=requests.get(f"https://pokeapi.co/api/v2/type/{N}")
    
    if response.status_code==200:
        payload = response.json()
        
        resultTipo=payload.get('pokemon',[])
        
        if resultTipo:
            j=0
            for i in resultTipo:
                if j<=l:
                    list_Pokemon_Tipo=pd.concat([list_Pokemon_Tipo,get_listar_pokemos(i['pokemon']['name'])])
                    j+=1
                else:
                    break
    print(f"pokemones de tipo: {payload['name']}")
    return list_Pokemon_Tipo            
        
#listar por habilidad

def Listar_PorHabilidad(N):
    list_Pokemon_Habilidad=pd.DataFrame(columns=["nombre","habilidad_es", "Url_img"])
    response=requests.get(f"https://pokeapi.co/api/v2/ability/{N}")
    
    if response.status_code==200:
        payload = response.json()
        
        resultHabilidad=payload.get('pokemon',[])
        
        if resultHabilidad:
            
            for i in resultHabilidad:
                list_Pokemon_Habilidad=pd.concat([list_Pokemon_Habilidad,get_listar_pokemos(i['pokemon']['name'])])
    print(f"pokemones con habilidad de: {payload['name']}")           
    return list_Pokemon_Habilidad        


#listar specie
def Listar_PorEspecie(N):
    list_Pokemon_Especie=pd.DataFrame(columns=["nombre","habilidad_es", "Url_img"])
    response=requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{N}")
    
    if response.status_code==200:
        payload = response.json()
        
        resultEspecie=payload.get('varieties',[])
        
        if resultEspecie:            
            for i in resultEspecie:
                list_Pokemon_Especie=pd.concat([list_Pokemon_Especie,get_listar_pokemos(i['pokemon']['name'])])
    #print(f"pokemones pertenecientes : {payload['name']}")           
    return list_Pokemon_Especie   

#Listar por habitad
def Listar_PorHabitad(l:int,N):
    list_Pokemon_Habitad=pd.DataFrame(columns=["nombre","habilidad_es", "Url_img"])
    response=requests.get(f"https://pokeapi.co/api/v2/pokemon-habitat/{N}")
    
    if response.status_code==200:
        payload = response.json()
        
        resultHabitad=payload.get('pokemon_species',[])
       
        if resultHabitad:
            j=0
            for i in resultHabitad:
                if j<=l:
                    list_Pokemon_Habitad=pd.concat([list_Pokemon_Habitad,Listar_PorEspecie(i['name'])])
                    j+=1
                else:
                    break
    print(f"pokemones de Habitad: {payload['name']}")
    return list_Pokemon_Habitad 

#listar por forma
def Listar_PorForma(l:int,N):
    list_Pokemon_Forma=pd.DataFrame(columns=["nombre","habilidad_es", "Url_img"])
    response=requests.get(f"https://pokeapi.co/api/v2/pokemon-shape/{N}")
    
    if response.status_code==200:
        payload = response.json()
        
        resultForma=payload.get('pokemon_species',[])
       
        if resultForma:
            j=0
            for i in resultForma:
                if j<=l:
                    list_Pokemon_Forma=pd.concat([list_Pokemon_Forma,Listar_PorEspecie(i['name'])])
                    j+=1
                else:
                    break
    print(f"pokemones de Forma: {payload['name']}")
    return list_Pokemon_Forma 

def Listar_tags(N):
    response=requests.get(f"https://pokeapi.co/api/v2/{N}")
        
    if response.status_code==200:
        payload = response.json()
               
        result=payload.get('results',[])
        listTag=[]
        
        if result:
            j=1
            for i in result:
                lisAux=[j,i["name"]]
                listTag.append(lisAux)
                j+=1  
                
    return listTag

#MENU
continuar=1
while continuar==1:
    system("cls")
    print("----------------------------------------------------")
    print("Bienvenido Al Menu")
    print("---------------------------------------------------")

    print("1:listar pokemon por generacion")
    print("2:listar pokemon segun su forma")
    print("3:listar pokemon segun una habilidad")
    print("4:listar pokemon segun su  habitad")
    print("5:listar pokemon segun su tipo")
    print("6:salir del menu")
    oppcion=input("ingrese el numero de la opcion elegida: " )
    link=""
    if oppcion==str(1):
        link="generation"
        system("cls")
        print("----------------------------------------------------")
        print("LISTAR POKEMON POR GENERACION")
        print("---------------------------------------------------")
        print(Listar_tags(link))
        print("...................................................")
        dato=input("ingrese una opci??n(numero u nombre")
        N=input("ingrese un numero(cantidad de pokemones que quiera ver)")
        print(Listar_generacion(int(N),dato))
        input("presione cualquier tecla para volver al menu")
    elif oppcion==str(2):
        link="pokemon-shape"
        print("----------------------------------------------------")
        print("LISTAR POKEMON SU FORMA")
        print("---------------------------------------------------")
        print(Listar_tags(link))
        print("...................................................")
        dato=input("ingrese una opci??n(numero 0 nombre")
        N=input("ingrese un numero(cantidad de pokemones que quiera ver)")
        print(Listar_PorForma(int(N),dato))
        input("presione cualquier tecla para volver al menu")
    elif oppcion==str(3):
        link="ability"
        print("----------------------------------------------------")
        print("LISTAR POKEMON POR UNA HABILIDAD")
        print("---------------------------------------------------")
        print(Listar_tags(link))
        print("...................................................")
        dato=input("ingrese una opci??n(numero u nombre")
        print(Listar_PorHabilidad(dato))
        input("presione cualquier tecla para volver al menu")
    elif oppcion==str(4):
        link="pokemon-habitat"
        print("----------------------------------------------------")
        print("LISTAR POKEMON SEGUN HABITAD")
        print("---------------------------------------------------")
        print(Listar_tags(link))
        print("...................................................")
        dato=input("ingrese una opci??n(numero u nombre")
        N=input("ingrese un numero(cantidad de pokemones que quiera ver)")
        print(Listar_PorHabitad(int(N),dato))
        input("presione cualquier tecla para volver al menu")
    elif oppcion==str(5):
        link="type"
        print("----------------------------------------------------")
        print("LISTAR POKEMON POR TIPO")
        print("---------------------------------------------------")
        print(Listar_tags(link)[0:18])
        print("...................................................")
        dato=input("ingrese una opci??n(numero u nombre")
        N=input("ingrese un numero(cantidad de pokemones que quiera ver)")
        print(Listar_PorTipo(int(N),dato))
        input("presione cualquier tecla para volver al menu")
    elif oppcion==str(6):
        print("saliendo del menu")
        time.sleep(2)
        continuar=2
    else:
        print("dato incorrecto, ingrese un valor valido ")
        time.sleep(2)