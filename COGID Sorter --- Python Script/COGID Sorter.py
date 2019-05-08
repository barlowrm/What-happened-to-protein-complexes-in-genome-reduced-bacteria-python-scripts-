"""
Author: Ruairidh Barlow

    This program requires

    1. BNFO_620_COGID.py
    2. "EggNOG COGID to single letter functional group mod.csv"
    3. MOD_BUCAI_APS_ALL_COGIDs.csv
    4. MOD_BUCAI_Cc_ALL_COGIDs.csv
    5. EcoliComplexConservation.csv
    6. MYCTU_All_COGIDs.csv
    7. MYCLE_All_COGIDs.csv

    to be in the same directory to work

Last edit: 05/04/2019
"""




import pandas as pd
from BNFO_620_COGID import make_dict
import csv
#importing the make_dict function from the BNFO_620_COGID file made my Ruairidh Barlow

Imported_COGID_Dict = make_dict("EggNOG COGID to single letter functional group mod.csv")
#Passing in the file downloaded from the EggNOG database and saving the stratified dictionary to this script
from random import randint



"""**********************IMPORTANT*******************************************************
Important file read in
"""
#ECOLIcomplexes = pd.read_csv("EcoliComplexConservation.csv")

ECOLIcomplexes = pd.read_csv("ExpandedEcoliComplexConservation.csv")
ECOLIcomplexes = ECOLIcomplexes.as_matrix()

MYCTUlist = pd.read_csv("MYCTU_All_COGIDs.csv")
MYCTUlist = MYCTUlist.as_matrix()

Essential_MYCTU_List = pd.read_csv("Essential_COGIDS_TB.csv")
Essential_MYCTU_List = Essential_MYCTU_List.as_matrix()

MYCLElist = pd.read_csv("MYCLE_All_COGIDs.csv")
MYCLElist = MYCLElist.as_matrix()

BUCAI_APS_ALL_list = pd.read_csv("MOD_BUCAI_APS_ALL_COGIDs.csv")
BUCAI_APS_ALL_list = BUCAI_APS_ALL_list.as_matrix()

BUCAI_Cc_ALL_list = pd.read_csv("MOD_BUCAI_Cc_ALL_COGIDs.csv")
BUCAI_Cc_ALL_list = BUCAI_Cc_ALL_list.as_matrix()

Ecoli_conserved_list = pd.read_csv("Ecoli Essential COGIDS Scrap.csv")
Ecoli_conserved_list = Ecoli_conserved_list.as_matrix()



MYCTUconserve = ECOLIcomplexes[:, 30]
MYCLEconserve = ECOLIcomplexes[:, 32]
BUCAI_APSconserve = ECOLIcomplexes[:, 34]
BUCAI_Ccconserve = ECOLIcomplexes[:, 36]
ECOLIlist = []

complexSize = []


for line in ECOLIcomplexes:
    count = 0
    for item in line:
        item = str(item)
        if item.startswith("COG"):
            ECOLIlist.append(item)
            count += 1
    complexSize.append(count)

complexSize = pd.DataFrame(complexSize)
complexSize.to_csv("complexSize.csv")


def list_maker (data_structure):
    list_structure = []
    for line in data_structure:
        for item in line:
            item = str(item)
            if item.startswith("COG"):
                list_structure.append(item)
    return list_structure

R_MYCTU_LIST = list_maker(MYCTUlist)
R_MYCLE_LIST = list_maker(MYCLElist)
R_BUCAI_APS_LIST = list_maker(BUCAI_APS_ALL_list)
R_BUCAI_Cc_LIST = list_maker(BUCAI_Cc_ALL_list)
R_Essential_MYCTU_List = list_maker(Essential_MYCTU_List)
R_Ecoli_conserved_list = list_maker(Ecoli_conserved_list)



complexSize = pd.DataFrame(complexSize)
complexSize.to_csv("complexSize.csv")



def Make_COGID_DICT(imported_dict, input_list):
    COGID_DICT = {}
    #Creating a dictionary for oganization of the COGIDS that are found in the bacteria strains we intend to randomize

    for k, v in imported_dict.items():
        #Iterating through the master imported dictionary
        COGID_DICT[k]=[]
        #Saving all the keys from the imported dictionary to this one

    no_duplicates = list(set(input_list))
    #ECOLlist had duplicate COGIDS, using the set function I was able to get rid of duplicates
    #Since all we are interested in is organizing the COGIDs

    for i in no_duplicates:
        #Iterate through the the no duplicate list of COGIDS
        for k, v in imported_dict.items():
            #Look up the COGIDS in the master dictionary by iterating through the master dictionary
            if i in v:
                # if the COGID is found
                COGID_DICT[k].append(i)
                #the COGID is added to the functional group it belongs to in the COGID_DICT

    return COGID_DICT



