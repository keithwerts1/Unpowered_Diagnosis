"""
This is a program that is used to generate the UnpoweredDevices report
"""


import csv
import sys
import pickle
import re
import fnmatch
import glob
import copy
import os
from datetime import datetime
import time


__author__ ="Keith Wertsching"
__version__ ="1.0.0"
__status__="Development"



"""                
print('################################################################')
print('################################################################')
print('################################################################')
"""




############## Code ##############


class KEEPER:
    def __init__(self, Name):
        self.Name = Name

    def InitStatement(x):
        chlist = [' ','(',')']
        namelist = []
        for name in x:
            display = "".join(", " + name + ' = ""')
            namelist.append(display)
        return ''.join(namelist)

    def CleanName(x):
        chlist = [' ','(',')','+','#']
        y = list(x)
        for ch in chlist:
            while ch in y:
                y.remove(ch)
        
        return "".join(y)

    def CreateKeeper(f,c):
        NewList = f
        NLHeaders = [KEEPER.CleanName(name) for name in NewList.pop(0)]

        print("class "+c+":")
        print('     \"""', c, '\"""')
        print("     def __init__(self, Name",KEEPER.InitStatement(NLHeaders)+'):')
        print("          KEEPER.__init__(self, Name)")
        for name in NLHeaders:
            print("          self."+name+" = "+name)
        print("")
        print("     def get_Name(self):")
        print("          return self.Name")
        print("")
        for name in NLHeaders:
            print("     def get_"+name+"(self):")
            print("          return self."+name)
            print("")
    
        print("     def Search_by_Name(x):")
        print("          for child in "+c+"DB:")
        print("               if x in "+c+".get_Name(child):")
        print("                    print('--------------------')")
        for name in NLHeaders:
            print("                    print('"+name+": ', "+c+".get_"+name+"(child))")
        print("                    print('--------------------')")

        print("")
        print("")
        print("#with open('Data\\"+c+"Pickle', 'rb') as "+c+"DBRead:")
        print("#    "+c+"DB = pickle.load("+c+"DBRead)")

        print("")
        print("########################")
        print("### Create Databases ###")
        print("########################")
        print("")
        print("")
        print("")
        print(c)
        print("")
        print("")
        print("")
        print(c+"DB = []")
        print("for item in "+c+"List:")
        print("    child = "+c+"(item[0])")
        print("    "+c+"DB.append(child)")
        count = 0
        for name in NLHeaders:
            print("    child."+name+" = (item["+str(count)+"])")
            count += 1
        print("")
        print("")
        print("with open('Data\\"+c+"Pickle', 'wb') as "+c+"DBCreate:")
        print("    pickle.dump("+c+"DB, "+c+"DBCreate)")
        print("")
        print("")
        print("with open('Data\\"+c+"Pickle', 'rb') as "+c+"DBRead:")
        print("    "+c+"DB = pickle.load("+c+"DBRead)")
        print("############## Zoo ##############")
        print("")
        print("")
        print(c+".Search_by_Name('"+NewList[1][0]+"')")






