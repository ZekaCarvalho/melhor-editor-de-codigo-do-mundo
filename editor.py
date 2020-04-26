# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editor.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EditorDeTexto(object):
    def setupUi(self, EditorDeTexto):
        EditorDeTexto.setObjectName("EditorDeTexto")
        EditorDeTexto.resize(800, 600)
        self.JanelaPrincipal = QtWidgets.QWidget(EditorDeTexto)
        self.JanelaPrincipal.setObjectName("JanelaPrincipal")
        self.btn_Fechar = QtWidgets.QPushButton(self.JanelaPrincipal)
        self.btn_Fechar.setGeometry(QtCore.QRect(710, 10, 71, 61))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/sair.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btn_Fechar.setIcon(icon)
        self.btn_Fechar.setIconSize(QtCore.QSize(40, 40))
        self.btn_Fechar.setObjectName("btn_Fechar")
        self.btn_AbrirArquivo = QtWidgets.QPushButton(self.JanelaPrincipal)
        self.btn_AbrirArquivo.setGeometry(QtCore.QRect(10, 10, 141, 61))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/abrir.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btn_AbrirArquivo.setIcon(icon1)
        self.btn_AbrirArquivo.setIconSize(QtCore.QSize(40, 40))
        self.btn_AbrirArquivo.setObjectName("btn_AbrirArquivo")
        self.editorDeTexto = QtWidgets.QTextEdit(self.JanelaPrincipal)
        self.editorDeTexto.setGeometry(QtCore.QRect(10, 90, 771, 481))
        self.editorDeTexto.setObjectName("editorDeTexto")
        self.btn_Salvar = QtWidgets.QPushButton(self.JanelaPrincipal)
        self.btn_Salvar.setGeometry(QtCore.QRect(160, 10, 141, 61))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("img/salvar.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btn_Salvar.setIcon(icon2)
        self.btn_Salvar.setIconSize(QtCore.QSize(40, 40))
        self.btn_Salvar.setObjectName("btn_Salvar")
        EditorDeTexto.setCentralWidget(self.JanelaPrincipal)
        self.statusbar = QtWidgets.QStatusBar(EditorDeTexto)
        self.statusbar.setObjectName("statusbar")
        EditorDeTexto.setStatusBar(self.statusbar)

        self.retranslateUi(EditorDeTexto)
        self.btn_Fechar.clicked.connect(EditorDeTexto.close)
        QtCore.QMetaObject.connectSlotsByName(EditorDeTexto)

    def retranslateUi(self, EditorDeTexto):
        _translate = QtCore.QCoreApplication.translate
        EditorDeTexto.setWindowTitle(_translate("EditorDeTexto", "MainWindow"))
        self.btn_Fechar.setText(_translate("EditorDeTexto", "Sair"))
        self.btn_AbrirArquivo.setText(_translate("EditorDeTexto", "Abrir Arquivo"))
        self.btn_Salvar.setText(_translate("EditorDeTexto", "Salvar"))
