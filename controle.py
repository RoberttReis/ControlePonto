# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'controle.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(550, 140)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_minutos = QtWidgets.QPushButton(self.centralwidget)
        self.btn_minutos.setObjectName("btn_minutos")
        self.gridLayout.addWidget(self.btn_minutos, 2, 0, 1, 1)
        self.input_horas = QtWidgets.QLineEdit(self.centralwidget)
        self.input_horas.setObjectName("input_horas")
        self.gridLayout.addWidget(self.input_horas, 1, 1, 1, 1)
        self.btn_horas = QtWidgets.QPushButton(self.centralwidget)
        self.btn_horas.setObjectName("btn_horas")
        self.gridLayout.addWidget(self.btn_horas, 1, 0, 1, 1)
        self.input_minutos = QtWidgets.QLineEdit(self.centralwidget)
        self.input_minutos.setObjectName("input_minutos")
        self.gridLayout.addWidget(self.input_minutos, 2, 1, 1, 1)
        self.entrada = QtWidgets.QPushButton(self.centralwidget)
        self.entrada.setObjectName("entrada")
        self.gridLayout.addWidget(self.entrada, 1, 4, 1, 1)
        self.saida = QtWidgets.QPushButton(self.centralwidget)
        self.saida.setObjectName("saida")
        self.gridLayout.addWidget(self.saida, 3, 4, 1, 1)
        self.relatorio = QtWidgets.QLineEdit(self.centralwidget)
        self.relatorio.setObjectName("relatorio")
        self.gridLayout.addWidget(self.relatorio, 2, 4, 1, 1)
        self.qtd_hora_restantes = QtWidgets.QLineEdit(self.centralwidget)
        self.qtd_hora_restantes.setObjectName("qtd_hora_restantes")
        self.gridLayout.addWidget(self.qtd_hora_restantes, 3, 1, 1, 1)
        self.text_restando = QtWidgets.QLabel(self.centralwidget)
        self.text_restando.setObjectName("text_restando")
        self.gridLayout.addWidget(self.text_restando, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Controle Ponto Robertt"))
        self.btn_minutos.setText(_translate("MainWindow", "Minutos"))
        self.btn_horas.setText(_translate("MainWindow", "Horas"))
        self.entrada.setText(_translate("MainWindow", "Entrada"))
        self.saida.setText(_translate("MainWindow", "Saida"))
        self.text_restando.setText(_translate("MainWindow", "Horas restantes"))
