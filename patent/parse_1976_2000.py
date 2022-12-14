# #%%
# # library
# import pandas as pd
# import re

# #%%
# with open('1976.txt', 'r') as f:
#     text = f.read()

# #%%
# text[0:5]
# # %%
# pattern_WKU = re.compile(r'WKU\s\s(RE)?\d+')
# matches = pattern_WKU.finditer(text)
# list = []
# for match in matches:
#     value = match.group()

#     list.append(value)
# print(list[5])

# #%%
# len(list) #1379
# #%%
# abs_match = list
# # %%
# type(abs_match)

# #%%
# abs_match
# #%%
# str_abs = ''.join(abs_match)
# print(str_abs[0:10])
# #%%
# p = re.compile(r'\W+(RE)?\d+')
# matches = p.finditer(str_abs)
# wku_num = []
# for match in matches:
#     value = match.group() # same value for 19760106_wk1
    
#     wku_num.append(value)
# #print(match.group())

# #%%
# sum(1 for _ in re.finditer(p,str_abs))

# #%%
# print(list)
# ## Looping over regex matches inside text
# #for match_num, match in enumerate(re.finditer(reg, test, re.MULTILINE), start=1):
# #    print(f"Match {match_num} was found at {match.start()}-{match.end()}: {match.group()}")
# # %%
# sum(1 for _ in re.finditer(pattern_WKU,text))
# # 1379 products
# # %%
# type(match.group())
# #%%
# pattern_ISD = re.compile(r'ISD\s\s(1976)\d+')
# matches = pattern_ISD.finditer(text)
# ISD = []
# for match in matches:
#     value = match.group() # same value for 19760106_wk1
    
#     ISD.append(value)
# print(ISD[5])
# #%%
# ISD_str = ''.join(ISD)
# #%%
# pattern_ISD1 = re.compile(r'\W(1976)\d+')
# matches = pattern_ISD1.finditer(ISD_str)
# ISD_num = []
# for match in matches:
#     value = match.group() # same value for 19760106_wk1
    
#     ISD_num.append(value)
#     #print(match.group())
# #%%
# sum(1 for _ in re.finditer(pattern_ISD1,ISD_str))
# #8363
# #becasue there are many ISD value besides the one associate with publish time
# #publish time start with 1976 #1379
# #%%%
# #pattern_ABS = re.compile(r'ABST\s.+\s.+[A-Z]$')
# #matches = pattern_ABS.finditer(text)
# #for match in matches:
#  #   print(match.group())


# #%%
# pattern_ABS = re.compile(r'ABST\n*\n*((?:\n.*)+?)(?=\n[A-Z]{4}|\Z)')
# matches = pattern_ABS.finditer(text)
# #for match in matches:
# #    print(match.group())     
# #    .*\n*: Match rest of the line followed by 0 or more line breaks
# #((?:\n.*)+?): Capture group 1 to capture our text which 1 or lines of everything until next condition is satisfied
# #(?=\nAREA:|\Z): Assert that we have a line break followed by AREA: or end of input right ahead of the current position

# #%%
# ABST = []
# for match in matches:
#     val = match.group()
#     ABST.append(val)
# print(ABST[5])
# #%%
# #abst_str = ''.join(ABST)
# #%%
# #pattern_ABS1 = re.compile(r'ABST\n*\n*((?:\n.*)+?)(?=\n[A-Z]{4}|\Z)')
# #matches = pattern_ABS1.finditer(abst_str)
# #for match in matches:
# #    print(match.group())     

# #%%
# #abst = pd.DataFrame({'ABST':ABST})
# #abst.to_excel('abst_check.xlsx')
# #%%
# sum(1 for _ in re.finditer(pattern_ABS1,abst_str))
# # Search for 'ABST' 1379
# # search in text file by case is 1379
# # search by paragraph with 1384 
# # add'\n' after ABST match #1379
# #%%

# #%%
# #test
# with open('test.txt', 'r') as f:
#     text1 = f.read()


# #%%
# sum(1 for _ in re.finditer(pattern_ISD,text))

