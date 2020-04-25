print("step 1 - import packages")
import pandas as pd
import jupyter as js
import numpy as np

print("step 2 - read in excel")
excel1 = pd.read_excel('Dummy RWA Data.xlsx','Sheet1')
excel2 = pd.read_excel('Dummy RWA Data.xlsx','Sheet2')

print("step 3 - print imported data")
print(excel1)
print(excel2)

print("step 4 - attempt join 1")
JoinedData = excel2.append(excel1)
print(JoinedData)

print("step 5 - attempt join 2")
frames = [excel1, excel2]
result = pd.concat(frames, axis = 1, join = 'outer')
print(result)

print("step 6 - attempt join 3")
left_join_pandas = pd.merge(excel1, excel2, left_on = ['account_id', 'AssetClass'], right_on = ['account_id', 'AssetClass'], how = 'left')
print(left_join_pandas)

print("step 7 - select MRTG data only")
##print(excel1)
##print(excel2)
##account_number = excel1[1,]
##print(account_number)
print(excel1[['account_id', 'AssetClass']].head(100))
mortgages = excel1[excel1['AssetClass'] == 'Mortgage']
print(mortgages)
##SLIPRE = excel1[['AssetClass'] == 'SLIPRE']
