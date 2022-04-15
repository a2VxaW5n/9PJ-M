import numpy as np
from scipy.optimize import linear_sum_assignment
import pandas as pd
import random
import time
import hashlib

file = "choises.csv"

## Check if file is valid
#with open(file,'rb') as fp:
    #filedata = fp.read()
#file_md5 = hashlib.md5(filedata).hexdigest()
#print(file_md5)
#if file_md5 != "416ea4af5301c689555607dfd30778d7":
    #raise Exception("Invalid File")

## Main
data = pd.read_csv(file,index_col=0)
#print(data)

seed = int(time.time()) # 便利のため実行時の時間をseedとする
#seed = 114514 # 事後再現用
print("SEED:",seed)
chara = data.index.to_list()
random.Random(seed).shuffle(chara) # ハンガリアンの被った場合は順番依存なので，順番をランダムシードでシャッフルする
#print(chara)

weapon = data.columns.to_list()

cost = []
for name in chara:
    cost.append(data.loc[name].values.tolist())

row_ind, col_ind = linear_sum_assignment(cost,maximize=True)
table = pd.DataFrame(index=weapon,columns=[str(seed)])
for i in range(len(col_ind)):
    table[str(seed)][weapon[col_ind[i]]] = chara[i]

#table.to_csv("result.txt",sep=":")

## Print
print("('*'は未回答者)")
print("======= 結果 =======")
for wp in table.index:
    print(f"{wp}: {table[str(seed)][wp]}")

print("======= 効用 =======")
print(f"=== 個別:")
y = []
for wp in table.index:
    yv = data[wp][table[str(seed)][wp]]
    y.append(yv)
    print(f"    {table[str(seed)][wp]}: {yv}")
print(f"=== 平均: {sum(y)/len(y):.2g}")
print(f"=== 最大: {max(y)} (計{y.count(max(y))}人)")
print(f"=== 最小: {min(y)} (計{y.count(min(y))}人)")
