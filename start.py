# -*- coding: cp1252 -*-
import sys

import codecs #Evita problemas de compatibilidade de Strings

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog, QMessageBox
from PyQt5.QtGui import QIcon


#Importo a classe principal da minha interface
from editor import Ui_EditorDeTexto

class Start_minhaAplicacao(QMainWindow):
    
    def __init__(self, parent=None):
        
        QWidget.__init__(self, parent)
        # Quando usar para outra interface, mudar o nome da classe
        self.ui = Ui_EditorDeTexto()
        
        self.ui.setupUi(self)

        # Sobrescrevo o ícone (novo ícone)
        self.setWindowIcon(QIcon("img/editor.png"))
        # Sobrescrevo o título (novo título)
        self.setWindowTitle("Meu Editor de Texto")

        # Aqui conectamos os sinais com os slots
        self.ui.btn_AbrirArquivo.clicked.connect(self.abrirArquivo)

        self.ui.btn_Salvar.clicked.connect(self.salvarArquivo)

    def abrirArquivo(self):
        arquivo = QFileDialog.getOpenFileName(self, "Abrir Arquivo", "/home")
        try:    
            #Lê o conteúdo do arquivo e armazena na variável
            textoDoArquivo = codecs.open(arquivo[0], 'r', "cp1252").read()
            #Atribui ao Widget editorDeTexto o conteúdo do arquivo
            self.ui.editorDeTexto.setPlainText(textoDoArquivo)
        except:
            #Atividade pra vocês: Implementem exceções para este caso de uso
            pass
    
    def salvarArquivo(self):
    
        formatos = "Texto (*.txt);; Python (*.py)"
        arquivo = QFileDialog.getSaveFileName(self, "Salvar", "Sem título.txt", formatos)
        
        with open(arquivo[0], 'w') as arq:
            arq.write(self.ui.editorDeTexto.toPlainText())

    
    def closeEvent(self, e):
        pergunta = QMessageBox.question(self, "Editor ZK", "Você realmente deseja sair?", QMessageBox.Yes, QMessageBox.No)
        if pergunta == QMessageBox.No: e.ignore() 

        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    minhaApp = Start_minhaAplicacao()
    minhaApp.show()
    sys.exit(app.exec_())
