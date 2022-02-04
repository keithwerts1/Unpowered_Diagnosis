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
from UNPDReportCODE import *


__author__ ="Keith Wertsching"
__version__ ="1.0.0"
__status__="Development"



"""                
print('################################################################')
print('################################################################')
print('################################################################')
"""



############## Load Data ##############




###G3E_FEATURES Information from G/TECH Database
    
with open(r'Pickles\G3E_FEATUREPickle', 'rb') as Create:
    G3E_FEATUREDB = pickle.load(Create)

############## Modules ##############

def ParseSQLCSV(file):
    L = list(csv.reader(open(file, 'rt'), delimiter = ','))
    x = 0
    if [] in L[0:50]:
         while x < len(L):
            if L[x] != []:
                L.pop(x)
            else:
                break

    else:        
        while x < len(L):
            if list(set(item for item in L[x])) != ['']:
                L.pop(x)
            else:
                break
        
    L.pop(0)

    L.pop()
    L.pop()
    L.pop()
    L.pop()
    return L

def CK(f):
    fname = str(f.split("\\")[-1])
    name = str(fname.split(".")[0])
    KEEPER.CreateKeeper(ParseSQLCSV(f), name)


def Counter(l):
    counter = []
    ls = set(l)
    for item in ls:
        count = 0
        for match in l:
            if item == match:
                count += 1
        counter.append([item, count])
    counter.sort(key=lambda k: (k[1], -k[1]), reverse=True)
    return counter

def Tester():
    start = time.time()
    x = 1
    while x < 1001:
        if x % 100 == 0:
            print(x)
        x += 1
    end = time.time()
    
    print(end-start)

    

def Print_SQL():
    print("Run this SQL on SQL Developer on a Migration Server against the OMS Migration Database:")
    print("")
    print("")
    print("############## Query Start ##############")
    print("")
    print("")
    print('set SQLFORMAT csv')
    print("spool 'D:\FeederData\CountByFeeders - For Report.csv'")
    print("select concat(ssta_c, feeder_nbr), ssta_c, feeder_nbr, count(u.mslink), max(c.mslink) from oms_connectivity c left join oms_unpowered_features u on c.mslink = u.mslink group by ssta_c, feeder_nbr order by count(u.mslink) desc;")
    print("spool off;")
    print('set SQLFORMAT csv')
    print("spool 'D:\FeederData\CountByFeeders.csv'")
    print("select concat(ssta_c, feeder_nbr), ssta_c, feeder_nbr, count(u.mslink), max(c.mslink) from oms_connectivity c inner join oms_unpowered_features u on c.mslink = u.mslink")
    print("where c.mslink not in (select c.mslink from oms_connectivity c inner join oms_unpowered_features u on c.mslink = u.mslink where c.phase !=  u.phase)")
    print("and c.mslink not in (select c.mslink from oms_connectivity c inner join oms_unpowered_features u on c.mslink = u.mslink where feature_state_c != 'Closed') group by ssta_c, feeder_nbr order by count(u.mslink) desc;")
    print("spool off;")
    print('set SQLFORMAT csv')
    print("spool 'D:\FeederData\CountByFeature - For Report.csv'")
    print("select c.feature_id, count(c.mslink) from oms_connectivity c inner join oms_unpowered_features u on c.mslink = u.mslink group by c.feature_id order by count(c.mslink) desc;")
    print("spool off;")
    print('set SQLFORMAT csv')
    print(r"spool 'D:\FeederData\NullPhase.csv'")
    print("select concat(ssta_c, feeder_nbr), ssta_c, feeder_nbr, count(*) from oms_connectivity where phase is null and feature_id in (8,9) group by ssta_c, feeder_nbr order by count(*) desc;")
    print("spool off;")
    print("set SQLFORMAT csv")
    print("spool 'D:\FeederData\Hotspots1.csv'")    
    print("select concat(ssta_c, feeder_nbr), u.mslink, c.feature_id, c.owner1_id from oms_unpowered_features u")
    print("left join oms_connectivity c on u.mslink = c.mslink where c.feature_id in (8,9) and c.owner1_id is not null and c.owner1_id != 0 and")
    print("c.owner1_id in (select c.owner1_id from oms_connectivity c left join oms_unpowered_features u on c.mslink = u.mslink where u.mslink is null and c.feature_id in (8,9))")
    print("and c.owner1_id in (select c.owner1_id from oms_connectivity c left join oms_unpowered_features u on c.mslink = u.mslink where u.mslink is not null and c.feature_id in (8,9));")
    print("spool off;")
    print("set SQLFORMAT csv")
    print("spool 'D:\FeederData\Hotspots2.csv'")  
    print("select concat(ssta_c, feeder_nbr), u.mslink, c.feature_id, c.owner2_id from oms_unpowered_features u") 
    print("left join oms_connectivity c on u.mslink = c.mslink where c.feature_id in (8,9) and c.owner2_id is not null and c.owner2_id != 0 and")
    print("c.owner2_id in (select c.owner2_id from oms_connectivity c left join oms_unpowered_features u on c.mslink = u.mslink where u.mslink is null and c.feature_id in (8,9))")
    print("and c.owner2_id in (select c.owner2_id from oms_connectivity c left join oms_unpowered_features u on c.mslink = u.mslink where u.mslink is not null and c.feature_id in (8,9));")
    print("spool off;")
    print("")
    print("############## Query End ##############")
    print("")
    print("Run this SQL on SQL Developer on a Migration Server against the AEGIS Source Database:")
    print("")
    print("")
    print("############## Query Start ##############")
    print("")
    print("")
    print('set SQLFORMAT csv')
    print("spool 'D:\FeederData\BatchUpdateTrace.csv'")
    print("select * from update_trace_batch;")
    print("spool off;")
    print("set SQLFORMAT csv")
    print("spool 'D:\FeederData\DistinctOwnerID.csv'")
    print("select distinct owner1_id, owner2_id from common_n where g3e_fno = 10;")
    print("spool off;")
    print("")
    print("")
    print("############## Query End ##############")
    prompt = input("Type Y when you have had a chance to run the SQL below and replace the file FeederData\CountByFeeders - For Report.csv:")
    prompt = input("Type Y when you have had a chance to replace FeederData\hfc_substationFailures.log and FeederData\Oncor_Aegis.net_error.txt:")
    print('Looks like the error file was last modified on:',datetime.fromtimestamp(os.stat('FeederData\Oncor_Aegis.net_error.txt').st_mtime))
    print('Looks like the Substation Failure file was last modified on:',datetime.fromtimestamp(os.stat('FeederData\hfc_substationFailures.log').st_mtime))
    prompt = input("Type Y to continue:")    
    