class CONNECTIVITY:
     """ CONNECTIVITY """
     def __init__(self, Name , MSLINK = "", FEATURE_ID = "", NODE1 = "", NODE2 = "", NORMAL_STATUS = "", PHASE = "", LOCATION = "", X_COORD = "", Y_COORD = "", RATING_KVA = "", RATING_AMPS = "", SWITCHING_GROUP_ID = "", VOLTAGE_KV = "", GANG_OPERABLE = "", STYLE_SET_ID = "", NORMAL_FEEDER_A = "", NORMAL_FEEDER_B = "", NORMAL_FEEDER_C = "", NORMAL_OVERRIDES_A = "", NORMAL_OVERRIDES_B = "", NORMAL_OVERRIDES_C = "", MAP_LEVEL = "", FEEDER_NBR = "", TIE_SSTA_C = "", TIE_FEEDER_NBR = "", FEEDER_TYPE_C = "", PROTECTIVE_DEVICE_FID = "", PHASE_OPERATED = "", STATUS_NORMAL_C = "", CONFIG_C = "", VOLT_2_Q = "", NETWORK_ID = "", UPSTREAM_PROTDEV_Q = "", UPSTREAM_NODE = "", PP_FEEDER_1_ID = "", PP_SSTA_C = "", PP_FEEDER_NBR = "", PP_FEEDER_2_ID = "", PP_TIE_SSTA_C = "", PP_TIE_FEEDER_NBR = "", PP_PROTECTIVE_DEVICE_FID = "", PP_VOLT_1_Q = "", PP_VOLT_2_Q = "", PP_NETWORK_ID = "", PP_UPSTREAM_PROTDEV_Q = "", PP_UPSTREAM_NODE = "", SSTA_C = "", FEEDER_1_ID = "", FEEDER_2_ID = "", OMS_NAME = "", FEATURE_STATE_C = "", ORIENTATION_C = "", OWNER1_ID = "", OWNER2_ID = "", DATA_UTIL_C = "", STRUCTURE_ID = "", OGGX_H = "", OGGY_H = "", OGGZ_H = "", LATITUDE = "", LONGITUDE = "", OWNED_TYPE_C = "", MAINTAINED_BY_C = "", DESIGN_RESP = "", LOC_GRADE = "", COLLECT_METH = "", COLLECT_D = "", ABANDONED_D = "", LENGTH_GRAPHIC_Q = "", LENGTH_ACTUAL_Q = "", REPLACED_FID = "", LENGTH_GRAPHIC_FT = "", MOBILE_SUBSET_C = "", G3E_ID = "", CUSTOMER_DEVICE_NAME = "", FNN = [], SNN = [], PSTATUS = []):
          KEEPER.__init__(self, Name)
          self.MSLINK = MSLINK
          self.FEATURE_ID = FEATURE_ID
          self.NODE1 = NODE1
          self.NODE2 = NODE2
          self.NORMAL_STATUS = NORMAL_STATUS
          self.PHASE = PHASE
          self.LOCATION = LOCATION
          self.X_COORD = X_COORD
          self.Y_COORD = Y_COORD
          self.RATING_KVA = RATING_KVA
          self.RATING_AMPS = RATING_AMPS
          self.SWITCHING_GROUP_ID = SWITCHING_GROUP_ID
          self.VOLTAGE_KV = VOLTAGE_KV
          self.GANG_OPERABLE = GANG_OPERABLE
          self.STYLE_SET_ID = STYLE_SET_ID
          self.NORMAL_FEEDER_A = NORMAL_FEEDER_A
          self.NORMAL_FEEDER_B = NORMAL_FEEDER_B
          self.NORMAL_FEEDER_C = NORMAL_FEEDER_C
          self.NORMAL_OVERRIDES_A = NORMAL_OVERRIDES_A
          self.NORMAL_OVERRIDES_B = NORMAL_OVERRIDES_B
          self.NORMAL_OVERRIDES_C = NORMAL_OVERRIDES_C
          self.MAP_LEVEL = MAP_LEVEL
          self.FEEDER_NBR = FEEDER_NBR
          self.TIE_SSTA_C = TIE_SSTA_C
          self.TIE_FEEDER_NBR = TIE_FEEDER_NBR
          self.FEEDER_TYPE_C = FEEDER_TYPE_C
          self.PROTECTIVE_DEVICE_FID = PROTECTIVE_DEVICE_FID
          self.PHASE_OPERATED = PHASE_OPERATED
          self.STATUS_NORMAL_C = STATUS_NORMAL_C
          self.CONFIG_C = CONFIG_C
          self.VOLT_2_Q = VOLT_2_Q
          self.NETWORK_ID = NETWORK_ID
          self.UPSTREAM_PROTDEV_Q = UPSTREAM_PROTDEV_Q
          self.UPSTREAM_NODE = UPSTREAM_NODE
          self.PP_FEEDER_1_ID = PP_FEEDER_1_ID
          self.PP_SSTA_C = PP_SSTA_C
          self.PP_FEEDER_NBR = PP_FEEDER_NBR
          self.PP_FEEDER_2_ID = PP_FEEDER_2_ID
          self.PP_TIE_SSTA_C = PP_TIE_SSTA_C
          self.PP_TIE_FEEDER_NBR = PP_TIE_FEEDER_NBR
          self.PP_PROTECTIVE_DEVICE_FID = PP_PROTECTIVE_DEVICE_FID
          self.PP_VOLT_1_Q = PP_VOLT_1_Q
          self.PP_VOLT_2_Q = PP_VOLT_2_Q
          self.PP_NETWORK_ID = PP_NETWORK_ID
          self.PP_UPSTREAM_PROTDEV_Q = PP_UPSTREAM_PROTDEV_Q
          self.PP_UPSTREAM_NODE = PP_UPSTREAM_NODE
          self.SSTA_C = SSTA_C
          self.FEEDER_1_ID = FEEDER_1_ID
          self.FEEDER_2_ID = FEEDER_2_ID
          self.OMS_NAME = OMS_NAME
          self.FEATURE_STATE_C = FEATURE_STATE_C
          self.ORIENTATION_C = ORIENTATION_C
          self.OWNER1_ID = OWNER1_ID
          self.OWNER2_ID = OWNER2_ID
          self.DATA_UTIL_C = DATA_UTIL_C
          self.STRUCTURE_ID = STRUCTURE_ID
          self.OGGX_H = OGGX_H
          self.OGGY_H = OGGY_H
          self.OGGZ_H = OGGZ_H
          self.LATITUDE = LATITUDE
          self.LONGITUDE = LONGITUDE
          self.OWNED_TYPE_C = OWNED_TYPE_C
          self.MAINTAINED_BY_C = MAINTAINED_BY_C
          self.DESIGN_RESP = DESIGN_RESP
          self.LOC_GRADE = LOC_GRADE
          self.COLLECT_METH = COLLECT_METH
          self.COLLECT_D = COLLECT_D
          self.ABANDONED_D = ABANDONED_D
          self.LENGTH_GRAPHIC_Q = LENGTH_GRAPHIC_Q
          self.LENGTH_ACTUAL_Q = LENGTH_ACTUAL_Q
          self.REPLACED_FID = REPLACED_FID
          self.LENGTH_GRAPHIC_FT = LENGTH_GRAPHIC_FT
          self.MOBILE_SUBSET_C = MOBILE_SUBSET_C
          self.G3E_ID = G3E_ID
          self.CUSTOMER_DEVICE_NAME = CUSTOMER_DEVICE_NAME
          self.FNN = FNN
          self.SNN = SNN
          self.PSTATUS = PSTATUS

     def get_Name(self):
          return self.Name

     def get_MSLINK(self):
          return self.MSLINK

     def get_FEATURE_ID(self):
          return self.FEATURE_ID

     def get_NODE1(self):
          return self.NODE1

     def get_NODE2(self):
          return self.NODE2

     def get_NORMAL_STATUS(self):
          return self.NORMAL_STATUS

     def get_PHASE(self):
          return self.PHASE

     def get_LOCATION(self):
          return self.LOCATION

     def get_X_COORD(self):
          return self.X_COORD

     def get_Y_COORD(self):
          return self.Y_COORD

     def get_RATING_KVA(self):
          return self.RATING_KVA

     def get_RATING_AMPS(self):
          return self.RATING_AMPS

     def get_SWITCHING_GROUP_ID(self):
          return self.SWITCHING_GROUP_ID

     def get_VOLTAGE_KV(self):
          return self.VOLTAGE_KV

     def get_GANG_OPERABLE(self):
          return self.GANG_OPERABLE

     def get_STYLE_SET_ID(self):
          return self.STYLE_SET_ID

     def get_NORMAL_FEEDER_A(self):
          return self.NORMAL_FEEDER_A

     def get_NORMAL_FEEDER_B(self):
          return self.NORMAL_FEEDER_B

     def get_NORMAL_FEEDER_C(self):
          return self.NORMAL_FEEDER_C

     def get_NORMAL_OVERRIDES_A(self):
          return self.NORMAL_OVERRIDES_A

     def get_NORMAL_OVERRIDES_B(self):
          return self.NORMAL_OVERRIDES_B

     def get_NORMAL_OVERRIDES_C(self):
          return self.NORMAL_OVERRIDES_C

     def get_MAP_LEVEL(self):
          return self.MAP_LEVEL

     def get_FEEDER_NBR(self):
          return self.FEEDER_NBR

     def get_TIE_SSTA_C(self):
          return self.TIE_SSTA_C

     def get_TIE_FEEDER_NBR(self):
          return self.TIE_FEEDER_NBR

     def get_FEEDER_TYPE_C(self):
          return self.FEEDER_TYPE_C

     def get_PROTECTIVE_DEVICE_FID(self):
          return self.PROTECTIVE_DEVICE_FID

     def get_PHASE_OPERATED(self):
          return self.PHASE_OPERATED

     def get_STATUS_NORMAL_C(self):
          return self.STATUS_NORMAL_C

     def get_CONFIG_C(self):
          return self.CONFIG_C

     def get_VOLT_2_Q(self):
          return self.VOLT_2_Q

     def get_NETWORK_ID(self):
          return self.NETWORK_ID

     def get_UPSTREAM_PROTDEV_Q(self):
          return self.UPSTREAM_PROTDEV_Q

     def get_UPSTREAM_NODE(self):
          return self.UPSTREAM_NODE

     def get_PP_FEEDER_1_ID(self):
          return self.PP_FEEDER_1_ID

     def get_PP_SSTA_C(self):
          return self.PP_SSTA_C

     def get_PP_FEEDER_NBR(self):
          return self.PP_FEEDER_NBR

     def get_PP_FEEDER_2_ID(self):
          return self.PP_FEEDER_2_ID

     def get_PP_TIE_SSTA_C(self):
          return self.PP_TIE_SSTA_C

     def get_PP_TIE_FEEDER_NBR(self):
          return self.PP_TIE_FEEDER_NBR

     def get_PP_PROTECTIVE_DEVICE_FID(self):
          return self.PP_PROTECTIVE_DEVICE_FID

     def get_PP_VOLT_1_Q(self):
          return self.PP_VOLT_1_Q

     def get_PP_VOLT_2_Q(self):
          return self.PP_VOLT_2_Q

     def get_PP_NETWORK_ID(self):
          return self.PP_NETWORK_ID

     def get_PP_UPSTREAM_PROTDEV_Q(self):
          return self.PP_UPSTREAM_PROTDEV_Q

     def get_PP_UPSTREAM_NODE(self):
          return self.PP_UPSTREAM_NODE

     def get_SSTA_C(self):
          return self.SSTA_C

     def get_FEEDER_1_ID(self):
          return self.FEEDER_1_ID

     def get_FEEDER_2_ID(self):
          return self.FEEDER_2_ID

     def get_OMS_NAME(self):
          return self.OMS_NAME

     def get_FEATURE_STATE_C(self):
          return self.FEATURE_STATE_C

     def get_ORIENTATION_C(self):
          return self.ORIENTATION_C

     def get_OWNER1_ID(self):
          return self.OWNER1_ID

     def get_OWNER2_ID(self):
          return self.OWNER2_ID

     def get_DATA_UTIL_C(self):
          return self.DATA_UTIL_C

     def get_STRUCTURE_ID(self):
          return self.STRUCTURE_ID

     def get_OGGX_H(self):
          return self.OGGX_H

     def get_OGGY_H(self):
          return self.OGGY_H

     def get_OGGZ_H(self):
          return self.OGGZ_H

     def get_LATITUDE(self):
          return self.LATITUDE

     def get_LONGITUDE(self):
          return self.LONGITUDE

     def get_OWNED_TYPE_C(self):
          return self.OWNED_TYPE_C

     def get_MAINTAINED_BY_C(self):
          return self.MAINTAINED_BY_C

     def get_DESIGN_RESP(self):
          return self.DESIGN_RESP

     def get_LOC_GRADE(self):
          return self.LOC_GRADE

     def get_COLLECT_METH(self):
          return self.COLLECT_METH

     def get_COLLECT_D(self):
          return self.COLLECT_D

     def get_ABANDONED_D(self):
          return self.ABANDONED_D

     def get_LENGTH_GRAPHIC_Q(self):
          return self.LENGTH_GRAPHIC_Q

     def get_LENGTH_ACTUAL_Q(self):
          return self.LENGTH_ACTUAL_Q

     def get_REPLACED_FID(self):
          return self.REPLACED_FID

     def get_LENGTH_GRAPHIC_FT(self):
          return self.LENGTH_GRAPHIC_FT

     def get_MOBILE_SUBSET_C(self):
          return self.MOBILE_SUBSET_C

     def get_G3E_ID(self):
          return self.G3E_ID
    
     def get_CUSTOMER_DEVICE_NAME(self):
          return self.CUSTOMER_DEVICE_NAME

     def get_FNN(self):
          return self.FNN

     def get_SNN(self):
          return self.SNN

     def get_PSTATUS(self):
          return self.PSTATUS
    

     def Search_by_Name(x):
          for child in CONNECTIVITYDB:
               if x in CONNECTIVITY.get_Name(child):
                    print('--------------------')
                    print('Name: ', CONNECTIVITY.get_Name(child))
                    print('MSLINK: ', CONNECTIVITY.get_MSLINK(child))
                    print('Feature ID: ', CONNECTIVITY.get_FEATURE_ID(child))
                    print('Feature: ', G3E_FEATURE.Return_G3E_USERNAME(CONNECTIVITY.get_FEATURE_ID(child)))
                    print('Phase: ', CONNECTIVITY.get_PHASE(child))
                    print('NODE1: ', CONNECTIVITY.get_NODE1(child))
                    print('NODE2: ', CONNECTIVITY.get_NODE2(child))
                    print('OWNER1: ', CONNECTIVITY.get_OWNER1_ID(child))
                    print('OWNER2: ', CONNECTIVITY.get_OWNER2_ID(child))
                    print('FNN: ', CONNECTIVITY.get_FNN(child))
                    print('SNN: ', CONNECTIVITY.get_SNN(child))
                    print('PSTATUS: ', CONNECTIVITY.get_PSTATUS(child))

     def Search_by_Owner(x):
        for child in CONNECTIVITYDB:
            if x in CONNECTIVITY.get_OWNER1_ID(child):
                    print('--------------------')
                    print('Name: ', CONNECTIVITY.get_Name(child))
                    print('MSLINK: ', CONNECTIVITY.get_MSLINK(child))
                    print('Feature ID: ', CONNECTIVITY.get_FEATURE_ID(child))
                    print('Feature: ', G3E_FEATURE.Return_G3E_USERNAME(CONNECTIVITY.get_FEATURE_ID(child)))
                    print('Phase: ', CONNECTIVITY.get_PHASE(child))
                    print('NODE1: ', CONNECTIVITY.get_NODE1(child))
                    print('NODE2: ', CONNECTIVITY.get_NODE2(child))
                    print('OWNER1: ', CONNECTIVITY.get_OWNER1_ID(child))
                    print('OWNER2: ', CONNECTIVITY.get_OWNER2_ID(child))
                    print('FNN: ', CONNECTIVITY.get_FNN(child))
                    print('SNN: ', CONNECTIVITY.get_SNN(child))
                    print('PSTATUS: ', CONNECTIVITY.get_PSTATUS(child))
            elif x in CONNECTIVITY.get_OWNER2_ID(child):
                    print('--------------------')
                    print('Name: ', CONNECTIVITY.get_Name(child))
                    print('MSLINK: ', CONNECTIVITY.get_MSLINK(child))
                    print('Feature ID: ', CONNECTIVITY.get_FEATURE_ID(child))
                    print('Feature: ', G3E_FEATURE.Return_G3E_USERNAME(CONNECTIVITY.get_FEATURE_ID(child)))
                    print('Phase: ', CONNECTIVITY.get_PHASE(child))
                    print('NODE1: ', CONNECTIVITY.get_NODE1(child))
                    print('NODE2: ', CONNECTIVITY.get_NODE2(child))
                    print('OWNER1: ', CONNECTIVITY.get_OWNER1_ID(child))
                    print('OWNER2: ', CONNECTIVITY.get_OWNER2_ID(child))
                    print('FNN: ', CONNECTIVITY.get_FNN(child))
                    print('SNN: ', CONNECTIVITY.get_SNN(child))
                    print('PSTATUS: ', CONNECTIVITY.get_PSTATUS(child))

     def Search_by_Node(x):
        for child in CONNECTIVITYDB:
            if x in CONNECTIVITY.get_NODE1(child) and CONNECTIVITY.get_NODE1(child) != 0:
                    print('--------------------')
                    print('Name: ', CONNECTIVITY.get_Name(child))
                    print('MSLINK: ', CONNECTIVITY.get_MSLINK(child))
                    print('Feature ID: ', CONNECTIVITY.get_FEATURE_ID(child))
                    print('Feature: ', G3E_FEATURE.Return_G3E_USERNAME(CONNECTIVITY.get_FEATURE_ID(child)))
                    print('Phase: ', CONNECTIVITY.get_PHASE(child))
                    print('NODE1: ', CONNECTIVITY.get_NODE1(child))
                    print('NODE2: ', CONNECTIVITY.get_NODE2(child))
                    print('OWNER1: ', CONNECTIVITY.get_OWNER1_ID(child))
                    print('OWNER2: ', CONNECTIVITY.get_OWNER2_ID(child))
                    print('FNN: ', CONNECTIVITY.get_FNN(child))
                    print('SNN: ', CONNECTIVITY.get_SNN(child))
                    print('PSTATUS: ', CONNECTIVITY.get_PSTATUS(child))
            elif x in CONNECTIVITY.get_NODE2(child) and CONNECTIVITY.get_NODE2(child) != 0:
                    print('--------------------')
                    print('Name: ', CONNECTIVITY.get_Name(child))
                    print('MSLINK: ', CONNECTIVITY.get_MSLINK(child))
                    print('Feature ID: ', CONNECTIVITY.get_FEATURE_ID(child))
                    print('Feature: ', G3E_FEATURE.Return_G3E_USERNAME(CONNECTIVITY.get_FEATURE_ID(child)))
                    print('Phase: ', CONNECTIVITY.get_PHASE(child))
                    print('NODE1: ', CONNECTIVITY.get_NODE1(child))
                    print('NODE2: ', CONNECTIVITY.get_NODE2(child))
                    print('OWNER1: ', CONNECTIVITY.get_OWNER1_ID(child))
                    print('OWNER2: ', CONNECTIVITY.get_OWNER2_ID(child))
                    print('FNN: ', CONNECTIVITY.get_FNN(child))
                    print('SNN: ', CONNECTIVITY.get_SNN(child))
                    print('PSTATUS: ', CONNECTIVITY.get_PSTATUS(child))  

                
    


