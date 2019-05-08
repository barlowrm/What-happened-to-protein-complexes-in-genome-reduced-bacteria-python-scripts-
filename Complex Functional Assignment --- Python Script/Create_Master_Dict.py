"""
Author: Ruairidh Barlow
Last edit: 03/21/2019
"""

def make_dict(file):
    #Function that makes a dictionary
    #Keys are functional groups following the same naming as used in the EggNOG database
    #Values are cogids that belong to that functional group

    #What should be passed in is a master excel sheet downloaded from the EggNOG database that has a record of every
    # COGID and its respecitve functional group

    f = open(file, "r")
    d = open(file, "r")

    #Opened the file twice to interate through it twice below

    one_letter_function = {}
    #Creating an empty dictionary

    for line in f:
        #First iteration through file
        line = line.strip()
        #get rid of white space
        temp = line.split(',')
        #Make the line in the file accessable by index

        one_letter_function[temp[1]] = []
        #Saving all the functional function names as keys
        #Fuctional groups are the second thing in a line so you use index position one

    for row in d:
        #Second iteration through file
        row = row.strip()
        temp1 = row.split(',')
        #stripping white space and making the file acessable by index

        if temp1[1] in one_letter_function.keys():
            #If the functional group is a key in the dictionary (which it is)
            if "ENOG" in str(temp1[0]):
                #Filtering out ENOG IDs we are only working with CIOGIDs
                pass
                #ignore them
            else:
                temp1[0] = temp1[0].replace("\xef\xbb\xbf", "")
                one_letter_function[temp1[1]].append(temp1[0])
                #Save the COGIDs to the approiate function dictionary key
        else:
            if "ENOG" in str(temp1[0]):
                #again ignore the ENOGIDS
                pass
            else:
                one_letter_function["Unkown"].append(temp1[0])
                #if there is a case where there is a COGID that has a functional group that is not a key in the dictionary it will be saved here
                #There is not a case of this, the unknown key will have an empty list
    f.close()
    d.close()

    return one_letter_function

#function_dict = make_dict("EggNOG COGID to single letter functional group mod.csv")

#for k, v in function_dict.items():
#    print k,v