###########################################
__author__ = "ToorajJahangiri"
__email__ = "Toorajjahangiri@gmail.com"
###########################################

# IMPORT
import sys
import os

# IMPORT GUI APPLICATION
from PySide6.QtWidgets import QApplication

# IMPORT UI
from ui_app import *

# ADJUST QT FONT DPI FOR HIGHT SCALE AN 4K MONITOR
os.environ["QT_FONT_DPI"] = "96"


if __name__ == "__main__":
    # APPLICATION
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    # EXEC APP
    raise SystemExit(app.exec())
