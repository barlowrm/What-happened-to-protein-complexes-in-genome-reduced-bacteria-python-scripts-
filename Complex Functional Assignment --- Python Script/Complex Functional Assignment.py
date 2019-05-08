from Create_Master_Dict import make_dict
import csv

file1 = "Ecoli_Reference_Complex.csv"
file2 = "MYCTU_All_COGIDs.csv"
file3 = "MYCLE_All_COGIDs.csv"
file4 = "MOD_BUCAI_APS_ALL_COGIDs.csv"
file5 = "MOD_BUCAI_Cc_ALL_COGIDs.csv"
file6 ="Hu2009_COGIDS.csv"
file7 = "Babu2017_S3_COGIDS.csv"
file8 = "Babu2017_S6_COGIDS.csv"

f = open(file1,"r")
f2 = open(file2,"r")
f3 = open(file3, "r")
f4 = open(file4, "r")
f5 = open(file5, "r")
f6 = open(file6, "r")
f7 = open(file7, "r")
f8 = open(file8, "r")

master_dict = make_dict("EggNOG COGID to single letter functional group mod.csv")


def most_frequent(List):
    return max(set(List), key = List.count)

def file_writer(dict, name):
    #Simple file writer function
    w = csv.writer(open(name, "w"))
    for key, val in dict.items():
        w.writerow([key, val])

def majority (dict_in):
    dict_out ={}
    for k , v in dict_in.items():
        if len(v) == 0:
            dict_out[k] = "NOTHING"
        else:
            majority = most_frequent(v)
            dict_out[k] = majority
    return dict_out

def list_maker(file):
    list = []
    for line in file:
        line = line.split(",")
        for i in line:
            if "COG" in str(i):
                i = i.strip()
                i = i.replace("\xef\xbb\xbf", "")
                list.append(str(i))
    return list

def complex_maker(list_input):
    output_dict = {}
    for k , v in Ecoli_complex_dict.items():
        output_dict[k]=[]
    for i in list_input:
        for k , v in Ecoli_complex_dict.items():
            if i in v:
                output_dict[k].append(i)
    return output_dict
def functions_dict_maker(input_dict):
    output_dict = {}
    for k, v in input_dict.items():
        output_dict[k] = []

    for k, v in input_dict.items():
        for i in v:
            for k1, v1 in master_dict.items():
                if i in v1:
                    output_dict[k].append(k1)
    return output_dict


MYCTU_list = list(set(list_maker(f2)))
"""How are we going to handle this"""
MYCLE_list = list(set(list_maker(f3)))
BUCAI_APS = list(set(list_maker(f4)))
BUCAI_Cc = list(set(list_maker(f5)))
Hu_Ecoli = list(set(list_maker(f6)))
Babu_S3_Ecoli = list(set(list_maker(f7)))
Babu_S6_Ecoli = list(set(list_maker(f8)))
ee = ['COG0051', 'COG0781', 'COG0187', 'COG0188', 'COG0847', 'COG0587', 'COG1466', 'COG0470', 'COG2812', 'COG0592', 'COG3050', 'COG2927', 'COG0191', 'COG4573', 'COG0706', 'COG1862', 'COG0341', 'COG0342', 'COG0690', 'COG1314', 'COG0201', 'COG0244', 'COG0222', 'COG0795', 'COG1137', 'COG0795', 'COG3096', 'COG3006', 'COG3095', 'COG3095', 'COG3006', 'COG0188', 'COG0187', 'COG1589', 'COG0208', 'COG3116', 'COG0209', 'COG0208', 'COG0484', 'COG0443', 'COG0576', 'COG0459', 'COG0234', 'COG0751', 'COG0752', 'COG2884', 'COG2177', 'COG0191', 'COG4573', 'COG2812', 'COG0470', 'COG1466', 'COG0209', 'COG0208', 'COG4591', 'COG1136', 'COG4591', 'COG0825', 'COG0777', 'COG0777', 'COG0825', 'COG0439', 'COG0511', 'COG1452', 'COG2980', 'COG1538', 'COG1136', 'COG0845', 'COG0389', 'COG1974', 'COG1952', 'COG0653', 'COG0201', 'COG1314', 'COG0690', 'COG0342', 'COG0341', 'COG1862', 'COG0706', 'COG2913', 'COG3317', 'COG4105', 'COG4775', 'COG1520', 'COG0855', 'COG1530', 'COG0513', 'COG1185', 'COG0148', 'COG0587', 'COG0847', 'COG0085', 'COG0086', 'COG0202', 'COG1595', 'COG0085', 'COG0086', 'COG0202', 'COG1508', 'COG0085', 'COG0086', 'COG0202', 'COG0568', 'COG0085', 'COG0086', 'COG0202', 'COG0568', 'COG0085', 'COG0086', 'COG0202', 'COG1595', 'COG0085', 'COG0086', 'COG0202', 'COG0568', 'COG1191', 'COG0085', 'COG0086', 'COG0202', 'COG1077', 'COG1792', 'COG2891', 'COG2980', 'COG1452', 'COG0795', 'COG1137', 'COG0795', 'COG3117', 'COG1934', 'COG0016', 'COG0073', 'COG0202', 'COG0086', 'COG0085']
Essential_ecoli = list(set(ee))


