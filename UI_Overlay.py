# Form implementation generated from reading ui file 'assets/Overlay.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Overlay(object):
    def setupUi(self, Overlay):
        Overlay.setObjectName("Overlay")
        Overlay.resize(400, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Overlay.sizePolicy().hasHeightForWidth())
        Overlay.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(Overlay)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Overlay_label = QtWidgets.QLabel(parent=Overlay)
        font = QtGui.QFont()
        font.setKerning(True)
        self.Overlay_label.setFont(font)
        self.Overlay_label.setStyleSheet("QLabel\n"
"{\n"
"    background-color: transparent;\n"
"}")
        self.Overlay_label.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.Overlay_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop)
        self.Overlay_label.setIndent(0)
        self.Overlay_label.setObjectName("Overlay_label")
        self.verticalLayout.addWidget(self.Overlay_label)

        self.retranslateUi(Overlay)
        QtCore.QMetaObject.connectSlotsByName(Overlay)

    def retranslateUi(self, Overlay):
        _translate = QtCore.QCoreApplication.translate
        Overlay.setWindowTitle(_translate("Overlay", "Form"))
        self.Overlay_label.setText(_translate("Overlay", "VideoTitle"))