import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow, QLabel, QApplication
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QFont

contador = 0
class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initIU()
    
    def initIU(self):
        # Altura e largura
        self.x = 480
        self.y = 270

        # Tamanho mínimo e máximo para a janela
        self.setMinimumSize(QSize(480, 270))
        self.setMaximumSize(QSize(480, 270))

        # Título da janela
        self.setWindowTitle("d) ")

        global contador
        self.textoContador = QLabel("{}".format(contador),self)
        self.textoContador.setAlignment(QtCore.Qt.AlignCenter)
        self.textoContador.setFont(QFont('Consolas', 30))
        self.textoContador.move(self.x / 2 - 50 , self.y / 4)
        
        # Criar botão Somar
        self.botaoSomar = QtWidgets.QPushButton(self)
        self.botaoSomar.setText("Somar")
        self.botaoSomarX = self.x / 4 - 50
        self.botaoSomarY = self.y / 4 + 50
        self.botaoSomar.move(self.botaoSomarX, self.botaoSomarY)
        self.botaoSomar.clicked.connect(self.clicar_botaoSomar)

        # Criar botão Subtrair
        self.botaoSubtrair = QtWidgets.QPushButton(self)
        self.botaoSubtrair.setText("Subtrair")
        self.botaoSubtrairX = self.x / 2 - 50
        self.botaoSubtrairY = self.y / 4 + 50
        self.botaoSubtrair.move(self.botaoSubtrairX, self.botaoSubtrairY)
        self.botaoSubtrair.clicked.connect(self.clicar_botaoSubtrair)

        # Criar botão Zerar
        self.botaoZerar = QtWidgets.QPushButton(self)
        self.botaoZerar.setText("Zerar")
        self.botaoZerarX = self.x / 4 * 3 - 50
        self.botaoZerarY = self.y / 4 + 50
        self.botaoZerar.move(self.botaoZerarX, self.botaoZerarY)
        self.botaoZerar.clicked.connect(self.clicar_botaoZerar)


    # Metodo do botao Somar
    def clicar_botaoSomar(self):
        global contador
        contador += 1
        self.textoContador.setText("{}".format(contador))

    def clicar_botaoSubtrair(self):
        global contador
        contador -= 1
        self.textoContador.setText("{}".format(contador))

    def clicar_botaoZerar(self):
        global contador
        contador = 0
        self.textoContador.setText("{}".format(contador))

def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()