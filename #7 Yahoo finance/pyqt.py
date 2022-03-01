# import torch
import sys
import glob
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QCalendarWidget, QComboBox, QMainWindow, QLabel, QApplication, QWidget, QGridLayout, QLineEdit, QFormLayout, QMessageBox
from PyQt5.QtCore import QSize, Qt, QProcess, QDate
from PyQt5.QtGui import QFont, QDoubleValidator
from datetime import datetime
import yfinance as yf
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setup_main_window()
        self.initUI()

    def setup_main_window(self):
        self.x = 1200
        self.y = 600
        self.setMinimumSize(QSize(self.x, self.y))
        #self.setMaximumSize(QSize(self.x, self.y))
        
        self.setWindowTitle("Séries temporais - Yahoo Finanças")
        self.wid = QWidget(self)
        self.setCentralWidget(self.wid)
        self.layout = QGridLayout()
        self.wid.setLayout(self.layout)
        self.wid.setStyleSheet("""
            QWidget {
                background: #2F3136;
            }
            QPushButton {
                background: #26282C;
                border-radius: 5px;
                font-size: 14px;
                font-weight: 600;
                color: white;
                min-height: 40px;
                min-width: 150px;
            }
            QPushButton:hover {
                background: rgb(64, 68, 75);
            }
            QLabel {
                color: white;
                font-size: 16px;
            }
            QLabel#status {
                color: white;
                font-size: 12px;
            }
            QLineEdit {
                background: #26282C;
                padding: 5px;
                border-radius: 5px;
                border-color: #26282C;
                font-size: 16px;
                color: white;
            }
            """)

    def initUI(self):
        # Combobox das ações de empresas
        self.combobox = QtWidgets.QComboBox(self)
        self.combobox.setStyleSheet("""
                                    QComboBox{
                                        background-color: #26282C;
                                        border-radius: 1px;
                                        min-height: 50px;
                                        min-width: 50px;
                                        font-size: 16px;
                                        color: white;
                                        
                                    }
                                        
                                    QComboBox QAbstractItemView{
                                        color: white;
                                        background-color: #26282C
                                        
                                    }
                                    
                                    QComboBox:hover{
                                            background: rgb(64, 68, 75);
                                            border: 2px solid #26282C;
                                    }

                                    QComboBox::placeholder{
                                        color: white;
                                        font-size: 16px;
                                    }
                                    """)
        self.combobox.addItems(["VALE3.SA", "PETR4.SA", "BBDC4.SA", "AZUL4.SA", "BPAC11.SA", "ITUB4.SA", "SUZB3.SA", "BOVA11.SA", "BBAS3.SA", "LREN3.SA"])
        self.empresa = str(self.combobox.currentText())
        # Botao de Plotar Gráfico
        self.botaoData = QtWidgets.QPushButton(self)
        self.botaoData.setText("Escolher Data")
        self.botaoData.clicked.connect(self.escolherDataInicio)

        # Layout
        self.layout.addWidget(self.combobox, 1, 0, 1, 2)
        self.layout.addWidget(self.botaoData, 3, 0, 1, 2)
        
        # Controladores
        self.calendarioInicioExiste = False
        self.calendarioFimExiste = False

    def escolherDataInicio(self):
        self.date = datetime.now()
        self.ano = self.date.year
        self.mes = self.date.month
        self.dia = self.date.day
        self.textoEscolhaData = QLabel('Escolha a Data Inicial e Final')
        self.layout.addWidget(self.textoEscolhaData, 4, 0, 1, 2)
        self.textoEscolhaData.setAlignment(Qt.AlignCenter)
        self.textoEscolhaData.setStyleSheet("margin: 20px")
        self.calendarioInicio = QCalendarWidget(self)
        self.calendarioInicio.selectionChanged.connect(self.onChangedDataInicio)
        self.calendarioInicio.setMaximumDate(QDate(self.ano, self.mes, self.dia))
        self.calendarioInicio.setStyleSheet("""
        QCalendarWidget QWidget { 
            alternate-background-color: rgb(128, 128, 128);
        }
        
        /* normal days */
        QCalendarWidget QAbstractItemView:enabled 
        {
            color: white;  
            background-color: #26282C;  
            selection-background-color: rgb(128, 128, 128); 
            selection-color: rgb(0, 255, 0); 
            font-size: 18px;
        }
        
        /* days in other months */
        QCalendarWidget QAbstractItemView:disabled { 
            color: rgb(128, 128, 128); 
        }""")
        self.escolhaCalendarioInicio = self.calendarioInicio.selectedDate().toString('yyyy-MM-dd')
        self.calendarioInicioTexto = QLabel(f'Data Início (Ano/Mês/Dia): {self.escolhaCalendarioInicio}')
        self.layout.addWidget(self.calendarioInicio, 5, 0)
        self.layout.addWidget(self.calendarioInicioTexto, 6, 0)
        self.calendarioInicioTexto.setAlignment(Qt.AlignCenter)
        self.calendarioInicioTexto.setStyleSheet("margin: 10px")
        self.calendarioFim = QCalendarWidget(self)
        self.calendarioFim.selectionChanged.connect(self.onChangedDataFim)
        self.calendarioFim.setMaximumDate(QDate(self.ano, self.mes, self.dia+1))
        self.calendarioFim.setStyleSheet("""
        QCalendarWidget QWidget { 
            alternate-background-color: rgb(128, 128, 128);
        }
        
        /* normal days */
        QCalendarWidget QAbstractItemView:enabled 
        {
            color: white;  
            background-color: #26282C;  
            selection-background-color: rgb(128, 128, 128); 
            selection-color: rgb(0, 255, 0); 
            font-size: 18px;
        }
        /* days in other months */
        QCalendarWidget QAbstractItemView:disabled { 
            color: rgb(128, 128, 128); 
        }""")
        self.escolhaCalendarioFim = self.calendarioFim.selectedDate().toString('yyyy-MM-dd')
        self.calendarioFimTexto  = QLabel(f'Data Fim (Ano/Mês/Dia): {self.escolhaCalendarioFim}')
        self.layout.addWidget(self.calendarioFim, 5, 1)
        self.layout.addWidget(self.calendarioFimTexto, 6, 1)
        self.calendarioFimTexto.setAlignment(Qt.AlignCenter)
        self.calendarioFimTexto.setStyleSheet("margin: 10px")
        self.calendarioInicioExiste = True
        self.botaoGraf = QtWidgets.QPushButton(self)
        self.botaoGraf.setText("Mostrar Gráficos")
        self.botaoGraf.clicked.connect(self.mostrarGrafico)
        self.layout.addWidget(self.botaoGraf, 3, 0, 1, 2)
        self.botaoVoltar = QtWidgets.QPushButton(self)
        self.botaoVoltar.setText("Voltar")
        self.layout.addWidget(self.botaoVoltar, 0, 0, 1, 2)
        self.botaoVoltar.clicked.connect(self.removerPaginaCalendarios)
        self.layout.removeWidget(self.botaoData)
        self.botaoData = False

    def removerPaginaCalendarios(self):
        self.botaoVoltar.deleteLater()
        self.calendarioInicio.deleteLater()
        self.calendarioInicioTexto.deleteLater()
        self.calendarioFim.deleteLater()
        self.calendarioFimTexto.deleteLater()
        self.textoEscolhaData.deleteLater()
        self.botaoGraf.deleteLater()
        self.combobox.deleteLater()
        self.initUI()

    def mostrarGrafico(self):
        # Coletar dados da empresa
        if (self.calendarioInicioExiste):
            self.botaoVoltar.deleteLater()
            self.calendarioInicio.deleteLater()
            self.calendarioInicioTexto.deleteLater()
            self.calendarioFim.deleteLater()
            self.calendarioFimTexto.deleteLater()
            self.textoEscolhaData.deleteLater()
            self.botaoGraf.deleteLater()
            self.combobox.deleteLater()
        
        # Botao de Previsão
        self.botaoPrev = QtWidgets.QPushButton(self)
        self.botaoPrev.setText("Fazer Previsão")
        self.botaoPrev.clicked.connect(self.previsao)
        self.layout.addWidget(self.botaoPrev, 2, 0, 1, 2)
        self.empresa = str(self.combobox.currentText())
        self.data = yf.download(self.empresa, start=self.escolhaCalendarioInicio, end=self.escolhaCalendarioFim)
        
        #Coletar somente o fechamento diário
        self.data = self.data.Close
        self.fig = Figure((7, 4), dpi=100)
        self.canvas = FigureCanvas(self.fig)
        self.axes = self.fig.add_subplot(111)
        self.axes.plot(self.data[:], 'g-')
        self.axes.set_ylabel("VALOR R$")
        self.axes.set_xlabel("DIAS")
        self.axes.set_title(self.empresa)
        self.layout.addWidget(self.canvas, 5, 0, 1, 2)

    def onChangedDataInicio(self):
        self.escolhaCalendarioInicio = self.calendarioInicio.selectedDate().toString('yyyy-MM-dd')
        self.calendarioInicioTexto.setText(f'Data Início (Ano/Mês/Dia): {self.escolhaCalendarioInicio}')
    def onChangedDataFim(self):
        self.escolhaCalendarioFim = self.calendarioFim.selectedDate().toString('yyyy-MM-dd')
        self.calendarioFimTexto.setText(f'Data Fim (Ano/Mês/Dia): {self.escolhaCalendarioFim}')

    def previsao(self):
        import pandas as pd
        import numpy as np
        import math
        import torch
        if (self.canvas):
            self.canvas.deleteLater()

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
        data = yf.download(self.empresa, start='2016-01-01', end=self.escolhaCalendarioFim)

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
        variacao = fechamento[(len(fechamento)-2)][0]-fechamento[-1][0]
        self.variacaoText = QLabel("Variação: {:.2f}".format(variacao))
        self.layout.addWidget(self.variacaoText, 5, 0)
        self.textoPrev = QLabel('Previsão R$: {:.2f}'.format(fechamento[-1][0]))
        self.layout.addWidget(self.textoPrev, 4, 0)
        self.botaoRemvGraf = QtWidgets.QPushButton(self)
        self.botaoRemvGraf.setText("Página Inicial")
        self.botaoRemvGraf.clicked.connect(self.removerPrevisao)
        self.layout.addWidget(self.botaoRemvGraf, 0, 0, 1, 2)
        self.botaoPrev.deleteLater()

    def removerPrevisao(self):
        self.textoPrev.deleteLater()
        self.variacaoText.deleteLater()
        self.botaoRemvGraf.deleteLater()
        self.initUI()

def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()