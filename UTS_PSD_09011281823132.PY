from PyQt5.QtWidgets import *  # QApplication, QMainWindow, QWidget
import sys
from PyQt5.QtChart import QChart, QChartView, QLineSeries, QValueAxis
from PyQt5.QtCore import *  # QPointF, QRectF
from PyQt5.QtGui import *  # QPainter
from PyQt5.QtCore import *  # Qt

from collections import Counter

from PyQt5 import QtCore, QtGui, QtWidgets


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("09011281823132")
        self.setGeometry(100, 100, 680, 650)

        self.chart = QChart()  # buat chart
        # set posisi dan ukuran (posisiX,posisiY,lebar(width),tinggi(height))
        self.chart.setPlotArea(QRectF(30, 10, 581, 221))

        self.chartview = QChartView(self.chart)

        self.series = QLineSeries(self)
        self.series2 = QLineSeries(self)
        self.chart.addSeries(self.series)
        self.chart.addSeries(self.series2)

        self.styling_axis()

        # checkbox
        self.check = QtWidgets.QCheckBox(self)
        self.check.setGeometry(QtCore.QRect(380, 250, 150, 17))
        self.check.setChecked(True)

        # geser
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(200, 270, 47, 13))
        # scale
        # self.label2 = QtWidgets.QLabel(self)
        # self.label2.setGeometry(QtCore.QRect(200, 290, 47, 13))

        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(270, 270, 81, 20))
        self.lineEdit.setText("0")
        # self.lineEdit2 = QtWidgets.QLineEdit(self)
        # self.lineEdit2.setGeometry(QtCore.QRect(270, 290, 81, 20))
        # self.lineEdit2.setText("2")

        self.lineedittext2 = QtWidgets.QTextEdit(self)
        self.lineedittext2.setGeometry(QtCore.QRect(310, 420, 290, 141))
        self.lineedittext = QtWidgets.QTextEdit(self)
        self.lineedittext.setGeometry(QtCore.QRect(10, 420, 290, 141))

        self.label1 = QtWidgets.QLabel(self)
        self.label1.setGeometry(QtCore.QRect(220, 90, 47, 13))

        # Sinyal 1
        self.button1 = QtWidgets.QPushButton(self)
        self.button1.setGeometry(QtCore.QRect(10, 270, 171, 131))
        self.button1.clicked.connect(lambda: self.sinyal())

        # Geser
        # self.button2 = QtWidgets.QPushButton(self)
        # self.button2.setGeometry(QtCore.QRect(190, 320, 151, 71))
        # self.button2.clicked.connect(lambda: self.ganti_nilai_btn())

        # Bersih chart
        self.button3 = QtWidgets.QPushButton(self)
        self.button3.setGeometry(QtCore.QRect(340, 320, 151, 71))
        self.button3.clicked.connect(lambda: self.clear_all_line())

        self.horizontalSlider = QtWidgets.QSlider(Qt.Horizontal, self)
        self.horizontalSlider.setGeometry(QtCore.QRect(360, 290, 201, 22))
        self.horizontalSlider.setMinimum(-50)
        self.horizontalSlider.setMaximum(50)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setValue(0)
        self.horizontalSlider.valueChanged.connect(
            lambda: self.ganti_nilai())

        self.sinyal()

        self.retranstaleUi()

    def clear_all_line(self):
        self.series.clear()
        self.series2.clear()

    # def ganti_nilai_btn(self):
    #     self.clear_line()
    #     nilai = float(self.lineEdit.text())
        # nilai = float(self.lineEdit2.text())

    #     self.lineEdit.setText(str(nilai))

        # scale = float(self.lineEdit2.text())

    #     y = [None] * 800
    #     t_gs = nilai * 100
    #     m = int(t_gs)
    #     for i in range(len(self.x1)):
    #         c = (self.x1[i]+nilai)/scale
    #         self.a[i] = c
    #     for i in range(len(self.y1)):
    #         c = (self.y1[i]+nilai)/scale
    #         self.b[i] = c
    #     for i in range(len(self.x1)):
    #         self.series2.append(self.a[i], self.y1[i])

    def ganti_nilai(self):
        self.clear_line()
        geser = self.horizontalSlider.value()/10

        self.lineEdit.setText(str(geser))

        for i in range(len(self.x1)):
            c = (3*(self.x1[i])+geser)
            self.a[i] = c
        for i in range(len(self.y1)):
            if(self.check.isChecked()):
                scale = (3*(self.y1[i])+2)
            else:
                scale = 1
            c = (3*(self.y1[i]))/scale
            self.b[i] = c
        for i in range(len(self.x1)):
            self.series2.append(self.a[i], self.b[i])

        self.lineedittext2.setText('''
        x
        '''+str(self.a))
        self.lineedittext.setText('''
        y
        '''+str(self.b))

    def clear_line(self):
        self.series2.clear()

    def styling_axis(self):

        self.x_axis = QValueAxis()
        self.x_axis.setRange(-5, 5)
        # self.x_axis.setTickCount(25)

        self.y_axis = QValueAxis()  # defines the y-axis
        self.y_axis.setRange(0.00, 4)
        # self.y_axis.setTickCount(16)

        self.chart.addAxis(self.x_axis, Qt.AlignBottom)
        self.chart.addAxis(self.y_axis, Qt.AlignLeft)

        self.series.attachAxis(self.x_axis)
        self.series.attachAxis(self.y_axis)
        self.series2.attachAxis(self.x_axis)
        self.series2.attachAxis(self.y_axis)

        self.pen = self.series2.pen()
        self.pen.setBrush(QColor(255, 0, 0))
        self.series2.setPen(self.pen)

        # self.chart.setAnimationOptions(QChart.SeriesAnimations)

        # set legenda jadi terlihat. ubah false jika ingin tidak terlihat
        self.chart.legend().setVisible(False)
        self.chart.legend().setAlignment(Qt.AlignBottom)

        self.chartview.setRenderHint(QPainter.Antialiasing)

        self.setCentralWidget(self.chartview)

    def sinyal(self):
        self.clear_line()
        self.a = [None] * 800
        self.b = [None] * 800
        self.x1 = [None] * 800
        self.y1 = [None] * 800
        for n in range(-400, 400):
            t = n/100
            if t >= -1 and t <= 0:
                self.y1[n] = (t+1)
                self.x1[n] = t
            elif t >= 0 and t <= 1:
                self.y1[n] = (-t+1)
                self.x1[n] = t
            else:
                self.y1[n] = 0
                self.x1[n] = t
            self.series.append(self.x1[n], self.y1[n])

        self.lineedittext2.setText(str(self.x1))
        self.lineedittext.setText(str(self.y1))
        self.lineEdit.setText(str(self.horizontalSlider.value()))

    def retranstaleUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.button1.setText(_translate("MainWindow", "Sinyal"))
        # self.button2.setText(_translate("MainWindow", "Geser"))
        self.button3.setText(_translate("MainWindow", "Bersihkan chart"))
        self.check.setText(_translate("MainWindow", "Gunakan Skala"))
        self.label.setText(_translate("MainWindow", "geser :"))
        # self.label2.setText(_translate("MainWindow", "scale :"))


App = QApplication(sys.argv)
window = Window()
window.__init__()
window.show()
sys.exit(App.exec_())
