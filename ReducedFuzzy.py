# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 15:07:35 2023

@author: Tame
"""

#import time
import numpy as np
#import pandas as pd
#from matplotlib import pyplot as plt
import skfuzzy as fuzz
from skfuzzy import control as ctrl
#Input and output variables
Qg = ctrl.Antecedent(np.arange(0,61,1),'Qg')
Qr = ctrl.Antecedent(np.arange(0,61,1),'Qr')
Emg = ctrl.Antecedent(np.arange(0,3,1),'Emg')
Emr = ctrl.Antecedent(np.arange(0,3,1),'Emr')
Wtg = ctrl.Antecedent(np.arange(0,301,10),'Wtg')
Wtr = ctrl.Antecedent(np.arange(0,301,10),'Wtr')
Dht= ctrl.Consequent(np.arange(0,61,1), 'Dht')
Pem= ctrl.Consequent(np.arange(0,3,1), 'Pem')
Swr= ctrl.Consequent(np.arange(0,2,1),'Swr')
Ge=  ctrl.Consequent(np.arange(0,61,1),'Ge')
# Membership Functions

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
Emr['none']= fuzz.zmf(Emr.universe, 0, 1)
Emr['few']= fuzz.smf(Emr.universe, 0, 1)
Emr['many']= fuzz.smf(Emr.universe, 1, 2)

Wtr ['zero'] = fuzz.trimf(Wtr.universe,[0,0,75])
Wtr ['short'] = fuzz.trimf(Wtr.universe,[0,75,125])
Wtr ['medium'] = fuzz.trimf(Wtr.universe,[125,175,200])
Wtr ['long'] = fuzz.trimf(Wtr.universe,[200,250,275])
Wtr ['very long'] = fuzz.smf(Wtr.universe,275,300)
#Wtr.view()
Wtg ['zero'] = fuzz.trimf(Wtg.universe,[0,0,50])
Wtg ['short'] = fuzz.trimf(Wtg.universe,[0,50,150])
Wtg ['medium'] = fuzz.trimf(Wtg.universe,[125,150,175])
Wtg ['long'] = fuzz.trimf(Wtg.universe,[175,225,275])
Wtg ['very long'] = fuzz.smf(Wtg.universe,275,300)
#Wtg.view()
Pem['no']= fuzz.zmf(Pem.universe, 0, 1)
Pem['Emg']= fuzz.smf(Pem.universe, 0, 1)
Pem['Emr']= fuzz.smf(Pem.universe, 1, 2)
#Pem.view()
Swr['switchr']= fuzz.smf(Swr.universe, 0, 1)
Swr['keepg']= fuzz.smf(Swr.universe, 1, 2)
#Swr.view()

Dht['zero']= fuzz.trimf(Dht.universe,[0,0,15])
Dht['small']= fuzz.trimf(Dht.universe,[0,15,30])
Dht['medium']= fuzz.trimf(Dht.universe,[15,30,45])
Dht['large']= fuzz.trimf(Dht.universe,[30,45,60])
Dht['very large']= fuzz.smf(Dht.universe, 45, 60)
#Dht.view()
Ge['turnr']= fuzz.trimf(Ge.universe,[0,0,15])
Ge['short']= fuzz.trimf(Ge.universe,[0,15,30])
Ge['medium']= fuzz.trimf(Ge.universe,[15,30,45])
Ge['long']= fuzz.trimf(Ge.universe,[30,45,60])
Ge['very long']= fuzz.smf(Ge.universe, 45, 60)

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
rule22 = ctrl.Rule(Qr['very large'] & Wtr['medium'] |Qr['very large'] & Wtr['long'] |Qr['very large'] & Wtr['very long'], Dht['very large'])

                                                
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
rule26=ctrl.Rule(Dht['zero'] | Qg['large'] & Wtr['medium'] & Wtg['short'] | 
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

#Module of Extension time of green time
rule59 = ctrl.Rule(Dht['zero'] & Qg['zero'] & Pem['no'] & Swr['keepg'], Ge['short'])
rule60 = ctrl.Rule(Dht['zero'] & Qg['medium'] & Pem['no'] & Swr['keepg'], Ge['medium'])
rule61 = ctrl.Rule(Dht['zero'] & Qg['very large'] & Pem['no'] & Swr['keepg'], Ge['very long'])
rule62 = ctrl.Rule(Dht['zero'] & Qg['zero'] | Dht['zero'] & Qg['small']|
                   Dht['zero'] & Qg['medium']|Dht['zero'] & Qg['large']|
                   Dht['zero'] & Qg['very large'] & Pem['no']  & Swr['switchr'], Ge['turnr'])
rule63 = ctrl.Rule(Dht['small'] & Qg['zero'] | Dht['small'] & Qg['small']|
                   Dht['small'] & Qg['medium']|Dht['small'] & Qg['large']|
                   Dht['small'] & Qg['very large'] & Pem['no']  & Swr['switchr'], Ge['turnr'])
rule64 = ctrl.Rule(Dht['medium'] & Qg['zero'] | Dht['medium'] & Qg['small']| 
                   Dht['medium'] & Qg['medium']|Dht['medium'] & Qg['large']|
                   Dht['medium'] & Qg['very large'] & Pem['no']  & Swr['switchr'], Ge['turnr'])
rule65 = ctrl.Rule(Dht['medium'] & Qg['zero'] & Pem['no'] & Swr['keepg'], Ge['turnr'])
rule66 = ctrl.Rule(Dht['medium'] & Qg['medium'] & Pem['no'] & Swr['keepg'], Ge['medium'])
rule67 = ctrl.Rule(Dht['medium'] & Qg['very large'] & Pem['no'] & Swr['keepg'], Ge['long'])
rule68 = ctrl.Rule(Dht['large'] & Qg['zero'] & Pem['no'] & Swr['switchr'], Ge['short'])
rule69 = ctrl.Rule(Dht['large'] & Qg['small'] & Pem['no'] & Swr['switchr'], Ge['turnr'])
rule70 = ctrl.Rule(Dht['large'] & Qg['medium'] & Pem['no'] & Swr['switchr'], Ge['short'])
rule71 = ctrl.Rule(Dht['large'] & Qg['large'] | Dht['very large'] & Qg['large'] & Pem['no'] & Swr['switchr'], Ge['medium'])
rule72 = ctrl.Rule(Dht['large'] & Qg['very large'] | Dht['very large'] & Qg['very large'] & Pem['no'] & Swr['switchr'], Ge['long'])
rule73 = ctrl.Rule(Dht['very large'] & Qg['zero'] & Pem['no'] & Swr['keepg'], Ge['turnr'])
rule74 = ctrl.Rule(Dht['very large'] & Qg['medium'] & Pem['no'] & Swr['keepg'], Ge['short'])
rule75 = ctrl.Rule(Dht['very large'] & Qg['very large'] & Pem['no'] & Swr['keepg'], Ge['long'])
rule76 = ctrl.Rule(Dht['very large'] & Qg['zero'] | Dht['very large'] & Qg['small']|
                   Dht['very large'] & Qg['medium'] & Pem['no']  & Swr['switchr'], Ge['turnr'])
rule77 = ctrl.Rule(Dht['zero'] & Qg['zero'] & Pem['Emg']  & Swr['keepg'], Ge['medium'])
rule78 = ctrl.Rule(Dht['zero'] & Qg['medium'] & Pem['Emg'] & Swr['keepg'], Ge['medium'])
rule79 = ctrl.Rule(Dht['zero'] & Qg['very large'] & Pem['Emg'] & Swr['keepg'], Ge['very long'])
rule80 = ctrl.Rule(Dht['medium'] & Qg['zero'] & Pem['Emg'] & Swr['keepg'], Ge['short'])
rule81 = ctrl.Rule(Dht['medium'] & Qg['medium'] & Pem['Emg'] & Swr['keepg'], Ge['medium'])
rule82 = ctrl.Rule(Dht['medium'] & Qg['very large'] & Pem['Emg'] & Swr['keepg'], Ge['very long'])
rule83 = ctrl.Rule(Dht['very large'] & Qg['zero'] & Pem['Emg'] & Swr['keepg'], Ge['short'])
rule84 = ctrl.Rule(Dht['very large'] & Qg['medium'] & Pem['Emg'] & Swr['keepg'], Ge['medium'])
rule85 = ctrl.Rule(Dht['very large'] & Qg['very large'] & Pem['Emg'] & Swr['keepg'], Ge['very long'])
rule86 = ctrl.Rule(Dht['zero'] & Qg['zero'] & Pem['Emg']  & Swr['switchr'], Ge['medium'])
rule87 =ctrl.Rule(Dht['small'] & Qg['zero'] | Dht['medium'] & Qg['zero'] | Dht['large'] & Qg['zero'] |
                  Dht['very large'] & Qg['zero'] & Pem['Emg'] & Swr['switchr'], Ge['short'])
rule88 =ctrl.Rule(Dht['zero'] & Qg['small'] | Dht['small'] & Qg['small'] | 
                  Dht['medium'] & Qg['small'] & Pem['Emg'] & Swr['switchr'], Ge['short'])
rule89 =ctrl.Rule(Dht['large'] & Qg['small'] | Dht['very large'] & Qg['small']  & Pem['Emg'] & Swr['switchr'], Ge['medium'])
rule90 = ctrl.Rule(Dht['zero'] & Qg['medium'] & Pem['Emg']  & Swr['switchr'], Ge['medium'])
rule91 = ctrl.Rule(Dht['small'] & Qg['medium'] & Pem['Emg']  & Swr['switchr'], Ge['short'])
rule92 =ctrl.Rule(Dht['medium'] & Qg['medium'] | Dht['large'] & Qg['medium'] | 
                  Dht['very large'] & Qg['medium'] & Pem['Emg'] & Swr['switchr'], Ge['medium'])
rule93 =ctrl.Rule(Dht['zero'] & Qg['large'] | Dht['small'] & Qg['large'] | 
                  Dht['medium'] & Qg['large'] & Pem['Emg'] & Swr['switchr'], Ge['medium'])
rule94 =ctrl.Rule(Dht['large'] & Qg['large'] | 
                  Dht['very large'] & Qg['large']  & Pem['Emg'] & Swr['switchr'], Ge['long'])
rule95 =ctrl.Rule(Dht['zero'] & Qg['very large'] | Dht['small'] & Qg['very large'] | 
                  Dht['medium'] & Qg['very large'] & Pem['Emg'] & Swr['switchr'], Ge['long'])
rule96 =ctrl.Rule(Dht['large'] & Qg['very large'] |
                  Dht['very large'] & Qg['very large']  & Pem['Emg'] & Swr['switchr'], Ge['very long'])
rule97 = ctrl.Rule(Dht['zero'] & Qg['zero'] & Pem['Emr'] & Swr['switchr'], Ge['turnr'])
rule98 = ctrl.Rule(Dht['zero'] & Qg['medium'] & Pem['Emr'] & Swr['switchr'], Ge['turnr'])
rule99 = ctrl.Rule(Dht['zero'] & Qg['very large'] & Pem['Emr'] & Swr['switchr'], Ge['turnr'])
rule100 = ctrl.Rule(Dht['medium'] & Qg['zero'] & Pem['Emr'] & Swr['switchr'], Ge['turnr'])
rule101 = ctrl.Rule(Dht['medium'] & Qg['medium'] & Pem['Emr'] & Swr['switchr'], Ge['turnr'])
rule102 = ctrl.Rule(Dht['medium'] & Qg['very large'] & Pem['Emr'] & Swr['switchr'], Ge['turnr'])
rule103 = ctrl.Rule(Dht['very large'] & Qg['zero'] & Pem['Emr'] & Swr['switchr'], Ge['turnr'])
rule104 = ctrl.Rule(Dht['very large'] & Qg['medium'] & Pem['Emr'] & Swr['switchr'], Ge['turnr'])
rule105 = ctrl.Rule(Dht['very large'] & Qg['very large'] & Pem['Emr'] & Swr['switchr'], Ge['turnr'])
rule106 = ctrl.Rule(Dht['medium'] & Qg['small'] & Pem['Emr'] & Swr['switchr'], Ge['short'])
rule107 = ctrl.Rule(Dht['zero'] & Qg['zero'] & Pem['Emr'] & Swr['keepg'], Ge['turnr'])
rule108 = ctrl.Rule(Dht['zero'] & Qg['medium'] & Pem['Emr'] & Swr['keepg'], Ge['turnr'])
rule109 = ctrl.Rule(Dht['zero'] & Qg['very large'] & Pem['Emr'] & Swr['keepg'], Ge['turnr'])
rule110 = ctrl.Rule(Dht['medium'] & Qg['zero'] & Pem['Emr'] & Swr['keepg'], Ge['turnr'])
rule111 = ctrl.Rule(Dht['medium'] & Qg['medium'] & Pem['Emr'] & Swr['keepg'], Ge['turnr'])
rule112 = ctrl.Rule(Dht['medium'] & Qg['very large'] & Pem['Emr'] & Swr['keepg'], Ge['turnr'])
rule113 = ctrl.Rule(Dht['very large'] & Qg['zero'] & Pem['Emr'] & Swr['keepg'], Ge['turnr'])
rule114 = ctrl.Rule(Dht['very large'] & Qg['medium'] & Pem['Emr'] & Swr['keepg'], Ge['turnr'])
rule115 = ctrl.Rule(Dht['very large'] & Qg['very large'] & Pem['Emr'] & Swr['keepg'], Ge['turnr'])


Etdm_ctrl = ctrl.ControlSystem([rule1, rule2, rule3,rule4,rule5,rule6, rule7,rule8,rule9,rule10,
                                rule11, rule12,rule13,rule14,rule15, rule16, rule17,rule18,rule19,
                                rule20, rule21,rule22,rule23, rule24,rule25,rule26, rule27,rule28,
                                rule29, rule30,rule31,rule32,rule33, rule34,rule35,rule36,rule37,rule38,
                                rule39, rule40,rule41,rule42, rule43,rule44,rule45, rule46,rule47,rule48,
                                rule49,rule50, rule51, rule52,rule53,rule54, rule55,
                                rule56,rule57,rule58,rule59,rule60,rule61,rule62,rule63,rule64, 
                                rule65,rule66,rule67,rule68,rule69,rule70,rule71,rule72,rule73,rule74,rule75,rule76,
                                rule77,rule78,rule79,rule80,rule81,rule82,rule83,rule84,rule85,rule86,rule87,rule88,
                                rule89,rule90,rule91,rule92,rule93,rule94,rule95,rule96,rule97,rule98,rule99,rule100,
                                rule101,rule102,rule103,rule104,rule105,rule106,rule107,rule108,rule109,rule110,rule111,
                                rule112,rule113,rule114,rule115])
Extension_time = ctrl.ControlSystemSimulation(Etdm_ctrl)

def fuzzy_controller_function1(no_vehicles_in_red_lanes,
                                            no_vehicles_in_green_lanes,
                                            no_emv_current_lane,  no_emv_other_lane, 
                                            max_waiting_time_in_red_lanes, 
                                            max_waiting_time_in_green_lanes):
                                            
                                           
                                            
    Extension_time.input['Qr'] = int(no_vehicles_in_red_lanes)
    Extension_time.input['Qg'] = int(no_vehicles_in_green_lanes)
    Extension_time.input['Emg'] = int(no_emv_current_lane)
    Extension_time.input['Emr'] = int(no_emv_other_lane)
    Extension_time.input['Wtr'] = int(max_waiting_time_in_red_lanes)
    Extension_time.input['Wtg'] = int(max_waiting_time_in_green_lanes)
    #Extension_time.input['Dht'] = int(heavy_traffic)
    #Extension_time.input['Pem'] = int(priority_Emg)
    #Extension_time.input['Swr'] = int(Swr)
    #Extension_time.input['Wtg'] = int(max_waiting_time_in_green_lanes)
   # Extension_time.input['Wtr'] = int(max_waiting_time_in_red_lanes)
   # Extension_time.input['Wemr'] = int(emv_waiting_time_red_lane)
    #Extension_time.input['Wemg'] = int(emv_waiting_time_green_lane)
  
    
    
   
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
    
    # Prioritize emergency car
    '''
    Prioritize_emergencyCar.compute()
    output = Prioritize_emergencyCar.output('Pem')
    print('prioritize_emergency' + str(output))
    return  output
    '''
    
    '''
    # defuzification for Degree of heavy traffic
    Extension_time.compute()
    Degree_heavy_traffic = Extension_time.Degree_heavy_traffic['Dht']
    print('Degree_heavy_traffic ' + str(Degree_heavy_traffic))
    return Degree_heavy_traffic
    '''
   
     #Calculate Extenstion time 
    Extension_time.compute()
    output = Extension_time.output['Ge']
    print('output ' + str(output))
    return output











































































































































































