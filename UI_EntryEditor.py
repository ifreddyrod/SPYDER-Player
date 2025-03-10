# Form implementation generated from reading ui file 'assets/EntryEditor.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_EntryEditor(object):
    def setupUi(self, EntryEditor):
        EntryEditor.setObjectName("EntryEditor")
        EntryEditor.resize(780, 430)
        EntryEditor.setStyleSheet("/*background-color: rgb(42, 42, 42);*/\n"
"\n"
"QLabel\n"
"{\n"
"    color: rgb(216, 216, 216);\n"
"}\n"
"\n"
"QPushButton \n"
"{    \n"
"    color: rgb(216, 216, 216);\n"
"    background-color: rgb(0, 0, 0);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover \n"
"{\n"
"    background-color: rgb(35, 11, 63);\n"
"}\n"
"\n"
"QPushButton:disabled\n"
"{\n"
"    color: rgb(73, 73, 73);\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{\n"
"    background-color: rgb(82, 26, 149);\n"
"}\n"
"\n"
"QTableWidget\n"
"{\n"
"    background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QTableWidget::item::selected\n"
"{\n"
"    background-color: rgb(0, 58, 201);\n"
"}\n"
"\n"
"QHeaderView::section\n"
"{\n"
"    background-color: rgb(20, 6, 36);\n"
"}\n"
"\n"
"QHeaderView\n"
"{\n"
"    background-color: rgb(30, 30, 30);\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"    color: rgb(216, 216, 216);\n"
"    background-color: rgb(0, 0, 0);\n"
"    padding-left:10px;\n"
"}\n"
"\n"
"QTextEdit\n"
"{\n"
"    color: rgb(216, 216, 216);\n"
"    background-color: rgb(0, 0, 0);\n"
"    padding-left:25px;\n"
"}\n"
"\n"
"QComboBox\n"
"{\n"
"    color: rgb(216, 216, 216);\n"
"    background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"     border: 1px solid grey;\n"
"     /*background: black;*/\n"
"    selection-color: rgb(216, 216, 216);\n"
"      background-color: rgb(30, 30, 30);\n"
"}\n"
"")
        self.Titlebar_widget = QtWidgets.QWidget(parent=EntryEditor)
        self.Titlebar_widget.setGeometry(QtCore.QRect(0, 0, 781, 31))
        self.Titlebar_widget.setStyleSheet("background-color: rgb(27, 27, 27);")
        self.Titlebar_widget.setObjectName("Titlebar_widget")
        self.Titlebar_label = QtWidgets.QLabel(parent=self.Titlebar_widget)
        self.Titlebar_label.setGeometry(QtCore.QRect(20, 0, 251, 21))
        self.Titlebar_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.Titlebar_label.setObjectName("Titlebar_label")
        self.Back_button = QtWidgets.QPushButton(parent=EntryEditor)
        self.Back_button.setGeometry(QtCore.QRect(10, 380, 141, 41))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/white-left-arrow.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/white-left-arrow-disabled.png"), QtGui.QIcon.Mode.Disabled, QtGui.QIcon.State.Off)
        self.Back_button.setIcon(icon)
        self.Back_button.setIconSize(QtCore.QSize(15, 15))
        self.Back_button.setObjectName("Back_button")
        self.Name_textedit = QtWidgets.QLineEdit(parent=EntryEditor)
        self.Name_textedit.setGeometry(QtCore.QRect(150, 110, 481, 31))
        self.Name_textedit.setStyleSheet("QLineEdit\n"
"{\n"
"    border: 1px solid rgb(30, 30, 30);\n"
"    background-color: black;\n"
"    border-radius: 10px;\n"
"    padding-left: 10px;\n"
"    color: rgb(20, 205, 255); \n"
"}")
        self.Name_textedit.setText("")
        self.Name_textedit.setFrame(False)
        self.Name_textedit.setObjectName("Name_textedit")
        self.EntryName_label = QtWidgets.QLabel(parent=EntryEditor)
        self.EntryName_label.setGeometry(QtCore.QRect(11, 120, 131, 16))
        self.EntryName_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.EntryName_label.setObjectName("EntryName_label")
        self.Save_button = QtWidgets.QPushButton(parent=EntryEditor)
        self.Save_button.setGeometry(QtCore.QRect(630, 380, 141, 41))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/white-diskette.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/white-diskette-disabled.png"), QtGui.QIcon.Mode.Disabled, QtGui.QIcon.State.Off)
        self.Save_button.setIcon(icon1)
        self.Save_button.setIconSize(QtCore.QSize(20, 20))
        self.Save_button.setObjectName("Save_button")
        self.OpenFiles_button = QtWidgets.QPushButton(parent=EntryEditor)
        self.OpenFiles_button.setGeometry(QtCore.QRect(150, 230, 35, 51))
        self.OpenFiles_button.setAutoFillBackground(False)
        self.OpenFiles_button.setStyleSheet("border-radius: 10px;\n"
"/*background-color: rgba(1, 0, 0, 0);*/\n"
"")
        self.OpenFiles_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/white-folder.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/white-folder-disabled.png"), QtGui.QIcon.Mode.Disabled, QtGui.QIcon.State.Off)
        self.OpenFiles_button.setIcon(icon2)
        self.OpenFiles_button.setIconSize(QtCore.QSize(20, 20))
        self.OpenFiles_button.setFlat(False)
        self.OpenFiles_button.setObjectName("OpenFiles_button")
        self.Source_label = QtWidgets.QLabel(parent=EntryEditor)
        self.Source_label.setGeometry(QtCore.QRect(11, 230, 131, 16))
        self.Source_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.Source_label.setObjectName("Source_label")
        self.Source_textedit = QtWidgets.QTextEdit(parent=EntryEditor)
        self.Source_textedit.setGeometry(QtCore.QRect(151, 230, 481, 51))
        self.Source_textedit.setStyleSheet("border-radius: 10px;\n"
"color: rgb(20, 205, 255); \n"
"padding-left: 40px;")
        self.Source_textedit.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.Source_textedit.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.Source_textedit.setLineWrapColumnOrWidth(0)
        self.Source_textedit.setAcceptRichText(False)
        self.Source_textedit.setObjectName("Source_textedit")
        self.SourceType_combobox = QtWidgets.QComboBox(parent=EntryEditor)
        self.SourceType_combobox.setGeometry(QtCore.QRect(151, 170, 120, 30))
        self.SourceType_combobox.setStyleSheet("color: rgb(20, 205, 255); \n"
"")
        self.SourceType_combobox.setObjectName("SourceType_combobox")
        self.SourceType_combobox.addItem("")
        self.SourceType_combobox.addItem("")
        self.SourceType_label = QtWidgets.QLabel(parent=EntryEditor)
        self.SourceType_label.setGeometry(QtCore.QRect(11, 180, 131, 16))
        self.SourceType_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.SourceType_label.setObjectName("SourceType_label")
        self.background_widget = QtWidgets.QWidget(parent=EntryEditor)
        self.background_widget.setGeometry(QtCore.QRect(0, 30, 801, 421))
        self.background_widget.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.369, y1:0.182, x2:1, y2:1, stop:0 rgba(57, 9, 126, 255), stop:1 rgba(129, 18, 129, 255));")
        self.background_widget.setObjectName("background_widget")
        self.background_widget.raise_()
        self.Titlebar_widget.raise_()
        self.Back_button.raise_()
        self.Name_textedit.raise_()
        self.EntryName_label.raise_()
        self.Save_button.raise_()
        self.Source_label.raise_()
        self.SourceType_combobox.raise_()
        self.SourceType_label.raise_()
        self.Source_textedit.raise_()
        self.OpenFiles_button.raise_()

        self.retranslateUi(EntryEditor)
        QtCore.QMetaObject.connectSlotsByName(EntryEditor)

    def retranslateUi(self, EntryEditor):
        _translate = QtCore.QCoreApplication.translate
        EntryEditor.setWindowTitle(_translate("EntryEditor", "Form"))
        self.Titlebar_label.setText(_translate("EntryEditor", "Entry Editor"))
        self.Back_button.setText(_translate("EntryEditor", "  Back     "))
        self.Name_textedit.setPlaceholderText(_translate("EntryEditor", "Name your entry"))
        self.EntryName_label.setText(_translate("EntryEditor", "PlayList Name:"))
        self.Save_button.setText(_translate("EntryEditor", "  Save"))
        self.Source_label.setText(_translate("EntryEditor", "Source:"))
        self.Source_textedit.setPlaceholderText(_translate("EntryEditor", "Paste full link here (https://myplaylistlink.com/list) or select a File in Dialog"))
        self.SourceType_combobox.setItemText(0, _translate("EntryEditor", "file"))
        self.SourceType_combobox.setItemText(1, _translate("EntryEditor", "url"))
        self.SourceType_label.setText(_translate("EntryEditor", "Source Type:"))
