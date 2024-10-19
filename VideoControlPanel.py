# Form implementation generated from reading ui file 'assets/VideoControlPanel.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_VideoControlPanel(object):
    def setupUi(self, VideoControlPanel):
        VideoControlPanel.setObjectName("VideoControlPanel")
        VideoControlPanel.resize(628, 127)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(VideoControlPanel.sizePolicy().hasHeightForWidth())
        VideoControlPanel.setSizePolicy(sizePolicy)
        VideoControlPanel.setFocusPolicy(QtCore.Qt.FocusPolicy.ClickFocus)
        VideoControlPanel.setStyleSheet("QFrame\n"
"{\n"
"    background-color: rgba(0, 0, 0, 128);  /*rgba(0, 0, 0, 150);*/\n"
"    border: 1px solid rgb(128, 128, 128); /*white;*/\n"
"    border-radius: 10px;  \n"
"}\n"
"\n"
"QPushButton \n"
"{\n"
"    /*background-color: transparent;*/\n"
"    color: white;\n"
"    border: 1px solid white;\n"
"    border-radius: 10px;  \n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color: rgb(43, 43, 43);\n"
"}\n"
"\n"
"QPushButton:disabled\n"
"{\n"
"    color: rgb(38, 38, 38);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: rgb(101, 101, 101)\n"
"}\n"
"\n"
"\n"
"\n"
"/*QSlider::groove:horizontal\n"
"{\n"
"    background-color: white;\n"
"        height: 1px;\n"
"        margin: 0px;\n"
"}*/\n"
"\n"
"/*QSlider::handle:horizontal:enabled\n"
"{\n"
"        background-color: white;\n"
"        border: 2px solid white;\n"
"        height: 5px;\n"
"        width: 2px;\n"
"        margin: -5px 0px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:disabled\n"
"{\n"
"        background-color: rgb(128, 128, 128);\n"
"        border: 2px solid rgb(128, 128, 128);;\n"
"        height: 5px;\n"
"        width: 2px;\n"
"        margin: -5px 0px;\n"
"}\n"
"\n"
"QSlider::groove:horizontal:enabled\n"
"{\n"
"        background-color: white;\n"
"        height: 1px;\n"
"        margin: 0px;\n"
"}\n"
"\n"
"QSlider::groove:horizontal:disabled:\n"
"{\n"
"    background-color: rgb(128, 128, 128);\n"
"    height: 1px;\n"
"        margin: 0px;\n"
"}*/\n"
"\n"
"QSlider::groove:horizontal \n"
"{\n"
"    /*border: 1px solid white;*/\n"
"    height: 1px;\n"
"    background: white;\n"
"    margin: 0px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal \n"
"{\n"
"    /*background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);*/\n"
"    background: white;\n"
"    border: 2px solid white;\n"
"        height: 5px;\n"
"        width: 2px;\n"
"        margin: -5px 0px;\n"
"}\n"
"\n"
"QSlider::groove:horizontal:enabled \n"
"{\n"
"    background: white;\n"
"}\n"
"\n"
"QSlider::groove:horizontal:disabled \n"
"{\n"
"    background: rgb(128, 128, 128);\n"
"}\n"
"\n"
"QSlider::handle:horizontal:enabled \n"
"{\n"
"    background: white;\n"
"    border: 2px solid white;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:disabled \n"
"{\n"
"    background: rgb(128, 128, 128);\n"
"    border: 2px solid rgb(128, 128, 128);\n"
"}\n"
"")
        self.verticalLayout = QtWidgets.QVBoxLayout(VideoControlPanel)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.Control_frame = QtWidgets.QFrame(parent=VideoControlPanel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Control_frame.sizePolicy().hasHeightForWidth())
        self.Control_frame.setSizePolicy(sizePolicy)
        self.Control_frame.setMinimumSize(QtCore.QSize(600, 125))
        self.Control_frame.setStyleSheet("")
        self.Control_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.Control_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.Control_frame.setObjectName("Control_frame")
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.Control_frame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(70, 20, 421, 106))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMaximumSize)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Backward_button = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Backward_button.sizePolicy().hasHeightForWidth())
        self.Backward_button.setSizePolicy(sizePolicy)
        self.Backward_button.setMinimumSize(QtCore.QSize(40, 25))
        self.Backward_button.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.Backward_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/previous.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.Backward_button.setIcon(icon)
        self.Backward_button.setObjectName("Backward_button")
        self.gridLayout_2.addWidget(self.Backward_button, 0, 1, 1, 1)
        self.Previous_button = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Previous_button.sizePolicy().hasHeightForWidth())
        self.Previous_button.setSizePolicy(sizePolicy)
        self.Previous_button.setMinimumSize(QtCore.QSize(40, 25))
        self.Previous_button.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.Previous_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/back.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.Previous_button.setIcon(icon1)
        self.Previous_button.setIconSize(QtCore.QSize(14, 14))
        self.Previous_button.setObjectName("Previous_button")
        self.gridLayout_2.addWidget(self.Previous_button, 1, 1, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setHorizontalSpacing(2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.Mute_button = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Mute_button.sizePolicy().hasHeightForWidth())
        self.Mute_button.setSizePolicy(sizePolicy)
        self.Mute_button.setMinimumSize(QtCore.QSize(25, 25))
        self.Mute_button.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.Mute_button.setStyleSheet("border: none;")
        self.Mute_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/mute.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.Mute_button.setIcon(icon2)
        self.Mute_button.setIconSize(QtCore.QSize(20, 20))
        self.Mute_button.setObjectName("Mute_button")
        self.gridLayout_3.addWidget(self.Mute_button, 0, 0, 1, 1)
        self.FullVolume_button = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FullVolume_button.sizePolicy().hasHeightForWidth())
        self.FullVolume_button.setSizePolicy(sizePolicy)
        self.FullVolume_button.setMinimumSize(QtCore.QSize(25, 25))
        self.FullVolume_button.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.FullVolume_button.setStyleSheet("border: none;")
        self.FullVolume_button.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/volume.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.FullVolume_button.setIcon(icon3)
        self.FullVolume_button.setIconSize(QtCore.QSize(20, 20))
        self.FullVolume_button.setObjectName("FullVolume_button")
        self.gridLayout_3.addWidget(self.FullVolume_button, 0, 2, 1, 1)
        self.Volume_slider = QtWidgets.QSlider(parent=self.horizontalLayoutWidget)
        self.Volume_slider.setStyleSheet("color: rgb(255, 255, 255);")
        self.Volume_slider.setMaximum(100)
        self.Volume_slider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.Volume_slider.setObjectName("Volume_slider")
        self.gridLayout_3.addWidget(self.Volume_slider, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_3, 1, 0, 1, 1)
        self.ToggleList_button = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ToggleList_button.sizePolicy().hasHeightForWidth())
        self.ToggleList_button.setSizePolicy(sizePolicy)
        self.ToggleList_button.setMinimumSize(QtCore.QSize(40, 25))
        self.ToggleList_button.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ToggleList_button.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.ToggleList_button.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons/list.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.ToggleList_button.setIcon(icon4)
        self.ToggleList_button.setObjectName("ToggleList_button")
        self.gridLayout_2.addWidget(self.ToggleList_button, 0, 0, 1, 1)
        self.horizontalLayout_3.addLayout(self.gridLayout_2)
        self.Play_button = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Play_button.sizePolicy().hasHeightForWidth())
        self.Play_button.setSizePolicy(sizePolicy)
        self.Play_button.setMinimumSize(QtCore.QSize(70, 70))
        self.Play_button.setFocusPolicy(QtCore.Qt.FocusPolicy.ClickFocus)
        self.Play_button.setStyleSheet("\n"
"border-radius: 35px;  \n"
"")
        self.Play_button.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/icons/play.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.Play_button.setIcon(icon5)
        self.Play_button.setIconSize(QtCore.QSize(32, 32))
        self.Play_button.setObjectName("Play_button")
        self.horizontalLayout_3.addWidget(self.Play_button)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setVerticalSpacing(14)
        self.gridLayout.setObjectName("gridLayout")
        self.Stop_button = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Stop_button.sizePolicy().hasHeightForWidth())
        self.Stop_button.setSizePolicy(sizePolicy)
        self.Stop_button.setMinimumSize(QtCore.QSize(40, 25))
        self.Stop_button.setFocusPolicy(QtCore.Qt.FocusPolicy.ClickFocus)
        self.Stop_button.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/icons/stop.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.Stop_button.setIcon(icon6)
        self.Stop_button.setObjectName("Stop_button")
        self.gridLayout.addWidget(self.Stop_button, 1, 1, 1, 1)
        self.Forward_button = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Forward_button.sizePolicy().hasHeightForWidth())
        self.Forward_button.setSizePolicy(sizePolicy)
        self.Forward_button.setMinimumSize(QtCore.QSize(40, 25))
        self.Forward_button.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.Forward_button.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/icons/forward.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.Forward_button.setIcon(icon7)
        self.Forward_button.setObjectName("Forward_button")
        self.gridLayout.addWidget(self.Forward_button, 0, 0, 1, 1)
        self.Next_button = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Next_button.sizePolicy().hasHeightForWidth())
        self.Next_button.setSizePolicy(sizePolicy)
        self.Next_button.setMinimumSize(QtCore.QSize(40, 25))
        self.Next_button.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.Next_button.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/icons/next.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.Next_button.setIcon(icon8)
        self.Next_button.setIconSize(QtCore.QSize(14, 14))
        self.Next_button.setObjectName("Next_button")
        self.gridLayout.addWidget(self.Next_button, 1, 0, 1, 1)
        self.Last_button = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Last_button.sizePolicy().hasHeightForWidth())
        self.Last_button.setSizePolicy(sizePolicy)
        self.Last_button.setMinimumSize(QtCore.QSize(40, 25))
        self.Last_button.setFocusPolicy(QtCore.Qt.FocusPolicy.ClickFocus)
        self.Last_button.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icons/icons/last.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.Last_button.setIcon(icon9)
        self.Last_button.setIconSize(QtCore.QSize(24, 24))
        self.Last_button.setObjectName("Last_button")
        self.gridLayout.addWidget(self.Last_button, 1, 2, 1, 1)
        self.horizontalLayout_3.addLayout(self.gridLayout)
        self.TotalDuration_label = QtWidgets.QLabel(parent=self.Control_frame)
        self.TotalDuration_label.setGeometry(QtCore.QRect(540, 90, 71, 21))
        self.TotalDuration_label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.TotalDuration_label.setStyleSheet("border: 0px;\n"
"background-color: rgba(255, 255, 255, 0);")
        self.TotalDuration_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.TotalDuration_label.setObjectName("TotalDuration_label")
        self.VideoPosition_slider = QtWidgets.QSlider(parent=self.Control_frame)
        self.VideoPosition_slider.setGeometry(QtCore.QRect(70, 90, 461, 25))
        self.VideoPosition_slider.setMouseTracking(True)
        self.VideoPosition_slider.setMaximum(1000)
        self.VideoPosition_slider.setTracking(True)
        self.VideoPosition_slider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.VideoPosition_slider.setObjectName("VideoPosition_slider")
        self.CurrentTime_label = QtWidgets.QLabel(parent=self.Control_frame)
        self.CurrentTime_label.setGeometry(QtCore.QRect(-10, 90, 71, 21))
        self.CurrentTime_label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.CurrentTime_label.setStyleSheet("border: 0px;\n"
"background-color: rgba(255, 255, 255, 0);")
        self.CurrentTime_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.CurrentTime_label.setObjectName("CurrentTime_label")
        self.horizontalLayout.addWidget(self.Control_frame)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(VideoControlPanel)
        QtCore.QMetaObject.connectSlotsByName(VideoControlPanel)

    def retranslateUi(self, VideoControlPanel):
        _translate = QtCore.QCoreApplication.translate
        VideoControlPanel.setWindowTitle(_translate("VideoControlPanel", "Form"))
        self.TotalDuration_label.setText(_translate("VideoControlPanel", "00:00:00"))
        self.CurrentTime_label.setText(_translate("VideoControlPanel", "00:00:00"))
