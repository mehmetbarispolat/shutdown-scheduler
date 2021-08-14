# import os
import sys

from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon

from UI.main_window import Ui_MainWindow

def main():
    # command = f"shutdown -s -t {time}"
    # os.system(command)
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.shutdownButton.setIcon(QIcon("images/window_icon.png"))
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()