def SubstationFailures():

    S_Errors = list(csv.reader(x.replace('\0', '') for x in open('FeederData\hfc_substationFailures.log', 'rt')))
    ss = []
    for line in S_Errors:
        if line == ['']:
            pass
        else:
            for entry in line:
                if entry not in ss:
                    ss.append(entry)
    print("Substations that failed:")
    for s in ss:
        print(s.split(" ")[-1])
    




############## Float / Sink ##############

def Initialize():
    prompt = input("Type Y to continue:")
    A_Errors = list(csv.reader(open(r'FeederData\Oncor_Aegis.net_error.txt', 'rt'), delimiter='\t'))
    A_Errors_MSL = []
    for item in A_Errors:
        try:
            if "Total of" not in item[0]:
                A_Errors_MSL.append(item[0])
            else:
                break
        except:
            continue
    A_Errors_MSL.pop(0)
    A_Errors_MSL.pop(0)
    with open('Pickles\A_Errors_MSL', 'wb') as Create:
        pickle.dump(A_Errors_MSL, Create)
    print("I am seeing:",len(A_Errors_MSL),"Unpowered Features in the Error file. Let's start diagnosing!")

    DeadOwnersRaw = ParseSQLCSV(r'FeederData\DistinctOwnerID.csv')
    DeadOwnersRaw.pop(0)
    DeadOwners1 = list(set([item[0] for item in DeadOwnersRaw]))
    DeadOwners2 = list(set([item[1] for item in DeadOwnersRaw]))
    DeadOwners = list(set(DeadOwners1 + DeadOwners2))
    with open('Pickles\DeadOwners', 'wb') as Create:
        pickle.dump(DeadOwners, Create)
    


