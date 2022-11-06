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
