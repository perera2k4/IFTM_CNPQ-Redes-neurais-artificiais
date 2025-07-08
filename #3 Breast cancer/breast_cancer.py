"""
Classificação de Câncer de Mama (Breast Cancer)
Este script treina uma rede neural para classificar câncer de mama.

Foram estudadas 2 classes:
- Se o câncer for maligno: WDBC-Malignant
- Se o câncer for benigno: WDBC-Benign

Total de 569 amostras: 212 malignas e 357 benignas

Características analisadas (todas referentes à mama):
- Raio (média das distâncias do centro aos pontos do perímetro)
- Textura (desvio padrão dos valores da escala de cinza)
- Perímetro
- Área
- Suavidade (variação local em comprimentos de raio)
- Compacidade (perímetro ^ 2 / área - 1,0)
- Concavidade (severidade das porções côncavas do contorno)
- Pontos côncavos (número de porções côncavas do contorno)
- Simetria
- Dimensão fractal ("aproximação do litoral" - 1)
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
    graf02.set_title('Errors')
    plt.plot(errors, '-')
    plt.xlabel('Epochs')
    
    # Gráfico de testes
    graf03 = plt.subplot(1, 2, 2)
    graf03.set_title('Tests')
    a = plt.plot(saida_testes.numpy(), 'yo', label='Real')
    plt.setp(a, markersize=10)
    a = plt.plot(y_pred.detach().numpy(), 'b+', label='Predicted')
    plt.setp(a, markersize=10)
    plt.legend(loc=7)
    plt.show()

def main():
    """Função principal do programa"""
    # Carregar dados do Breast Cancer
    breast_cancer = datasets.load_breast_cancer()
    dados = breast_cancer.data
    classes = breast_cancer.target
    
    print("Dataset Breast Cancer carregado:")
    print(f"Formato dos dados: {dados.shape}")
    print(f"Número de amostras por classe: {np.bincount(classes)}")
    print(f"Total de amostras: {len(dados)}")
    print(f"Classes: {breast_cancer.target_names}")
    
    # Converter para tensor
    entrada = torch.FloatTensor(dados) / 1000
    saida = torch.FloatTensor(classes)
    
    # Embaralhar os dados
    entrada, saida = shuffle(entrada, saida)
    
    # Separar os dados em treinamento e testes
    entrada_treinamento = entrada[0:539, :]
    saida_treinamento = saida[0:539]
    entrada_testes = entrada[509:569, :]
    saida_testes = saida[509:569]
    
    print(f"Dados de treinamento: {entrada_treinamento.shape}")
    print(f"Dados de teste: {entrada_testes.shape}")
    
    # Montar o modelo para o treinamento
    input_size = entrada_treinamento.size()[1]
    hidden_size = 30
    modelo = Net(input_size, hidden_size)
    
    print(f"Modelo criado - Input size: {input_size}, Hidden size: {hidden_size}")
    
    # Treinar o modelo
    epochs = 100000
    criterion = torch.nn.MSELoss()
    optimizer = torch.optim.SGD(modelo.parameters(), lr=0.9, momentum=0.3)
    
    errors = []  # array para guardar os erros de cada época
    
    print("Iniciando treinamento...")
    for epoch in range(epochs):
        optimizer.zero_grad()
        # Forward pass
        y_pred = modelo(entrada_treinamento)
        # Compute Loss
        loss = criterion(y_pred.squeeze(), saida_treinamento)
        errors.append(loss.item())
        if epoch % 1000 == 0:
            print('Epoca {}: aprendizado: {}'.format(epoch, loss.item()))
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
