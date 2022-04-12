# -*- coding: utf-8 -*-
# -*- coding: iso-8859-1 -*-
# =====================================================================>
## By CT(T) ALANA
## =====================================================================>

# Import libraries
import datetime, time
import os, sys
import pandas as pd

# =====================================================================>
print("="*50)
print('DATE TIME: ', end='')
print(datetime.datetime.today().now())
print('Temperature into CMCs ICEX')
print("="*50)
os.system("sshpass -p '@dmd@30' ssh root@10.13.100.30 'cmcexec sensor | grep -i Inlet' > temperature_dpns30.log")
with open("temperature_dpns30.log", "r") as temperature:
        tempdpns30 = temperature.read()
print(tempdpns30)

df = pd.read_log('temperature_dpns30.log')
print(df)

# =====================================================================>
print("="*50)
print('DATE TIME: ', end='')
print(datetime.datetime.today().now())
print('Temperature into Apollo (dpns41 and nodes)')
print("="*50)
os.system("sshpass -p '@dmd@40' ssh root@10.13.100.40 'pdsh -g compute ipmitool sensor | grep -i Ambient' > temperature_dpns40.log")
with open("temperature_dpns40.log", "r") as temperature:
        tempdpns40 = temperature.read()
print(tempdpns40)


