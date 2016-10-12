from PyQt4 import QtGui                                                           # Importa o PyQt para a criação da GUI
from T09_Diagrams import plot_m_diagram                           # Importa o script que calcula os diagramas de momento
import sys                                                  # Importa o sistema, que será usado para fechar o aplicativo


# Classe que define a janela principal
class MainWindow(QtGui.QMainWindow):                                            # Define a janela principal da aplicação
    def __init__(self, parent=None):                                     # Define a função de inicialização da aplicação
        super(MainWindow, self).__init__(parent)                                                              # "Mágica"

        # Define o widget principal à partir da classe MainWidget, que será inserido dentro da janela principal
        mainWidget = MainWidget(self)                                      # Define um widget dentro da janela principal
        self.setCentralWidget(mainWidget)                 # Coloca a widget acima na janela principal na posição central

        # Propriedades da Janela
        self.setGeometry(100, 100, 300, 400)             # (posição linha, posição coluna, tamnho linha, tamanho coluna)
        self.setWindowTitle('CivCom Diagram Calculator')                                    # Título da janela principal
        self.setWindowIcon(QtGui.QIcon('icon_64.png'))                                          # Define ícone da janela

        self.quit_act()                                                        # Chama a função que define o Sair da GUI
        self.about_act()                                                      # Chama a função que define o Sobre da GUI
        self.menu_act()                                                               # Chama a função que define o Menu

        self.show()                                                                             # Torna a janela visível
        # self.showMaximized()                                                                # Abre a janela maximizada
        # self.showFullScreen()                                                            # Abre a janela em tela cheia

    def quit_act(self):
        # Ação de 'Sair'
        self.quitAct = QtGui.QAction('Sair', self)                                            # Define a ação e seu nome
        self.quitAct.setShortcut('Ctrl+Q')                                     # Define um atalho no teclado para a ação
        self.quitAct.setStatusTip('Fecha o programa.')                   # Define a frase da barra de status para a ação
        self.quitAct.triggered.connect(sys.exit)                                     # "O que acontece ao ativar a ação"

    def about_act(self):
        # Pop-up 'Sobre'
        self.aboutmsg = QtGui.QMessageBox()                          # Pop-uo de Mensagem que aparece ao clicar em sobre
        self.aboutmsg.setText('CivCom Diagram Calculator - Versão 0.1')         # Text inicial
        self.aboutmsg.setInformativeText('Esse programa toma as variáveis de uma viga biengastada ' +
                                  'e do carregamento sobre ela e gera os diagramas de momento ' +
                                  'e deflexão da viga')                                             # Texto complementar
        self.aboutmsg.setWindowTitle('CivCom Diagram Calculator')                                     # Título da pop-up
        self.aboutmsg.setIconPixmap(QtGui.QPixmap('logo-90.png'))                                      # Imagem da pop-up

        # Ação 'Sobre' (vide ação 'Sair')
        self.aboutAct = QtGui.QAction('Sobre', self)
        self.aboutAct.setShortcut('F1')
        self.aboutAct.setStatusTip('Mostra as informações do programa')
        self.aboutAct.triggered.connect(self.aboutmsg.exec_)

    def menu_act(self):
        # Menus Principais
        mainMenu = self.menuBar()                                                                # Cria a barra de menus
        fileMenu = mainMenu.addMenu('Arquivo')                                                   # Cria o menu 'Arquivo'
        helpMenu = mainMenu.addMenu('Ajuda')                                                       # Cria o menu 'Ajuda'
        fileMenu.addAction(self.quitAct)                                             # Adiciona 'Sair' ao menu 'Arquivo'
        helpMenu.addAction(self.aboutAct)                                             # Adiciona 'Sobre' ao menu 'Ajuda'
        self.statusBar()                                          # Gera uma barra de status (na parte inferior da tela)


# Classe que define o Widget Principal
class MainWidget(QtGui.QWidget):                                                             # Define o widget principal
    def __init__(self, parent):                                                      # Função de inicialização do widget
        super(MainWidget, self).__init__(parent)                                                               # "Mágica

        # Texto
        self.lbl1 = QtGui.QLabel('Tipo de Carga: ')                                                      # Texto simples

        # Combo Box
        self.dbtn = QtGui.QComboBox(self)                                                   # Botão de seleção de opções
        self.dbtn.addItem('Uniforme')                                                      # Adiciona a opção 'Uniforme'
        self.dbtn.addItem('Concentrada')                                                # Adiciona a opção 'Concentrada'

        # Texto
        self.lbl2 = QtGui.QLabel('Comprimento da Barra (m): ')

        # Line Edit
        self.ledit1 = QtGui.QLineEdit(self)                 # Adiciona uma linha para que o usuário escreva o valor de L
        self.ledit1.setPlaceholderText('Digite o comprimento da barra aqui.')      # "Texto cinza pré-definido na linha"

        # Texto
        self.lbl3 = QtGui.QLabel('Magnitude do Carregamento (kN ou kN/m): ')

        # Line Edit
        self.ledit2 = QtGui.QLineEdit(self)
        self.ledit2.setPlaceholderText('Digite a magnitude do carregamento aqui.')

        # Botão
        self.pshbtn1 = QtGui.QPushButton('Plotar Diagrama', self)                        # Define o botão e o texto nele
        self.pshbtn1.clicked.connect(self.calc_diagram)                                 # Define ação ao apertar o botão

        # Botão
        # self.pshbtn2 = QtGui.QPushButton('Plotar Deflexão', self)
        # self.pshbtn2.clicked.connect(self.calc_deflection)

        # Layout
        grid = QtGui.QGridLayout()                                                               # Define layout em grid
        grid.addWidget(self.lbl1, 1, 1)                                 # Adiciona Texto 1 à posição (linha=1, coluna=1)
        grid.addWidget(self.dbtn, 1, 2)                               # Adiciona Combo Box à posição (linha=1, coluna=2)
        grid.addWidget(self.lbl2, 2, 1)                                                                            # ...
        grid.addWidget(self.ledit1, 2, 2)                                                                          # ...
        grid.addWidget(self.lbl3, 3, 1)                                                                            # ...
        grid.addWidget(self.ledit2, 3, 2)                                                                          # ...
        grid.addWidget(self.pshbtn1, 4, 1, 1, 2)                                                                   # ...
        # grid.addWidget(self.pshbtn2, 4, 2)                                                                       # ...
        self.setLayout(grid)                                    # Define o layout do widget como sendo a variável 'grid'

    # Ação ao apertar o botão 'Plotar Diagrama'
    def calc_diagram(self):
        ltype = self.dbtn.currentText()                                                   # Obtem o tipo de carregamento
        length = float(self.ledit1.text())                                                # Obtem o comprimento da barra
        magnitude = float(self.ledit2.text())                                        # Obtem a magnitude do carregamento
        plot_m_diagram(ltype, length, magnitude)                      # Chama a função para plotar o diagrama de momento

        # Nas duas últimas linhas, utiliza-se o objeto 'Moment' do script 'T09_diagramas' e seu método para plotar
        # o gráfico de momento fletor

    # Ação ao apertar o botão 'Ploatar Deflexão'
    def calc_deflection(self):
        pass


# Define a função principal da GUI
def main():
    app = QtGui.QApplication(sys.argv)                                                                   # Inicia o PyQt
    GUI = MainWindow()                                                             # Inicia a GUI e o loop do aplicativo
    sys.exit(app.exec_())                                                                            # Sai do aplicativo

if __name__ == '__main__':                                             # Só roda a GUI caso ela seja o arquivo principal
    main()                                                                                               # Função da GUI
