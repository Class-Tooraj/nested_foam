###########################################
__author__ = "ToorajJahangiri"
__email__ = "Toorajjahangiri@gmail.com"
###########################################

# IMPORT BACKEND
from ui_app.backend import text_cipher, crypto

# IMPORT GUI MODULE
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


# BASE WIDGET INITIALIZE
class Ui_Raw_Input(object):
    def setupUi(self, Raw_Input):
        if not Raw_Input.objectName():
            Raw_Input.setObjectName(u"Raw_Input")
        Raw_Input.resize(638, 459)
        Raw_Input.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.verticalLayout = QVBoxLayout(Raw_Input)
        self.verticalLayout.setSpacing(7)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_3 = QLabel(Raw_Input)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_9.addWidget(self.label_3)

        self.key_input = QLineEdit(Raw_Input)
        self.key_input.setObjectName(u"key_input")
        self.key_input.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.horizontalLayout_9.addWidget(self.key_input)

        self.cmb_cipher_key = QComboBox(Raw_Input)
        self.cmb_cipher_key.addItem("")
        self.cmb_cipher_key.addItem("")
        self.cmb_cipher_key.addItem("")
        self.cmb_cipher_key.addItem("")
        self.cmb_cipher_key.addItem("")
        self.cmb_cipher_key.addItem("")
        self.cmb_cipher_key.addItem("")
        self.cmb_cipher_key.addItem("")
        self.cmb_cipher_key.addItem("")
        self.cmb_cipher_key.addItem("")
        self.cmb_cipher_key.addItem("")
        self.cmb_cipher_key.setObjectName(u"cmb_cipher_key")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmb_cipher_key.sizePolicy().hasHeightForWidth())
        self.cmb_cipher_key.setSizePolicy(sizePolicy)
        self.cmb_cipher_key.setMinimumSize(QSize(115, 0))

        self.horizontalLayout_9.addWidget(self.cmb_cipher_key)

        self.btn_clear_key = QPushButton(Raw_Input)
        self.btn_clear_key.setObjectName(u"btn_clear_key")

        self.horizontalLayout_9.addWidget(self.btn_clear_key)


        self.verticalLayout.addLayout(self.horizontalLayout_9)

        self.line_9 = QFrame(Raw_Input)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShadow(QFrame.Plain)
        self.line_9.setFrameShape(QFrame.HLine)

        self.verticalLayout.addWidget(self.line_9)

        self.label = QLabel(Raw_Input)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.input_text = QPlainTextEdit(Raw_Input)
        self.input_text.setObjectName(u"input_text")
        self.input_text.setFrameShape(QFrame.Box)
        self.input_text.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.input_text)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.cmb_cipher_method = QComboBox(Raw_Input)
        self.cmb_cipher_method.addItem("")
        self.cmb_cipher_method.addItem("")
        self.cmb_cipher_method.addItem("")
        self.cmb_cipher_method.addItem("")
        self.cmb_cipher_method.addItem("")
        self.cmb_cipher_method.addItem("")
        self.cmb_cipher_method.addItem("")
        self.cmb_cipher_method.addItem("")
        self.cmb_cipher_method.addItem("")
        self.cmb_cipher_method.addItem("")
        self.cmb_cipher_method.setObjectName(u"cmb_cipher_method")
        sizePolicy.setHeightForWidth(self.cmb_cipher_method.sizePolicy().hasHeightForWidth())
        self.cmb_cipher_method.setSizePolicy(sizePolicy)
        self.cmb_cipher_method.setMinimumSize(QSize(115, 0))

        self.horizontalLayout_8.addWidget(self.cmb_cipher_method)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_2)

        self.rdb_encode = QRadioButton(Raw_Input)
        self.rdb_encode.setObjectName(u"rdb_encode")

        self.horizontalLayout_8.addWidget(self.rdb_encode)

        self.rdb_decode = QRadioButton(Raw_Input)
        self.rdb_decode.setObjectName(u"rdb_decode")

        self.horizontalLayout_8.addWidget(self.rdb_decode)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.line_7 = QFrame(Raw_Input)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShadow(QFrame.Plain)
        self.line_7.setFrameShape(QFrame.HLine)

        self.verticalLayout.addWidget(self.line_7)

        self.label_2 = QLabel(Raw_Input)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.result_text = QPlainTextEdit(Raw_Input)
        self.result_text.setObjectName(u"result_text")
        self.result_text.setFrameShape(QFrame.Box)
        self.result_text.setFrameShadow(QFrame.Sunken)
        self.result_text.setUndoRedoEnabled(False)
        self.result_text.setReadOnly(True)

        self.verticalLayout.addWidget(self.result_text)

        self.line_8 = QFrame(Raw_Input)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShadow(QFrame.Plain)
        self.line_8.setFrameShape(QFrame.HLine)

        self.verticalLayout.addWidget(self.line_8)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.btn_refresh = QPushButton(Raw_Input)
        self.btn_refresh.setObjectName(u"btn_refresh")

        self.horizontalLayout_7.addWidget(self.btn_refresh)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer)

        self.btn_save = QPushButton(Raw_Input)
        self.btn_save.setObjectName(u"btn_save")

        self.horizontalLayout_7.addWidget(self.btn_save)

        self.btn_generate = QPushButton(Raw_Input)
        self.btn_generate.setObjectName(u"btn_generate")

        self.horizontalLayout_7.addWidget(self.btn_generate)


        self.verticalLayout.addLayout(self.horizontalLayout_7)


        self.retranslateUi(Raw_Input)

        QMetaObject.connectSlotsByName(Raw_Input)
    # setupUi

    def retranslateUi(self, Raw_Input):
        Raw_Input.setWindowTitle(QCoreApplication.translate("Raw_Input", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("Raw_Input", u"Crypto Key :", None))
        self.cmb_cipher_key.setItemText(0, QCoreApplication.translate("Raw_Input", u"None", None))
        self.cmb_cipher_key.setItemText(1, QCoreApplication.translate("Raw_Input", u"b64", None))
        self.cmb_cipher_key.setItemText(2, QCoreApplication.translate("Raw_Input", u"ab64", None))
        self.cmb_cipher_key.setItemText(3, QCoreApplication.translate("Raw_Input", u"mb64", None))
        self.cmb_cipher_key.setItemText(4, QCoreApplication.translate("Raw_Input", u"eb64", None))
        self.cmb_cipher_key.setItemText(5, QCoreApplication.translate("Raw_Input", u"lb64", None))
        self.cmb_cipher_key.setItemText(6, QCoreApplication.translate("Raw_Input", u"rb64", None))
        self.cmb_cipher_key.setItemText(7, QCoreApplication.translate("Raw_Input", u"rab64", None))
        self.cmb_cipher_key.setItemText(8, QCoreApplication.translate("Raw_Input", u"rmb64", None))
        self.cmb_cipher_key.setItemText(9, QCoreApplication.translate("Raw_Input", u"reb64", None))
        self.cmb_cipher_key.setItemText(10, QCoreApplication.translate("Raw_Input", u"rlb64", None))

        self.btn_clear_key.setText(QCoreApplication.translate("Raw_Input", u"Clear", None))
        self.label.setText(QCoreApplication.translate("Raw_Input", u"Input Your Text", None))
        self.cmb_cipher_method.setItemText(0, QCoreApplication.translate("Raw_Input", u"URL Safe Base 64", None))
        self.cmb_cipher_method.setItemText(1, QCoreApplication.translate("Raw_Input", u"ab64", None))
        self.cmb_cipher_method.setItemText(2, QCoreApplication.translate("Raw_Input", u"mb64", None))
        self.cmb_cipher_method.setItemText(3, QCoreApplication.translate("Raw_Input", u"eb64", None))
        self.cmb_cipher_method.setItemText(4, QCoreApplication.translate("Raw_Input", u"lb64", None))
        self.cmb_cipher_method.setItemText(5, QCoreApplication.translate("Raw_Input", u"rb64", None))
        self.cmb_cipher_method.setItemText(6, QCoreApplication.translate("Raw_Input", u"rab64", None))
        self.cmb_cipher_method.setItemText(7, QCoreApplication.translate("Raw_Input", u"rmb64", None))
        self.cmb_cipher_method.setItemText(8, QCoreApplication.translate("Raw_Input", u"reb64", None))
        self.cmb_cipher_method.setItemText(9, QCoreApplication.translate("Raw_Input", u"rlb64", None))

        self.rdb_encode.setText(QCoreApplication.translate("Raw_Input", u"Encode", None))
        self.rdb_decode.setText(QCoreApplication.translate("Raw_Input", u"Decode", None))
        self.label_2.setText(QCoreApplication.translate("Raw_Input", u"Results", None))
        self.btn_refresh.setText(QCoreApplication.translate("Raw_Input", u"Refresh", None))
        self.btn_save.setText(QCoreApplication.translate("Raw_Input", u"Save Results", None))
        self.btn_generate.setText(QCoreApplication.translate("Raw_Input", u"Generate", None))
    # retranslateUi


# RAW INPUT WIDGET
class RawInputPage(QWidget, Ui_Raw_Input):

    def __init__(self, parent=None) -> None:
        super(RawInputPage, self).__init__(parent)
        self.setupUi(self)
        self._cipher_method = 'b64'
        self._key_cipher = None
        self._mode_action = 'encode'
        # Connect Signals
        self.btn_clear_key.clicked.connect(lambda : self.key_input.setText(''))
        self.btn_refresh.clicked.connect(self.refresh)
        self.rdb_encode.toggled.connect(self.encode_set)
        self.rdb_decode.toggled.connect(self.decode_set)
        self.cmb_cipher_method.currentTextChanged.connect(self.method_change)
        self.cmb_cipher_key.currentTextChanged.connect(self.key_cipher_method)
        self.btn_generate.clicked.connect(self.generate)
        self.btn_save.clicked.connect(self.save_result)

        self.rdb_encode.setChecked(True)
        # Show Widget
        #self.show()

    def encode_set(self) -> None:
        self.rdb_decode.setChecked(False)
        self._mode_action = 'encode'

    def decode_set(self) -> None:
        self.rdb_encode.setChecked(False)
        self._mode_action = 'decode'

    def method_change(self, txt: str) -> None:
        if txt == "URL Safe Base 64":
            self._cipher_method = 'b64'
        else:
            self._cipher_method = txt

    def key_cipher_method(self, txt: str) -> None:
        if txt in ('None', None):
            self._key_cipher = None
        else:
            self._key_cipher = txt

    def generate(self) -> None:
        if self.input_text.toPlainText() in ("", " ", None):
            _title = 'Empty Inputs!'
            _msg = "The Input Is Empty !!\nType Your Text Into The Input"
            _mesage = QMessageBox(self)
            _mesage.setIcon(QMessageBox.Information)
            _mesage.setWindowTitle(_title)
            _mesage.setText(_msg)
            _mesage.setStandardButtons(QMessageBox.Ok)
            return _mesage.exec()

        _key_inp = None if self.key_input.text() == '' else self.key_input.text()

        try:
            self.result_text.setPlainText('')

            _nc = text_cipher(
                self._cipher_method,
                self._mode_action,
                self.input_text.toPlainText(),
                _key_inp,
                self._key_cipher,
                )

            self.result_text.setPlainText(_nc)

        except (BaseException, Exception) as err:
            _title = f'{type(err).__name__}'
            _msg = f"{type(err).__name__}\n{err}"
            _mesage = QMessageBox(self)
            _mesage.setIcon(QMessageBox.Critical)
            _mesage.setWindowTitle(_title)
            _mesage.setText(_msg)
            _mesage.setStandardButtons(QMessageBox.Ok)
            return _mesage.exec()

    def save_result(self) -> None:
        if self.result_text.toPlainText() in ("", " ", None):
            _msg = "The Results Is Empty !!\nPress 'Generate' Button For Get Result"
            _title = 'Empty Results Warning'
            _mesage = QMessageBox(self)
            _mesage.setIcon(QMessageBox.Warning)
            _mesage.setWindowTitle(_title)
            _mesage.setText(_msg)
            _mesage.setStandardButtons(QMessageBox.Ok)
            return _mesage.exec()

        _formats = "Text File (*.txt);; All File (*.*)"
        _path_save, _ = QFileDialog.getSaveFileName(self, "Save Results", filter = _formats)
        if _path_save != '':
            try:
                with open(_path_save, 'w') as f:
                    f.write(self.result_text.toPlainText())
                f.close()
            except (IOError, OSError, BaseException, Exception) as err:
                _title = f'{type(err).__name__}'
                _msg = f"{type(err).__name__}\n{err}"
                _mesage = QMessageBox(self)
                _mesage.setIcon(QMessageBox.Critical)
                _mesage.setWindowTitle(_title)
                _mesage.setText(_msg)
                _mesage.setStandardButtons(QMessageBox.Ok)
                return _mesage.exec()
            finally:
                f.close()

    def refresh(self) -> None:
        self.key_input.setText('')
        self.input_text.setPlainText('')
        self.result_text.setPlainText('')
        self.cmb_cipher_method.setCurrentIndex(0)
        self.cmb_cipher_key.setCurrentIndex(0)
        self.rdb_encode.setChecked(True)
        self._cipher_method = 'b64'
        self._mode_action = 'encode'


__dir__ = ('RawInputPage',)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    widget = RawInputPage()
    window = QDialog(widget)
    widget.show()
    raise SystemExit(app.exec())