class G3E_FEATURE:
     """ G3E_FEATURE """
     def __init__(self, Name , G3E_FNO = "", G3E_USERNAME = "", G3E_TOOLTIP = "", G3E_PRIMARYGEOGRAPHICCNO = "", G3E_PRIMARYATTRIBUTECNO = "", G3E_DCNO = "", G3E_PRIMARYDETAILCNO = "", G3E_NUMBEROFNODES = "", G3E_IMPORTFEATURENAME = "", G3E_REPLACE = "", G3E_NAME = "", G3E_EDITDATE = "", G3E_LOCALECOMMENT = "", G3E_MERGE = "", G3E_CLASSIFICATIONANO = "", G3E_IDENTIFIERVIEW = "", G3E_BULKEDIT = "", G3E_ICONORDINAL = "", G3E_EDITROLE = "", G3E_SELECTROLE = "", G3E_DELETEROLE = "", G3E_RINO = "", G3E_RIARGGROUPNO = "", G3E_PRIMARYSCHEMCNO = "", G3E_SECONDARYSCHEMCNO = "", G3E_LABELSCHEMCNO = "", G3E_ADDRELATEDROLE = "", G3E_EDITRELATIONSHIPSROLE = ""):
          KEEPER.__init__(self, Name)
          self.G3E_FNO = G3E_FNO
          self.G3E_USERNAME = G3E_USERNAME
          self.G3E_TOOLTIP = G3E_TOOLTIP
          self.G3E_PRIMARYGEOGRAPHICCNO = G3E_PRIMARYGEOGRAPHICCNO
          self.G3E_PRIMARYATTRIBUTECNO = G3E_PRIMARYATTRIBUTECNO
          self.G3E_DCNO = G3E_DCNO
          self.G3E_PRIMARYDETAILCNO = G3E_PRIMARYDETAILCNO
          self.G3E_NUMBEROFNODES = G3E_NUMBEROFNODES
          self.G3E_IMPORTFEATURENAME = G3E_IMPORTFEATURENAME
          self.G3E_REPLACE = G3E_REPLACE
          self.G3E_NAME = G3E_NAME
          self.G3E_EDITDATE = G3E_EDITDATE
          self.G3E_LOCALECOMMENT = G3E_LOCALECOMMENT
          self.G3E_MERGE = G3E_MERGE
          self.G3E_CLASSIFICATIONANO = G3E_CLASSIFICATIONANO
          self.G3E_IDENTIFIERVIEW = G3E_IDENTIFIERVIEW
          self.G3E_BULKEDIT = G3E_BULKEDIT
          self.G3E_ICONORDINAL = G3E_ICONORDINAL
          self.G3E_EDITROLE = G3E_EDITROLE
          self.G3E_SELECTROLE = G3E_SELECTROLE
          self.G3E_DELETEROLE = G3E_DELETEROLE
          self.G3E_RINO = G3E_RINO
          self.G3E_RIARGGROUPNO = G3E_RIARGGROUPNO
          self.G3E_PRIMARYSCHEMCNO = G3E_PRIMARYSCHEMCNO
          self.G3E_SECONDARYSCHEMCNO = G3E_SECONDARYSCHEMCNO
          self.G3E_LABELSCHEMCNO = G3E_LABELSCHEMCNO
          self.G3E_ADDRELATEDROLE = G3E_ADDRELATEDROLE
          self.G3E_EDITRELATIONSHIPSROLE = G3E_EDITRELATIONSHIPSROLE

     def get_Name(self):
          return self.Name

     def get_G3E_FNO(self):
          return self.G3E_FNO

     def get_G3E_USERNAME(self):
          return self.G3E_USERNAME

     def get_G3E_TOOLTIP(self):
          return self.G3E_TOOLTIP

     def get_G3E_PRIMARYGEOGRAPHICCNO(self):
          return self.G3E_PRIMARYGEOGRAPHICCNO

     def get_G3E_PRIMARYATTRIBUTECNO(self):
          return self.G3E_PRIMARYATTRIBUTECNO

     def get_G3E_DCNO(self):
          return self.G3E_DCNO

     def get_G3E_PRIMARYDETAILCNO(self):
          return self.G3E_PRIMARYDETAILCNO

     def get_G3E_NUMBEROFNODES(self):
          return self.G3E_NUMBEROFNODES

     def get_G3E_IMPORTFEATURENAME(self):
          return self.G3E_IMPORTFEATURENAME

     def get_G3E_REPLACE(self):
          return self.G3E_REPLACE

     def get_G3E_NAME(self):
          return self.G3E_NAME

     def get_G3E_EDITDATE(self):
          return self.G3E_EDITDATE

     def get_G3E_LOCALECOMMENT(self):
          return self.G3E_LOCALECOMMENT

     def get_G3E_MERGE(self):
          return self.G3E_MERGE

     def get_G3E_CLASSIFICATIONANO(self):
          return self.G3E_CLASSIFICATIONANO

     def get_G3E_IDENTIFIERVIEW(self):
          return self.G3E_IDENTIFIERVIEW

     def get_G3E_BULKEDIT(self):
          return self.G3E_BULKEDIT

     def get_G3E_ICONORDINAL(self):
          return self.G3E_ICONORDINAL

     def get_G3E_EDITROLE(self):
          return self.G3E_EDITROLE

     def get_G3E_SELECTROLE(self):
          return self.G3E_SELECTROLE

     def get_G3E_DELETEROLE(self):
          return self.G3E_DELETEROLE

     def get_G3E_RINO(self):
          return self.G3E_RINO

     def get_G3E_RIARGGROUPNO(self):
          return self.G3E_RIARGGROUPNO

     def get_G3E_PRIMARYSCHEMCNO(self):
          return self.G3E_PRIMARYSCHEMCNO

     def get_G3E_SECONDARYSCHEMCNO(self):
          return self.G3E_SECONDARYSCHEMCNO

     def get_G3E_LABELSCHEMCNO(self):
          return self.G3E_LABELSCHEMCNO

     def get_G3E_ADDRELATEDROLE(self):
          return self.G3E_ADDRELATEDROLE

     def get_G3E_EDITRELATIONSHIPSROLE(self):
          return self.G3E_EDITRELATIONSHIPSROLE
        
     def Return_G3E_USERNAME(x):
         for child in G3E_FEATUREDB:
             if x.upper() in G3E_FEATURE.get_Name(child):
                 return G3E_FEATURE.get_G3E_USERNAME(child)

     def Search_by_Name(x):
          for child in G3E_FEATUREDB:
               if x in G3E_FEATURE.get_Name(child):
                    print('--------------------')
                    print('G3E_FNO: ', G3E_FEATURE.get_G3E_FNO(child))
                    print('G3E_USERNAME: ', G3E_FEATURE.get_G3E_USERNAME(child))
                    print('G3E_TOOLTIP: ', G3E_FEATURE.get_G3E_TOOLTIP(child))
                    print('G3E_PRIMARYGEOGRAPHICCNO: ', G3E_FEATURE.get_G3E_PRIMARYGEOGRAPHICCNO(child))
                    print('G3E_PRIMARYATTRIBUTECNO: ', G3E_FEATURE.get_G3E_PRIMARYATTRIBUTECNO(child))
                    print('G3E_DCNO: ', G3E_FEATURE.get_G3E_DCNO(child))
                    print('G3E_PRIMARYDETAILCNO: ', G3E_FEATURE.get_G3E_PRIMARYDETAILCNO(child))
                    print('G3E_NUMBEROFNODES: ', G3E_FEATURE.get_G3E_NUMBEROFNODES(child))
                    print('G3E_IMPORTFEATURENAME: ', G3E_FEATURE.get_G3E_IMPORTFEATURENAME(child))
                    print('G3E_REPLACE: ', G3E_FEATURE.get_G3E_REPLACE(child))
                    print('G3E_NAME: ', G3E_FEATURE.get_G3E_NAME(child))
                    print('G3E_EDITDATE: ', G3E_FEATURE.get_G3E_EDITDATE(child))
                    print('G3E_LOCALECOMMENT: ', G3E_FEATURE.get_G3E_LOCALECOMMENT(child))
                    print('G3E_MERGE: ', G3E_FEATURE.get_G3E_MERGE(child))
                    print('G3E_CLASSIFICATIONANO: ', G3E_FEATURE.get_G3E_CLASSIFICATIONANO(child))
                    print('G3E_IDENTIFIERVIEW: ', G3E_FEATURE.get_G3E_IDENTIFIERVIEW(child))
                    print('G3E_BULKEDIT: ', G3E_FEATURE.get_G3E_BULKEDIT(child))
                    print('G3E_ICONORDINAL: ', G3E_FEATURE.get_G3E_ICONORDINAL(child))
                    print('G3E_EDITROLE: ', G3E_FEATURE.get_G3E_EDITROLE(child))
                    print('G3E_SELECTROLE: ', G3E_FEATURE.get_G3E_SELECTROLE(child))
                    print('G3E_DELETEROLE: ', G3E_FEATURE.get_G3E_DELETEROLE(child))
                    print('G3E_RINO: ', G3E_FEATURE.get_G3E_RINO(child))
                    print('G3E_RIARGGROUPNO: ', G3E_FEATURE.get_G3E_RIARGGROUPNO(child))
                    print('G3E_PRIMARYSCHEMCNO: ', G3E_FEATURE.get_G3E_PRIMARYSCHEMCNO(child))
                    print('G3E_SECONDARYSCHEMCNO: ', G3E_FEATURE.get_G3E_SECONDARYSCHEMCNO(child))
                    print('G3E_LABELSCHEMCNO: ', G3E_FEATURE.get_G3E_LABELSCHEMCNO(child))
                    print('G3E_ADDRELATEDROLE: ', G3E_FEATURE.get_G3E_ADDRELATEDROLE(child))
                    print('G3E_EDITRELATIONSHIPSROLE: ', G3E_FEATURE.get_G3E_EDITRELATIONSHIPSROLE(child))
                    print('--------------------')





###G3E_FEATURES Information from G/TECH Database

try:
    with open(r'Pickles\G3E_FEATUREPickle', 'rb') as Create:
        G3E_FEATUREDB = pickle.load(Create)
except:
    pass














