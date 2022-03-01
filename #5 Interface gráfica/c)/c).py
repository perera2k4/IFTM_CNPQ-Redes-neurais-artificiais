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
        self.setWindowTitle("c)")

        # Metodo de imagem 1
        self.imagem1 = QLabel(self)
        self.imagem1Endereco = QtGui.QPixmap('Atividade\Imagens\logoIF.ppm')
        self.imagem1.setPixmap(self.imagem1Endereco)
        self.imagem1.setGeometry(self.x / 2 - 100 , self.y / 8 - 100, 350, 350)
        
        # Criar botão
        self.botao1 = QtWidgets.QPushButton(self)
        self.botao1.setText("Clique aqui")
        self.botao1X = self.x / 2 - 50
        self.botao1Y = self.y / 2
        self.botao1.move(self.botao1X, self.botao1Y)
        self.botao1.clicked.connect(self.clicar_botao1)


    # Metodo do botao1
    def clicar_botao1(self):
        self.imagem1Endereco = QtGui.QPixmap('Atividade\Imagens\logoIF.pgm')
        self.imagem1.setPixmap(self.imagem1Endereco)
        

def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()