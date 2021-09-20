###########################################
__author__ = "ToorajJahangiri"
__email__ = "Toorajjahangiri@gmail.com"
###########################################

# IMPORT STANDARD PACKAGE
from typing import Iterable

# IMPORT BACKEND
try:
    from ui_app.backend import key_maker
except ImportError:
    from backend import key_maker

# IMPORT GUI MODULE
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


# BASE WIDGET INITIALIZE
class Ui_Key_Maker(object):
    def setupUi(self, Key_Maker):
        if not Key_Maker.objectName():
            Key_Maker.setObjectName(u"Key_Maker")
        Key_Maker.resize(638, 459)
        Key_Maker.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.verticalLayout = QVBoxLayout(Key_Maker)
        self.verticalLayout.setSpacing(7)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(Key_Maker)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_4.addWidget(self.label_2)

        self.input_chars = QLineEdit(Key_Maker)
        self.input_chars.setObjectName(u"input_chars")
        self.input_chars.setReadOnly(True)

        self.horizontalLayout_4.addWidget(self.input_chars)

        self.cmb_chars = QComboBox(Key_Maker)
        self.cmb_chars.addItem("")
        self.cmb_chars.addItem("")
        self.cmb_chars.setObjectName(u"cmb_chars")
        self.cmb_chars.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_4.addWidget(self.cmb_chars)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_3 = QLabel(Key_Maker)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_5.addWidget(self.label_3)

        self.input_skip = QLineEdit(Key_Maker)
        self.input_skip.setObjectName(u"input_skip")
        self.input_skip.setReadOnly(True)

        self.horizontalLayout_5.addWidget(self.input_skip)

        self.cmb_skip = QComboBox(Key_Maker)
        self.cmb_skip.addItem("")
        self.cmb_skip.addItem("")
        self.cmb_skip.addItem("")
        self.cmb_skip.addItem("")
        self.cmb_skip.addItem("")
        self.cmb_skip.addItem("")
        self.cmb_skip.addItem("")
        self.cmb_skip.addItem("")
        self.cmb_skip.addItem("")
        self.cmb_skip.addItem("")
        self.cmb_skip.setObjectName(u"cmb_skip")
        self.cmb_skip.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_5.addWidget(self.cmb_skip)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.line_3 = QFrame(Key_Maker)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShadow(QFrame.Plain)
        self.line_3.setFrameShape(QFrame.HLine)

        self.verticalLayout.addWidget(self.line_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lbl_start_char = QLabel(Key_Maker)
        self.lbl_start_char.setObjectName(u"lbl_start_char")
        self.lbl_start_char.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.lbl_start_char)

        self.input_start_char = QLineEdit(Key_Maker)
        self.input_start_char.setObjectName(u"input_start_char")
        self.input_start_char.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.input_start_char)

        self.lbl_end_char = QLabel(Key_Maker)
        self.lbl_end_char.setObjectName(u"lbl_end_char")
        self.lbl_end_char.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.lbl_end_char)

        self.input_end_char = QLineEdit(Key_Maker)
        self.input_end_char.setObjectName(u"input_end_char")
        self.input_end_char.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.input_end_char)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.btn_pattern_info = QPushButton(Key_Maker)
        self.btn_pattern_info.setObjectName(u"btn_pattern_info")
        self.btn_pattern_info.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.btn_pattern_info)

        self.cbx_pattern_connect = QCheckBox(Key_Maker)
        self.cbx_pattern_connect.setObjectName(u"cbx_pattern_connect")

        self.horizontalLayout_3.addWidget(self.cbx_pattern_connect)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.line = QFrame(Key_Maker)
        self.line.setObjectName(u"line")
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setFrameShape(QFrame.HLine)

        self.verticalLayout.addWidget(self.line)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_4 = QLabel(Key_Maker)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout.addWidget(self.label_4)

        self.spb_len = QSpinBox(Key_Maker)
        self.spb_len.setObjectName(u"spb_len")
        self.spb_len.setMinimum(1)
        self.spb_len.setMaximum(10000)

        self.horizontalLayout.addWidget(self.spb_len)

        self.label_5 = QLabel(Key_Maker)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout.addWidget(self.label_5)

        self.spb_counter = QSpinBox(Key_Maker)
        self.spb_counter.setObjectName(u"spb_counter")
        self.spb_counter.setMinimum(1)
        self.spb_counter.setMaximum(99999)

        self.horizontalLayout.addWidget(self.spb_counter)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_generate = QPushButton(Key_Maker)
        self.btn_generate.setObjectName(u"btn_generate")

        self.horizontalLayout.addWidget(self.btn_generate)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.line_4 = QFrame(Key_Maker)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShadow(QFrame.Plain)
        self.line_4.setFrameShape(QFrame.HLine)

        self.verticalLayout.addWidget(self.line_4)

        self.label = QLabel(Key_Maker)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.lst_results = QListWidget(Key_Maker)
        self.lst_results.setObjectName(u"lst_results")

        self.verticalLayout.addWidget(self.lst_results)

        self.line_2 = QFrame(Key_Maker)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShadow(QFrame.Plain)
        self.line_2.setFrameShape(QFrame.HLine)

        self.verticalLayout.addWidget(self.line_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_refresh = QPushButton(Key_Maker)
        self.btn_refresh.setObjectName(u"btn_refresh")

        self.horizontalLayout_2.addWidget(self.btn_refresh)

        self.btn_clear_key = QPushButton(Key_Maker)
        self.btn_clear_key.setObjectName(u"btn_clear_key")

        self.horizontalLayout_2.addWidget(self.btn_clear_key)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.cbx_remove_line_number = QCheckBox(Key_Maker)
        self.cbx_remove_line_number.setObjectName(u"cbx_remove_line_number")

        self.horizontalLayout_2.addWidget(self.cbx_remove_line_number)

        self.btn_save = QPushButton(Key_Maker)
        self.btn_save.setObjectName(u"btn_save")

        self.horizontalLayout_2.addWidget(self.btn_save)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Key_Maker)

        QMetaObject.connectSlotsByName(Key_Maker)
    # setupUi

    def retranslateUi(self, Key_Maker):
        Key_Maker.setWindowTitle(QCoreApplication.translate("Key_Maker", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("Key_Maker", u"Char", None))
        self.cmb_chars.setItemText(0, QCoreApplication.translate("Key_Maker", u"ASCII - 32/126", None))
        self.cmb_chars.setItemText(1, QCoreApplication.translate("Key_Maker", u"Custom", None))

        self.label_3.setText(QCoreApplication.translate("Key_Maker", u"Skip ", None))
        self.cmb_skip.setItemText(0, QCoreApplication.translate("Key_Maker", u"None", None))
        self.cmb_skip.setItemText(1, QCoreApplication.translate("Key_Maker", u"Symbol", None))
        self.cmb_skip.setItemText(2, QCoreApplication.translate("Key_Maker", u"Number", None))
        self.cmb_skip.setItemText(3, QCoreApplication.translate("Key_Maker", u"All Alphabet", None))
        self.cmb_skip.setItemText(4, QCoreApplication.translate("Key_Maker", u"Lower Alphabet", None))
        self.cmb_skip.setItemText(5, QCoreApplication.translate("Key_Maker", u"Upper Alphabet", None))
        self.cmb_skip.setItemText(6, QCoreApplication.translate("Key_Maker", u"Symbol + Number", None))
        self.cmb_skip.setItemText(7, QCoreApplication.translate("Key_Maker", u"Alphabet + Number", None))
        self.cmb_skip.setItemText(8, QCoreApplication.translate("Key_Maker", u"Alphabet + Symbol", None))
        self.cmb_skip.setItemText(9, QCoreApplication.translate("Key_Maker", u"Custom", None))

        self.lbl_start_char.setText(QCoreApplication.translate("Key_Maker", u"Starts With", None))
        self.lbl_end_char.setText(QCoreApplication.translate("Key_Maker", u"Ends With", None))
        self.btn_pattern_info.setText(QCoreApplication.translate("Key_Maker", u"Pattern Info", None))
        self.cbx_pattern_connect.setText(QCoreApplication.translate("Key_Maker", u"Connect", None))
        self.label_4.setText(QCoreApplication.translate("Key_Maker", u"Key Length", None))
        self.spb_len.setSpecialValueText(QCoreApplication.translate("Key_Maker", u"32", None))
        self.label_5.setText(QCoreApplication.translate("Key_Maker", u"Counter", None))
        self.spb_counter.setSpecialValueText(QCoreApplication.translate("Key_Maker", u"1", None))
        self.btn_generate.setText(QCoreApplication.translate("Key_Maker", u"Generated", None))
        self.label.setText(QCoreApplication.translate("Key_Maker", u"Generated Key", None))
        self.btn_refresh.setText(QCoreApplication.translate("Key_Maker", u"Refresh", None))
        self.btn_clear_key.setText(QCoreApplication.translate("Key_Maker", u"Clear Key", None))
        self.cbx_remove_line_number.setText(QCoreApplication.translate("Key_Maker", u"Remove Line Number", None))
        self.btn_save.setText(QCoreApplication.translate("Key_Maker", u"Save", None))
    # retranslateUi


# KEY MAKER WIDGET
class KeyMakerPage(QWidget, Ui_Key_Maker):
    ASCII_CHARS = ''.join([chr(i) for i in range(32, 126)])

    def __init__(self, parent=None) -> None:
        super(KeyMakerPage, self).__init__(parent)
        # Setup Base Ui
        self.setupUi(self)
        # Set Character Active
        self.input_chars.setText(self.ASCII_CHARS)
        self.spb_len.setValue(32)
        self.spb_counter.setValue(1)
        # Connect Object
        self.cmb_chars.currentTextChanged.connect(self.chars_set)
        self.cmb_skip.currentTextChanged.connect(self.skip_set)
        self.cbx_pattern_connect.toggled.connect(self.pattern_active)
        self.btn_pattern_info.clicked.connect(self.pattern_info)
        self.btn_generate.clicked.connect(self.generate)
        self.btn_save.clicked.connect(self.save)
        self.btn_clear_key.clicked.connect(lambda: self.lst_results.clear())
        self.btn_refresh.clicked.connect(self.refresh)
        # Show
        #self.show()

    def chars_set(self, txt: str) -> None:
        print(f"CHAR - {txt}")
        if txt == 'Custom':
            self.input_chars.setReadOnly(False)
        else:
            self.input_chars.setReadOnly(True)
            self.input_chars.setText(self.ASCII_CHARS)

    def skip_set(self, txt: str) -> None:
        print(f"SKIP - {txt}")
        _dec = {
            'Symbol': " ()+'\\-_\"?/<>~!@#$%^&*.,[]{}|`:;=",
            'Number': "0123456789",
            'All Alphabet': "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
            'Lower Alphabet': "abcdefghijklmnopqrstuvwxyz",
            'Upper Alphabet': "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        }
        _dec = { **_dec,
            'Symbol + Number': _dec['Symbol'] + _dec['Number'],
            'Alphabet + Number': _dec['All Alphabet'] + _dec['Number'],
            'Alphabet + Symbol': _dec['All Alphabet'] + _dec['Symbol'],
        }

        if txt == 'None':
            self.input_skip.setReadOnly(True)
            self.input_skip.setText('')
        elif txt == 'Custom':
            self.input_skip.setReadOnly(False)
        else:
            self.input_skip.setReadOnly(True)
            self.input_skip.setText(_dec[txt])

    def pattern_active(self, act: bool) -> None:
        self.input_start_char.setEnabled(act)
        self.lbl_start_char.setEnabled(act)

        self.input_end_char.setEnabled(act)
        self.lbl_end_char.setEnabled(act)

        self.btn_pattern_info.setEnabled(act)

    def pattern_info(self) -> None:
        _title = 'Patter Information'
        _msg = """
        Special Chars :

        \\d : All Digit [0-9]
        -
        \\A : Upper Alphabet [A-Z]
        -
        \\a : Lower Alphabet [a-z]
        -
        \\s : All Symbol Except 'Space'
        -


        If Use The Special Chars Must Use " " (One Space) for escaping from The Other Chars

        ---
        Example:
            Withot Special Chars:
                Starts With : 'c#abc' - Ends With : '00*0e'
                result : 'c#abc...00*0e'

            With Special Chars:
                Starts With : '\\A \\d ep' - Ends With : '00> \\a \\a \\s 1010'
                result : 'W3ep...00>ed?1010'
        ---
        """
        _mesage = QMessageBox(self)
        _mesage.setIcon(QMessageBox.Information)
        _mesage.setWindowTitle(_title)
        _mesage.setText(_msg)
        _mesage.setStandardButtons(QMessageBox.Ok)
        return _mesage.exec()

    def generate(self) -> None:
        _listItem = lambda txt: QListWidgetItem(txt, self.lst_results)
        _skip_char = None
        _pattern = None
        _splitter = ' '

        if self.input_skip.text() not in ('', ' '):
            _skip_char = self.input_skip.text()

        if self.cbx_pattern_connect.isChecked():
            _pattern = {'start': None, 'end': None, 'splitter': _splitter}
            if self.input_start_char.text() != '':
                _pattern['start'] = fr"{self.input_start_char.text()}"

            if self.input_end_char.text() != '':
                _pattern['end'] = fr"{self.input_end_char.text()}"

        _values: tuple = (self.spb_len.value(), self.input_chars.text(), _skip_char, _pattern)
        _gen_key: Iterable = (key_maker(*_values) for _ in range(0, self.spb_counter.value()))

        _line = self.lst_results.count()
        for key in _gen_key:
            _tmp = f"{_line}      {key}"
            self.lst_results.addItem(_listItem(_tmp))
            _line += 1

    def save(self) -> None:
        _crow = self.lst_results.count()
        if _crow == 0:
            _title = "Empty Results!"
            _msg = "The Results is Empty.\nPress 'Generate' For Generates Key And Try Again."
            _mesage = QMessageBox(self)
            _mesage.setIcon(QMessageBox.Information)
            _mesage.setWindowTitle(_title)
            _mesage.setText(_msg)
            _mesage.setStandardButtons(QMessageBox.Ok)
            return _mesage.exec()

        _formats = "CSV (*.csv);; All File (*.*)"
        _path_save, _ = QFileDialog.getSaveFileName(self, "Save Results", filter = _formats)
        if _path_save != '':
            try:
                with open(_path_save, 'w') as f:
                    for r in range(0, _crow):
                        _pref = f"{r}      "
                        _pref_length = len(_pref)
                        _tmp = self.lst_results.item(r).text()

                        if self.cbx_remove_line_number.isChecked():
                            _tmp = _tmp[_pref_length :]

                        _tmp += '\n'
                        f.write(_tmp)

            except (IOError, OSError, BaseException, Exception) as err:
                _title = f'{type(err).__name__}'
                _msg = f"{type(err).__name__}\n{err}"
                _mesage = QMessageBox(self)
                _mesage.setIcon(QMessageBox.Critical)
                _mesage.setWindowTitle(_title)
                _mesage.setText(_msg)
                _mesage.setStandardButtons(QMessageBox.Ok)
                return _mesage.exec()

    def refresh(self) -> None:
        self.cmb_chars.setCurrentIndex(0)
        self.input_chars.setText(self.ASCII_CHARS)
        self.input_chars.setEnabled(False)
        self.cmb_skip.setCurrentIndex(0)
        self.input_skip.setText('')
        self.input_skip.setEnabled(False)
        self.input_regex.setText('')
        self.cbx_regex_connect.setChecked(False)
        self.spb_len.setValue(32)
        self.spb_counter.setValue(1)
        self.lst_results.clear()


__dir__ = ('KeyMakerPage',)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    widget = KeyMakerPage()
    window = QDialog(widget)
    widget.show()
    raise SystemExit(app.exec())

