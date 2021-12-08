import sys
import controle
from PyQt5.QtWidgets import QMainWindow, QApplication
from datetime import datetime, timedelta


class ControlePonto(QMainWindow, controle.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.h = 0
        self.m = 0
        self.horas_para_trabalhar = datetime.strptime("00:00:00", '%H:%M:%S')

        self.btn_horas.clicked.connect(self.pega_hora)
        self.btn_minutos.clicked.connect(self.pega_minuto)

        self.entrada.setStyleSheet('background: green;')
        self.saida.setStyleSheet('background: red;')
        self.saida.setDisabled(True)

        self.entrada.clicked.connect(self.hora_entrada)
        self.saida.clicked.connect(self.hora_saida)

    def pega_hora(self):
        self.h = int(self.input_horas.text())
        self.input_horas.setDisabled(True)
        self.horas_para_trabalhar += timedelta(hours=self.h)
        self.qtd_hora_restantes.setText(str(self.horas_para_trabalhar.time()))

    def pega_minuto(self):
        self.m = int(self.input_minutos.text())
        self.input_minutos.setDisabled(True)
        self.horas_para_trabalhar += timedelta(minutes=self.m)
        self.qtd_hora_restantes.setText(str(self.horas_para_trabalhar.time()))

    def botoes(self):
        if self.estado:
            self.entrada.setStyleSheet('background: green;')
            self.saida.setStyleSheet('background: red;')
            self.entrada.setDisabled(False)
            self.saida.setDisabled(True)
        else:
            self.entrada.setStyleSheet('background: red;')
            self.saida.setStyleSheet('background: green;')
            self.saida.setDisabled(False)
            self.entrada.setDisabled(True)

    def hora_entrada(self):
        self.entrou = datetime.now()
        relato = self.entrou.strftime('%d/%m/%Y %H:%M:%S') + ' ENTRADA'
        self.relatorio.setText(relato)
        self.estado = False
        self.botoes()

    def hora_saida(self):
        self.saiu = datetime.now()
        relato = self.saiu.strftime('%d/%m/%Y %H:%M:%S') + ' SAIDA'
        self.relatorio.setText(relato)
        self.estado = True
        self.botoes()
        self.calculo_horas_trabalhadas()

    def calculo_horas_trabalhadas(self):
        tempo_trabalhado = datetime.strptime(self.saiu.strftime('%H:%M:%S'), '%H:%M:%S') - \
            datetime.strptime(self.entrou.strftime('%H:%M:%S'), '%H:%M:%S')
        qtd_nova = (self.horas_para_trabalhar - timedelta(seconds=tempo_trabalhado.seconds)).time()
        self.qtd_hora_restantes.setText(str(qtd_nova))
        self.horas_para_trabalhar -= timedelta(seconds=tempo_trabalhado.seconds)


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    control = ControlePonto()
    control.show()
    qt.exec_()