def CreateDB(file):
    with open('Pickles\A_Errors_MSL', 'rb') as Create:
        A_Errors_MSL = pickle.load(Create)
    
    CONNECTIVITYDB = []
    BadList = [0,'0',"","Null"]
    FEEDERList = list(csv.reader(open(file, 'rt'), delimiter=','))
    FEEDERSQL = FEEDERList.pop(0)
    FEEDERList.pop(0)
    FEEDERList.pop(0)
    FEEDERList.pop(0)
    FEEDERHeader = FEEDERList.pop(0)
    
    FEEDERList.pop()
    FEEDERList.pop()
    FEEDERList.pop()
    FEEDERList.pop()
    
    for item in FEEDERList:
        child = CONNECTIVITY(item[0])
        CONNECTIVITYDB.append(child)
        child.MSLINK = (item[0])
        child.FEATURE_ID = (item[1])
        child.NODE1 = (item[2])
        child.NODE2 = (item[3])
        child.NORMAL_STATUS = (item[4])
        child.PHASE = (item[5])
        child.LOCATION = (item[6])
        child.X_COORD = (item[7])
        child.Y_COORD = (item[8])
        child.RATING_KVA = (item[9])
        child.RATING_AMPS = (item[10])
        child.SWITCHING_GROUP_ID = (item[11])
        child.VOLTAGE_KV = (item[12])
        child.GANG_OPERABLE = (item[13])
        child.STYLE_SET_ID = (item[14])
        child.NORMAL_FEEDER_A = (item[15])
        child.NORMAL_FEEDER_B = (item[16])
        child.NORMAL_FEEDER_C = (item[17])
        child.NORMAL_OVERRIDES_A = (item[18])
        child.NORMAL_OVERRIDES_B = (item[19])
        child.NORMAL_OVERRIDES_C = (item[20])
        child.MAP_LEVEL = (item[21])
        child.FEEDER_NBR = (item[22])
        child.TIE_SSTA_C = (item[23])
        child.TIE_FEEDER_NBR = (item[24])
        child.FEEDER_TYPE_C = (item[25])
        child.PROTECTIVE_DEVICE_FID = (item[26])
        child.PHASE_OPERATED = (item[27])
        child.STATUS_NORMAL_C = (item[28])
        child.CONFIG_C = (item[29])
        child.VOLT_2_Q = (item[30])
        child.NETWORK_ID = (item[31])
        child.UPSTREAM_PROTDEV_Q = (item[32])
        child.UPSTREAM_NODE = (item[33])
        child.PP_FEEDER_1_ID = (item[34])
        child.PP_SSTA_C = (item[35])
        child.PP_FEEDER_NBR = (item[36])
        child.PP_FEEDER_2_ID = (item[37])
        child.PP_TIE_SSTA_C = (item[38])
        child.PP_TIE_FEEDER_NBR = (item[39])
        child.PP_PROTECTIVE_DEVICE_FID = (item[40])
        child.PP_VOLT_1_Q = (item[41])
        child.PP_VOLT_2_Q = (item[42])
        child.PP_NETWORK_ID = (item[43])
        child.PP_UPSTREAM_PROTDEV_Q = (item[44])
        child.PP_UPSTREAM_NODE = (item[45])
        child.SSTA_C = (item[46])
        child.FEEDER_1_ID = (item[47])
        child.FEEDER_2_ID = (item[48])
        child.FEATURE_STATE_C = (item[49])
        child.ORIENTATION_C = (item[50])
        child.OWNER1_ID = (item[51])
        child.OWNER2_ID = (item[52])
        FNNL = []
        for node in FEEDERList:
            if item[0] == node[0]:
                pass
            elif item[2] in BadList:
                pass
            elif item[2] == node[3]:
                FNNL.append(node[0])
        if FNNL == []:
            FNNL.append('end')
        child.FNN = FNNL
        SNNL = []
        for node in FEEDERList:
            if item[0] == node[0]:
                pass
            elif item[3] in BadList:
                pass
            elif item[3] == node[2]:
                SNNL.append(node[0])
        if SNNL == []:
            SNNL.append('end')
        child.SNN = SNNL
        if item[0] in A_Errors_MSL:
            child.PSTATUS = 'UNPOWERED'
        else:
            child.PSTATUS = 'POWERED'

    with open('Pickles\CONNECTIVITYDB', 'wb') as Create:
        pickle.dump(CONNECTIVITYDB, Create)





