import pandas as pd
import numpy as np
import torch
import matplotlib.pyplot as plt

vazoesDataFrame = pd.read_csv('vazoes.csv', header=0, sep=',')
entradaDF = vazoesDataFrame.iloc[:100]
entradaDF['Media'] = entradaDF['Media'].replace(np.nan, 0)
data = entradaDF['Media']

# Criar janela deslizante
janelas = 10
data_final = np.zeros([data.size - janelas, janelas + 1])

for i in range(len(data_final)):
  for j in range(janelas+1):
    data_final[i][j] = data.iloc[i+j]

max = 0
min = 0
for k in range(len(data_final)):
  if max < data_final[k].max():
    max = data_final[k].max()
  elif min > data_final[k].min():
    min = data_final[k].min()
dif = max - min
data_final = (data_final - min)/dif
x = data_final[:, :-1]
y = data_final[:, 0]

# Converter para tensor
#Entrada do treinamento
#Saída do treinamento
training_input = torch.FloatTensor(x[:70, :])
training_output = torch.FloatTensor(y[:70])

#Entrada do teste
#Saída do teste
test_input = torch.FloatTensor(x[70: , :])
test_output = torch.FloatTensor(y[70:])
last_input = test_input[len(test_input)-1]

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
hidden_size = 20
model = Net(input_size, hidden_size)
#print(f'Entrada: {input_size}')
#print(f'Escondida: {hidden_size}')
#print(model)

# Critério de erro
criterion = torch.nn.MSELoss()

# Criando os paramêtros (learning rate[obrigatória] e momentum[opcional])
training_values = open("treinamento.txt", "r", encoding="utf8")
readLines = training_values.readlines()
lr = float(readLines[0])
momentum = float(readLines[1])
optimizer = torch.optim.SGD(model.parameters(), lr, momentum)

# Para visualizar os pesos
for param in model.parameters():
  # print(param)
  pass

# Treinamento
model.train()
epochs = int(readLines[2])
errors = []
for epoch in range(epochs):
  optimizer.zero_grad()
  # Fazer o forward
  y_pred = model(training_input)
  # Cálculo do erro
  loss = criterion(y_pred.squeeze(), training_output)
  errors.append(loss.item())
  if epoch % 10000 == 0:
    print(f'Época: {epoch}. Diferença: {loss.item()}.')
  # Backpropagation
  loss.backward()
  optimizer.step()
# Testar o modelo já treinado
model.eval()
y_pred = model(test_input)
after_train = criterion(y_pred.squeeze(), test_output)
print('Testando perda apos o treinamento' , after_train.item())

# Gráficos de erro e de previsão
def plotcharts(errors):
    errors = np.array(errors)
    lasterrors = np.array(errors[-25000:])
    plt.figure(figsize=(8, 6))
    graf01 = plt.subplot(1, 3, 1) # nrows, ncols, index
    graf01.set_title('Erros')
    plt.plot(errors, '-')
    plt.xlabel('Épocas')
    graf02 = plt.subplot(1, 3, 2) # nrows, ncols, index
    graf02.set_title('Ultimos 25k erros')
    plt.plot(lasterrors, '-')
    plt.xlabel('Epochs')
    graf03 = plt.subplot(1, 3, 3)
    graf03.set_title('Tests')
    a = plt.plot(test_output.numpy(), 'y-', label='Real')
    #plt.setp(a, markersize=10)
    a = plt.plot(y_pred.detach().numpy(), '--', label='Predicted')
    #plt.setp(a, markersize=10)
    plt.legend(loc=7)
    plt.savefig("imagens/treinamentoGraficos.png")
plotcharts(errors)