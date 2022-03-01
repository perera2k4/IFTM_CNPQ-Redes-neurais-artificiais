# Importar bibliotecas 
import yfinance as yf
import pandas as pd
import numpy as np
import math
import torch
import matplotlib.pyplot as plt

# Classe do modelo da Rede Neural
class Net(torch.nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.input_size = 50
        self.hidden_size = 100
        self.fc1 = torch.nn.Linear(self.input_size, self.hidden_size)
        self.relu = torch.nn.ReLU()
        self.fc2 = torch.nn.Linear(self.hidden_size, 1)
    def forward(self, x):
        hidden = self.fc1(x)
        relu = self.relu(hidden)
        output = self.fc2(relu)
        output = self.relu(output)
        return output

classificadorLoaded = Net()
state_dict = torch.load('checkpoint.pth')
classificadorLoaded.load_state_dict(state_dict)
classificadorLoaded.eval()
data = yf.download('GOLL4.SA', start='2016-01-01', end='2020-11-19')

#Coletar somente o fechamento diário
data = data.Close

# Criar janela deslizante
janelas = 50

data_final = np.zeros([data.size - janelas, janelas + 1])

for i in range(len(data_final)):
    for j in range(janelas+1):
        data_final[i][j] = data.iloc[i+j]
# Normalizar entre 0 e 1
dif = data_final.max() - data_final.min()
soma = data_final.max() + data_final.min()
data_final = (data_final - data_final.min())/dif

x = data_final[:, :-1]
y = data_final[:, -1]

#Entrada do teste
#Saída do teste
test_input = torch.FloatTensor(x[850: , :])
y_pred = classificadorLoaded(test_input)
fechamento = (y_pred + data_final.min())*soma
fechamento = fechamento.detach().numpy()

print(fechamento[-1][0])