def function_reassignment(functional_dict):
    #if the number of cogids in a function is less than 5
    #in the new dictionary it will be reassigned to function group S (unknown)

    new_dict = {}
    for k, v in functional_dict.items():
        new_dict[k] = []
    for k2,v2 in functional_dict.items():
        if len(v2) < 5 :
            new_dict["S"].extend(v2)
        else:
            new_dict[k2].extend(v2)
    return new_dict


def makeRandomDict(master_dict):
    #this function takes in the sorted dictionary of COGIDS made in the Make_COGID_DICT function

    no_duplicates = list(set(ECOLIlist))
    #gets rid of duplicate COGIDS
    random_dict = {}
    #creating a new empty dict
    for k, v in master_dict.items():
        random_dict[k] = []
    #adding the keys from the master dict (functional groups) and adding an empty list as the value

    for k, v in master_dict.items():
        #iterating through the master dict
        if len(v) == 0:
        #if there wasn't a cogid in a group it is skipped and kept empty, we can change this
        #note if we do this we are going to have to fix the list of COGIDS we can work with because we will run out of them
            pass
        else:
        # if there are cogids in the group
            for i in v:
                #iterate through that list, gets the length
                x = len(no_duplicates) - 1
                #remeber index position will be used have to subtract 1 to avoid an index out of bounds error
                pos = randint(0, x)
                #saving a random generated number between 0 and the length of the list
                #length will change cant hard code this
                j = no_duplicates[pos]
                # grabbing the COGID from the randomization list at that random index
                random_dict[k].append(j)
                #appending it to the list in that key (functional group)
                no_duplicates.pop(pos)
                #get rid of the COGID that we just used so it won't be in more than one group at a time
    return random_dict


ECOLI_COGID_DICT = Make_COGID_DICT(Imported_COGID_Dict, ECOLIlist)
MYCTU_COGID_DICT = Make_COGID_DICT(Imported_COGID_Dict, R_MYCTU_LIST)
MYCLE_COGID_DICT = Make_COGID_DICT(Imported_COGID_Dict, R_MYCLE_LIST)
BUCAI_APS_COGID_DICT = Make_COGID_DICT(Imported_COGID_Dict, R_BUCAI_APS_LIST)
BUCAI_Cc_COGID_DICT = Make_COGID_DICT(Imported_COGID_Dict, R_BUCAI_Cc_LIST)
Essential_MYCTU_DICT = Make_COGID_DICT(Imported_COGID_Dict, R_Essential_MYCTU_List)
Ecoli_conserved_DICT = Make_COGID_DICT(Imported_COGID_Dict, R_Ecoli_conserved_list)

#These are creating the functionial dictionaries for each strand

reassigned_ECOLI_COGID_DICT = function_reassignment(ECOLI_COGID_DICT)
reassigned_MYCTU_COGID_DICT = function_reassignment(MYCTU_COGID_DICT)
reassigned_MYCLE_COGID_DICT = function_reassignment(MYCLE_COGID_DICT)
reassigned_BUCAI_APS_COGID_DICT = function_reassignment(BUCAI_APS_COGID_DICT)
reassigned_BUCAI_Cc_COGID_DICT = function_reassignment(BUCAI_Cc_COGID_DICT)
reassigned_Essential_MYCTU_DICT = function_reassignment(Essential_MYCTU_DICT)
reassigned_Ecoli_conserved_DICT = function_reassignment(Ecoli_conserved_DICT)


# Block of code below was added to make an excel sheet that is used to show the distribution of cogids
def file_writer(dict, name):
    #Simple file writer function
    w = csv.writer(open(name, "w"))
    for key, val in dict.items():
        if len(val) > 0:
            temp = str(val)
            temp = temp.replace("[","")
            temp = temp.replace("]","")
            temp = temp.replace("\'","")
            w.writerow([key, temp])

ecoli_out = file_writer(reassigned_ECOLI_COGID_DICT, "Reassigned_Expanded_Ecoli_COGID.csv")
MYCTU_out = file_writer(reassigned_MYCTU_COGID_DICT, "Reassigned_MYCTU_COGID.csv")
MYCLE_out = file_writer(reassigned_MYCLE_COGID_DICT, "Reassigned_MYCLE_COGID.csv")
BUCAI_APS_out = file_writer(reassigned_BUCAI_APS_COGID_DICT, "Reassigned_BUCAI_APS_COGID.csv")
BUCAI_Cc_out = file_writer(reassigned_BUCAI_Cc_COGID_DICT, "Reassigned_BUCAI_Cc_COGID.csv")
Essential_MYCTU_out = file_writer(reassigned_Essential_MYCTU_DICT, "Reassigned_Essential_MYCTU_COGID.csv")
Ecoli_conserved_out = file_writer(Ecoli_conserved_DICT, "Ecoli_Conserved_COGID.csv")

