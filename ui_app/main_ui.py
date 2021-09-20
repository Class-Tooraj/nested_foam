###########################################
__author__ = "ToorajJahangiri"
__email__ = "Toorajjahangiri@gmail.com"
###########################################

# IMPORT STANDARD PACKAGE
import os

# IMPORT UI
from ui_app.base_ui import Ui_MainWindow, QMainWindow, QApplication
from ui_app.raw_input_ui import RawInputPage
from ui_app.file_input_ui import FileInputPage
from ui_app.key_maker_ui import KeyMakerPage


# REMOVE TEMP FILE FROM TEMP DIRE
def remove_temp_file(tmp_dir_path: str, prefix: str = '', suffix: str = '') -> tuple[int, int]:
    _tmp_dir = os.path.realpath(tmp_dir_path)
    _walk = os.walk(_tmp_dir)
    prefix = prefix if prefix not in ('', None) else None
    suffix = suffix if suffix not in ('', None) else None
    _del_file = 0
    _all_file = 0
    for _roots, _, _files in _walk:
        for _file in _files:
            _all_file += 1
            _rm_path = None
            if prefix and suffix:
                if _file.startswith(prefix) and _file.endswith(suffix):
                    _rm_path = os.path.join(_roots, _file)
            elif prefix:
                if _file.startswith(prefix):
                    _rm_path = os.path.join(_roots, _file)
            elif suffix:
                if _file.endswith(suffix):
                    _rm_path = os.path.join(_roots, _file)
            else:
                _rm_path = os.path.join(_roots, _file)
            if _rm_path is not None:
                if os.path.exists(_rm_path):
                    try:
                        os.remove(_rm_path)
                        _del_file += 1
                    except BaseException as err:
                        raise err
    return _del_file, _all_file

# MAIN WINDOW GUI
class MainWindow(QMainWindow, Ui_MainWindow):
    TEMP_DIRECTORY = './__tmp__'

    def __init__(self, parent=None) -> None:
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.TEMP_DIRECTORY = os.path.realpath(self.TEMP_DIRECTORY)
        # Connect Menu Buttons
        self.btn_raw_input.clicked.connect(lambda : self.stackedWidget.setCurrentIndex(0))
        self.btn_file_input.clicked.connect(lambda : self.stackedWidget.setCurrentIndex(1))
        self.btn_key_maker.clicked.connect(lambda : self.stackedWidget.setCurrentIndex(2))
        self.btn_exit.clicked.connect(lambda : self.close())

        # Initialize Page Widgets
        widget_raw_input = RawInputPage()       # Page 1 - Raw Input
        widget_file_input = FileInputPage()     # Page 2 - File Input
        widget_key_maker = KeyMakerPage()       # Page 3 - Key Maker

        # Add Page Widgets To Page Layout
        self.lyt_page_raw.addWidget(widget_raw_input)       # Page 1
        self.lyt_page_file.addWidget(widget_file_input)     # Page 2
        self.lyt_page_key.addWidget(widget_key_maker)       # Page 3

        # Show
        #self.show()

    def closeEvent(self, event: object) -> None:
        # Remove Temp File
        print('REMOVE TEMP FILE BEFORE CLOSING')
        _rm_tmp = remove_temp_file(self.TEMP_DIRECTORY, suffix = '.tmp')
        print(f"DELETED {_rm_tmp[0]} FROM {_rm_tmp[1]}")
        print('... CLOSING ...')
        return super(MainWindow, self).closeEvent(event)


__dir__ = ('MainWindow',)


if __name__ == "__main__":
    import sys
    # APPLICATION
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    # EXEC APP
    raise SystemExit(app.exec())
