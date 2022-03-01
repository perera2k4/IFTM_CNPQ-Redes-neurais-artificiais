import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow, QLabel, QApplication
from PyQt5.QtCore import QSize

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initIU()
    
    def initIU(self):
        # Altura e largura
        self.x = 640
        self.y = 480

        # Tamanho mínimo para a janela
        self.setMinimumSize(QSize(640, 480))
        
        # Título da janela
        self.setWindowTitle("b)")

        # Metodo de imagem 1
        self.imagem1 = QLabel(self)
        self.imagem1Endereco = QtGui.QPixmap('Atividade\Imagens\logoIF.ppm')
        self.imagem1.setPixmap(self.imagem1Endereco)
        self.imagem1.setGeometry(self.x / 4 - 50, self.y / 4 , 350, 350)

        # Metodo de imagem 2
        self.imagem2 = QLabel(self)
        self.imagem2Endereco = QtGui.QPixmap('Atividade\Imagens\logoIF.pgm')
        self.imagem2.setPixmap(self.imagem2Endereco)
        self.imagem2.setGeometry(self.x / 2 , self.y / 4, 350, 350)

        # Criar botão 1
        self.botao1 = QtWidgets.QPushButton(self)
        self.botao1.setText("Original")
        self.botao1X = self.x / 4
        self.botao1Y = self.y / 1.25 + 50
        self.botao1.move(self.botao1X, self.botao1Y)
        self.botao1.clicked.connect(self.clicar_botao1)

        # Criar botão 2
        self.botao2 = QtWidgets.QPushButton(self)
        self.botao2.setText("Transformada")
        self.botao2X = self.x / 2 + 50
        self.botao2Y = self.y / 1.25 + 50
        self.botao2.move(self.botao2X, self.botao2Y)
        self.botao2.clicked.connect(self.clicar_botao2)


    # Metodo do botao 1
    def clicar_botao1(self):
        print("Clique imagem .ppm")
        
    # Metodo do botao 2
    def clicar_botao2(self):
        print("Clique imagem .pgm")

def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()