###########################################
__author__ = "ToorajJahangiri"
__email__ = "Toorajjahangiri@gmail.com"
###########################################

# IMPORT STANDARD PACKAGE
import os

# IMPORT BACKEND
from ui_app.backend import file_cipher

# IMPORT GUI MODULE
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

# BASE WIDGET INITIALIZE
class Ui_File_Input(object):
    def setupUi(self, File_Input):
        if not File_Input.objectName():
            File_Input.setObjectName(u"File_Input")
        File_Input.resize(638, 459)
        File_Input.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.verticalLayout = QVBoxLayout(File_Input)
        self.verticalLayout.setSpacing(7)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_3 = QLabel(File_Input)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_9.addWidget(self.label_3)

        self.key_input = QLineEdit(File_Input)
        self.key_input.setObjectName(u"key_input")
        self.key_input.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.horizontalLayout_9.addWidget(self.key_input)

        self.cmb_cipher_key = QComboBox(File_Input)
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

        self.btn_clear_key = QPushButton(File_Input)
        self.btn_clear_key.setObjectName(u"btn_clear_key")

        self.horizontalLayout_9.addWidget(self.btn_clear_key)


        self.verticalLayout.addLayout(self.horizontalLayout_9)

        self.line_9 = QFrame(File_Input)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShadow(QFrame.Plain)
        self.line_9.setFrameShape(QFrame.HLine)

        self.verticalLayout.addWidget(self.line_9)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_5 = QLabel(File_Input)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_4.addWidget(self.label_5)

        self.cmb_file_type = QComboBox(File_Input)
        self.cmb_file_type.addItem("")
        self.cmb_file_type.addItem("")
        self.cmb_file_type.setObjectName(u"cmb_file_type")
        self.cmb_file_type.setMinimumSize(QSize(160, 0))

        self.horizontalLayout_4.addWidget(self.cmb_file_type)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(File_Input)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.file_input = QLineEdit(File_Input)
        self.file_input.setObjectName(u"file_input")
        self.file_input.setReadOnly(True)

        self.horizontalLayout.addWidget(self.file_input)

        self.btn_open_file = QPushButton(File_Input)
        self.btn_open_file.setObjectName(u"btn_open_file")

        self.horizontalLayout.addWidget(self.btn_open_file)

        self.btn_clear_input_file = QPushButton(File_Input)
        self.btn_clear_input_file.setObjectName(u"btn_clear_input_file")

        self.horizontalLayout.addWidget(self.btn_clear_input_file)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(File_Input)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.result_save_input = QLineEdit(File_Input)
        self.result_save_input.setObjectName(u"result_save_input")
        self.result_save_input.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.result_save_input)

        self.btn_save = QPushButton(File_Input)
        self.btn_save.setObjectName(u"btn_save")

        self.horizontalLayout_3.addWidget(self.btn_save)

        self.btn_clear_result_file = QPushButton(File_Input)
        self.btn_clear_result_file.setObjectName(u"btn_clear_result_file")

        self.horizontalLayout_3.addWidget(self.btn_clear_result_file)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.cmb_cipher_method = QComboBox(File_Input)
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

        self.rdb_encode = QRadioButton(File_Input)
        self.rdb_encode.setObjectName(u"rdb_encode")

        self.horizontalLayout_8.addWidget(self.rdb_encode)

        self.rdb_decode = QRadioButton(File_Input)
        self.rdb_decode.setObjectName(u"rdb_decode")

        self.horizontalLayout_8.addWidget(self.rdb_decode)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.line_7 = QFrame(File_Input)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShadow(QFrame.Plain)
        self.line_7.setFrameShape(QFrame.HLine)

        self.verticalLayout.addWidget(self.line_7)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.btn_show_results = QPushButton(File_Input)
        self.btn_show_results.setObjectName(u"btn_show_results")

        self.horizontalLayout_7.addWidget(self.btn_show_results)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer)

        self.btn_generate = QPushButton(File_Input)
        self.btn_generate.setObjectName(u"btn_generate")

        self.horizontalLayout_7.addWidget(self.btn_generate)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_2 = QLabel(File_Input)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_5.addWidget(self.label_2)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)

        self.lbl_results_status = QLabel(File_Input)
        self.lbl_results_status.setObjectName(u"lbl_results_status")

        self.horizontalLayout_5.addWidget(self.lbl_results_status)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.result_text = QPlainTextEdit(File_Input)
        self.result_text.setObjectName(u"result_text")
        self.result_text.setFrameShape(QFrame.Box)
        self.result_text.setFrameShadow(QFrame.Sunken)
        self.result_text.setUndoRedoEnabled(False)
        self.result_text.setReadOnly(True)

        self.verticalLayout.addWidget(self.result_text)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_refresh = QPushButton(File_Input)
        self.btn_refresh.setObjectName(u"btn_refresh")

        self.horizontalLayout_2.addWidget(self.btn_refresh)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.btn_clear_results = QPushButton(File_Input)
        self.btn_clear_results.setObjectName(u"btn_clear_results")

        self.horizontalLayout_2.addWidget(self.btn_clear_results)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(File_Input)

        QMetaObject.connectSlotsByName(File_Input)
    # setupUi

    def retranslateUi(self, File_Input):
        File_Input.setWindowTitle(QCoreApplication.translate("File_Input", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("File_Input", u"Crypto Key :", None))
        self.cmb_cipher_key.setItemText(0, QCoreApplication.translate("File_Input", u"None", None))
        self.cmb_cipher_key.setItemText(1, QCoreApplication.translate("File_Input", u"b64", None))
        self.cmb_cipher_key.setItemText(2, QCoreApplication.translate("File_Input", u"ab64", None))
        self.cmb_cipher_key.setItemText(3, QCoreApplication.translate("File_Input", u"mb64", None))
        self.cmb_cipher_key.setItemText(4, QCoreApplication.translate("File_Input", u"eb64", None))
        self.cmb_cipher_key.setItemText(5, QCoreApplication.translate("File_Input", u"lb64", None))
        self.cmb_cipher_key.setItemText(6, QCoreApplication.translate("File_Input", u"rb64", None))
        self.cmb_cipher_key.setItemText(7, QCoreApplication.translate("File_Input", u"rab64", None))
        self.cmb_cipher_key.setItemText(8, QCoreApplication.translate("File_Input", u"rmb64", None))
        self.cmb_cipher_key.setItemText(9, QCoreApplication.translate("File_Input", u"reb64", None))
        self.cmb_cipher_key.setItemText(10, QCoreApplication.translate("File_Input", u"rlb64", None))

        self.btn_clear_key.setText(QCoreApplication.translate("File_Input", u"Clear", None))
        self.label_5.setText(QCoreApplication.translate("File_Input", u"Source File Type :", None))
        self.cmb_file_type.setItemText(0, QCoreApplication.translate("File_Input", u"Text  - Unicode Supports", None))
        self.cmb_file_type.setItemText(1, QCoreApplication.translate("File_Input", u"Binarray - Any Type Of File", None))

        self.label.setText(QCoreApplication.translate("File_Input", u"File Input ", None))
        self.btn_open_file.setText(QCoreApplication.translate("File_Input", u"Open", None))
        self.btn_clear_input_file.setText(QCoreApplication.translate("File_Input", u"Clear", None))
        self.label_4.setText(QCoreApplication.translate("File_Input", u"Result File", None))
        self.btn_save.setText(QCoreApplication.translate("File_Input", u"Save Results", None))
        self.btn_clear_result_file.setText(QCoreApplication.translate("File_Input", u"Clear", None))
        self.cmb_cipher_method.setItemText(0, QCoreApplication.translate("File_Input", u"b64", None))
        self.cmb_cipher_method.setItemText(1, QCoreApplication.translate("File_Input", u"ab64", None))
        self.cmb_cipher_method.setItemText(2, QCoreApplication.translate("File_Input", u"mb64", None))
        self.cmb_cipher_method.setItemText(3, QCoreApplication.translate("File_Input", u"eb64", None))
        self.cmb_cipher_method.setItemText(4, QCoreApplication.translate("File_Input", u"lb64", None))
        self.cmb_cipher_method.setItemText(5, QCoreApplication.translate("File_Input", u"rb64", None))
        self.cmb_cipher_method.setItemText(6, QCoreApplication.translate("File_Input", u"rab64", None))
        self.cmb_cipher_method.setItemText(7, QCoreApplication.translate("File_Input", u"rmb64", None))
        self.cmb_cipher_method.setItemText(8, QCoreApplication.translate("File_Input", u"reb64", None))
        self.cmb_cipher_method.setItemText(9, QCoreApplication.translate("File_Input", u"rlb64", None))

        self.rdb_encode.setText(QCoreApplication.translate("File_Input", u"Encode", None))
        self.rdb_decode.setText(QCoreApplication.translate("File_Input", u"Decode", None))
        self.btn_show_results.setText(QCoreApplication.translate("File_Input", u"Show Results", None))
        self.btn_generate.setText(QCoreApplication.translate("File_Input", u"Generate", None))
        self.label_2.setText(QCoreApplication.translate("File_Input", u"Limited Results", None))
        self.lbl_results_status.setText(QCoreApplication.translate("File_Input", u"", None))
        self.btn_refresh.setText(QCoreApplication.translate("File_Input", u"Refresh", None))
        self.btn_clear_results.setText(QCoreApplication.translate("File_Input", u"Clear Results", None))
    # retranslateUi

# FILE INPUT WIDGET
class FileInputPage(QWidget, Ui_File_Input):

    def __init__(self, parent=None) -> None:
        super(FileInputPage, self).__init__(parent)
        self.setupUi(self)
        self._cipher_method = 'b64'
        self._key_cipher = None
        self._mode_action = 'encode'
        self._file_type = 't'
        self._file_path = None
        self._tmp_path = os.path.realpath('./__tmp__/_file_.tmp')
        self._show_path = None
        # Remove Old Temp File
        if os.path.exists(self._tmp_path):
            os.remove(self._tmp_path)
        # Connect Signals
        self.btn_clear_key.clicked.connect(lambda : self.key_input.setText(''))
        #
        self.cmb_file_type.currentTextChanged.connect(self.file_type_set)
        self.btn_open_file.clicked.connect(self.get_file)
        self.btn_clear_input_file.clicked.connect(lambda : self.file_input.setText(''))
        self.btn_clear_result_file.clicked.connect(lambda : self.result_save_input.setText(''))
        self.btn_show_results.clicked.connect(self.show_results)
        self.btn_clear_results.clicked.connect(lambda : (self.result_text.setPlainText(''), self.lbl_results_status.setText('')))
        #
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
        self._cipher_method = txt

    def key_cipher_method(self, txt: str) -> None:
        if txt in ('None', None):
            self._key_cipher = None
        else:
            self._key_cipher = txt

    def file_type_set(self, txt: str) -> None:
        if 'Text' in txt:
            self._file_type = 't'
        elif 'Binarray' in txt:
            self._file_type = 'b'

    def get_file(self) -> None:
        _formats = "All File (*.*)"
        _path_file, _ = QFileDialog.getOpenFileName(self, "Load File", filter = _formats)
        if _path_file != '':
            self._file_path = _path_file
            self.file_input.setText(self._file_path)

    def show_results(self) -> None:
        if self._file_path is None or self._show_path is None:
            _title = 'Empty Results!'
            _msg = "The File Input Or Results Is Empty !!\nSelect File And Press 'Generate' And Try Again"
            _mesage = QMessageBox(self)
            _mesage.setIcon(QMessageBox.Information)
            _mesage.setWindowTitle(_title)
            _mesage.setText(_msg)
            _mesage.setStandardButtons(QMessageBox.Ok)
            return _mesage.exec()

        if self._show_path:
            _size_file = os.path.getsize(self._show_path)
            try:
                with open(self._show_path, 'r') as f:
                    if _size_file > 50000:
                        _reader = f.read(50000)
                    else:
                        _reader = f.read()
                    self.result_text.setPlainText(_reader)
                    self.lbl_results_status.setText(f"Show Size : '{len(_reader)}'  -  Result Size: '{_size_file}'")
                f.close()
                del _reader, f, _size_file
            except (BaseException, Exception) as err:
                _title = f'{type(err).__name__}'
                _msg = f"{type(err).__name__}\n{err}"
                _mesage = QMessageBox(self)
                _mesage.setIcon(QMessageBox.Critical)
                _mesage.setWindowTitle(_title)
                _mesage.setText(_msg)
                _mesage.setStandardButtons(QMessageBox.Ok)
                return _mesage.exec()

    def generate(self) -> None:
        if self._file_path is None:
            _title = 'File is Empty!'
            _msg = "Select File Before Press 'Generate'"
            _mesage = QMessageBox(self)
            _mesage.setIcon(QMessageBox.Information)
            _mesage.setWindowTitle(_title)
            _mesage.setText(_msg)
            _mesage.setStandardButtons(QMessageBox.Ok)
            return _mesage.exec()

        try:
            self.result_text.setPlainText('')
            file_cipher(
                self._cipher_method,
                self._mode_action,
                (self._file_path, self._file_type),
                self._tmp_path,
                self.key_input.text(),
                self._key_cipher,
            )
            self._show_path = self._tmp_path

            _title = 'Process Is Done'
            _msg = f"File : {self._file_path}\nIs Generated.\nPress 'Save Results' for Save File"
            _mesage = QMessageBox(self)
            _mesage.setIcon(QMessageBox.Information)
            _mesage.setWindowTitle(_title)
            _mesage.setText(_msg)
            _mesage.setStandardButtons(QMessageBox.Ok)
            return _mesage.exec()

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
        if self._show_path is None:
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
                os.replace(self._tmp_path, _path_save)
                self._show_path = None

                if os.path.exists(self._tmp_path):
                    os.remove(self._tmp_path)

                _title = "Saved Results"
                _msg = f"Results Path : {_path_save}\nRemoved Temp File."
                _mesage = QMessageBox(self)
                _mesage.setIcon(QMessageBox.Information)
                _mesage.setWindowTitle(_title)
                _mesage.setText(_msg)
                _mesage.setStandardButtons(QMessageBox.Ok)
                return _mesage.exec()

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
        self.key_input.setText('')
        self.result_text.setPlainText('')
        self.cmb_cipher_key.setCurrentIndex(0)
        self.cmb_cipher_method.setCurrentIndex(0)
        self.cmb_file_type.setCurrentIndex(0)
        self.file_input.setText('')
        self.result_save_input.setText('')
        self.rdb_encode.setChecked(True)
        self._cipher_method = 'b64'
        self._mode_action = 'encode'
        self._file_type = 't'
        self._file_path = None
        self._show_path = None

        if os.path.exists(self._tmp_path):
            os.remove(self._tmp_path)


__dir__ = ('FileInputPage',)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    widget = FileInputPage()
    window = QDialog(widget)
    widget.show()
    raise SystemExit(app.exec())
