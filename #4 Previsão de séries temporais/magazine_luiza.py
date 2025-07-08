"""
Previsão de Séries Temporais - Magazine Luiza (MGLU3.SA)
Este script treina uma rede neural para prever o preço de ações da Magazine Luiza.
"""

import pandas as pd
import numpy as np
import math
import torch
import matplotlib.pyplot as plt
import yfinance as yf

class Net(torch.nn.Module):
    """Modelo de Rede Neural para previsão de séries temporais"""
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

def criar_janela_deslizante(data, janelas=50):
    """Cria uma janela deslizante para os dados"""
    data_final = np.zeros([data.size - janelas, janelas + 1])
    
    for i in range(len(data_final)):
        for j in range(janelas + 1):
            data_final[i][j] = data.iloc[i + j]
    
    return data_final

def normalizar_dados(data_final):
    """Normaliza os dados entre 0 e 1"""
    max_val = data_final.max()
    min_val = data_final.min()
    dif = max_val - min_val
    data_normalizada = (data_final - min_val) / dif
    
    return data_normalizada, max_val, min_val, dif

def plotcharts(errors, test_output, y_pred):
    """Função para plotar gráficos de erro e previsão"""
    errors = np.array(errors)
    lasterrors = np.array(errors[-25000:])
    
    plt.figure(figsize=(18, 5))
    
    # Gráfico de erros
    graf01 = plt.subplot(1, 3, 1)
    graf01.set_title('Errors')
    plt.plot(errors, '-')
    plt.xlabel('Epochs')
    
    # Gráfico dos últimos 25k erros
    graf02 = plt.subplot(1, 3, 2)
    graf02.set_title('Last 25k Errors')
    plt.plot(lasterrors, '-')
    plt.xlabel('Epochs')
    
    # Gráfico de testes
    graf03 = plt.subplot(1, 3, 3)
    graf03.set_title('Tests')
    a = plt.plot(test_output.numpy(), 'y-', label='Real')
    a = plt.plot(y_pred.detach().numpy(), 'b-', label='Predicted')
    plt.legend(loc=7)
    plt.show()

def main():
    """Função principal do programa"""
    print("Instalando e importando o Yahoo Finance...")
    
    # Coletar dados da Magazine Luiza
    print("Coletando dados da Magazine Luiza (MGLU3.SA)...")
    data = yf.download('MGLU3.SA', start='2016-01-01', end='2020-11-20')
    
    # Coletar somente o fechamento diário
    data = data.Close
    
    print(f"Dados coletados: {len(data)} pontos")
    
    # Plotar o gráfico todo
    plt.figure(figsize=(18, 6))
    plt.plot(data, '-')
    plt.xlabel('DIAS')
    plt.ylabel('VALOR R$')
    plt.title('MGLU3.SA')
    plt.show()
    
    # Plotar treinamento e teste
    plt.figure(figsize=(18, 6))
    plt.plot(data[:850], 'r-')
    plt.plot(data[850:], 'g-')
    plt.xlabel('DIAS')
    plt.ylabel('VALOR R$')
    plt.title('MGLU3.SA')
    plt.axvline(data.index[850], 0, 30, color='k', linestyle='dashed', label='Teste')
    plt.text(data.index[320], 25, 'Treinamento', fontsize='x-large')
    plt.text(data.index[910], 15, 'Testes', fontsize='x-large')
    plt.show()
    
    # Criar janela deslizante
    janelas = 50
    data_final = criar_janela_deslizante(data, janelas)
    
    # Normalizar entre 0 e 1
    data_final, max_val, min_val, dif = normalizar_dados(data_final)
    
    x = data_final[:, :-1]
    y = data_final[:, -1]
    
    # Converter para tensor
    training_input = torch.FloatTensor(x[:850, :])
    training_output = torch.FloatTensor(y[:850])
    
    test_input = torch.FloatTensor(x[850:, :])
    test_output = torch.FloatTensor(y[850:])
    
    print(f"Dados de treinamento: {training_input.shape}")
    print(f"Dados de teste: {test_input.shape}")
    
    # Criar a instância do modelo
    input_size = training_input.size()[1]
    hidden_size = 100
    model = Net(input_size, hidden_size)
    
    print(f'Entrada: {input_size}')
    print(f'Escondida: {hidden_size}')
    print(model)
    
    # Critério de erro
    criterion = torch.nn.MSELoss()
    
    # Criando os parâmetros (learning rate[obrigatória] e momentum[opcional])
    lr = 0.09
    momentum = 0.03
    optimizer = torch.optim.SGD(model.parameters(), lr, momentum)
    
    # Treinamento
    model.train()
    epochs = 100001
    errors = []
    
    print("Iniciando treinamento...")
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
    print('Test loss after Training:', after_train.item())
    
    # Plotar gráficos
    plotcharts(errors, test_output, y_pred)
    
    # Plotar detalhamento
    plt.figure(figsize=(10, 6))
    plt.plot(test_output.numpy(), 'b-', label='Real')
    plt.plot(y_pred.detach().numpy(), 'r-', label='Predicted')
    plt.grid()
    plt.legend()
    plt.xlabel('DIAS')
    plt.ylabel('VALOR R$')
    plt.title('MGLU3.SA - Detalhes da Previsão')
    plt.show()
    
    # Roll - Ajuste de predição
    roll = torch.roll(y_pred, -1, 0)
    roll[-1] = roll[-2]
    
    plt.figure(figsize=(10, 6))
    plt.plot(test_output.numpy(), 'b-', label='Real')
    plt.plot(roll.detach().numpy(), 'r-', label='Predicted (Roll)')
    plt.grid()
    plt.legend()
    plt.xlabel('DIAS')
    plt.ylabel('VALOR R$')
    plt.title('MGLU3.SA - Previsão com Roll')
    plt.show()

if __name__ == "__main__":
    main()
