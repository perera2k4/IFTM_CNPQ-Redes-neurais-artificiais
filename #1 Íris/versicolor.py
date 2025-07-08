"""
Classificação de flores Íris - Detecção de Virginica
Este script treina uma rede neural para classificar flores íris,
especificamente para detectar a classe Virginica.
"""

import torch
import numpy as np
from sklearn import datasets
from sklearn.utils import shuffle
import matplotlib.pyplot as plt

class Net(torch.nn.Module):
    """Modelo de Rede Neural para classificação binária"""
    def __init__(self, input_size, hidden_size):
        super(Net, self).__init__()
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.fc1 = torch.nn.Linear(self.input_size, self.hidden_size)  # full connected
        self.relu = torch.nn.ReLU()  # (0, infinito)
        self.fc2 = torch.nn.Linear(self.hidden_size, 1)
        self.sigmoid = torch.nn.Sigmoid()  # (0, 1)
        # self.tanh = torch.nn.Tanh() # (-1, 1)
    
    def forward(self, x):
        hidden = self.fc1(x)
        relu = self.relu(hidden)
        output = self.fc2(relu)
        output = self.sigmoid(output)
        return output

def plotcharts(errors, saida_testes, y_pred):
    """Função para plotar gráficos de erro e resultados"""
    errors = np.array(errors)
    plt.figure(figsize=(12, 5))
    
    # Gráfico de erros
    graf02 = plt.subplot(1, 2, 1)  # nrows, ncols, index
    graf02.set_title('Erros')
    plt.plot(errors, '-')
    plt.xlabel('Épocas')

    # Gráfico de testes
    graf03 = plt.subplot(1, 2, 2)
    plt.hlines(0.5, 0, 30, colors='k', linestyles='dashed')
    graf03.set_title('Testes')
    a = plt.plot(saida_testes.numpy(), 'yo', label='Real')
    plt.setp(a, markersize=10)
    a = plt.plot(y_pred.detach().numpy(), 'b+', label='Previsão')
    plt.setp(a, markersize=10)
    plt.legend(loc=7)
    plt.show()

def main():
    """Função principal do programa"""
    # Carregar dados da Iris
    iris = datasets.load_iris()
    dados = iris.data
    classes = iris.target
    nomes_classes = iris.target_names
    
    print("Dataset Iris carregado:")
    print(f"Formato dos dados: {dados.shape}")
    print(f"Classes: {nomes_classes}")
    print(f"Número de amostras por classe: {np.bincount(classes)}")
    
    # Converter as classes para detecção de Virginica
    # 0: setosa = 0; 1: versicolor = 0; 2: virginica = 1
    saida = np.where(classes == 2, 1, 0)
    print(f"Distribuição das classes convertidas: {np.bincount(saida)}")
    
    # Converter para tensor
    entrada = torch.FloatTensor(dados) / 10
    saida = torch.FloatTensor(saida)
    print(f"Saída tensor: {saida}")
    
    # Embaralhar os dados
    entrada, saida = shuffle(entrada, saida)
    
    # Separar os dados em treinamento e testes
    entrada_treinamento = entrada[0:120, :]
    saida_treinamento = saida[0:120]
    entrada_testes = entrada[120:150, :]
    saida_testes = saida[120:150]
    
    print(f"Dados de treinamento: {entrada_treinamento.shape}")
    print(f"Dados de teste: {entrada_testes.shape}")
    
    # Montar o modelo para o treinamento
    input_size = entrada_treinamento.size()[1]
    hidden_size = 5
    modelo = Net(input_size, hidden_size)
    
    print(f"Modelo criado - Input size: {input_size}, Hidden size: {hidden_size}")
    
    # Treinar o modelo
    epochs = 10000
    criterion = torch.nn.MSELoss()
    optimizer = torch.optim.SGD(modelo.parameters(), lr=0.9)
    
    errors = []  # array para guardar os erros de cada época
    
    print("Iniciando treinamento...")
    for epoch in range(epochs):
        optimizer.zero_grad()
        # Forward pass
        y_pred = modelo(entrada_treinamento)
        # Compute Loss
        loss = criterion(y_pred.squeeze(), saida_treinamento)
        errors.append(loss.item())
        if epoch % 100 == 0:
            print('Epoch {}: train loss: {}'.format(epoch, loss.item()))
        # Backward pass
        loss.backward()
        optimizer.step()
    
    # Testar o modelo com dados nunca vistos
    print("\nTestando o modelo...")
    y_pred = modelo(entrada_testes)
    
    # Calcular acurácia
    predictions = (y_pred.detach().numpy() > 0.5).astype(int)
    accuracy = np.mean(predictions.flatten() == saida_testes.numpy())
    print(f"Acurácia: {accuracy:.2%}")
    
    # Plotar gráficos
    plotcharts(errors, saida_testes, y_pred)

if __name__ == "__main__":
    main()
