# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 17:46:51 2024

@author: Tame
"""

#import time
import numpy as np
#import pandas as pd
#from matplotlib import pyplot as plt
import skfuzzy as fuzz
from skfuzzy import control as ctrl
#import math
#Input and output variables
Qg = ctrl.Antecedent(np.arange(0,61,1),'Qg')
Qr = ctrl.Antecedent(np.arange(0,61,1),'Qr')
Emg = ctrl.Antecedent(np.arange(0,3,1),'Emg')
Emr = ctrl.Antecedent(np.arange(0,3,1),'Emr')
Wtg = ctrl.Antecedent(np.arange(0,201,1),'Wtg')
Wtr = ctrl.Antecedent(np.arange(0,201,1),'Wtr')
Dr = ctrl.Antecedent(np.arange(0, 101, 1), 'Dr')  
Dg = ctrl.Antecedent(np.arange(0, 101, 1), 'Dg') 
Dht= ctrl.Consequent(np.arange(0,81,1), 'Dht')
Pem= ctrl.Consequent(np.arange(0,3,1), 'Pem')
Swr= ctrl.Consequent(np.arange(0,3,1),'Swr')
OGd= ctrl.Consequent(np.arange(0,101,1),'OGd')
Ge=  ctrl.Consequent(np.arange(0,91,1),'Ge')

# Antecedent Membership functions
Qg['zero']= fuzz.trimf(Qg.universe,[0,0,15])
Qg['small']= fuzz.trimf(Qg.universe,[0,15,30])
Qg['medium']= fuzz.trimf(Qg.universe,[15,30,45])
Qg['large']= fuzz.trimf(Qg.universe,[30,45,60])
Qg['very large']= fuzz.smf(Qg.universe, 45,60)
#Qg.view()
Qr['zero']= fuzz.trimf(Qr.universe,[0,0,15])
Qr['small']= fuzz.trimf(Qr.universe,[0,15,30])
Qr['medium']= fuzz.trimf(Qr.universe,[15,30,45])
Qr['large']= fuzz.trimf(Qr.universe,[30,45,60])
Qr['very large']= fuzz.smf(Qr.universe, 45,60)
#Qr.view()
Emg['none']= fuzz.zmf(Emg.universe, 0, 1)
Emg['few']= fuzz.smf(Emg.universe,0, 1)
Emg['many']= fuzz.smf(Emg.universe,1, 2)
#Eg.view()
# emergency_vehicles_in_current_lane.view()
#P.view()
Emr['none']= fuzz.zmf(Emr.universe, 0, 1)
Emr['few']= fuzz.smf(Emr.universe, 0, 1)
Emr['many']= fuzz.smf(Emr.universe, 1, 2)

Wtr ['zero'] = fuzz.trimf(Wtr.universe,[0,0,50])
Wtr ['short'] = fuzz.trimf(Wtr.universe,[0,50,100])
Wtr ['medium'] = fuzz.trimf(Wtr.universe,[50,100,150])
Wtr ['long'] = fuzz.trimf(Wtr.universe,[100,150,200])
Wtr ['very long'] = fuzz.smf(Wtr.universe,150,200)

#Wtr.view()
Wtg ['zero'] = fuzz.trimf(Wtg.universe,[0,0,50])
Wtg ['short'] = fuzz.trimf(Wtg.universe,[0,50,100])
Wtg ['medium'] = fuzz.trimf(Wtg.universe,[50,100,150])
Wtg ['long'] = fuzz.trimf(Wtg.universe,[100,150,200])
Wtg ['very long'] = fuzz.smf(Wtg.universe,150,200)
#Wtg.view()
Dr['close']=fuzz.trimf(Dr.universe,[0,0,25])
Dr['medium']=fuzz.trimf(Dr.universe,[0,25,75])
Dr['far']=fuzz.smf(Dr.universe,25,75)

Dg['close']=fuzz.trimf(Dg.universe,[0,0,25])
Dg['medium']=fuzz.trimf(Dg.universe,[0,25,75])
Dg['far']=fuzz.smf(Dg.universe,25,75)

# Consuquent  Membership functions
Pem['no']= fuzz.zmf(Pem.universe, 0, 1)
Pem['Emg']= fuzz.smf(Pem.universe, 0, 1)
Pem['Emr']= fuzz.smf(Pem.universe, 1, 2)
#Pem.view()
Swr['switchr']= fuzz.smf(Swr.universe, 0, 1)
Swr['keepg']= fuzz.smf(Swr.universe, 1, 2)
#Swr.view()
Dht['zero']= fuzz.trimf(Dht.universe,[0,0,20])
Dht['small']= fuzz.trimf(Dht.universe,[0,20,40])
Dht['medium']= fuzz.trimf(Dht.universe,[20,40,60])
Dht['large']= fuzz.trimf(Dht.universe,[40,60,80])
Dht['very large']= fuzz.smf(Dht.universe,60, 80)

OGd['switch']=fuzz.trimf(OGd.universe,[0,0,25])
OGd['short']=fuzz.trimf(OGd.universe,[0,25,75])
OGd['medium']=fuzz.smf(OGd.universe,25,75)

#Dht.view()
Ge['turnr']= fuzz.trimf(Ge.universe,[0,0,25])
Ge['short']= fuzz.trimf(Ge.universe,[0,25,50])
Ge['medium']= fuzz.trimf(Ge.universe,[25,50,75])
Ge['long']= fuzz.trimf(Ge.universe,[50,75,90])
Ge['very long']= fuzz.smf(Ge.universe,75,90)
#Ge.view()

# Module Prioritize Emergency Car
rule1 = ctrl.Rule(Emg['none'] & Emr['none'], Pem['no'])
rule2 = ctrl.Rule(Emg['none'] & Emr['few'] | 
                  Emg['none'] & Emr['many'],Pem['Emr'])
rule3 = ctrl.Rule(Emg['few'] & Emr['none'] | 
                  Emg['many'] & Emr['none'],Pem['Emg'])
rule4 = ctrl.Rule(Emg['few'] & Emr['few'] | 
                  Emg['many'] & Emr['few'],Pem['Emg'])
rule5 = ctrl.Rule(Emg['few'] & Emr['many'], Pem['Emr'])
rule6 = ctrl.Rule(Emg['many'] & Emr['many'], Pem['Emg'])

#Module of Degree of heavy traffic in red phase.
rule7 = ctrl.Rule(Qr['zero'] & Wtr['zero'] | Qr['zero'] & Wtr['short'], Dht['zero'])
rule8 = ctrl.Rule(Qr['zero'] & Wtr['medium'] | Qr['zero'] & Wtr['long'], Dht['small'])
rule9 = ctrl.Rule(Qr['zero'] & Wtr['very long'], Dht['medium'])
rule10 = ctrl.Rule(Qr['small'] & Wtr['zero'], Dht['zero'])
rule11 = ctrl.Rule(Qr['small'] & Wtr['short'], Dht['small'])
rule12 = ctrl.Rule(Qr['small'] & Wtr['medium'] | Qr['small'] & Wtr['long'], Dht['medium'])
rule13 = ctrl.Rule(Qr['small'] & Wtr['very long'], Dht['large'])
rule14 = ctrl.Rule(Qr['medium'] & Wtr['zero'], Dht['small'])
rule15 = ctrl.Rule(Qr['medium'] & Wtr['short'] |Qr['medium'] & Wtr['medium'], Dht['medium'])
rule16 = ctrl.Rule(Qr['medium'] & Wtr['long']|Qr['medium'] & Wtr['very long'], Dht['large'])
rule17 = ctrl.Rule(Qr['large'] & Wtr['zero'] | Qr['large'] & Wtr['short'], Dht['medium'])
rule18 = ctrl.Rule(Qr['large'] & Wtr['medium'] | Qr['large'] & Wtr['long'], Dht['large'])
rule19 = ctrl.Rule(Qr['large'] & Wtr['very long'], Dht['very large'])
rule20 = ctrl.Rule(Qr['very large'] & Wtr['zero'], Dht['medium'])
rule21 = ctrl.Rule(Qr['very large'] & Wtr['short'], Dht['large'])
rule22 = ctrl.Rule(Qr['very large'] & Wtr['medium'] |Qr['very large'] & Wtr['long'] |
                   Qr['very large'] & Wtr['very long'], Dht['very large'])

#module of calculating waiting time module
rule23 = ctrl.Rule(Dht['zero'] | Qg['large'] & Wtr['zero'] & Wtg['zero'] |
                   Wtr['zero'] & Wtg['short'] |Wtr['zero'] &  Wtg['medium'] | 
                   Wtr['zero'] & Wtg['long'] | Wtr['zero'] & Wtg['very long'], 
                   Swr['keepg'])
rule24 =ctrl.Rule(Dht['zero'] | Qg['large'] & Wtr['short'] & Wtg['zero'] |  
                  Wtr['medium'] & Wtg['zero'] |  Wtr['long'] & Wtg['zero'] | 
                  Wtr['very long'] & Wtg['zero'],
                  Swr['switchr'])
rule25 =ctrl.Rule(Dht['zero'] | Qg['large'] & Wtr['short'] & Wtg['short'] |
                  Wtr['short'] & Wtg['medium'] | Wtr['short'] & Wtg['long'] |
                  Wtr['short'] & Wtg['very long'],Swr['keepg'] )
rule26 =ctrl.Rule(Dht['zero'] | Qg['large'] & Wtr['medium'] & Wtg['short'] | 
                 Wtr['long'] & Wtg['short'] |Wtr['very long'] & Wtg['short'],
                 Swr['switchr'])
rule27 =ctrl.Rule(Dht['zero'] | Qg['large'] &  Wtr['medium'] & Wtg['medium'] | 
                  Wtr['medium'] & Wtg['long'] |Wtr['medium'] & Wtg['very long'], 
                  Swr['keepg'])
rule28 = ctrl.Rule(Dht['zero'] | Qg['large'] & Wtr['long'] & Wtg['medium'] |
                   Wtr['very long'] & Wtg['medium'],Swr['switchr'])
rule29= ctrl.Rule(Dht['zero'] | Qg['large'] & Wtr['long'] & Wtg['long'] | 
                  Wtr['long'] & Wtg['very long'],Swr['keepg'])
rule30 = ctrl.Rule(Dht['zero'] | Qg['large'] & Wtr['very long'] & Wtg['long'],Swr['switchr'])
rule31 = ctrl.Rule(Dht['zero'] | Qg['large'] & Wtr['very long'] & Wtg['very long'],Swr['keepg'])
rule32= ctrl.Rule(Dht['small'] | Qg['large'] & Wtr['zero'] & Wtg['zero'] |
                  Wtr['zero'] & Wtg['short']|Wtr['zero'] & Wtg['medium']|
                  Wtr['zero'] & Wtg['long']| Wtr['zero'] & Wtg['very long'],Swr['keepg'])
rule33 =ctrl.Rule(Dht['small'] | Qg['large'] & Wtr['short'] & Wtg['zero'] | 
                  Wtr['medium'] & Wtg['zero']|Wtr['long'] & Wtg['zero']|
                  Wtr['very long'] & Wtg['zero'], Swr['switchr'])
rule34= ctrl.Rule(Dht['small'] | Qg['large'] & Wtr['short'] & Wtg['short'] | 
                  Wtr['short'] & Wtg['medium'] |Wtr['short'] & Wtg['long']|
                  Wtr['short'] & Wtg['very long'],Swr['keepg'])
rule35 =ctrl.Rule(Dht['small']| Qg['large'] & Wtr['medium'] & Wtg['short'] | 
                  Wtr['long'] & Wtg['short'] | Wtr['very long'] & Wtg['short'],Swr['switchr'])
rule36 = ctrl.Rule(Dht['small'] | Qg['large'] & Wtr['medium'] & Wtg['medium'] | 
                   Wtr['medium'] & Wtg['long'] | Wtr['medium'] & Wtg['very long'],Swr['keepg'])
rule37 = ctrl.Rule(Dht['small'] | Qg['large'] & Wtr['long']  & Wtg['medium']| 
                   Wtr['very long'] & Wtg['medium'],Swr['switchr'])
rule38 = ctrl.Rule(Dht['small'] | Qg['large'] & Wtr['long'] & Wtg['long']|
                   Wtr['long'] & Wtg['very long'], Swr['keepg'])
rule39 = ctrl.Rule(Dht['small'] | Qg['large'] & Wtr['very long'] & Wtg['long'],Swr['switchr'])
rule40 = ctrl.Rule(Dht['small'] | Qg['large'] & Wtr['very long'] & Wtg['very long'],Swr['keepg'])
rule41 = ctrl.Rule(Dht['zero'] | Qg['very large'] & Wtr['zero'] & Wtg['zero'] |
                   Wtr['zero'] & Wtg['short']|Wtr['zero'] & Wtg['medium']|
                   Wtr['zero'] & Wtg['long']| Wtr['zero'] & Wtg['very long'],Swr['keepg'])
rule42 = ctrl.Rule(Dht['zero'] | Qg['very large'] &  Wtr['short'] & Wtg['zero'] |
                   Wtr['medium'] & Wtg['zero']|Wtr['long'] & Wtg['zero']|
                   Wtr['very long'] & Wtg['zero'], Swr['switchr'])
rule43 = ctrl.Rule(Dht['zero'] | Qg['very large'] & Wtr['short'] & Wtg['short'] | 
                   Wtr['short'] & Wtg['medium'] | Wtr['short'] & Wtg['long'] | 
                   Wtr['short'] & Wtg['very long'], Swr['keepg'])
rule44 = ctrl.Rule(Dht['zero'] | Qg['very large'] & Wtr['medium'] & Wtg['short'] | 
                   Wtr['long'] & Wtg['short'] |Wtr['very long'] & Wtg['short'],Swr['switchr'])
rule45= ctrl.Rule(Dht['zero'] | Qg['very large'] & Wtr['medium'] & Wtg['medium'] | 
                  Wtr['medium'] & Wtg['long'] | Wtr['medium'] & Wtg['very long'],Swr['keepg'])
rule46 = ctrl.Rule(Dht['zero'] | Qg['very large'] & Wtr['long'] & Wtg['medium'] |
                   Wtr['very long'] & Wtg['medium'], Swr['switchr'])
rule47 = ctrl.Rule(Dht['zero'] | Qg['very large'] & Wtr['long'] & Wtg['long'] |
                   Wtr['long'] & Wtg['very long'], Swr['keepg'])
rule48 = ctrl.Rule(Dht['zero'] | Qg['very large'] & Wtr['very long'] & Wtg['long'],Swr['switchr'])
rule49 = ctrl.Rule(Dht['zero'] | Qg['very large'] & Wtr['very long'] & Wtg['very long'],Swr['keepg'])
rule50 = ctrl.Rule(Dht['small'] | Qg['very large'] & Wtr['zero'] & Wtg['zero'] |
                   Wtr['zero'] & Wtg['short']|
                   Wtr['zero'] & Wtg['medium']| Wtr['zero'] & Wtg['long']| 
                   Wtr['zero'] & Wtg['very long'],Swr['keepg'])
rule51 = ctrl.Rule(Dht['small'] | Qg['very large'] & Wtr['short'] & Wtg['zero'] | 
                   Wtr['medium'] & Wtg['zero'] |  Wtr['long'] & Wtg['zero'] | 
                   Wtr['very long'] &  Wtg['zero'], Swr['switchr'])
rule52 = ctrl.Rule(Dht['small'] | Qg['very large'] & Wtr['short'] & Wtg['short'] |
                   Wtr['short'] & Wtg['medium'] | Wtr['short'] & Wtg['long'] |
                   Wtr['short'] & Wtg['very long'], Swr['keepg'])
rule53 = ctrl.Rule(Dht['small'] | Qg['very large'] & Wtr['medium'] & Wtg['short'] |
                   Wtr['long'] & Wtg['short'] | Wtr['very long'] & Wtg['short'],Swr['switchr'])
rule54 = ctrl.Rule(Dht['small'] | Qg['very large'] & Wtr['medium'] & Wtg['medium'] |
                   Wtr['medium'] & Wtg['long'] | Wtr['medium'] & Wtg['very long'],Swr['keepg'])
rule55 = ctrl.Rule(Dht['small'] | Qg['very large'] & Wtr['long'] & Wtg['medium'] |
                   Wtr['very long'] & Wtg['medium'], Swr['switchr'])
rule56 = ctrl.Rule(Dht['small'] | Qg['very large'] & Wtr['long'] & Wtg['long'] |
                   Wtr['long'] & Wtg['very long'], Swr['keepg'])
rule57 = ctrl.Rule(Dht['small'] | Qg['very large'] & Wtr['very long'] & Wtg['long'],Swr['switchr'])
rule58 = ctrl.Rule(Dht['small']| Qg['very large'] & Wtr['very long'] & Wtg['very long'],Swr['keepg'])

#Exceptional Fuzzy Rules
rule59 =  ctrl.Rule(Dht['medium'] | Qg['zero'] & Dht['large'] | Qg['zero'] &
                      Wtr['zero'] & Wtg['short'] |  Wtr['zero'] & Wtg['medium'] |
                      Wtr['zero'] & Wtg['long'] |  Wtr['zero'] & Wtg['very long'],Swr['keepg'])
rule60 =  ctrl.Rule(Dht['medium'] | Qg['small'] & Dht['large'] | Qg['small'] & Dht['very large'] | Qg['small'] &
                     Wtr['zero'] & Wtg['zero'] |  Wtr['zero'] & Wtg['short'] |  Wtr['zero'] & Wtg['medium'] |
                      Wtr['zero'] & Wtg['long'] |  Wtr['zero'] & Wtg['very long'],Swr['keepg'])
rule61 =  ctrl.Rule(Dht['medium'] | Qg['medium'] & Dht['large'] | Qg['medium'] & Dht['very large'] | Qg['medium'] &
                     Wtr['zero'] & Wtg['zero'] |  Wtr['zero'] & Wtg['short'] |  Wtr['zero'] & Wtg['medium'] |
                      Wtr['zero'] & Wtg['long'] |  Wtr['zero'] & Wtg['very long'],Swr['keepg'])
rule62 = ctrl.Rule(Dht['very large'] | Qg['zero'] & Wtr['zero'] & Wtg['zero'],Swr['switchr'])

rule63 =  ctrl.Rule(Dht['medium'] | Qg['zero'] & Dht['large'] | Qg['zero'] & Dht['very large'] | Qg['zero'] &
                     Wtr['short'] & Wtg['zero'] |  Wtr['short'] & Wtg['short'] |  Wtr['short'] & Wtg['medium'] |
                      Wtr['short'] & Wtg['long'] |  Wtr['short'] & Wtg['very long'],Swr['keepg'])

rule64 =  ctrl.Rule(Dht['medium'] | Qg['small'] & Dht['large'] | Qg['small'] & Dht['very large'] | Qg['small'] &
                     Wtr['short'] & Wtg['zero'] |  Wtr['short'] & Wtg['short'] |  Wtr['short'] & Wtg['medium'] |
                      Wtr['short'] & Wtg['long'] |  Wtr['short'] & Wtg['very long'],Swr['keepg'])

rule65 =  ctrl.Rule(Dht['medium'] | Qg['medium'] & Dht['large'] | Qg['medium'] & Dht['very large'] | Qg['medium'] &
                     Wtr['short'] & Wtg['zero'] |  Wtr['short'] & Wtg['short'] |  Wtr['short'] & Wtg['medium'] |
                      Wtr['short'] & Wtg['long'] |  Wtr['short'] & Wtg['very long'],Swr['keepg'])

rule66 =  ctrl.Rule(Dht['medium'] | Qg['zero'] & Dht['large'] | Qg['zero'] &  Wtr['medium'] & Wtg['short'] |  
                     Wtr['medium'] & Wtg['medium'] | Wtr['medium'] & Wtg['long'] |  Wtr['medium'] & 
                     Wtg['very long'],Swr['keepg'])
rule67 =  ctrl.Rule(Dht['medium'] | Qg['small'] & Dht['large'] | Qg['small'] & Dht['very large'] | Qg['small'] &
                     Wtr['medium'] & Wtg['zero'] |  Wtr['medium'] & Wtg['short'] |  Wtr['medium'] & Wtg['medium'] |
                      Wtr['medium'] & Wtg['long'] |  Wtr['medium'] & Wtg['very long'],Swr['keepg'])

rule68 =  ctrl.Rule(Dht['medium'] | Qg['medium'] & Dht['large'] | Qg['medium'] & Dht['very large'] | Qg['medium'] &
                     Wtr['medium'] & Wtg['zero'] |  Wtr['medium'] & Wtg['short'] |  Wtr['medium'] & Wtg['medium'] |
                      Wtr['medium'] & Wtg['long'] |  Wtr['medium'] & Wtg['very long'],Swr['keepg'])
rule69 = ctrl.Rule(Dht['very large'] | Qg['zero'] & Wtr['medium'] & Wtg['zero'] | Wtr['medium'] & Wtg['short'],Swr['switchr'])


rule70 =  ctrl.Rule(Dht['medium'] | Qg['zero'] & Dht['large'] | Qg['zero'] & 
                     Wtr['long'] & Wtg['zero'] |  Wtr['long'] & Wtg['short'] |  Wtr['long'] & Wtg['long'] |  
                     Wtr['long'] & Wtg['very long'],Swr['keepg'])

rule71 =  ctrl.Rule(Dht['medium'] | Qg['small'] & Dht['large'] | Qg['small']  &  Wtr['long'] & Wtg['medium'] |
                      Wtr['long'] & Wtg['long'] |  Wtr['long'] & Wtg['very long'],Swr['keepg'])
rule72 =  ctrl.Rule(Dht['medium'] | Qg['medium']  & Wtr['long'] & Wtg['zero'] |  Wtr['long'] & Wtg['short'] | 
                     Wtr['long'] & Wtg['medium'] | Wtr['long'] & Wtg['long'] |  Wtr['long'] & Wtg['very long'],Swr['keepg'])
rule73 = ctrl.Rule(Dht['large'] | Qg['zero'] & Dht['very large'] | Qg['zero'] & Wtr['long'] & Wtg['zero'],Swr['switchr'])
rule74 = ctrl.Rule(Dht['very large'] | Qg['small'] & Wtr['long'] & Wtg['zero'],Swr['switchr'])
rule75 = ctrl.Rule(Dht['large'] | Qg['medium'] & Dht['very large'] | Qg['medium'] & Wtr['long'] & Wtg['zero'],Swr['switchr'])

rule76 = ctrl.Rule(Dht['large'] | Qg['zero'] & Dht['very large'] | Qg['zero'] & Dht['very large'] | Qg['small'] & Wtr['long'] &
                    Wtg['short'],Swr['switchr'])
rule77 = ctrl.Rule(Dht['very large'] | Qg['zero'] & Wtr['long'] & Wtg['medium'],Swr['switchr'])

rule78 =  ctrl.Rule(Dht['medium'] | Qg['zero'] & Dht['large'] | Qg['zero'] & Dht['very large'] | Qg['zero'] &
                     Wtr['very long'] & Wtg['zero'] |  Wtr['very long'] & Wtg['short'] ,Swr['switchr'])

rule79 =  ctrl.Rule(Dht['medium'] | Qg['small'] & Dht['large'] | Qg['small'] & Dht['very large'] | Qg['small'] &
                     Wtr['very long'] & Wtg['zero'] |  Wtr['very long'] & Wtg['short'] ,Swr['switchr'])

rule80 =  ctrl.Rule(Dht['medium'] | Qg['medium'] & Dht['large'] | Qg['medium'] & Dht['very large'] | Qg['medium'] &
                     Wtr['very long'] & Wtg['zero'] |  Wtr['very long'] & Wtg['short'] ,Swr['switchr'])

rule81 = ctrl.Rule(Dht['very large'] | Qg['zero'] & Dht['very large'] | Qg['small'] & Dht['very large'] | Qg['medium'] &
                    Wtr['very long'] & Wtg['medium'],Swr['switchr'])

rule82 =  ctrl.Rule(Dht['medium'] | Qg['zero'] & Dht['large'] | Qg['zero'] & Dht['very large'] | Qg['zero'] &
                      Wtr['very long'] & Wtg['medium'] |  Wtr['very long'] & Wtg['long'] |
                      Wtr['very long'] & Wtg['very long'],Swr['keepg'])
rule83 =  ctrl.Rule(Dht['medium'] | Qg['small'] & Dht['large'] | Qg['small'] & Dht['very large'] | Qg['small'] &
                      Wtr['very long'] & Wtg['medium'] |  Wtr['very long'] & Wtg['long'] |
                      Wtr['very long'] & Wtg['very long'],Swr['keepg'])

rule84 =  ctrl.Rule(Dht['medium'] | Qg['medium'] & Dht['large'] | Qg['medium'] & Dht['very large'] | Qg['medium'] &
                      Wtr['very long'] & Wtg['medium'] |  Wtr['very long'] & Wtg['long'] |
                      Wtr['very long'] & Wtg['very long'],Swr['keepg'])

rule85 = ctrl.Rule(Dht['large'] | Qg['zero'] & Dht['very large'] | Qg['zero'] & Wtr['very long'] & Wtg['long'],Swr['switchr'])

# Vehicle Trajectory Module 
rule86 = ctrl.Rule(Dr['close'] & Dg['close'], OGd['short'])
rule87 = ctrl.Rule(Dr['medium'] & Dg['close'] | Dr['far'] & Dg['close'], OGd['medium'])
rule88 = ctrl.Rule(Dr['close'] & Dg['medium'] | Dr['close'] & Dg['far'], OGd['switch'])
rule89 = ctrl.Rule(Dr['medium']  & Dg['medium'] ,OGd['short'])
rule90 = ctrl.Rule(Dr['far']  & Dg['medium'] ,OGd['medium'])
rule91 = ctrl.Rule(Dr['medium']& Dg['far'] ,OGd['switch'])
rule92 = ctrl.Rule(Dr['far']& Dg['far'] ,OGd['short'])
 # Extension Time Decision Module
rule93 = ctrl.Rule(Dht['zero'] & Qg['zero'] & Pem['no'] & OGd['switch'] & Swr['keepg'], Ge['short'])
rule94 = ctrl.Rule(Dht['small'] & Qg['zero'] | Dht['medium'] & Qg['zero'] | 
                   Dht['large'] & Qg['zero'] & Pem['no'] & OGd['switch'] & Swr['keepg'], Ge['turnr'])
rule95 = ctrl.Rule(Dht['very large'] & Qg['zero'] & Pem['no'] & OGd['switch'] & Swr['keepg'], Ge['short'])

rule96 = ctrl.Rule(Dht['zero'] & Qg['small'] | Dht['small'] & Qg['small'] | 
                   Dht['medium'] & Qg['small'] | Dht['large'] & Qg['small'] |
                   Dht['very large'] & Qg['small'] & Pem['no'] & OGd['switch'] & Swr['keepg'], Ge['short'])

rule97 = ctrl.Rule(Dht['zero'] & Qg['medium'] | Dht['small'] & Qg['medium'] | 
                   Dht['medium'] & Qg['small']  & Pem['no'] & OGd['switch'] & Swr['keepg'], Ge['short'])

rule98 = ctrl.Rule(Dht['large'] & Qg['medium'] | 
                   Dht['very large'] & Qg['medium'] & Pem['no'] & OGd['switch'] & Swr['keepg'], Ge['medium'])

rule99 = ctrl.Rule(Dht['zero'] & Qg['large'] | Dht['small'] & Qg['large'] | 
                   Dht['medium'] & Qg['large']  | Dht['large'] & Qg['large'] |
                   Dht['very large'] & Qg['large']& Pem['no'] & OGd['switch'] & Swr['keepg'], Ge['medium'])

rule100 = ctrl.Rule(Dht['zero'] & Qg['very large'] & Pem['no'] & OGd['switch'] & Swr['keepg'], Ge['medium'])

rule101 = ctrl.Rule(Dht['small'] & Qg['very large'] | Dht['medium'] & Qg['very large'] & Pem['no'] & OGd['switch'] & Swr['keepg'], Ge['long'])
rule102 = ctrl.Rule(Dht['large'] & Qg['very large'] & Pem['no'] & OGd['switch'] & Swr['keepg'], Ge['medium'])
rule103 = ctrl.Rule(Dht['very large'] & Qg['very large'] & Pem['no'] & OGd['switch'] & Swr['keepg'], Ge['short'])

rule104 = ctrl.Rule(Dht['zero'] & Qg['zero'] | Dht['small'] & Qg['zero'] | Dht['medium'] & Qg['zero'] |
                    Dht['large'] & Qg['zero'] | Dht['very large'] & Qg['zero'] & Pem['no']  & OGd['switch'] & Swr['switchr'], Ge['turnr'])

rule105 = ctrl.Rule(Dht['zero'] & Qg['small'] | Dht['small'] & Qg['small'] | Dht['medium'] & Qg['small'] |
                    Dht['large'] & Qg['small'] | Dht['very large'] & Qg['small'] & Pem['no']  & OGd['switch'] & Swr['switchr'], Ge['turnr'])

rule106 = ctrl.Rule(Dht['zero'] & Qg['medium'] | Dht['small'] & Qg['medium'] | Dht['medium'] & Qg['medium'] |
                    Dht['large'] & Qg['medium'] | Dht['very large'] & Qg['medium'] & Pem['no']  & OGd['switch'] & Swr['switchr'], Ge['turnr'])

rule107 = ctrl.Rule(Dht['zero'] & Qg['large'] | Dht['small'] & Qg['large'] | Dht['medium'] & Qg['large'] |
                    Dht['large'] & Qg['large'] | Dht['very large'] & Qg['large'] & Pem['no']  & OGd['switch'] & Swr['switchr'], Ge['turnr'])

rule108 = ctrl.Rule(Dht['small'] & Qg['very large'] | Dht['medium'] & Qg['very large'] |
                    Dht['large'] & Qg['very large'] | Dht['very large'] & Qg['very large'] & Pem['no']  & OGd['switch'] & Swr['switchr'], Ge['turnr'])
rule109 = ctrl.Rule(Dht['zero'] & Qg['very large'] & Pem['no'] & OGd['switch'] & Swr['switchr'], Ge['medium'])

rule110 = ctrl.Rule(Dht['zero'] & Qg['zero'] | Dht['small'] & Qg['zero'] | Dht['medium'] & Qg['zero'] |
                    Dht['large'] & Qg['zero'] | Dht['very large'] & Qg['zero']& Pem['no'] & OGd['short'] & Swr['keepg'], Ge['short'])

rule111 = ctrl.Rule(Dht['zero'] & Qg['small'] | Dht['small'] & Qg['small'] | Dht['medium'] & Qg['small'] |
                    Dht['large'] & Qg['small'] | Dht['very large'] & Qg['small'] & Pem['no'] & OGd['short'] & Swr['keepg'], Ge['short'])
rule112 = ctrl.Rule(Dht['zero'] & Qg['medium'] | Dht['zero'] & Qg['large'] & Pem['no']  & OGd['short'] & Swr['keepg'], Ge['medium'])
rule113 = ctrl.Rule(Dht['small'] & Qg['medium'] & Pem['no'] & OGd['short'] & Swr['keepg'], Ge['short'])

rule114 = ctrl.Rule(Dht['medium'] & Qg['medium'] | Dht['large'] & Qg['medium'] |
                    Dht['very large'] & Qg['medium'] & Pem['no']  & OGd['short'] & Swr['keepg'], Ge['medium'])
rule115 = ctrl.Rule(Dht['small'] & Qg['large'] | Dht['medium'] & Qg['large'] | Dht['large'] & Qg['large'] |
                  Dht['very large'] & Qg['large'] & Pem['no']  & OGd['short'] & Swr['keepg'], Ge['long'])

rule116 = ctrl.Rule(Dht['zero'] & Qg['very large'] | Dht['small'] & Qg['very large'] | Dht['medium'] & Qg['very large'] |
                  Dht['large'] & Qg['very large'] & Pem['no']  & OGd['short'] & Swr['keepg'], Ge['long'])
rule117 = ctrl.Rule(Dht['very large'] & Qg['very large'] & Pem['no'] & OGd['short'] & Swr['keepg'], Ge['medium'])

rule118 = ctrl.Rule(Dht['zero'] & Qg['zero'] | Dht['zero'] & Qg['small'] | Dht['zero'] & Qg['medium'] & Pem['no']  & OGd['short'] & Swr['switchr'], Ge['short'])
rule119 = ctrl.Rule(Dht['small'] & Qg['zero'] | Dht['small'] & Qg['small'] | Dht['small'] & Qg['medium'] & Pem['no']  & OGd['short'] & Swr['switchr'], Ge['short'])
rule120 = ctrl.Rule(Dht['medium'] & Qg['zero'] | Dht['large'] & Qg['zero'] | Dht['very large'] & Qg['zero'] & Pem['no']  & OGd['short'] & Swr['switchr'], Ge['turnr'])

rule121 = ctrl.Rule(Dht['medium'] & Qg['small'] | Dht['large'] & Qg['small'] & Pem['no']  & OGd['short'] & Swr['switchr'], Ge['short'])
                    
rule122 = ctrl.Rule(Dht['medium'] & Qg['medium'] & Pem['no'] & OGd['short'] & Swr['switchr'], Ge['short'])
                    
rule123 = ctrl.Rule(Dht['large'] & Qg['medium'] & Pem['no'] & OGd['short'] & Swr['switchr'], Ge['medium'])
rule124 = ctrl.Rule(Dht['very large'] & Qg['small'] & Pem['no'] & OGd['short'] & Swr['switchr'], Ge['turnr'])
rule125 = ctrl.Rule(Dht['very large'] & Qg['medium'] & Pem['no'] & OGd['short'] & Swr['switchr'], Ge['short'])

rule126 = ctrl.Rule(Dht['zero'] & Qg['large'] | Dht['small'] & Qg['large'] | Dht['medium'] & Qg['large'] |
                    Dht['large'] & Qg['large'] | Dht['very large'] & Qg['large'] & Pem['no']  & OGd['short'] & Swr['switchr'], Ge['medium'])
rule127 = ctrl.Rule(Dht['zero'] & Qg['very large'] & Pem['no']  & OGd['short'] & Swr['switchr'], Ge['medium'])
rule128 = ctrl.Rule(Dht['small'] & Qg['very large'] | Dht['medium'] & Qg['very large'] & Pem['no']  & OGd['short'] & Swr['switchr'], Ge['long'])
rule129 = ctrl.Rule(Dht['large'] & Qg['very large'] & Pem['no']  & OGd['short'] & Swr['switchr'], Ge['medium'])
rule130 = ctrl.Rule(Dht['very large'] & Qg['very large'] & Pem['no']  & OGd['short'] & Swr['switchr'], Ge['short'])

rule131 = ctrl.Rule(Dht['zero'] & Qg['zero'] | Dht['small'] & Qg['zero'] | Dht['medium'] & Qg['zero'] |
                    Dht['large'] & Qg['zero'] | Dht['very large'] & Qg['zero'] & Pem['no'] & OGd['medium'] & Swr['keepg'], Ge['short'])

rule132 = ctrl.Rule(Dht['zero'] & Qg['small'] | Dht['small'] & Qg['small'] | Dht['medium'] & Qg['small'] |
                    Dht['large'] & Qg['small'] | Dht['very large'] & Qg['small'] & Pem['no'] & OGd['medium'] & Swr['keepg'], Ge['short'])
                    
rule133 = ctrl.Rule(Dht['zero'] & Qg['medium'] | Dht['small'] & Qg['medium'] | Dht['medium'] & Qg['medium'] |
                    Dht['large'] & Qg['medium'] | Dht['very large'] & Qg['medium'] & Pem['no'] & OGd['medium'] & Swr['keepg'], Ge['medium'])

rule134 = ctrl.Rule(Dht['zero'] & Qg['large'] & Pem['no'] & OGd['medium'] & Swr['keepg'], Ge['medium'])
                    
rule135 = ctrl.Rule(Dht['small'] & Qg['large'] | Dht['medium'] & Qg['large'] |
                    Dht['large'] & Qg['large'] | Dht['very large'] & Qg['large'] & Pem['no'] & OGd['medium'] & Swr['keepg'], Ge['long'])

rule136 = ctrl.Rule(Dht['zero'] & Qg['very large'] | Dht['small'] & Qg['very large'] |
                    Dht['medium'] & Qg['very large'] | Dht['large'] & Qg['very large'] & Pem['no'] & OGd['medium'] & Swr['keepg'], Ge['long'])
rule137 = ctrl.Rule(Dht['very large'] & Qg['very large'] & Pem['no'] & OGd['medium'] & Swr['keepg'], Ge['medium'])

rule138 = ctrl.Rule(Dht['zero'] & Qg['zero'] | Dht['small'] & Qg['zero'] | Dht['medium'] & Qg['zero'] |
                    Dht['large'] & Qg['zero'] | Dht['very large'] & Qg['zero']& Pem['no'] & OGd['medium'] & Swr['switchr'], Ge['short'])
                    
rule139 = ctrl.Rule(Dht['zero'] & Qg['small'] | Dht['small'] & Qg['small'] | Dht['medium'] & Qg['small'] |
                    Dht['large'] & Qg['small'] | Dht['very large'] & Qg['small']& Pem['no'] & OGd['medium'] & Swr['switchr'], Ge['short'])
rule140 = ctrl.Rule(Dht['zero'] & Qg['medium'] | Dht['small'] & Qg['medium'] | Dht['medium'] & Qg['medium'] & Pem['no'] & OGd['medium'] & Swr['switchr'], Ge['short'])

rule141 = ctrl.Rule(Dht['large'] & Qg['medium'] | Dht['very large'] & Qg['medium'] & Pem['no'] & OGd['medium'] & Swr['switchr'], Ge['medium'])
                    
rule142 = ctrl.Rule(Dht['zero'] & Qg['large'] | Dht['small'] & Qg['large'] | Dht['medium'] & Qg['large'] |
                    Dht['large'] & Qg['large'] | Dht['very large'] & Qg['large']& Pem['no'] & OGd['medium'] & Swr['switchr'], Ge['medium'])

rule143 = ctrl.Rule(Dht['zero'] & Qg['very large'] | Dht['small'] & Qg['very large'] | Dht['medium'] & Qg['very large'] & Pem['no'] & OGd['medium'] & Swr['switchr'], Ge['long'])

rule144 = ctrl.Rule(Dht['large'] & Qg['very large'] | Dht['very large'] & Qg['very large'] & Pem['no'] & OGd['medium'] & Swr['switchr'], Ge['medium'])

rule145 = ctrl.Rule(Dht['zero'] & Qg['zero'] | Dht['zero'] & Qg['small'] & Pem['Emg'] & OGd['switch'] & Swr['keepg'], Ge['medium'])

rule146 = ctrl.Rule(Dht['small'] & Qg['zero'] | Dht['medium'] & Qg['zero'] | Dht['large'] & Qg['zero'] |
                    Dht['very large'] & Qg['zero'] & Pem['Emg'] & OGd['switch'] & Swr['keepg'], Ge['short'])

rule147 = ctrl.Rule(Dht['small'] & Qg['small'] | Dht['medium'] & Qg['small'] | Dht['large'] & Qg['small'] |
                    Dht['very large'] & Qg['small'] & Pem['Emg'] & OGd['switch'] & Swr['keepg'], Ge['short'])

rule148 = ctrl.Rule(Dht['zero'] & Qg['medium'] | Dht['small'] & Qg['medium'] | Dht['medium'] & Qg['medium'] | 
                    Dht['large'] & Qg['medium'] | Dht['very large'] & Qg['medium'] & Pem['Emg'] & OGd['switch'] & Swr['keepg'], Ge['medium'])

rule149 = ctrl.Rule(Dht['zero'] & Qg['large'] | Dht['small'] & Qg['large'] | Dht['medium'] & Qg['large'] | 
                    Dht['large'] & Qg['large'] | Dht['very large'] & Qg['large'] & Pem['Emg'] & OGd['switch'] & Swr['keepg'], Ge['long'])

rule150 = ctrl.Rule(Dht['zero'] & Qg['very large'] | Dht['small'] & Qg['very large'] | Dht['medium'] & Qg['very large'] | 
                    Dht['large'] & Qg['very large'] | Dht['very large'] & Qg['very large'] & Pem['Emg'] & OGd['switch'] & Swr['keepg'], Ge['very long'])
rule151 = ctrl.Rule(Dht['zero'] & Qg['zero']  | Dht['zero'] & Qg['small']  & Pem['Emg'] & OGd['switch'] & Swr['switchr'], Ge['medium'])

rule152 = ctrl.Rule(Dht['small'] & Qg['zero'] | Dht['medium'] & Qg['zero'] | Dht['large'] & Qg['zero'] |
                    Dht['very large'] & Qg['zero'] & Pem['Emg'] & OGd['switch'] & Swr['switchr'], Ge['short'])

rule153 = ctrl.Rule(Dht['small'] & Qg['small'] | Dht['medium'] & Qg['small'] | Dht['large'] & Qg['small'] |
                    Dht['very large'] & Qg['small'] & Pem['Emg'] & OGd['switch'] & Swr['switchr'], Ge['short'])

rule154 = ctrl.Rule(Dht['zero'] & Qg['medium']|Dht['small'] & Qg['medium'] | Dht['medium'] & Qg['medium'] | Dht['large'] & Qg['medium'] |
                    Dht['very large'] & Qg['medium'] & Pem['Emg'] & OGd['switch'] & Swr['switchr'], Ge['medium'])
rule155 = ctrl.Rule(Dht['zero'] & Qg['large']| Dht['small'] & Qg['large'] | Dht['medium'] & Qg['large'] | Dht['large'] & Qg['large'] |
                    Dht['very large'] & Qg['large'] & Pem['Emg'] & OGd['switch'] & Swr['switchr'], Ge['long'])
rule156 = ctrl.Rule(Dht['zero'] & Qg['very large']| Dht['small'] & Qg['very large'] | Dht['medium'] & Qg['very large'] | Dht['large'] & Qg['very large'] |
                    Dht['very large'] & Qg['very large'] & Pem['Emg'] & OGd['switch'] & Swr['switchr'], Ge['very long'])
rule157 = ctrl.Rule(Dht['zero'] & Qg['zero'] | Dht['zero'] & Qg['small'] & Pem['Emg'] & OGd['short'] & Swr['keepg'], Ge['medium'])
rule158 = ctrl.Rule(Dht['small'] & Qg['zero'] | Dht['medium'] & Qg['zero'] | Dht['large'] & Qg['zero'] |
                    Dht['very large'] & Qg['zero'] & Pem['Emg'] & OGd['short'] & Swr['keepg'], Ge['short'])
rule159 = ctrl.Rule(Dht['small'] & Qg['small'] | Dht['medium'] & Qg['small'] | Dht['large'] & Qg['small'] |
                    Dht['very large'] & Qg['small'] & Pem['Emg'] & OGd['short'] & Swr['keepg'], Ge['short'])
rule160 = ctrl.Rule(Dht['zero'] & Qg['medium']| Dht['small'] & Qg['medium'] | Dht['medium'] & Qg['medium'] | Dht['large'] & Qg['medium'] |
                    Dht['very large'] & Qg['medium'] & Pem['Emg'] & OGd['short'] & Swr['keepg'], Ge['medium'])
rule161 = ctrl.Rule(Dht['zero'] & Qg['large']| Dht['small'] & Qg['large'] | Dht['medium'] & Qg['large'] | Dht['large'] & Qg['large'] |
                    Dht['very large'] & Qg['large'] & Pem['Emg'] & OGd['short'] & Swr['keepg'], Ge['long'])
rule162 = ctrl.Rule(Dht['zero'] & Qg['very large']| Dht['small'] & Qg['very large'] | Dht['medium'] & Qg['very large'] | Dht['large'] & Qg['very large'] |
                    Dht['very large'] & Qg['very large'] & Pem['Emg'] & OGd['short'] & Swr['keepg'], Ge['very long'])

rule163 = ctrl.Rule(Dht['zero'] & Qg['zero'] | Dht['zero'] & Qg['small'] & Pem['Emg'] & OGd['short'] & 
                    Swr['switchr'], Ge['medium'])

rule164 = ctrl.Rule(Dht['small'] & Qg['zero'] | Dht['medium'] & Qg['zero'] | Dht['large'] & Qg['zero'] |
                    Dht['very large'] & Qg['zero'] & Pem['Emg'] & OGd['short'] & Swr['switchr'], Ge['short'])
rule165 = ctrl.Rule(Dht['small'] & Qg['small'] | Dht['medium'] & Qg['small'] | Dht['large'] & Qg['small'] |
                    Dht['very large'] & Qg['small'] & Pem['Emg'] & OGd['short'] & Swr['switchr'], Ge['short'])
rule166 = ctrl.Rule(Dht['zero'] & Qg['medium']| Dht['small'] & Qg['medium'] | Dht['medium'] & Qg['medium'] | Dht['large'] & Qg['medium'] |
                    Dht['very large'] & Qg['medium'] & Pem['Emg'] & OGd['short'] & Swr['switchr'], Ge['medium'])

rule167 = ctrl.Rule(Dht['zero'] & Qg['large']| Dht['small'] & Qg['large'] | Dht['medium'] & Qg['large'] | Dht['large'] & Qg['large'] |
                    Dht['very large'] & Qg['large'] & Pem['Emg'] & OGd['short'] & Swr['switchr'], Ge['long'])

rule168 = ctrl.Rule(Dht['zero'] & Qg['very large']| Dht['small'] & Qg['very large'] | Dht['medium'] & Qg['very large'] | Dht['large'] & Qg['very large'] |
                    Dht['very large'] & Qg['very large'] & Pem['Emg'] & OGd['short'] & Swr['switchr'], Ge['very long'])

rule169 = ctrl.Rule(Dht['zero'] & Qg['zero']| Dht['zero'] & Qg['small'] & Pem['Emg'] & OGd['medium'] & 
                    Swr['keepg'], Ge['medium'])
rule170 = ctrl.Rule(Dht['small'] & Qg['zero']| Dht['medium'] & Qg['zero'] | Dht['large'] & Qg['zero'] |
                    Dht['very large'] & Qg['zero'] & Pem['Emg'] & OGd['medium'] & Swr['keepg'], Ge['short'])
rule171 = ctrl.Rule(Dht['small'] & Qg['small']| Dht['medium'] & Qg['small'] | Dht['large'] & Qg['small'] |
                    Dht['very large'] & Qg['small'] & Pem['Emg'] & OGd['medium'] & Swr['keepg'], Ge['short'])
rule172 = ctrl.Rule(Dht['zero'] & Qg['medium'] | Dht['small'] & Qg['medium']| Dht['medium'] & Qg['medium'] | Dht['large'] & Qg['medium'] |
                    Dht['very large'] & Qg['medium'] & Pem['Emg'] & OGd['medium'] & Swr['keepg'], Ge['medium'])
rule173 = ctrl.Rule(Dht['zero'] & Qg['large'] | Dht['small'] & Qg['large']| Dht['medium'] & Qg['large'] | Dht['large'] & Qg['large'] |
                    Dht['very large'] & Qg['large'] & Pem['Emg'] & OGd['medium'] & Swr['keepg'], Ge['long'])
rule174 = ctrl.Rule(Dht['zero'] & Qg['very large'] | Dht['small'] & Qg['very large']| Dht['medium'] & Qg['very large'] | Dht['large'] & Qg['very large'] |
                    Dht['very large'] & Qg['very large'] & Pem['Emg'] & OGd['medium'] & Swr['keepg'], Ge['very long'])

rule175 = ctrl.Rule(Dht['zero'] & Qg['zero'] | Dht['zero'] & Qg['small'] & Pem['Emg'] & OGd['medium'] & 
                    Swr['switchr'], Ge['medium'])
rule176 = ctrl.Rule(Dht['small'] & Qg['zero'] | Dht['medium'] & Qg['zero'] | Dht['large'] & Qg['zero'] |
                    Dht['very large'] & Qg['zero'] & Pem['Emg'] & OGd['medium'] & Swr['switchr'], Ge['short'])
rule177 = ctrl.Rule(Dht['small'] & Qg['small'] | Dht['medium'] & Qg['small'] | Dht['large'] & Qg['small'] |
                    Dht['very large'] & Qg['small'] & Pem['Emg'] & OGd['medium'] & Swr['switchr'], Ge['short'])
rule178 = ctrl.Rule(Dht['zero'] & Qg['medium'] | Dht['small'] & Qg['medium'] | Dht['medium'] & Qg['medium'] | Dht['large'] & Qg['medium'] |
                    Dht['very large'] & Qg['medium'] & Pem['Emg'] & OGd['medium'] & Swr['switchr'], Ge['medium'])
rule179 = ctrl.Rule(Dht['zero'] & Qg['large'] | Dht['small'] & Qg['large'] | Dht['medium'] & Qg['large'] | Dht['large'] & Qg['large'] |
                    Dht['very large'] & Qg['large'] & Pem['Emg'] & OGd['medium'] & Swr['switchr'], Ge['long'])
rule180 = ctrl.Rule(Dht['zero'] & Qg['very large'] | Dht['small'] & Qg['very large'] | Dht['medium'] & Qg['very large'] | Dht['large'] & Qg['very large'] |
                    Dht['very large'] & Qg['very large'] & Pem['Emg'] & OGd['medium'] & Swr['switchr'], Ge['very long'])
rule181 = ctrl.Rule(Dht['zero'] & Qg['zero'] | Dht['small'] & Qg['zero'] | Dht['medium'] & Qg['zero'] |
                    Dht['large'] & Qg['zero'] | Dht['very large'] & Qg['zero']& Pem['Emr'] & OGd['switch'] & Swr['keepg'], Ge['turnr'])
rule182 = ctrl.Rule(Dht['zero'] & Qg['small'] | Dht['small'] & Qg['small'] | Dht['medium'] & Qg['small'] |
                    Dht['large'] & Qg['small'] | Dht['very large'] & Qg['small']& Pem['Emr'] & OGd['switch'] & Swr['keepg'], Ge['turnr'])
rule183 = ctrl.Rule(Dht['zero'] & Qg['medium'] | Dht['small'] & Qg['medium'] | Dht['medium'] & Qg['medium'] |
                    Dht['large'] & Qg['medium'] | Dht['very large'] & Qg['medium']& Pem['Emr'] & OGd['switch'] & Swr['keepg'], Ge['turnr'])
rule184 = ctrl.Rule(Dht['zero'] & Qg['large'] | Dht['small'] & Qg['large'] | Dht['medium'] & Qg['large'] |
                    Dht['large'] & Qg['large'] | Dht['very large'] & Qg['large'] & Pem['Emr'] & OGd['switch'] & Swr['keepg'], Ge['turnr'])
rule185 = ctrl.Rule(Dht['zero'] & Qg['very large'] | Dht['small'] & Qg['very large'] | Dht['medium'] & Qg['very large'] |
                    Dht['large'] & Qg['very large'] | Dht['very large'] & Qg['very large'] & Pem['Emr'] & OGd['switch'] & Swr['keepg'], Ge['turnr'])

rule186 = ctrl.Rule(Dht['zero'] & Qg['zero'] | Dht['small'] & Qg['zero'] | Dht['medium'] & Qg['zero'] |
                    Dht['large'] & Qg['zero'] | Dht['very large'] & Qg['zero']& Pem['Emr'] & OGd['switch'] & Swr['switchr'], Ge['turnr'])
rule187 = ctrl.Rule(Dht['zero'] & Qg['small'] | Dht['small'] & Qg['small'] | Dht['medium'] & Qg['small'] |
                    Dht['large'] & Qg['small'] | Dht['very large'] & Qg['small']& Pem['Emr'] & OGd['switch'] & Swr['switchr'], Ge['turnr'])
rule188 = ctrl.Rule(Dht['zero'] & Qg['medium'] | Dht['small'] & Qg['medium'] | Dht['medium'] & Qg['medium'] |
                    Dht['large'] & Qg['medium'] | Dht['very large'] & Qg['medium']& Pem['Emr'] & OGd['switch'] & Swr['switchr'], Ge['turnr'])
rule189 = ctrl.Rule(Dht['zero'] & Qg['large'] | Dht['small'] & Qg['large'] | Dht['medium'] & Qg['large'] |
                    Dht['large'] & Qg['large'] | Dht['very large'] & Qg['large'] & Pem['Emr'] & OGd['switch'] & Swr['switchr'], Ge['turnr'])
rule190 = ctrl.Rule(Dht['zero'] & Qg['very large'] | Dht['small'] & Qg['very large'] | Dht['medium'] & Qg['very large'] |
                    Dht['large'] & Qg['very large'] | Dht['very large'] & Qg['very large'] & Pem['Emr'] & OGd['switch'] & Swr['switchr'], Ge['turnr'])

rule191 = ctrl.Rule(Dht['zero'] & Qg['zero'] | Dht['small'] & Qg['zero'] | Dht['medium'] & Qg['zero'] |
                    Dht['large'] & Qg['zero'] | Dht['very large'] & Qg['zero']& Pem['Emr'] & OGd['short'] &  Swr['keepg'], Ge['turnr'])
rule192 = ctrl.Rule(Dht['zero'] & Qg['small'] | Dht['small'] & Qg['small'] | Dht['medium'] & Qg['small'] |
                    Dht['large'] & Qg['small'] | Dht['very large'] & Qg['small']& Pem['Emr'] & OGd['short'] &  Swr['keepg'], Ge['turnr'])
rule193 = ctrl.Rule(Dht['zero'] & Qg['medium'] | Dht['small'] & Qg['medium'] | Dht['medium'] & Qg['medium'] |
                    Dht['large'] & Qg['medium'] | Dht['very large'] & Qg['medium']& Pem['Emr'] & OGd['short'] &  Swr['keepg'], Ge['turnr'])
rule194 = ctrl.Rule(Dht['zero'] & Qg['large'] | Dht['small'] & Qg['large'] | Dht['medium'] & Qg['large'] |
                    Dht['large'] & Qg['large'] | Dht['very large'] & Qg['large'] & Pem['Emr'] & OGd['short'] &  Swr['keepg'], Ge['turnr'])
rule195 = ctrl.Rule(Dht['zero'] & Qg['very large'] | Dht['small'] & Qg['very large'] | Dht['medium'] & Qg['very large'] |
                    Dht['large'] & Qg['very large'] | Dht['very large'] & Qg['very large'] & Pem['Emr'] & OGd['short'] &  Swr['keepg'], Ge['turnr'])

rule196 = ctrl.Rule(Dht['zero'] & Qg['zero'] | Dht['small'] & Qg['zero'] | Dht['medium'] & Qg['zero'] |
                    Dht['large'] & Qg['zero'] | Dht['very large'] & Qg['zero']& Pem['Emr'] & OGd['short'] &  Swr['switchr'], Ge['turnr'])
rule197 = ctrl.Rule(Dht['zero'] & Qg['small'] | Dht['small'] & Qg['small'] | Dht['medium'] & Qg['small'] |
                    Dht['large'] & Qg['small'] | Dht['very large'] & Qg['small']& Pem['Emr'] & OGd['short'] &  Swr['switchr'], Ge['turnr'])
rule198 = ctrl.Rule(Dht['zero'] & Qg['medium'] | Dht['small'] & Qg['medium'] | Dht['medium'] & Qg['medium'] |
                    Dht['large'] & Qg['medium'] | Dht['very large'] & Qg['medium']& Pem['Emr'] & OGd['short'] &  Swr['switchr'], Ge['turnr'])
rule199 = ctrl.Rule(Dht['zero'] & Qg['large'] | Dht['small'] & Qg['large'] | Dht['medium'] & Qg['large'] |
                    Dht['large'] & Qg['large'] | Dht['very large'] & Qg['large'] & Pem['Emr'] & OGd['short'] &  Swr['switchr'], Ge['turnr'])
rule200 = ctrl.Rule(Dht['zero'] & Qg['very large'] | Dht['small'] & Qg['very large'] | Dht['medium'] & Qg['very large'] |
                    Dht['large'] & Qg['very large'] | Dht['very large'] & Qg['very large'] & Pem['Emr'] & OGd['short'] &  Swr['switchr'], Ge['turnr'])

rule201 = ctrl.Rule(Dht['zero'] & Qg['zero'] | Dht['small'] & Qg['zero'] | Dht['medium'] & Qg['zero'] |
                    Dht['large'] & Qg['zero'] | Dht['very large'] & Qg['zero']& Pem['Emr'] & OGd['medium'] &  Swr['keepg'], Ge['turnr'])
rule202 = ctrl.Rule(Dht['zero'] & Qg['small'] | Dht['small'] & Qg['small'] | Dht['medium'] & Qg['small'] |
                    Dht['large'] & Qg['small'] | Dht['very large'] & Qg['small']& Pem['Emr'] & OGd['medium'] &  Swr['keepg'], Ge['turnr'])
rule203 = ctrl.Rule(Dht['zero'] & Qg['medium'] | Dht['small'] & Qg['medium'] | Dht['medium'] & Qg['medium'] |
                    Dht['large'] & Qg['medium'] | Dht['very large'] & Qg['medium']& Pem['Emr'] & OGd['medium'] &  Swr['keepg'], Ge['turnr'])
rule204 = ctrl.Rule(Dht['zero'] & Qg['large'] | Dht['small'] & Qg['large'] | Dht['medium'] & Qg['large'] |
                    Dht['large'] & Qg['large'] | Dht['very large'] & Qg['large'] & Pem['Emr'] & OGd['medium'] &  Swr['keepg'], Ge['turnr'])
rule205 = ctrl.Rule(Dht['zero'] & Qg['very large'] | Dht['small'] & Qg['very large'] | Dht['medium'] & Qg['very large'] |
                    Dht['large'] & Qg['very large'] | Dht['very large'] & Qg['very large'] & Pem['Emr'] & OGd['medium'] &  Swr['keepg'], Ge['turnr'])

rule206 = ctrl.Rule(Dht['zero'] & Qg['zero'] | Dht['small'] & Qg['zero'] | Dht['medium'] & Qg['zero'] |
                    Dht['large'] & Qg['zero'] | Dht['very large'] & Qg['zero']& Pem['Emr'] & OGd['medium'] &  Swr['switchr'], Ge['turnr'])
rule207 = ctrl.Rule(Dht['zero'] & Qg['small'] | Dht['small'] & Qg['small'] | Dht['medium'] & Qg['small'] |
                    Dht['large'] & Qg['small'] | Dht['very large'] & Qg['small']& Pem['Emr'] & OGd['medium'] &  Swr['switchr'], Ge['turnr'])
rule208 = ctrl.Rule(Dht['zero'] & Qg['medium'] | Dht['small'] & Qg['medium'] | Dht['medium'] & Qg['medium'] |
                    Dht['large'] & Qg['medium'] | Dht['very large'] & Qg['medium']& Pem['Emr'] & OGd['medium'] &  Swr['switchr'], Ge['turnr'])
rule209 = ctrl.Rule(Dht['zero'] & Qg['large'] | Dht['small'] & Qg['large'] | Dht['medium'] & Qg['large'] |
                    Dht['large'] & Qg['large'] | Dht['very large'] & Qg['large'] & Pem['Emr'] & OGd['medium'] &  Swr['switchr'], Ge['turnr'])
rule210 = ctrl.Rule(Dht['zero'] & Qg['very large'] | Dht['small'] & Qg['very large'] | Dht['medium'] & Qg['very large'] |
                    Dht['large'] & Qg['very large'] | Dht['very large'] & Qg['very large'] & Pem['Emr'] & OGd['medium'] &  Swr['switchr'], Ge['turnr'])

#Fuzzy Inference rules
Etdm_ctrl = ctrl.ControlSystem([rule1, rule2, rule3,rule4,rule5,rule6, rule7, rule8,rule9,rule10,rule11, rule12, rule13,rule14,rule15,rule16, rule17,
                                rule18,rule19,rule20,rule21,rule22, rule23, rule24,rule25,rule26, rule27, rule28,rule29,rule30,rule31, rule32, rule33,
                                rule34,rule35,rule36, rule37, rule38,rule39,rule40,rule41, rule42, rule43,rule44,rule45,rule46,rule47, rule48, rule49,
                                rule50,rule51, rule52, rule53,rule54,rule55,rule56, rule57, rule58,rule59,rule60,rule61, rule62, rule63,rule64,rule65,
                                rule66, rule67, rule68,rule69,rule70,rule71,rule72, rule73, rule74,rule75,rule76, rule77, rule78,rule79,rule80,rule81, 
                                rule82, rule83,rule84,rule85,rule86, rule87, rule88,rule89,rule90,rule91, rule92, rule93,rule94,rule95,rule96,rule97, 
                                rule98, rule99,rule99,rule100, rule101, rule102,rule103,rule104,rule105, rule106, rule107,rule108,rule109,rule110, 
                                rule111, rule112,rule113,rule114,rule115, rule116, rule117,rule118,rule119,rule120,rule121, rule122, rule123,rule124,
                                rule125,rule126, rule127,rule128,rule129,rule130,rule131,rule132,rule133,rule134,rule135,rule136,rule137,rule138,rule139,
                                rule140,rule141,rule142,rule143,rule144,rule145,rule146,rule147,rule148,rule149,rule150,rule151,rule152,rule153,rule154,
                                rule155,rule156,rule157,rule158,rule159,rule160,rule161,rule162,rule163,rule164,rule165,rule166,rule167,rule168,rule169,
                                rule170,rule171,rule172,rule173,rule174,rule175,rule176,rule177,rule178,rule179,rule180,rule181,rule182,rule183,rule184,
                                rule185,rule186,rule187,rule188,rule189,rule190,rule191,rule192,rule193,rule194,rule195,rule196,rule197,rule198,rule199,
                                rule200,rule201,rule202,rule203,rule204,rule205,rule206,rule207,rule208,rule209,rule210])
Extension_time = ctrl.ControlSystemSimulation(Etdm_ctrl)

def fuzzy_controller_function1(no_vehicles_in_red_lanes,
                                            no_vehicles_in_green_lanes,
                                            no_emv_current_lane,no_emv_other_lane,
                                            max_waiting_time_in_green_lanes, 
                                            max_waiting_time_in_red_lanes,
                                            total_distance_R,
                                            total_distance_G):
    
   Extension_time.input['Qr'] = int(no_vehicles_in_red_lanes)
   Extension_time.input['Qg'] = int(no_vehicles_in_green_lanes)
   Extension_time.input['Emg'] = int(no_emv_current_lane)
   Extension_time.input['Emr'] = int(no_emv_other_lane)
   Extension_time.input['Wtr'] = int(max_waiting_time_in_red_lanes)
   Extension_time.input['Wtg'] = int(max_waiting_time_in_green_lanes)
   Extension_time.input['Dr'] = int(total_distance_R)
   Extension_time.input['Dg'] = int(total_distance_G)
   
   print('Qr =' + str(no_vehicles_in_red_lanes))
   print('Qg = ' + str(no_vehicles_in_green_lanes))
  # print('Wtr ' + str(max_waiting_time_in_red_lanes))
  # print('Wtg ' + str(max_waiting_time_in_green_lanes))
   print('Emg =' + str(no_emv_current_lane))
  # print('Wemr ' + str(emv_waiting_time_red_lane))
   #print('Wemg' + str(emv_waiting_time_green_lane))
   print('Emr =' + str(no_emv_other_lane))
   print('Wtr = ' + str(max_waiting_time_in_red_lanes))
   print('Wtg = ' + str(max_waiting_time_in_green_lanes))
   print('Dr = ' + str(total_distance_R))
   print('Dg = ' + str(total_distance_G))
   
   #Calculate Extenstion time 
   Extension_time.compute()
   output = Extension_time.output['Ge']
   print('output ' + str(output))
   return output

 