Ecoli_complex_dict = {}
Ecoli_functions_dict = {}


for line in f:
    value = []
    line = line.strip()
    line = line.replace("\xef\xbb\xbf", "")
    line = line.split(",")
    key = line[0]
    for i in line:
        if "COG" in i:
            value.append(i)
    Ecoli_complex_dict[key] = value


MYCTU_Complex_dict = complex_maker(MYCTU_list)
MYCLE_Complex_dict = complex_maker(MYCLE_list)
BUCAI_APS_Complex_dict = complex_maker(BUCAI_APS)
BUCAI_Cc_Complex_dict = complex_maker(BUCAI_Cc)
Hu_Ecoli_Complex_dict = complex_maker(Hu_Ecoli)
Babu_S3_Ecoli_Complex_dict = complex_maker(Babu_S3_Ecoli)
Babu_S6_Ecoli_Complex_dict = complex_maker(Babu_S6_Ecoli)
Essential_ecoli_complex_dict = complex_maker(Essential_ecoli)

Ecoli_functions_dict = functions_dict_maker(Ecoli_complex_dict)
MYCTU_functions_dict = functions_dict_maker(MYCTU_Complex_dict)
MYCLE_functions_dict = functions_dict_maker(MYCLE_Complex_dict)
BUCAI_APS_functions_dict = functions_dict_maker(BUCAI_APS_Complex_dict)
BUCAI_Cc_functions_dict = functions_dict_maker(BUCAI_Cc_Complex_dict)
Hu_Ecoli_functions_dict = functions_dict_maker(Hu_Ecoli_Complex_dict)
Babu_S3_Ecoli_functions_dict = functions_dict_maker(Babu_S3_Ecoli_Complex_dict)
Babu_S6_Ecoli_functions_dict = functions_dict_maker(Babu_S6_Ecoli_Complex_dict)
Essential_ecoli_functions_dict = functions_dict_maker(Essential_ecoli_complex_dict)


Ecoli_reference_overall_complex_function = majority(Ecoli_functions_dict)
MYCTU_reference_overall_complex_function = majority(MYCTU_functions_dict)
MYCLE_reference_overall_complex_function = majority(MYCLE_functions_dict)
BUCAI_APS_reference_overall_complex_function = majority(BUCAI_APS_functions_dict)
BUCAI_Cc_reference_overall_complex_function = majority(BUCAI_Cc_functions_dict)
Hu_Ecoli_reference_overall_complex_function = majority(Hu_Ecoli_functions_dict)
Babu_S3_Ecoli_reference_overall_complex_function = majority(Babu_S3_Ecoli_functions_dict)
Babu_S6_Ecoli_reference_overall_complex_function = majority(Babu_S6_Ecoli_functions_dict)
Essential_ecoli_reference_overall_complex_function = majority(Essential_ecoli_functions_dict)

file_writer(Ecoli_reference_overall_complex_function, "Ecoli_Reference_Complex_Function.csv")
file_writer(MYCTU_reference_overall_complex_function, "MYCTU_Complex_Function.csv")
file_writer(MYCLE_reference_overall_complex_function, "MYCLE_Complex_Function.csv")
file_writer(BUCAI_APS_reference_overall_complex_function, "BUCAI_APS_Complex_Function.csv")
file_writer(BUCAI_Cc_reference_overall_complex_function, "BUCAI_Cc_Reference_Complex_Function.csv")
file_writer(Hu_Ecoli_reference_overall_complex_function, "Hu_Ecoli_Reference_Complex_Function.csv")
file_writer(Babu_S3_Ecoli_reference_overall_complex_function, "Babu_S3_Ecoli_Reference_Complex_Function.csv")
file_writer(Babu_S6_Ecoli_reference_overall_complex_function, "Babu_S6Ecoli_Reference_Complex_Function.csv")
file_writer(Essential_ecoli_reference_overall_complex_function, "Essential_Ecoli_Reference_Complex_Function.csv")


print MYCTU_reference_overall_complex_function
print MYCTU_Complex_dict
print MYCTU_functions_dict