# #%%
# #ICL
# #pattern_ICL = re.compile(r'ICL\s\s\w+')
# #matches = pattern_ICL.finditer(text)
# #for match in matches:
# #    print(match.group())
# #%%
# #sum(1 for _ in re.finditer(pattern_ICL,text))
# # search ICL\s\s\w+ #2023
# # some aplication has multiple line of ICL info

    
# # %%
# result_1976 = pd.DataFrame({'Pattent ID':wku_num, 'Publish Date':ISD_num, 'Abstract':ABST})
# #result_1976.to_excel('demo.xlsx')
# #%%
# result_1976.head(10)
# #%%
# # motified id
# result_1976['Adjusted ID'] = result_1976['Pattent ID'].iloc[5:].str[:-1]

# #%%
# result_1976['Abstract'] = result_1976['Abstract'].str[10:]
# #print(test1)
# #%%
# result_1976.head(10)
# #%%
# result_1976.to_pickle('demo1')
# #%%
# print(result_1976.tail())

# #%%
# test = pd.read_pickle('demo1')
# print(test.head(10))
# #%%
# #create new columns to remove last digit
# # remove the abst\npal 
# # beasutiful soup
# # CLAS ~ FSC for us class 
# # FD
# # %%
# # CLAS problems
# pattern_clas = re.compile(r'CLAS\n*\n*((?:\n.*)+?)(?=\nFSC|\Z)')
# matches = pattern_clas.finditer(text)
# CLAS = []
# for match in matches:
#     value = match.group()
#     CLAS.append(value)
#     #print(match.group())     

# #%%
# sum(1 for _ in re.finditer(pattern_clas,text))#1379

# #%%
# CLAS
# #%%
# clas = pd.DataFrame({'class':CLAS})
# # %%
# clas.head()
# # %%
# #import re
# #
# #r = re.compile(r'ICL\s\s')
# #newlist = list(filter(r.finditer, CLAS)) # Read Note below
# #print(newlist)
# # %%
# clas['class'][1]
# # %%
# clas['ICL'] = clas['class'].str.split('ICL')
# # %%
# new = clas['class'].str.split("ICL", n = 1, expand = True)
# # %%
# clas['class1']=new[0]
# clas['icl']=new[1]
# # %%
# test = clas['class1'][0]

# # %%
# new_class = []
# for x in clas['class1']:
#     x = re.sub(r'\nEDF\s\s\w+\n',' ',x)
#     x = re.sub('\n', ' ', x)
#     new_class.append(x)

# #%%
# len(new_class)
# # %%
# class_process(clas)
# %%
########################################################
#%%
# library
import pandas as pd
import re
import os
#%%
import os
#C:\Users\Ann's XPS\Downloads\1976\1967
# import os
# for root, _, files in os.walk(path):
#     for filename in files:
#         with open(os.path.join(root, filename), 'r') as f:
#             #your code goes here



#%%


#folder = "C:\Users\Ann's XPS\Downloads\1976\1967"
file_name = []
for filename in os.listdir(r"C:/Users/Ann's XPS/Downloads/1976/1976"):
    file_name.append(filename)
    # infilename = os.path.join(folder, filename)
    # if not os.path.isfile(infilename): continue

    # base, extension = os.path.splitext(filename)
    # infile = open(infilename, 'r')
    # outfile = open(os.path.join(folder, '{}_edit.{}'.format(base, extension)), 'w')
    # newfield2(infile, outfile)
#%%
par_f = file_name[0:10]
par_f

#%%
class text_process():
    
    def 
#%%
def text_processor(par_f):
    for i in par_f:
        with open(i, 'r') as f:
            text = f.read()

def get_Id(text):
    pattern_WKU = re.compile(r'WKU\s\s(RE)?\d+')
    matches = pattern_WKU.finditer(text)
    list = []
    for match in matches:
        value = match.group()
        list.append(value)
    return list
    
def get_Isd(text):
        
    pattern_ISD = re.compile(r'ISD\s\s(1976)\d+')
    matches = pattern_ISD.finditer(text)
    ISD = []
    for match in matches:
        value = match.group() # same value for 19760106_wk1
        ISD.append(value)
    return ISD
    
def get_Abs(text):
    pattern_ABS = re.compile(r'ABST\n*\n*((?:\n.*)+?)(?=\n[A-Z]{4}|\Z)')
    matches = pattern_ABS.finditer(text)
    ABST = []
    for match in matches:
        val = match.group()
        ABST.append(val)
    return ABST