def Querygen(file):
    C = ParseSQLCSV(file)
    C.pop(0)
    for item in C:
        if int(item[3]) > 0 and item[2] != "" and item[1] != "":
            print('set SQLFORMAT csv')
            print("spool 'D:\FeederData\Feeders\\"+item[1]+item[2]+".csv'")
            print("select * from oms_connectivity where ssta_c = '"+item[1]+"' and feeder_nbr = '"+item[2]+"';")
            print('spool off;')
    



def DiagnoseHotSpots(path):
    with open('Pickles\A_Errors_MSL', 'rb') as Create:
        A_Errors_MSL = pickle.load(Create)

    with open('Pickles\DeadOwners', 'rb') as Create:
        DeadOwners = pickle.load(Create)
    
    OPStart = str(time.time())
    HSL = []
    Stacked = []
    BadSwitches = []
    BadTransformers = []
    AList = []
    ABs = []
    BadList = [0,'0',"","Null"]
    
    count = 1
    Concert = []
    NotMusic = []
    for file in glob.glob(path):
        start = time.time()
        print(count, file)
        try:
            CreateDB(file)
            count += 1
        except:
            continue
            count += 1
        with open('Pickles\CONNECTIVITYDB', 'rb') as Create:
            CONNECTIVITYDB = pickle.load(Create)
        
    
        OL1 = list(set(CONNECTIVITY.get_OWNER1_ID(child) for child in CONNECTIVITYDB))
        OL2 = list(set(CONNECTIVITY.get_OWNER2_ID(child) for child in CONNECTIVITYDB))
        OL = list(set(OL1+OL2))

        N = []
        O = []
        F = []
        P = []
        P2 = []
        U = []
        NC = []
        for owner in OL:
            if owner in BadList:
                pass
            else:
                #SL = list(set(CONNECTIVITY.get_PSTATUS(child) for child in CONNECTIVITYDB if CONNECTIVITY.get_OWNER1_ID(child) == owner and CONNECTIVITY.get_FEATURE_ID(child) in ['8','9','84','85','96','97'] or CONNECTIVITY.get_OWNER2_ID(child) == owner and CONNECTIVITY.get_FEATURE_ID(child) in ['8','9','84','85','96','97']))
                SL = list(set(CONNECTIVITY.get_PSTATUS(child) for child in CONNECTIVITYDB if CONNECTIVITY.get_OWNER1_ID(child) == owner and CONNECTIVITY.get_FEATURE_ID(child) in ['8','9'] or CONNECTIVITY.get_OWNER2_ID(child) == owner and CONNECTIVITY.get_FEATURE_ID(child) in ['8','9']))
                PL = list(set(CONNECTIVITY.get_PHASE(child) for child in CONNECTIVITYDB if CONNECTIVITY.get_OWNER1_ID(child) == owner and CONNECTIVITY.get_FEATURE_ID(child) in ['8','9'] or CONNECTIVITY.get_OWNER2_ID(child) == owner and CONNECTIVITY.get_FEATURE_ID(child) in ['8','9']))
                FUSE = list(set(CONNECTIVITY.get_FEATURE_ID(child) for child in CONNECTIVITYDB if CONNECTIVITY.get_OWNER1_ID(child) == owner or CONNECTIVITY.get_OWNER2_ID == owner))
                if 'POWERED' in SL and 'UNPOWERED' in SL and "" in PL and owner not in DeadOwners:
                    N.append(owner)
                elif 'POWERED' in SL and 'UNPOWERED' in SL and len(set(PL)) == 1 and owner not in DeadOwners:
                    O.append(owner)
                elif 'POWERED' in SL and 'UNPOWERED' in SL and '11' in FUSE and owner not in DeadOwners:
                    F.append(owner)
                elif 'POWERED' in SL and 'UNPOWERED' in SL and owner not in DeadOwners:
                    P2.append(owner)
                elif 'UNPOWERED' in SL:
                    U.append(owner)
                elif 'POWERED' in SL:
                    P.append(owner)
                else:
                    NC.append(owner)
    

        for item in N:
            Feeder = list(set([str(CONNECTIVITY.get_SSTA_C(child)+CONNECTIVITY.get_FEEDER_NBR(child)) for child in CONNECTIVITYDB if CONNECTIVITY.get_OWNER1_ID(child) == item or CONNECTIVITY.get_OWNER2_ID(child) == item]))
            UML1 = list(set(CONNECTIVITY.get_Name(child) for child in CONNECTIVITYDB if CONNECTIVITY.get_OWNER2_ID(child) == item and CONNECTIVITY.get_PSTATUS(child) == 'UNPOWERED'))
            UML2 = list(set(CONNECTIVITY.get_Name(child) for child in CONNECTIVITYDB if CONNECTIVITY.get_OWNER1_ID(child) == item and CONNECTIVITY.get_PSTATUS(child) == 'UNPOWERED'))
            UML = list(set(UML1+UML2))
            Master = []
            Master.append(item)
            x = 1
            OL = ['Start']
            y = 20
            x = 0
            while x < y:
                for own in Master:
                    OL1 = list(set(CONNECTIVITY.get_OWNER1_ID(child) for child in CONNECTIVITYDB if CONNECTIVITY.get_OWNER2_ID(child) == own and CONNECTIVITY.get_OWNER1_ID(child) in U))
                    OL2 = list(set(CONNECTIVITY.get_OWNER2_ID(child) for child in CONNECTIVITYDB if CONNECTIVITY.get_OWNER1_ID(child) == own and CONNECTIVITY.get_OWNER2_ID(child) in U))
                    OL = list(set(OL1+OL2))
                    for i in OL:
                        if i not in Master:
                            Master.append(i)
                x += 1
            classroom = []
            for n in Master:
                children = list(set(CONNECTIVITY.get_Name(child) for child in CONNECTIVITYDB if CONNECTIVITY.get_OWNER2_ID(child) == n and CONNECTIVITY.get_PSTATUS(child) == 'UNPOWERED' or CONNECTIVITY.get_OWNER1_ID(child) == n and CONNECTIVITY.get_PSTATUS(child) == 'UNPOWERED'))
                for c in children:
                    if c not in classroom and c in A_Errors_MSL:
                        classroom.append(c)
            

            HSL.append([Feeder, UML[0], len(classroom), "NULLPHASE", item, len(Master)])
            #print([Feeder, UML[0], len(classroom), "NULLPHASE", item, len(Master)])
        with open(r'Pickles\HSL_Pickle'+OPStart, 'wb') as Create:
            pickle.dump(HSL, Create)

        for item in O:
            Feeder = list(set([str(CONNECTIVITY.get_SSTA_C(child)+CONNECTIVITY.get_FEEDER_NBR(child)) for child in CONNECTIVITYDB if CONNECTIVITY.get_OWNER1_ID(child) == item or CONNECTIVITY.get_OWNER2_ID(child) == item]))
            UML1 = list(set(CONNECTIVITY.get_Name(child) for child in CONNECTIVITYDB if CONNECTIVITY.get_OWNER2_ID(child) == item and CONNECTIVITY.get_PSTATUS(child) == 'UNPOWERED'))
            UML2 = list(set(CONNECTIVITY.get_Name(child) for child in CONNECTIVITYDB if CONNECTIVITY.get_OWNER1_ID(child) == item and CONNECTIVITY.get_PSTATUS(child) == 'UNPOWERED'))
            UML = list(set(UML1+UML2))
            Master = []
            Master.append(item)
            x = 1
            OL = ['Start']
            y = 20
            x = 0
            while x < y:
                for own in Master:
                    OL1 = list(set(CONNECTIVITY.get_OWNER1_ID(child) for child in CONNECTIVITYDB if CONNECTIVITY.get_OWNER2_ID(child) == own and CONNECTIVITY.get_OWNER1_ID(child) in U))
                    OL2 = list(set(CONNECTIVITY.get_OWNER2_ID(child) for child in CONNECTIVITYDB if CONNECTIVITY.get_OWNER1_ID(child) == own and CONNECTIVITY.get_OWNER2_ID(child) in U))
                    OL = list(set(OL1+OL2))
                    for i in OL:
                        if i not in Master:
                            Master.append(i)
                x += 1
            classroom = []
            for n in Master:
                children = list(set(CONNECTIVITY.get_Name(child) for child in CONNECTIVITYDB if CONNECTIVITY.get_OWNER2_ID(child) == n and CONNECTIVITY.get_PSTATUS(child) == 'UNPOWERED' or CONNECTIVITY.get_OWNER1_ID(child) == n and CONNECTIVITY.get_PSTATUS(child) == 'UNPOWERED'))
                for c in children:
                    if c not in classroom and c in A_Errors_MSL:
                        classroom.append(c)

            HSL.append([Feeder, UML[0], len(classroom), "HOTSPOT", item, len(Master)])
            #print([Feeder, UML[0], len(classroom), "HOTSPOT", item, len(Master)])
        with open(r'Pickles\HSL_Pickle'+OPStart, 'wb') as Create:
            pickle.dump(HSL, Create)
        
        for item in F:
            Feeder = list(set([str(CONNECTIVITY.get_SSTA_C(child)+CONNECTIVITY.get_FEEDER_NBR(child)) for child in CONNECTIVITYDB if CONNECTIVITY.get_OWNER1_ID(child) == item or CONNECTIVITY.get_OWNER2_ID(child) == item]))
            UML1 = list(set(CONNECTIVITY.get_Name(child) for child in CONNECTIVITYDB if CONNECTIVITY.get_OWNER2_ID(child) == item and CONNECTIVITY.get_PSTATUS(child) == 'UNPOWERED'))
            UML2 = list(set(CONNECTIVITY.get_Name(child) for child in CONNECTIVITYDB if CONNECTIVITY.get_OWNER1_ID(child) == item and CONNECTIVITY.get_PSTATUS(child) == 'UNPOWERED'))
            UML = list(set(UML1+UML2))
            Master = []
            Master.append(item)
            x = 1
            OL = ['Start']
            y = 20
            x = 0
            while x < y:
                for own in Master:
                    OL1 = list(set(CONNECTIVITY.get_OWNER1_ID(child) for child in CONNECTIVITYDB if CONNECTIVITY.get_OWNER2_ID(child) == own and CONNECTIVITY.get_OWNER1_ID(child) in U))
                    OL2 = list(set(CONNECTIVITY.get_OWNER2_ID(child) for child in CONNECTIVITYDB if CONNECTIVITY.get_OWNER1_ID(child) == own and CONNECTIVITY.get_OWNER2_ID(child) in U))
                    OL = list(set(OL1+OL2))
                    for i in OL:
                        if i not in Master:
                            Master.append(i)
                x += 1
            classroom = []
            for n in Master:
                children = list(set(CONNECTIVITY.get_Name(child) for child in CONNECTIVITYDB if CONNECTIVITY.get_OWNER2_ID(child) == n and CONNECTIVITY.get_PSTATUS(child) == 'UNPOWERED' or CONNECTIVITY.get_OWNER1_ID(child) == n and CONNECTIVITY.get_PSTATUS(child) == 'UNPOWERED'))
                for c in children:
                    if c not in classroom and c in A_Errors_MSL:
                        classroom.append(c)
            
            HSL.append([Feeder, UML[0], len(classroom), "FUSE", item, len(Master)])
            #print([Feeder, UML[0], len(classroom), "FUSE", item, len(Master)])
        with open(r'Pickles\HSL_Pickle'+OPStart, 'wb') as Create:
            pickle.dump(HSL, Create)

        for item in P2:
            Feeder = list(set([str(CONNECTIVITY.get_SSTA_C(child)+CONNECTIVITY.get_FEEDER_NBR(child)) for child in CONNECTIVITYDB if CONNECTIVITY.get_OWNER1_ID(child) == item or CONNECTIVITY.get_OWNER2_ID(child) == item]))
            UML1 = list(set(CONNECTIVITY.get_Name(child) for child in CONNECTIVITYDB if CONNECTIVITY.get_OWNER2_ID(child) == item and CONNECTIVITY.get_PSTATUS(child) == 'UNPOWERED'))
            UML2 = list(set(CONNECTIVITY.get_Name(child) for child in CONNECTIVITYDB if CONNECTIVITY.get_OWNER1_ID(child) == item and CONNECTIVITY.get_PSTATUS(child) == 'UNPOWERED'))
            UML = list(set(UML1+UML2))
            Master = []
            Master.append(item)
            x = 1
            OL = ['Start']
            y = 20
            x = 0
            while x < y:
                for own in Master:
                    OL1 = list(set(CONNECTIVITY.get_OWNER1_ID(child) for child in CONNECTIVITYDB if CONNECTIVITY.get_OWNER2_ID(child) == own and CONNECTIVITY.get_OWNER1_ID(child) in U))
                    OL2 = list(set(CONNECTIVITY.get_OWNER2_ID(child) for child in CONNECTIVITYDB if CONNECTIVITY.get_OWNER1_ID(child) == own and CONNECTIVITY.get_OWNER2_ID(child) in U))
                    OL = list(set(OL1+OL2))
                    for i in OL:
                        if i not in Master:
                            Master.append(i)
                x += 1
            classroom = []
            for n in Master:
                children = list(set(CONNECTIVITY.get_Name(child) for child in CONNECTIVITYDB if CONNECTIVITY.get_OWNER2_ID(child) == n and CONNECTIVITY.get_PSTATUS(child) == 'UNPOWERED' or CONNECTIVITY.get_OWNER1_ID(child) == n and CONNECTIVITY.get_PSTATUS(child) == 'UNPOWERED'))
                for c in children:
                    if c not in classroom and c in A_Errors_MSL:
                        classroom.append(c)
            

            HSL.append([Feeder, UML[0], len(classroom), "BAD-PHASING", item, len(Master)])
            #print([Feeder, UML[0], len(classroom), "BAD-PHASING", item, len(Master)])
        with open(r'Pickles\HSL_Pickle'+OPStart, 'wb') as Create:
            pickle.dump(HSL, Create)

        print("Total Hotspots Found:", len(HSL))

        

        
        end = time.time()
        #count += 1
        print(end-start)


    for line in HSL:
        print(line)







