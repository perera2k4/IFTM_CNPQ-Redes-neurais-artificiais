# Importar bibliotecas 
import yfinance as yf
import pandas as pd
import numpy as np
import math
import torch
import matplotlib.pyplot as plt

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

# Converter para tensor
#Entrada do treinamento
#Saída do treinamento
training_input = torch.FloatTensor(x[:850, :])
training_output = torch.FloatTensor(y[:850])

#Entrada do teste
#Saída do teste
test_input = torch.FloatTensor(x[850: , :])
test_output = torch.FloatTensor(y[850:])

# print(test_input)
# print(test_output)

# Classe do modelo da Rede Neural
class Net(torch.nn.Module):
    def __init__(self, input_size, hidden_size):
        super(Net, self).__init__()
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.fc1 = torch.nn.Linear(self.input_size, self.hidden_size)
        self.relu = torch.nn.ReLU()
        self.fc2 = torch.nn.Linear(self.hidden_size, 1)
    def forward(self, x):
        hidden = self.fc1(x)
        relu = self.relu(hidden)
        output = self.fc2(relu)
        output = self.relu(output)
        return output

# Criar a instância do modelo
input_size = training_input.size()[1]
hidden_size = 100
model = Net(input_size, hidden_size)
print(f'Entrada: {input_size}')
print(f'Escondida: {hidden_size}')
print(model)

# Critério de erro
criterion = torch.nn.MSELoss()

# Criando os paramêtros (learning rate[obrigatória] e momentum[opcional])
lr = 0.09 #0.01
momentum = 0.03 #0.01
optimizer = torch.optim.SGD(model.parameters(), lr, momentum)

# Para visualizar os pesos
for param in model.parameters():
  # print(param)
  pass

# Treinamento
model.train()
epochs = 1000
errors = []
for epoch in range(epochs):
    optimizer.zero_grad()
    # Fazer o forward
    y_pred = model(training_input)
    # Cálculo do erro
    loss = criterion(y_pred.squeeze(), training_output)
    errors.append(loss.item())
    if epoch % 1000 == 0:
      print(f'Epoch: {epoch}. Train loss: {loss.item()}.')
    # Backpropagation
    loss.backward()
    optimizer.step()

# Testar o modelo já treinado
model.eval()
y_pred = model(test_input)
after_train = criterion(y_pred.squeeze(), test_output)
print(model.state_dict())
print('Test loss after Training' , after_train.item())
fechamento = (y_pred + data_final.min())*soma
fechamento = fechamento.detach().numpy()
print(fechamento[-1][0])
torch.save(model.state_dict(), 'checkpoint.pth')