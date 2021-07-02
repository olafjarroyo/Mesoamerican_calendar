#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 16:33:47 2019

@author: olaf
"""

from datetime import date

def calendario_mesoamericano(anio_obj,mes_obj,dia_obj):
    
    #fecha_objetivo
    fecha_objetivo = date(anio_obj,mes_obj,dia_obj)
    
    #Fecha equivalente en calendario gregoriano a fecha juliana (1519/Enero/25): 1519/Feb/4
    fecha_origen = date(1519,2,4)

    #Calcula numero de dias entre ambas fechas    
    delta = (fecha_objetivo - fecha_origen).days
            
    #------------------------------------------------------------------------------                
    #DICCIONARIO DE DATOS DE TONALPOHUALLI
    
    # Define simbolo del dia de acuerdo al Tonalpohualli
    st = ['Cipactli', 'Ehecatl', 'Calli', 'Cuetzpallin','Coatl',\
          'Miquiztli','Mazatl','Tochtli','Atl','Itzcuintli',\
          'Ozomatli','Malinalli','Acatl','Ocelotl','Cuauhtli',\
          'Cozcacuauhtli','Ollin','Tecpatl','Quiahuitl','Xochitl']
    #Numero de dia del Tonalpohualli
    nt = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    
    # Nombres de los meses del Xiuhpohualli
    sx = ['Izcalli','Atlcahualo','Tlacaxipehualiztli','Tozoztontli',\
          'Hueytozoztli','Toxcatl','Etzalcualiztli','Tecuilhuitontli',\
          'Hueytecuilhuitl','Tlaxochimaco','Xocotlhuetzi','Ochpaniztli','Teotleco',\
          'Tepeilhuitl','Quecholli','Panquetzaliztli','Atemoztli','Tititl','Nemotenmi']
    
    #Nombre de los anios del Xiuhpohualli
    yx = ['Tochtli','Acatl','Tecpatl','Calli']
    
    #Numeral de los anios
    nyxi = [1, 2, 3, 4,5,6,7,8,9,10,11,12,13]
    #------------------------------------------------------------------------------                
    # DICCIONARIO DE CALENDARIO JULIANO
    
    nm_j = ['Enero','Febrero','Marzo','Abril','Mayo','Junio',\
           'Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
    nd_j = [31,28,31,30,31,30,31,31,30,31,30,31]
    #------------------------------------------------------------------------------                
    #Parametros del calendario mesoamericano
      
    c_ndt = 5    #<-- Numeral del primer dia del calculo (Primer dia de Izcalli - 1519: 6 -Caso)
    c_sdt = 13   #<-- Simbolo del primer dia del calculo (Primer dia de Izcalli - 1519: Ocelotl -Caso)
    c_trt = c_sdt - 1   #<-- Trecena (Primer dia de la Trecena)
    
    c_msx = 0    #<-- Mes Xiuhpohualli (Izcalli - Caso)
    c_nxi = 0   #<-- Anio Xiuhpohualli (1519: Uno - Caso)
    c_sxi = 1   #<-- Anio Xiuhpohualli (1519: Acatl - Caso)

    #------------------------------------------------------------------------------       
    #PARAMETROS DEL CALCULO
    #Contadores
    co1 = 0
    co2 = 0
    
    #Vectores para ordenar la formacion durante las iteraciones
    num_t = []
    sig_t = []
    tr_t = []
    mes_xi = []
    n_xi = []
    s_xi = []
    
    d_j = []
    m_j = []
    a_j = []
    #####################################
    #Numero total de dias a calcular
    nl = 365 * 600
    #####################################
    
    #for ntd in range(0,nl+1):
    for ntd in range(0,delta+1):           
         
    #------------------------------------------------------------------------------                
    # CALCULO DE  LOS MESES DEL XIUHPOHUALLI       
            
            # Asigna el mes correspondiente cuando la cuenta llega a 20 dias
            if co1 == 20:                  
                 c_msx = c_msx + 1
                 co2 = co2 + 1
                 co1 = 0 
            if c_ndt == 0:
                c_trt = c_sdt       # import pandas as pd
# import convertdate
    #------------------------------------------------------------------------------
    # ASIGNA LOS VALORES A LOS VECTORES CORRESPONDIENTES             
            sdt = st[c_sdt] #<-- Asigna el signo correcto (Tonalpohualli)
            ndt = nt[c_ndt] #<-- Asigna el numeral correcto (Tonalpohualli)
            trt = st[c_trt] #<-- Asigna trecena (Tonalpohualli)
            msx = sx[c_msx]   #<-- Asigna mes (Xiuhpohualli)
            nxi = nyxi[c_nxi] #<-- Asigna numeral de anio (Xiuhpohualli)
            sxi = yx[c_sxi]   #<-- Asigna signo de anio (Xiuhpohualli)
            
            #Guarda los datos calculados en el arreglo
            #Tonalpohualli
            sig_t.append(sdt)  
            num_t.append(ndt)
            tr_t.append(trt)
    #        
            #Xiuhpohualli
            mes_xi.append(msx)
            n_xi.append(nxi)
            s_xi.append(sxi)
    
            co1 = co1 + 1              
    #------------------------------------------------------------------------------
           # Actualiza contadores                
            c_ndt = c_ndt + 1 #<-- Contador de numeral (Tonalpohualli)
            c_sdt = c_sdt + 1 #<-- Contador de signo (Tonalpohualli)
                     
    #------------------------------------------------------------------------------                      
             #Reincia los contadores, si han llegado al final    
            if c_ndt == len(nt):
                c_ndt = 0
                
            if c_sdt == len(st):    
               c_sdt = 0                               
            
            if c_trt == 19:
               c_trt = 0
        
            if co2 == 18 and co1 == 5 :          
                 co1 = 0
                 co2 = 0
                 c_msx = 0
                 
                 if c_sxi == 3:     
                     c_sxi = 0
                 else:                       
                     c_sxi = c_sxi + 1
                
                 if c_nxi == 12:
                     c_nxi = 0      
                 else:                       
                     c_nxi = c_nxi + 1    
                                
    #------------------------------------------------------------------------------ 
                         
    # Guarda los datos en un diccionario             
    ndc = {'Numeral': num_t, 'Signo' : sig_t,'Trecena': tr_t,'Mes': mes_xi,'N_Año':n_xi,'S_Año':s_xi,\
           'Anio_J':a_j,'Mes_J':m_j,'Dia_J':d_j}  
        
    #------------------------------------------------------------------------------     
    
    #Imprime  el resultado del ultimo dia computado   
    print("Dia: ", num_t[-1], "-" ,sig_t[-1])    
    print("Trecena: ", tr_t[-1])  
    print("Veintena: ", mes_xi[-1])  
    print("Año: ", n_xi[-1], s_xi[-1]) 
    

    

    
#%%
calendario_mesoamericano(2021,1,1)