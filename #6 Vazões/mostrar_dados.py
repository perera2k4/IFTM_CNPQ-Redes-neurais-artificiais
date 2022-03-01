import pandas as pd
import numpy as np
import torch
import matplotlib.pyplot as plt

vazoesDataFrame = pd.read_csv('vazoes.csv', header=0, sep=',')
entradaDF = vazoesDataFrame.iloc[:100]
entradaDF['Media'] = entradaDF['Media'].replace(np.nan, 0)
data = entradaDF['Media']

plt.figure(figsize=(10, 6))
plt.plot(data, '-')
plt.xlabel('DIAS')
plt.ylabel('MÉDIA')
plt.title('Vazões Rio Da Prata')
plt.savefig("imagens/vazoesMedia.png")