def ger_Clas():
    pattern_clas = re.compile(r'CLAS\n*\n*((?:\n.*)+?)(?=\nFSC|\Z)')
    matches = pattern_clas.finditer(text)
    CLAS = []
    for match in matches:
        value = match.group()
        CLAS.append(value)

    clas = pd.DataFrame({'class':CLAS})

    new = clas['class'].str.split("ICL", n = 1, expand = True)
    return new


def class_process(df):
    new_class = []
    for x in df:
        x = re.sub(r'\nEDF\s\s\w+\n',',',x)
        x = re.sub('\n', ',', x)
        x = re.sub(r'(OCL|XCL)', ' ',x)
        new_class.append(x)
    return new_class


def icl_process(df):
    new_class1 = []
    for x in df:
        x = re.sub(r'ICL', ' ',x)
        x = re.sub('\n', ',', x)
        
        new_class1.append(x)
    return new_class1


# cla = class_process(new[0])

# #icl=[re.sub('\n', ',', x) for x in new[1]]
# icl = icl_process(new[1])


result_1976 = pd.DataFrame({'id_original':list, 'date':ISD, 
                            'abstract':ABST,'class_raw':CLAS,'clas':cla,'ICL':icl})

#%%
result_1976.head(10)
#%%
result_1976['abstract'] = result_1976['abstract'].str[10:]
#result_1976['Adjusted ID'] = result_1976['Pattent ID'].str[:-1]
result_1976['patent_id'] = result_1976['patent_id'].str[5:-1]

result_1976['date'] = result_1976['date'].str[5:]
result_1976['clas'] = result_1976['clas'].str[5:]




#%%

with open('1976.txt', 'r') as f:
    text = f.read()

# %%
pattern_WKU = re.compile(r'WKU\s\s(RE)?\d+')
matches = pattern_WKU.finditer(text)
list = []
for match in matches:
    value = match.group()

    list.append(value)
#print(list[5])
#%%
pattern_ISD = re.compile(r'ISD\s\s(1976)\d+')
matches = pattern_ISD.finditer(text)
ISD = []
for match in matches:
    value = match.group() # same value for 19760106_wk1
    
    ISD.append(value)
#print(ISD[5])

#%%
pattern_ABS = re.compile(r'ABST\n*\n*((?:\n.*)+?)(?=\n[A-Z]{4}|\Z)')
matches = pattern_ABS.finditer(text)
ABST = []
for match in matches:
    val = match.group()
    ABST.append(val)
#print(ABST[5])

#%%


# CLAS problems
pattern_clas = re.compile(r'CLAS\n*\n*((?:\n.*)+?)(?=\nFSC|\Z)')
matches = pattern_clas.finditer(text)
CLAS = []
for match in matches:
    value = match.group()
    CLAS.append(value)
#%%
clas = pd.DataFrame({'class':CLAS})

new = clas['class'].str.split("ICL", n = 1, expand = True)
#%%
new_class = []
def class_process(df):
    
    for x in df:
        x = re.sub(r'\nEDF\s\s\w+\n',',',x)
        x = re.sub('\n', ',', x)
        x = re.sub(r'(OCL|XCL)', ' ',x)
        new_class.append(x)
    return new_class
#%%
new_class1 = []
def icl_process(df):
    
    for x in df:
        x = re.sub(r'ICL', ' ',x)
        x = re.sub('\n', ',', x)
        
        new_class1.append(x)
    return new_class1

#%%
cla = class_process(new[0])
#%%
#icl=[re.sub('\n', ',', x) for x in new[1]]
icl = icl_process(new[1])
#%%
len(cla)
#%%
len(icl)
#%%
cla
#%%
result_1976 = pd.DataFrame({'id_original':list, 'date':ISD, 
                            'abstract':ABST,'class_raw':CLAS,'clas':cla,'ICL':icl})

#%%
result_1976.head(10)
#%%
result_1976['abstract'] = result_1976['abstract'].str[10:]
#result_1976['Adjusted ID'] = result_1976['Pattent ID'].str[:-1]
result_1976['patent_id'] = result_1976['patent_id'].str[5:-1]

result_1976['date'] = result_1976['date'].str[5:]
result_1976['clas'] = result_1976['clas'].str[5:]


#%%
result_1976.head(5)
# %%
result_1976.to_excel('1976_wk01.xlsx')
# %%
