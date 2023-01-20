# Монету подбросили 144 раза. Какова вероятность, что орел выпадет ровно 70 раз?
import numpy as np
from scipy.stats import binom

l = binom.pmf(k=70, n=144, p=0.5)

print(f'Вероятность, что орел выпадет ровно 70 раз = {(round(l*100, 2))}%')

