# -*- coding: utf-8 -*-
"""Pandas e Polars

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cuE8A26CBEQCwo2RzJ4dVVn8--VJLZsA
"""

!pip install polars
import pandas as pd
import polars as pl

array = [[f"2023{x*x-(-1)}" for x in range(10)],[x+2**4 for x in range(10)]]
array

array2 = [["2023"*x for x in range(10)],[x+3**x for x in range(10)]]
array2



df1= pd.DataFrame(array)
#for x in range(10):
df1

df1

df1= pd.DataFrame(array2)
df1

"""**Polars quebra quando usa range(1,10)**"""

df2= pl.DataFrame(array)
df2

df2= pl.DataFrame(array2)
df2

