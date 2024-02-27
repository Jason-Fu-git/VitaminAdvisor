import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

import home_ui

if __name__ == '__main__':
    # initialize the app
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = home_ui.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
