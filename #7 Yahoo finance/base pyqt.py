# import torch
import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow, QLabel, QApplication, QWidget, QGridLayout, QLineEdit, QFormLayout, QMessageBox
from PyQt5.QtCore import QSize, Qt, QProcess
from PyQt5.QtGui import QFont, QDoubleValidator

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setup_main_window()
        self.initUI()

    def setup_main_window(self):
        self.x = 1000
        self.y = 625
        self.setMinimumSize(QSize(self.x, self.y))
        self.showMaximized()
        self.setWindowTitle("Rede Neural - Vazões do Rio da Prata")
        self.wid = QWidget(self)
        self.setCentralWidget(self.wid)
        self.layout = QGridLayout()
        self.wid.setLayout(self.layout)
        self.wid.setStyleSheet("""
            .QWidget {
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
                background: rgb(64, 68, 75  );
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
        #Multiprocessos
        self.p = None
        self.menu_principal()
        self.setWindowIcon(QtGui.QIcon('imagens/icone.png'))
    def menu_principal(self):
        # Imagens
        self.imagem = QLabel(" ", self)
        self.imagem.setAlignment(Qt.AlignCenter)
        
        # Menu
            # Botões do menu
        self.botaoMostrarDadosVazao = QtWidgets.QPushButton(self)
        self.botaoMostrarDadosVazao.setText("Mostrar gráfico de vazão")
        self.botaoMostrarDadosVazao.clicked.connect(self.graficoMostrarDados)

        self.botaoTreinar = QtWidgets.QPushButton(self)
        self.botaoTreinar.setText("Rede Neural")
        self.botaoTreinar.clicked.connect(self.rede_neural)
        
        # Grid Layout
            # Layout Menu
        self.layout.addWidget(self.botaoMostrarDadosVazao, 0, 0)
        self.layout.addWidget(self.botaoTreinar, 0, 1)
    
    def graficoMostrarDados(self):
        # Remover botoes anteriores
        self.botaoTreinar.deleteLater()
        self.botaoMostrarDadosVazao.deleteLater()

        # Botao fechar
        self.botaoFechar = QtWidgets.QPushButton(self)
        self.botaoFechar.setText("Fechar")
        self.botaoFechar.clicked.connect(self.fechar_mostrarDados)

        if self.p is None:
            self.script = '.\mostrar_dados.py'            
            self.p = QProcess()
            self.p.finished.connect(self.process_finished)
            self.p.start("python", [self.script])
            self.endereco = QtGui.QPixmap("imagens/vazoesMedia.png")
            self.imagem.setPixmap(self.endereco)
            self.imagem.setAlignment(Qt.AlignCenter)

        # Layout
        self.layout.addWidget(self.imagem, 0,0)
        self.layout.addWidget(self.botaoFechar, 1,0)
            
    def rede_neural(self):
        # Remover botoes anteriores
        self.botaoTreinar.deleteLater()
        self.botaoMostrarDadosVazao.deleteLater()

        # Botao fechar
        self.botaoFechar = QtWidgets.QPushButton(self)
        self.botaoFechar.setText("Fechar")
        self.botaoFechar.clicked.connect(self.fechar_redeneural)

        # Imagens
        self.imagemRedeNeural = QLabel("", self)
        self.endereco = QtGui.QPixmap("imagens/espacador.png")
        self.imagemRedeNeural.setPixmap(self.endereco)
        self.imagemRedeNeural.setAlignment(Qt.AlignCenter)

        # Editar dados da rede
        self.editLR = QLineEdit(self)
        self.editLR.setPlaceholderText("Taxa de aprendizado")
        self.editMomentum = QLineEdit(self)
        self.editMomentum.setPlaceholderText("Momentum")
        self.editEpoch = QLineEdit(self)
        self.editEpoch.setPlaceholderText("Épocas")
        self.textLR = QLabel("Taxa de Aprendizado: ", self)
        self.textMomentum = QLabel("Momentum: ", self)
        self.textEpoch = QLabel("Épocas: ", self)
        self.status = QLabel("Treinamento parado", self)
        self.status.setObjectName('status')

        self.botaoTreinarRede = QtWidgets.QPushButton(self)
        self.botaoTreinarRede.setText("Treinar Rede")
        self.botaoTreinarRede.clicked.connect(self.treinamento_da_rede)
        
        # Layout
        self.layout.addWidget(self.editLR, 0, 0)
        self.layout.addWidget(self.editMomentum, 1, 0)
        self.layout.addWidget(self.editEpoch, 2, 0)
        self.layout.addWidget(self.textLR, 3, 0)
        self.layout.addWidget(self.textMomentum, 4, 0)
        self.layout.addWidget(self.textEpoch, 5, 0)
        self.layout.addWidget(self.botaoTreinarRede, 7, 0)
        self.layout.addWidget(self.botaoFechar, 8, 0)
        self.layout.addWidget(self.status, 6, 0)
        self.status.setAlignment(Qt.AlignCenter)

    def fechar_mostrarDados(self):
        self.imagem.deleteLater()
        self.botaoFechar.deleteLater()
        self.menu_principal()

    def fechar_redeneural(self):
        self.editLR.deleteLater()
        self.editMomentum.deleteLater()
        self.editEpoch.deleteLater()
        self.textLR.deleteLater()
        self.textMomentum.deleteLater()
        self.textEpoch.deleteLater()
        self.imagemRedeNeural.deleteLater()
        self.botaoTreinarRede.deleteLater()
        self.botaoFechar.deleteLater()
        self.status.deleteLater()
        self.endereco = QtGui.QPixmap("imagens/espacador.png")
        self.menu_principal()

    def process_finished(self):
        self.p = None

    def treinamento_da_rede(self):
        # Layout
        self.layout.addWidget(self.imagemRedeNeural, 0,0)
        self.imagemRedeNeural.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.editLR, 1, 0)
        self.layout.addWidget(self.editMomentum, 2, 0)
        self.layout.addWidget(self.editEpoch, 3, 0)
        self.layout.addWidget(self.textLR, 1, 2)
        self.layout.addWidget(self.textMomentum, 2, 2)
        self.layout.addWidget(self.textEpoch, 3, 2)
        self.layout.addWidget(self.botaoTreinarRede, 2, 3)
        self.layout.addWidget(self.botaoFechar, 3, 3)
        self.layout.addWidget(self.status, 1, 3)

        if (self.editLR.text() == "" or self.editMomentum.text() == "" or self.editEpoch.text() == ""):
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Critical)
            self.msg.setText("Você precisa colocar todos os parâmetros")
            self.msg.exec_()
        else:
            if (float(self.editLR.text()) >= 1):
                self.msg = QMessageBox()
                self.msg.setIcon(QMessageBox.Critical)
                self.msg.setText("A Taxa de aprendizado tem que ser menor que 0.1!")
                self.msg.exec_()
            else:
                self.textLR.setText("Taxa de Aprendizado: " + self.editLR.text())
            if (float(self.editMomentum.text()) >= 1):
                self.msg = QMessageBox()
                self.msg.setIcon(QMessageBox.Critical)
                self.msg.setText("A Taxa de aprendizado tem que ser menor que 0.1!")
                self.msg.exec_()
            else:
                self.textMomentum.setText("Momentum: " + self.editMomentum.text())
            if (int(self.editEpoch.text()) < 1):
                self.msg = QMessageBox()
                self.msg.setIcon(QMessageBox.Critical)
                self.msg.setText("As épocas devem ser maiores ou igual a 1!")
                self.msg.exec_()
            else:
                self.textEpoch.setText("Épocas: " + self.editEpoch.text())
            if (float(self.editLR.text()) <= 1) and (float(self.editMomentum.text()) <= 1) and(int(self.editEpoch.text()) >= 1):
                self.treinamento = open("treinamento.txt", "w", encoding='utf8')
                self.treinamento.write(f"{self.editLR.text()}\n")
                self.treinamento.write(f"{self.editMomentum.text()}\n")
                self.treinamento.write(f"{self.editEpoch.text()}")
                self.treinamento.close()

            if self.p is None:
                self.script = '.\main.py'
                self.p = QProcess()
                self.p.finished.connect(self.process_finished)
                self.p.start("python", [self.script])
                self.endereco = QtGui.QPixmap("imagens/treinamentoGraficos.png")
                self.imagemRedeNeural.setPixmap(self.endereco)
                self.imagemRedeNeural.setAlignment(Qt.AlignCenter)
                self.status.setText("Treinamento finalizado")


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()