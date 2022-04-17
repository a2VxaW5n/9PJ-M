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

def ሉ(ወ):
    return pd.read_csv(ወ,index_col=0)
def የ(ወ):
    return print(ወ)
def ዩ(ወ):
    return print(f"SEED:{ወ}")
def ያ(ወ):
    return print(f"\u914d\u5c5e\u9806:{ወ}")
def ፙ(ወ,ዉ):
    return random.Random(ወ).shuffle(ዉ)
def ቱ(ወ):
    return ወ.index.to_list()
def ቲ(ወ):
    return ወ.columns.to_list()
def ጲ():
    return int(time.time())
def ቆ(ወ,ዉ):
    ቋ = []
    for ዱ in ወ:
        ቋ.append(ዉ.loc[ዱ].values.tolist())
    return ቋ
def ኋ(ወ):
    return linear_sum_assignment(ወ,maximize=True)
def ቤ(ወ,ዉ,ዊ,ዋ):
    ዷ = pd.DataFrame(index=ወ,columns=[str(ዉ)])
    for ቴ in range(len(ዊ)):
        ዷ[str(ዉ)][ወ[ዊ[ቴ]]] = ዋ[ቴ]
    ዷ.to_csv("ግ.txt",sep=":")
    return ዷ
def እ(ወ,ዉ,ዊ):
    የ("('*'\u306f\u672a\u56de\u7b54\u8005)")
    የ("======= \u7d50\u679c =======")
    for ኄ in ወ.index:
        የ(f"{ኄ}: {ወ[str(ዉ)][ኄ]}")

    የ("======= \u52b9\u7528 =======")
    የ(f"=== \u500b\u5225:")
    ፎ = []
    for ሎ in ወ.index:
        ፌ = ዊ[ሎ][ወ[str(ዉ)][ሎ]]
        ፎ.append(ፌ)
        የ(f"    {ወ[str(ዉ)][ሎ]}: {ፌ}")
    የ(f"=== \u5e73\u5747: {sum(ፎ)/len(ፎ):.2g}")
    የ(f"=== \u6700\u5927: {max(ፎ)} (\u8a08{ፎ.count(max(ፎ))}\u4eba)")
    የ(f"=== \u6700\u5c0f: {min(ፎ)} (\u8a08{ፎ.count(min(ፎ))}\u4eba)")

