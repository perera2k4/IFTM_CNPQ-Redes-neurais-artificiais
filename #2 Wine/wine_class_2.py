"""
Classificação de Vinhos - Classe 2
Este script treina uma rede neural para classificar vinhos, focando na classe 2.

Relatório:
- Foram estudadas 3 classes: classe 0 (59), classe 1 (71), classe 2 (48) no total de 178 amostras
- Classes: ['class_0' 'class_1' 'class_2']
- Características: 13 features incluindo:
  - Álcool, Ácido málico, Cinzas, Alcalinidade de cinzas (Elementos minerais do vinho)
  - Magnésio, Total de fenóis, Flavonóides, Fenóis não flavanoides, Proantocianinas
  - Intensidade da cor, Tonalidade da cor, Nível OD280 / OD315 de vinhos diluídos
  - Níveis do aminoácido prolina
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
    graf02.set_title('Erros')
    plt.plot(errors, '-')
    plt.xlabel('Épocas')
    
    # Gráfico de testes
    graf03 = plt.subplot(1, 2, 2)
    graf03.set_title('Testes')
    a = plt.plot(saida_testes.numpy(), 'yo', label='Real')
    plt.setp(a, markersize=10)
    a = plt.plot(y_pred.detach().numpy(), 'b+', label='Previsao')
    plt.hlines(0.5, 0, 30, colors='k', linestyles='dashed')
    plt.setp(a, markersize=10)
    plt.legend(loc=7)
    plt.show()

def main():
    """Função principal do programa"""
    # Carregar dados do Wine
    wine = datasets.load_wine()
    dados = wine.data
    classes = wine.target
    
    print("Dataset Wine carregado:")
    print(f"Formato dos dados: {dados.shape}")
    print(f"Número de amostras por classe: {np.bincount(classes)}")
    print(f"Total de amostras: {len(dados)}")
    
    # Converter as classes - Classe 2 (classe 2 -> 0, outras -> original)
    saida = np.where(classes == 2, 0, classes)
    
    # Converter para tensor
    entrada = torch.FloatTensor(dados) / 1000
    saida = torch.FloatTensor(saida)
    
    # Embaralhar os dados
    entrada, saida = shuffle(entrada, saida)
    
    # Separar os dados em treinamento e testes
    entrada_treinamento = entrada[0:148, :]
    saida_treinamento = saida[0:148]
    entrada_testes = entrada[148:178, :]
    saida_testes = saida[148:178]
    
    print(f"Dados de treinamento: {entrada_treinamento.shape}")
    print(f"Dados de teste: {entrada_testes.shape}")
    
    # Montar o modelo para o treinamento
    input_size = entrada_treinamento.size()[1]
    hidden_size = 13
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
        if epoch % 10000 == 0:
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
