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




def SearchUnpowered():
    with open('Pickles\A_Errors_MSL', 'rb') as Create:
        A_Errors_MSL = pickle.load(Create)
    while True:
        prompt = input("MSLINK?:")
        if prompt in A_Errors_MSL:
            print("Unpowered!")
        else:
            print("That Device is Powered")

SearchUnpowered()
            





