import sys
from PyQt6.QtWidgets import *
from scripts import text_to_exel
from scripts import correct_image_file


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.win_sec_exel_clicked = SecondWindowExel()
        self.win_sec_img_file_clicked = SecondWindowImg()

        self.btn = QPushButton('OPAL exel',self)
        self.btn.clicked.connect(self.evt_opal_exel_clicked)


        self.btn2 = QPushButton('Convert img file', self)
        self.btn2.move(0, 50)
        self.btn2.clicked.connect(self.evt_convert_img_file_clicked)

    def evt_opal_exel_clicked(self):
        self.win_sec_exel_clicked.show()

    def evt_convert_img_file_clicked(self):
        self.win_sec_img_file_clicked.show()

class SecondWindowExel(QWidget):
    res_operation = False
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
        res_operation = text_to_exel.main(self.label.text())
        if res_operation == True:
            self.destroy()
class SecondWindowImg(QWidget):
    res_operation = False
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        self.x = QLineEdit()
        self.x.setText("Width")
        self.x.move(0, 510)
        layout.addWidget(self.x)

        self.y = QLineEdit()
        self.x.move(0,50)
        self.y.setText("Height")
        layout.addWidget(self.y)

        self.btn3 = QPushButton('Selekt folder', self)
        self.btn3.clicked.connect(self.evt_convert_clicked)
        layout.addWidget(self.btn3)

        self.setLayout(layout)

    def evt_convert_clicked(self):
        try:
            int(self.y.text())/1
            int(self.x.text())/1
            res = QFileDialog.getExistingDirectory(self, 'Open File', 'C:/')
            res_operation = correct_image_file.main(int(self.x.text()), int(self.y.text()), res)
            if res_operation == True:
                self.destroy()
        except:
            pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = MainWindow()#create main GUI window
    dlgMain.show()#show GUI
    sys.exit(app.exec())