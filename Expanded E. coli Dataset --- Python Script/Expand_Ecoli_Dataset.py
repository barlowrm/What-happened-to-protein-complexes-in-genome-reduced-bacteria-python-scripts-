"""
Author: Ruairidh Barlow

****NOTE****
This program needs:

    1. Filtered_proteins.txt
    2. entry_to_cogid.csventry_to_cogid.csv
    3. Ecoli_proteome.fasta

    to be in the same directory to work

^^^^OBJECTIVE^^^^

Expand Essential Ecoli Complex datasheet to include COGIDS of Ecoli proteins
That are from 2 papers provided by Dr. Peter Uetz

^^^^Links to papers^^^^

1. https://www.nature.com/articles/nbt.4024#supplementary-information
2. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2672614/

Last edit: 04/17/2019
"""



from Bio import SeqIO
import re

#Need to use BioPython library to process fasta file
#Need to import re library to use regular expressions

file = "Filtered_proteins.txt"
#Preprocessed excel file, every row of the file is a protein name from the two papers provided by Dr. Uetz

file2 = "entry_to_cogid.csv"
#This file is a key
#It allows you to convert the Uniprot protein entry name COGID

f = open(file, "r")
f2 = open(file2, "r")
w = open("Eggnog_map.txt", "w")

#opening the files
#Note that the output is being written to Eggnog_map.txt
#Files structure original protein name from Filtered_proteins.txt "," COGID from entry_to_cogid.csv

proteins = []
#This will be used to store the proteins from Filtered_proteins.txt

for line in f:
    #iterate through file
    line = line.strip()
    line = line.replace('\n', '')
    line = line.split(',')
    #processing lines in the file to be in a list format
    proteins.extend(line)
    #extending proteins list with list from the file

listcopy = list(set(proteins))
#removes duplicate proteins from list

entries = []
#This will be used to store protein entry identifiers

for i in listcopy:
#Iterating through the list of proteins
    for record in SeqIO.parse("Ecoli_proteome.fasta","fasta"):
        #iterating through file entries
        if i in str(record.description):
            #if the protein name is in the entry heading
            match = re.search(r'[|](\S+)[|]', str(record.description))
            #This regular expression looks for the entry id in Uniprot
            entry = match.group()
            entry = entry.replace('|','')
            #formats it
            entries.append((i,str(entry)))
            #Save tuples (protein name, entry name) to a list

for line2 in f2:
    #iterate through entry_to_cogid.csv
    for j in entries:
        #iterates through entries list
        if j[1] in line2:
            #if the entry is found
            line2 = str(line2)
            line2 = line2.strip()
            line2 = line2.replace(';', ',')
            line2 = line2.split(',')
            #Formatting the line to be iterated over like a list
            for p in line2:
                #iterating through that line
                if "COG" in str(p):
                    #if there is a COGID in the line
                    p = p.strip()
                    p = p.replace("\'","")
                    #The cogid is formatted

                    w.write(j[0])
                    w.write(",")
                    w.write(p)
                    w.write("\n")
                    #The original protein name and the corresponding cogid name is then written to Eggnog_map.txt