# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ConfocalSettingsUI.ui'
#
# Created: Wed Jun 17 21:06:29 2015
#      by: PyQt4 UI code generator 4.9.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_SettingsDialog(object):
    def setupUi(self, SettingsDialog):
        SettingsDialog.setObjectName(_fromUtf8("SettingsDialog"))
        SettingsDialog.resize(309, 366)
        self.gridLayout_2 = QtGui.QGridLayout(SettingsDialog)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_5 = QtGui.QLabel(SettingsDialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)
        self.label_4 = QtGui.QLabel(SettingsDialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.fixed_aspect_xy_checkBox = QtGui.QCheckBox(SettingsDialog)
        self.fixed_aspect_xy_checkBox.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fixed_aspect_xy_checkBox.sizePolicy().hasHeightForWidth())
        self.fixed_aspect_xy_checkBox.setSizePolicy(sizePolicy)
        self.fixed_aspect_xy_checkBox.setMaximumSize(QtCore.QSize(50, 16777215))
        self.fixed_aspect_xy_checkBox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.fixed_aspect_xy_checkBox.setAutoFillBackground(False)
        self.fixed_aspect_xy_checkBox.setText(_fromUtf8(""))
        self.fixed_aspect_xy_checkBox.setChecked(True)
        self.fixed_aspect_xy_checkBox.setProperty("accessibleDescription", _fromUtf8(""))
        self.fixed_aspect_xy_checkBox.setObjectName(_fromUtf8("fixed_aspect_xy_checkBox"))
        self.gridLayout.addWidget(self.fixed_aspect_xy_checkBox, 3, 2, 1, 1)
        self.label_2 = QtGui.QLabel(SettingsDialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.clock_frequency_InputWidget = QtGui.QSpinBox(SettingsDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clock_frequency_InputWidget.sizePolicy().hasHeightForWidth())
        self.clock_frequency_InputWidget.setSizePolicy(sizePolicy)
        self.clock_frequency_InputWidget.setMaximumSize(QtCore.QSize(50, 16777215))
        self.clock_frequency_InputWidget.setMouseTracking(True)
        self.clock_frequency_InputWidget.setAcceptDrops(True)
        self.clock_frequency_InputWidget.setWrapping(False)
        self.clock_frequency_InputWidget.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.clock_frequency_InputWidget.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.clock_frequency_InputWidget.setAccelerated(True)
        self.clock_frequency_InputWidget.setMaximum(1000000)
        self.clock_frequency_InputWidget.setProperty("value", 1000)
        self.clock_frequency_InputWidget.setObjectName(_fromUtf8("clock_frequency_InputWidget"))
        self.gridLayout.addWidget(self.clock_frequency_InputWidget, 0, 2, 1, 1)
        self.label_3 = QtGui.QLabel(SettingsDialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.fixed_aspect_depth_checkBox = QtGui.QCheckBox(SettingsDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fixed_aspect_depth_checkBox.sizePolicy().hasHeightForWidth())
        self.fixed_aspect_depth_checkBox.setSizePolicy(sizePolicy)
        self.fixed_aspect_depth_checkBox.setMaximumSize(QtCore.QSize(50, 16777215))
        self.fixed_aspect_depth_checkBox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.fixed_aspect_depth_checkBox.setText(_fromUtf8(""))
        self.fixed_aspect_depth_checkBox.setChecked(True)
        self.fixed_aspect_depth_checkBox.setObjectName(_fromUtf8("fixed_aspect_depth_checkBox"))
        self.gridLayout.addWidget(self.fixed_aspect_depth_checkBox, 4, 2, 1, 1)
        self.label = QtGui.QLabel(SettingsDialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.slider_stepwidth_InputWidget = QtGui.QDoubleSpinBox(SettingsDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.slider_stepwidth_InputWidget.sizePolicy().hasHeightForWidth())
        self.slider_stepwidth_InputWidget.setSizePolicy(sizePolicy)
        self.slider_stepwidth_InputWidget.setMaximumSize(QtCore.QSize(50, 16777215))
        self.slider_stepwidth_InputWidget.setMouseTracking(True)
        self.slider_stepwidth_InputWidget.setAcceptDrops(True)
        self.slider_stepwidth_InputWidget.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.slider_stepwidth_InputWidget.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
        self.slider_stepwidth_InputWidget.setAccelerated(True)
        self.slider_stepwidth_InputWidget.setDecimals(3)
        self.slider_stepwidth_InputWidget.setSingleStep(0.001)
        self.slider_stepwidth_InputWidget.setProperty("value", 0.001)
        self.slider_stepwidth_InputWidget.setObjectName(_fromUtf8("slider_stepwidth_InputWidget"))
        self.gridLayout.addWidget(self.slider_stepwidth_InputWidget, 5, 2, 1, 1)
        self.return_slowness_InputWidget = QtGui.QSpinBox(SettingsDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.return_slowness_InputWidget.sizePolicy().hasHeightForWidth())
        self.return_slowness_InputWidget.setSizePolicy(sizePolicy)
        self.return_slowness_InputWidget.setMaximumSize(QtCore.QSize(50, 16777215))
        self.return_slowness_InputWidget.setMouseTracking(True)
        self.return_slowness_InputWidget.setAcceptDrops(True)
        self.return_slowness_InputWidget.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.return_slowness_InputWidget.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.return_slowness_InputWidget.setAccelerated(True)
        self.return_slowness_InputWidget.setMaximum(1000)
        self.return_slowness_InputWidget.setProperty("value", 50)
        self.return_slowness_InputWidget.setObjectName(_fromUtf8("return_slowness_InputWidget"))
        self.gridLayout.addWidget(self.return_slowness_InputWidget, 1, 2, 1, 1)
        self.label_9 = QtGui.QLabel(SettingsDialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 6, 0, 1, 1)
        self.savePNG_checkBox = QtGui.QCheckBox(SettingsDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.savePNG_checkBox.sizePolicy().hasHeightForWidth())
        self.savePNG_checkBox.setSizePolicy(sizePolicy)
        self.savePNG_checkBox.setMaximumSize(QtCore.QSize(50, 16777215))
        self.savePNG_checkBox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.savePNG_checkBox.setText(_fromUtf8(""))
        self.savePNG_checkBox.setObjectName(_fromUtf8("savePNG_checkBox"))
        self.gridLayout.addWidget(self.savePNG_checkBox, 6, 2, 1, 1)
        self.save_purePNG_checkBox = QtGui.QCheckBox(SettingsDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save_purePNG_checkBox.sizePolicy().hasHeightForWidth())
        self.save_purePNG_checkBox.setSizePolicy(sizePolicy)
        self.save_purePNG_checkBox.setMaximumSize(QtCore.QSize(50, 16777215))
        self.save_purePNG_checkBox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.save_purePNG_checkBox.setText(_fromUtf8(""))
        self.save_purePNG_checkBox.setChecked(True)
        self.save_purePNG_checkBox.setObjectName(_fromUtf8("save_purePNG_checkBox"))
        self.gridLayout.addWidget(self.save_purePNG_checkBox, 7, 2, 1, 1)
        self.label_10 = QtGui.QLabel(SettingsDialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout.addWidget(self.label_10, 7, 0, 1, 1)
        self.line = QtGui.QFrame(SettingsDialog)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 2, 0, 1, 3)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 1, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(SettingsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Apply|QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout_2.addWidget(self.buttonBox, 2, 1, 1, 1)
        self.hardware_switch = QtGui.QPushButton(SettingsDialog)
        self.hardware_switch.setObjectName(_fromUtf8("hardware_switch"))
        self.gridLayout_2.addWidget(self.hardware_switch, 1, 1, 1, 1)

        self.retranslateUi(SettingsDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), SettingsDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), SettingsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SettingsDialog)
        SettingsDialog.setTabOrder(self.clock_frequency_InputWidget, self.return_slowness_InputWidget)
        SettingsDialog.setTabOrder(self.return_slowness_InputWidget, self.fixed_aspect_xy_checkBox)
        SettingsDialog.setTabOrder(self.fixed_aspect_xy_checkBox, self.fixed_aspect_depth_checkBox)
        SettingsDialog.setTabOrder(self.fixed_aspect_depth_checkBox, self.slider_stepwidth_InputWidget)
        SettingsDialog.setTabOrder(self.slider_stepwidth_InputWidget, self.savePNG_checkBox)
        SettingsDialog.setTabOrder(self.savePNG_checkBox, self.save_purePNG_checkBox)
        SettingsDialog.setTabOrder(self.save_purePNG_checkBox, self.hardware_switch)
        SettingsDialog.setTabOrder(self.hardware_switch, self.buttonBox)

    def retranslateUi(self, SettingsDialog):
        SettingsDialog.setWindowTitle(QtGui.QApplication.translate("SettingsDialog", "qudi: Confocal - Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("SettingsDialog", "Slider Stepwidth with Keys :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("SettingsDialog", "Fixed Aspect Ratio Depth Scan :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("SettingsDialog", "Return slowness :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("SettingsDialog", "Fixed Aspect Ratio XY Scan :", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("SettingsDialog", "Clock frequency :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("SettingsDialog", "Save ImageScene also as png file", None, QtGui.QApplication.UnicodeUTF8))
        self.savePNG_checkBox.setToolTip(QtGui.QApplication.translate("SettingsDialog", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">If you have pressed the save<br>routine in the Menu Bar,<br>with the svg file a png<br>file will be saved.</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("SettingsDialog", "Save pure Image as png", None, QtGui.QApplication.UnicodeUTF8))
        self.hardware_switch.setToolTip(QtGui.QApplication.translate("SettingsDialog", "This kills everything working on the nidaq. So I made this also more resilient to errors and made it come out of its locked state.\n"
"\n"
"Even if if throws numerous errors when trying, you can use everything normally after the hardware reset (just restart the counter twice).\n"
"\n"
"This also means that you should not touch qudi while running diqo since this will try to put the hardware focus back on qudi and will throw even more errors.", None, QtGui.QApplication.UnicodeUTF8))
        self.hardware_switch.setText(QtGui.QApplication.translate("SettingsDialog", "Switch off Hardware", None, QtGui.QApplication.UnicodeUTF8))

