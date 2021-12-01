from __future__ import annotations
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> #
#           < IN THE NAME OF GOD >           #
# ------------------------------------------ #
__AUTHOR__ = "ToorajJahangiri"
__EMAIL__ = "Toorajjahangiri@gmail.com"
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< #

# IMPORT
import sys
import os

# IMPORT GUI APPLICATION
from ui_app.base_ui import QApplication

# IMPORT UI
from ui_app.main_ui import MainWindow


# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\^////////////////////////////// #


# ADJUST QT FONT DPI FOR HIGHT SCALE AN 4K MONITOR
os.environ["QT_FONT_DPI"] = "96"

def init() -> int:
    if os.path.exists('./__tmp__/'):
        return 0
    else:
        os.mkdir('./__tmp__/')
        return 1

if __name__ == "__main__":
    # CHECK TEMP DIR IF NOT EXISTS CREATE
    init()
    # APPLICATION
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    # EXEC APP
    raise SystemExit(app.exec())
