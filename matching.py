# -*- coding: UTF-8 -*-

'''
        ∧　∧
      （＾ω＾)
     .(  O┬O
  .≡.◎-ヽJ┴◎

'''

import numpy as np
from scipy.optimize import linear_sum_assignment
import pandas as pd
import random
import time

ጰ = "choises.csv"

## Main
ጹ = pd.read_csv(ጰ,index_col=0)
#print(data)

ጲ = int(time.time())
#ጲ = 114514 
print("SEED:",ጲ)
ጷ = ጹ.index.to_list()
random.Random(ጲ).shuffle(ጷ)
print("\u914d\u5c5e\u9806:",ጷ)

ጵ = ጹ.columns.to_list()

ቋ = []
for ዱ in ጷ:
    ቋ.append(ጹ.loc[ዱ].values.tolist())

ቶ, ኆ = linear_sum_assignment(ቋ,maximize=True)
ዷ = pd.DataFrame(index=ጵ,columns=[str(ጲ)])
for ቴ in range(len(ኆ)):
    ዷ[str(ጲ)][ጵ[ኆ[ቴ]]] = ጷ[ቴ]

ዷ.to_csv("ግ.txt",sep=":")

## Print
print("('*'\u306f\u672a\u56de\u7b54\u8005)")
print("======= \u7d50\u679c =======")
for ኄ in ዷ.index:
    print(f"{ኄ}: {ዷ[str(ጲ)][ኄ]}")

print("======= \u52b9\u7528 =======")
print(f"=== \u500b\u5225:")
ፎ = []
for ሎ in ዷ.index:
    ፌ = ጹ[ሎ][ዷ[str(ጲ)][ሎ]]
    ፎ.append(ፌ)
    print(f"    {ዷ[str(ጲ)][ሎ]}: {ፌ}")
print(f"=== \u5e73\u5747: {sum(ፎ)/len(ፎ):.2g}")
print(f"=== \u6700\u5927: {max(ፎ)} (\u8a08{ፎ.count(max(ፎ))}\u4eba)")
print(f"=== \u6700\u5c0f: {min(ፎ)} (\u8a08{ፎ.count(min(ፎ))}\u4eba)")
