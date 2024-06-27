import sys
from PyQt6.QtWidgets import *
from scripts import text_to_exel
from scripts import correct_image_file


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.win_sec_exel_clicked = SecondWindowExel()
        self.win_sec_img_file_clicked = SecondWindowImg()

        self.resize(300, 300)

        self.btn = QPushButton('OPAL exel',self)
        self.btn.move(120, 100)
        self.btn.clicked.connect(self.evt_opal_exel_clicked)


        self.btn2 = QPushButton('Convert img file', self)
        self.btn2.move(120, 150)
        self.btn2.clicked.connect(self.evt_convert_img_file_clicked)

    def evt_opal_exel_clicked(self):
        self.win_sec_exel_clicked.show()
        pass
    def evt_convert_img_file_clicked(self):
        self.win_sec_img_file_clicked.show()

class SecondWindowExel(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        self.label = QLineEdit()
        self.label.setText("Text")
        layout.addWidget(self.label)

        self.btn3 = QPushButton('Convert', self)
        self.btn3.clicked.connect(self.evt_convert_clicked)
        layout.addWidget(self.btn3)

        self.setLayout(layout)
    def evt_convert_clicked(self):
        text_to_exel.main(self.label.text())

class SecondWindowImg(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        self.x = QLineEdit()
        self.x.setText("Set x")
        layout.addWidget(self.x)

        self.y = QLineEdit()
        self.y.setText("Set y")
        layout.addWidget(self.y)


        self.btn3 = QPushButton('Selekt folder', self)
        self.btn3.clicked.connect(self.evt_convert_clicked)
        layout.addWidget(self.btn3)

        self.setLayout(layout)

    def evt_convert_clicked(self):
        res = QFileDialog.getExistingDirectory(self, 'Open File', 'C:/')
        #correct_image_file.test(self.label.text())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = MainWindow()#create main GUI window
    dlgMain.show()#show GUI
    sys.exit(app.exec())