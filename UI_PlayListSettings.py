# Form implementation generated from reading ui file 'assets/PlayListSettings.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_PlayListSettings(object):
    def setupUi(self, PlayListSettings):
        PlayListSettings.setObjectName("PlayListSettings")
        PlayListSettings.resize(780, 430)
        PlayListSettings.setStyleSheet("/*background-color: rgb(42, 42, 42);*/\n"
"\n"
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
"    background-color: rgb(82, 26, 149);\n"
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
"}")
        self.Titlebar_widget = QtWidgets.QWidget(parent=PlayListSettings)
        self.Titlebar_widget.setGeometry(QtCore.QRect(0, 0, 781, 31))
        self.Titlebar_widget.setStyleSheet("background-color: rgb(27, 27, 27);")
        self.Titlebar_widget.setObjectName("Titlebar_widget")
        self.Titlebar_label = QtWidgets.QLabel(parent=self.Titlebar_widget)
        self.Titlebar_label.setGeometry(QtCore.QRect(20, 0, 251, 21))
        self.Titlebar_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.Titlebar_label.setObjectName("Titlebar_label")
        self.PlayList_table = QtWidgets.QTableWidget(parent=PlayListSettings)
        self.PlayList_table.setGeometry(QtCore.QRect(160, 50, 611, 371))
        self.PlayList_table.setStyleSheet("\n"
"/* Vertical Scrollbar */\n"
"QScrollBar:vertical \n"
"{\n"
"    border: 2px solid black;\n"
"    background: black;\n"
"    width: 15px;\n"
"    margin: 22px 0 22px 0;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical \n"
"{\n"
"    background: rgb(30, 30, 30);\n"
"    min-height: 40px;\n"
"    border-radius: 4px; \n"
"}\n"
"\n"
"QScrollBar::add-line:vertical \n"
"{\n"
"    border: 2px solid rgb(30, 30, 30);\n"
"    background: rgb(30, 30, 30);\n"
"    height: 15px;\n"
"    border-radius: 4px; \n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical \n"
"{\n"
"    border: 2px solid rgb(30, 30, 30);\n"
"    background: rgb(30, 30, 30);\n"
"    height: 15px;\n"
"    border-radius: 4px; \n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"/* Horizontal Scrollbar */\n"
"QScrollBar:horizontal \n"
"{\n"
"    border: 2px solid black;\n"
"    background: black;\n"
"    height: 15px;\n"
"    margin: 0 22px 0 22px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal \n"
"{\n"
"    background: rgb(30, 30, 30);\n"
"    min-width: 40px;\n"
"    border-radius: 4px; \n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal \n"
"{\n"
"    border: 2px solid rgb(30, 30, 30);\n"
"    background: rgb(30, 30, 30);\n"
"    width: 15px;\n"
"    border-radius: 4px; \n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal \n"
"{\n"
"    border: 2px solid rgb(30, 30, 30);\n"
"    background: rgb(30, 30, 30);\n"
"    width: 15px;\n"
"    border-radius: 4px; \n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QHeaderView::section \n"
"{\n"
"        color: white;  /* Font color for headers */\n"
"}\n"
"\n"
"QTableWidget::item\n"
"{\n"
"       color: rgb(20, 205, 255); \n"
"}\n"
"\n"
"QTableWidget \n"
"{\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"}\n"
"")
        self.PlayList_table.setAutoScroll(False)
        self.PlayList_table.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.PlayList_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.PlayList_table.setColumnCount(2)
        self.PlayList_table.setObjectName("PlayList_table")
        self.PlayList_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(15)
        item.setFont(font)
        self.PlayList_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(15)
        item.setFont(font)
        self.PlayList_table.setHorizontalHeaderItem(1, item)
        self.PlayList_table.horizontalHeader().setCascadingSectionResizes(False)
        self.PlayList_table.horizontalHeader().setDefaultSectionSize(250)
        self.PlayList_table.horizontalHeader().setSortIndicatorShown(False)
        self.PlayList_table.horizontalHeader().setStretchLastSection(False)
        self.PlayList_table.verticalHeader().setVisible(False)
        self.Edit_button = QtWidgets.QPushButton(parent=PlayListSettings)
        self.Edit_button.setGeometry(QtCore.QRect(10, 50, 141, 41))
        self.Edit_button.setStyleSheet("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/white-edit.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/white-edit-disabled.png"), QtGui.QIcon.Mode.Disabled, QtGui.QIcon.State.Off)
        self.Edit_button.setIcon(icon)
        self.Edit_button.setIconSize(QtCore.QSize(24, 24))
        self.Edit_button.setObjectName("Edit_button")
        self.Back_button = QtWidgets.QPushButton(parent=PlayListSettings)
        self.Back_button.setGeometry(QtCore.QRect(10, 380, 141, 41))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/white-left-arrow.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/white-left-arrow-disabled.png"), QtGui.QIcon.Mode.Disabled, QtGui.QIcon.State.Off)
        self.Back_button.setIcon(icon1)
        self.Back_button.setIconSize(QtCore.QSize(15, 15))
        self.Back_button.setObjectName("Back_button")
        self.Delete_button = QtWidgets.QPushButton(parent=PlayListSettings)
        self.Delete_button.setGeometry(QtCore.QRect(10, 150, 141, 41))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/white-minus.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/white-minus-disabled.png"), QtGui.QIcon.Mode.Disabled, QtGui.QIcon.State.Off)
        self.Delete_button.setIcon(icon2)
        self.Delete_button.setIconSize(QtCore.QSize(24, 24))
        self.Delete_button.setObjectName("Delete_button")
        self.AddNew_button = QtWidgets.QPushButton(parent=PlayListSettings)
        self.AddNew_button.setGeometry(QtCore.QRect(10, 100, 141, 41))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/white-plus-sign.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/white-plus-sign-disabled.png"), QtGui.QIcon.Mode.Disabled, QtGui.QIcon.State.Off)
        self.AddNew_button.setIcon(icon3)
        self.AddNew_button.setIconSize(QtCore.QSize(24, 24))
        self.AddNew_button.setObjectName("AddNew_button")
        self.background_widget = QtWidgets.QWidget(parent=PlayListSettings)
        self.background_widget.setGeometry(QtCore.QRect(0, 30, 801, 421))
        self.background_widget.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.369, y1:0.182, x2:1, y2:1, stop:0 rgba(57, 9, 126, 255), stop:1 rgba(129, 18, 129, 255));")
        self.background_widget.setObjectName("background_widget")
        self.Apply_button = QtWidgets.QPushButton(parent=PlayListSettings)
        self.Apply_button.setGeometry(QtCore.QRect(10, 270, 141, 41))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons/check.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons/check-disabled.png"), QtGui.QIcon.Mode.Disabled, QtGui.QIcon.State.Off)
        self.Apply_button.setIcon(icon4)
        self.Apply_button.setIconSize(QtCore.QSize(18, 18))
        self.Apply_button.setObjectName("Apply_button")
        self.Reorder_button = QtWidgets.QPushButton(parent=PlayListSettings)
        self.Reorder_button.setGeometry(QtCore.QRect(10, 200, 141, 41))
        self.Reorder_button.setStyleSheet("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/icons/reorder.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon5.addPixmap(QtGui.QPixmap(":/icons/icons/reorder-disabled.png"), QtGui.QIcon.Mode.Disabled, QtGui.QIcon.State.Off)
        self.Reorder_button.setIcon(icon5)
        self.Reorder_button.setIconSize(QtCore.QSize(24, 24))
        self.Reorder_button.setObjectName("Reorder_button")
        self.Cancel_button = QtWidgets.QPushButton(parent=PlayListSettings)
        self.Cancel_button.setGeometry(QtCore.QRect(10, 320, 141, 41))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/icons/cancel.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon6.addPixmap(QtGui.QPixmap(":/icons/icons/cancel-disabled.png"), QtGui.QIcon.Mode.Disabled, QtGui.QIcon.State.Off)
        self.Cancel_button.setIcon(icon6)
        self.Cancel_button.setIconSize(QtCore.QSize(18, 18))
        self.Cancel_button.setObjectName("Cancel_button")
        self.background_widget.raise_()
        self.Titlebar_widget.raise_()
        self.PlayList_table.raise_()
        self.Edit_button.raise_()
        self.Back_button.raise_()
        self.Delete_button.raise_()
        self.AddNew_button.raise_()
        self.Apply_button.raise_()
        self.Reorder_button.raise_()
        self.Cancel_button.raise_()

        self.retranslateUi(PlayListSettings)
        QtCore.QMetaObject.connectSlotsByName(PlayListSettings)

    def retranslateUi(self, PlayListSettings):
        _translate = QtCore.QCoreApplication.translate
        PlayListSettings.setWindowTitle(_translate("PlayListSettings", "Form"))
        self.Titlebar_label.setText(_translate("PlayListSettings", "PlayList Settings"))
        item = self.PlayList_table.horizontalHeaderItem(0)
        item.setText(_translate("PlayListSettings", "PlayList Name"))
        item = self.PlayList_table.horizontalHeaderItem(1)
        item.setText(_translate("PlayListSettings", "Source"))
        self.Edit_button.setText(_translate("PlayListSettings", " Edit        "))
        self.Back_button.setText(_translate("PlayListSettings", "  Back     "))
        self.Delete_button.setText(_translate("PlayListSettings", "  Delete       "))
        self.AddNew_button.setText(_translate("PlayListSettings", "Add New       "))
        self.Apply_button.setText(_translate("PlayListSettings", " Apply     "))
        self.Reorder_button.setText(_translate("PlayListSettings", " Reorder    "))
        self.Cancel_button.setText(_translate("PlayListSettings", "  Cancel       "))