def PrintHotspots(file):
    with open(file, 'rb') as Create:
        HSL = pickle.load(Create)
    for line in HSL:
        print(line)  
            
def SearchUnpowered():
    with open('Pickles\A_Errors_MSL', 'rb') as Create:
        A_Errors_MSL = pickle.load(Create)
    while True:
        prompt = input("MSLINK?:")
        if prompt in A_Errors_MSL:
            print("Unpowered!")
        else:
            print("That Device is Powered")


def PrintAdminMenu():
    print("     1. Run Full Report")
    print("     2. Run Program on Deltas Only")
    print("     3. Print previous HotSpots List")
    print("Note: to quit the program at any time please type 'quit'")
    print("")


def AdminUI():
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("Hello Admin, how can I help you today?")
    print("")
    print("")
    PrintAdminMenu()
    clearCalls = ["clear","clear screen","cls","ls"]
    prompt = ""
    while prompt != 'quit':
        prompt = input("How can I help you? (Please enter the number from the menu options): ")
    #function to clear 
        if prompt.lower() in clearCalls:
            os.system('cls')
            PrintAdminMenu()
        prompt2 = ""
        if prompt == "0":
            PrintAdminMenu()

        elif prompt.lower() == "1":
            Print_SQL()
            Querygen('FeederData\CountByFeeders - For Report.csv')
            SubstationFailures()
            Initialize()
            DiagnoseHotSpots('Export_by_Feeder\*')

        elif prompt.lower() == "2":
            Print_SQL()
            Querygen('FeederData\CountByFeeders - For Report - Deltas.csv')
            SubstationFailures()
            Initialize()
            DiagnoseHotSpots('Export_by_Feeder - Deltas\*')

        elif prompt.lower() == "3":
            for file in glob.glob('Pickles\*'):
                if 'HSL' in file:
                    print(file, "Modified on: ",datetime.fromtimestamp(os.stat(file).st_mtime))

            prompt = input("Which file would you like to print?: ")
            PrintHotspots(prompt)
            prompt = input("Please close the program when you are finished copying")




AdminUI()


