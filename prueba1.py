# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 19:33:41 2020

@author: MATEO
"""
def caso_who(ruta_archivo_csv: str)-> dict:
    import pandas as pd
    # import matplotlib.pyplot as plt
    
    if ruta_archivo_csv[-3:] =='csv' : 
        try :
            baseDatosppal = pd.read_csv(ruta_archivo_csv)
            continentes=baseDatosppal.continent
            fechas=baseDatosppal.date
            
            poblacion= baseDatosppal.population
            camaspormil=baseDatosppal.hospital_beds_per_thousand
            camasTotales= (camaspormil*poblacion)/1000
            
            casospormillon=baseDatosppal.total_cases_per_million
            
            casosTotales= (casospormillon*poblacion)/1000000
            razon_camas= casosTotales/camasTotales
            
            fechas.name='date'
            continentes.name='continent'
            razon_camas.name='razon_camas'
            
            casosDiarios = pd.concat([continentes,fechas,razon_camas], axis=1)
            casosDiarios.set_index('date')
            casosDiarios['date']=pd.to_datetime(casosDiarios['date'])
            
            resultado=  casosDiarios.groupby(['date','continent']).razon_camas.mean().unstack()
            
            
            # resultado.plot(kind='line')
            # plt.show()
            
            resultadoFinal= resultado.to_dict()
            return resultadoFinal
        
        except: 
            return 'Error al leer el archivo de datos.'
    else :
        return 'Extensión inválida.'        
  
   

print(caso_who(r"C:\Users\MATEO\Desktop\compartid\programacion mintic2020\actividades propuestas\reto_semana_5\owid-covid-data.csv"))

