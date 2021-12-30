import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog

from main_window_design import Ui_MainWindow


class MyMainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MyMainWindow, self).__init__()
        self.setupUi(self)

        self.open_test_action.triggered.connect(self.open_file)
        self.statusbar.messageChanged.connect(lambda args: self.status_changed(args))
        # TODO: дописать слоты и связать кнопки с ними

    def status_changed(self, args):
        if not args:
            self.statusBar().setStyleSheet("background-color: #EFEFEF")

    def open_file(self):
        file_name = QFileDialog.getOpenFileName(
            self,
            "выбрать тест",
            "",
            "Excel файл (*.xlsx *.xls)",
        )[0]
        if file_name:
            self.enable()
            self.parse_file(file_name)
            self.statusBar().showMessage("Файл выбран.", 5000)
            self.statusBar().setStyleSheet("background-color: green")
        else:
            self.statusBar().showMessage("Не выбран файл.", 5000)
            self.statusBar().setStyleSheet("background-color: red")

    def enable(self):
        self.question_label.setEnabled(True)
        self.previous_question.setEnabled(True)
        self.next_question.setEnabled(True)
        self.pushButton.setEnabled(True)  # TODO: изменить название объекта через дизайн
        self.answer_line_edit.setEnabled(True)

    def parse_file(self, path):
        # TODO: добавить парсинг Excel файла
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyMainWindow()
    win.show()
    sys.exit(app.exec_())
