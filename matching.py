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

ጲ = int(time.time()) # 便利のため実行時の時間をseedとする
#ጲ = 114514 # 事後再現用
print("SEED:",ጲ)
ጷ = ጹ.index.to_list()
random.Random(ጲ).shuffle(ጷ) # ハンガリアンの被った場合は順番依存なので，順番をランダムシードでシャッフルする
print("配属順:",ጷ)

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
print("('*'は未回答者)")
print("======= 結果 =======")
for ኄ in ዷ.index:
    print(f"{ኄ}: {ዷ[str(ጲ)][ኄ]}")

print("======= 効用 =======")
print(f"=== 個別:")
ፎ = []
for ሎ in ዷ.index:
    ፌ = ጹ[ሎ][ዷ[str(ጲ)][ሎ]]
    ፎ.append(ፌ)
    print(f"    {ዷ[str(ጲ)][ሎ]}: {ፌ}")
print(f"=== 平均: {sum(ፎ)/len(ፎ):.2g}")
print(f"=== 最大: {max(ፎ)} (計{ፎ.count(max(ፎ))}人)")
print(f"=== 最小: {min(ፎ)} (計{ፎ.count(min(ፎ))}人)")
