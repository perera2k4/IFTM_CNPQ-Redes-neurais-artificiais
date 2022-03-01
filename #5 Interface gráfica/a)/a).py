import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow, QLabel, QApplication
from PyQt5.QtCore import QSize

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initIU()
    
    def initIU(self):
        # textoAltura e textoLargura
        self.x = 640
        self.y = 480

        # Tamanho mínimo para a janela
        self.setMinimumSize(QSize(640, 480))
        
        # Título da janela
        self.setWindowTitle("a)")

        # Texto dentro da janela
        self.texto = QLabel("REDES NEURAIS ARTIFICIAIS E SUAS APLICAÇÕES PRÁTICAS: UM ESTUDO COM ESTUDANTES DO ENSINO MÉDIO", self)
        self.texto.adjustSize()
        self.textoLargura = self.texto.frameGeometry().width()
        self.textoAltura = self.texto.frameGeometry().height()
        self.texto.setAlignment(QtCore.Qt.AlignCenter)
        self.texto.move(self.x / 2 - self.textoLargura / 2 , self.y / 4 - self.textoAltura / 2)
        
        # Criar botão
        self.botao1 = QtWidgets.QPushButton(self)
        self.botao1.setText("Clique aqui")
        self.botao1X = self.x / 2 - 50
        self.botao1Y = self.y / 4 - self.textoAltura / 2 + 50
        self.botao1.move(self.botao1X, self.botao1Y)
        self.botao1.clicked.connect(self.clicar_botao1)

    # Metodo do botao1
    def clicar_botao1(self):
        self.texto.setText("BRUNO PEREIRA CARVALHO")
        self.texto.adjustSize()
        self.textoLargura = self.texto.frameGeometry().width()
        self.textoAltura = self.texto.frameGeometry().height()
        self.texto.setAlignment(QtCore.Qt.AlignCenter)
        self.texto.move(self.x / 2 - self.textoLargura / 2 , self.y / 4 - self.textoAltura / 2)
        

def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()