import os
import sys
import subprocess
from PyQt5 import QtCore, QtWidgets, QtGui


#
# Create default font setting
#
if '.font_settings.dat' not in os.listdir(os.getcwd()):
    default_font = open('%s/.font_settings.dat'%(os.getcwd()),'a+')
    default_font.write('font_size = 7')
    default_font.close()

def font_size():
	font_settings = open('%s/.font_settings.dat'%(os.getcwd()),'r+')
	font_init = font_settings.read()
	return int(font_init.split()[2])

font_setting = font_size()

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(619, 623)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("%s/resources/icon.png"%(os.getcwd()))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.verticalLayout_30 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_30.setObjectName(_fromUtf8("verticalLayout_30"))
        self.verticalLayout_29 = QtWidgets.QVBoxLayout()
        self.verticalLayout_29.setSpacing(6)
        self.verticalLayout_29.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_29.setObjectName(_fromUtf8("verticalLayout_29"))
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.verticalLayout_28 = QtWidgets.QVBoxLayout()
        self.verticalLayout_28.setObjectName(_fromUtf8("verticalLayout_28"))
        self.verticalLayout_26 = QtWidgets.QVBoxLayout()
        self.verticalLayout_26.setObjectName(_fromUtf8("verticalLayout_26"))
        self.label_14 = QtWidgets.QLabel(Dialog)
        self.label_14.setText(_fromUtf8(""))
        self.label_14.setPixmap(QtGui.QPixmap(_fromUtf8("%s/resources/splash.png"%(os.getcwd()))))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.verticalLayout_26.addWidget(self.label_14)
        spacerItem = QtWidgets.QSpacerItem(20, 17, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_26.addItem(spacerItem)
        self.verticalLayout_24 = QtWidgets.QVBoxLayout()
        self.verticalLayout_24.setObjectName(_fromUtf8("verticalLayout_24"))
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem1 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.update_label = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.update_label.sizePolicy().hasHeightForWidth())
        self.update_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(font_setting)
        self.update_label.setFont(font)
        self.update_label.setObjectName(_fromUtf8("update_label"))
        self.horizontalLayout_3.addWidget(self.update_label)
        self.verticalLayout_24.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem2 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout_22 = QtWidgets.QVBoxLayout()
        self.verticalLayout_22.setObjectName(_fromUtf8("verticalLayout_22"))
        self.update_button = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.update_button.sizePolicy().hasHeightForWidth())
        self.update_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(font_setting)
        self.update_button.setFont(font)
        self.update_button.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("%s/resources/1295008956_system-software-update.png"%(os.getcwd()))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.update_button.setIcon(icon1)
        self.update_button.setIconSize(QtCore.QSize(35, 34))
        self.update_button.setObjectName(_fromUtf8("update_button"))
        self.verticalLayout_22.addWidget(self.update_button)
        spacerItem3 = QtWidgets.QSpacerItem(13, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_22.addItem(spacerItem3)
        self.horizontalLayout.addLayout(self.verticalLayout_22)
        spacerItem4 = QtWidgets.QSpacerItem(13, 74, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout.addItem(spacerItem4)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        spacerItem5 = QtWidgets.QSpacerItem(124, 12, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.verticalLayout_24.addLayout(self.horizontalLayout_2)
        self.verticalLayout_26.addLayout(self.verticalLayout_24)
        self.verticalLayout_28.addLayout(self.verticalLayout_26)
        self.verticalLayout_23 = QtWidgets.QVBoxLayout()
        self.verticalLayout_23.setObjectName(_fromUtf8("verticalLayout_23"))
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        spacerItem6 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem6)
        self.verticalLayout_21 = QtWidgets.QVBoxLayout()
        self.verticalLayout_21.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_21.setObjectName(_fromUtf8("verticalLayout_21"))
        self.py_version_label = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.py_version_label.sizePolicy().hasHeightForWidth())
        self.py_version_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(font_setting)
        self.py_version_label.setFont(font)
        self.py_version_label.setObjectName(_fromUtf8("py_version_label"))
        self.verticalLayout_21.addWidget(self.py_version_label)
        self.air_version = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.air_version.sizePolicy().hasHeightForWidth())
        self.air_version.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(font_setting)
        self.air_version.setFont(font)
        self.air_version.setObjectName(_fromUtf8("air_version"))
        self.verticalLayout_21.addWidget(self.air_version)
        self.qt_version = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qt_version.sizePolicy().hasHeightForWidth())
        self.qt_version.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(font_setting)
        self.qt_version.setFont(font)
        self.qt_version.setObjectName(_fromUtf8("qt_version"))
        self.verticalLayout_21.addWidget(self.qt_version)
        self.horizontalLayout_6.addLayout(self.verticalLayout_21)
        self.verticalLayout_23.addLayout(self.horizontalLayout_6)
        spacerItem7 = QtWidgets.QSpacerItem(20, 37, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_23.addItem(spacerItem7)
        self.verticalLayout_28.addLayout(self.verticalLayout_23)
        self.horizontalLayout_7.addLayout(self.verticalLayout_28)
        self.verticalLayout_25 = QtWidgets.QVBoxLayout()
        self.verticalLayout_25.setObjectName(_fromUtf8("verticalLayout_25"))
        self.verticalLayout_27 = QtWidgets.QVBoxLayout()
        self.verticalLayout_27.setObjectName(_fromUtf8("verticalLayout_27"))
        self.verticalLayout_20 = QtWidgets.QVBoxLayout()
        self.verticalLayout_20.setSpacing(6)
        self.verticalLayout_20.setObjectName(_fromUtf8("verticalLayout_20"))
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.loading_label = QtWidgets.QLabel(Dialog)
        self.loading_label.setEnabled(True)
        self.loading_label.setText(_fromUtf8(""))
        self.loading_label.setPixmap(QtGui.QPixmap(_fromUtf8("%s/resources/loading.gif"%(os.getcwd()))))
        self.loading_label.setObjectName(_fromUtf8("loading_label"))
        self.horizontalLayout_5.addWidget(self.loading_label)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        spacerItem8 = QtWidgets.QSpacerItem(166, 3, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_9.addItem(spacerItem8)
        self.interface_combo = QtWidgets.QComboBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.interface_combo.sizePolicy().hasHeightForWidth())
        self.interface_combo.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(font_setting)
        self.interface_combo.setFont(font)
        self.interface_combo.setObjectName(_fromUtf8("interface_combo"))
        self.verticalLayout_9.addWidget(self.interface_combo)
        self.horizontalLayout_5.addLayout(self.verticalLayout_9)
        spacerItem9 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem9)
        self.verticalLayout_18 = QtWidgets.QVBoxLayout()
        self.verticalLayout_18.setObjectName(_fromUtf8("verticalLayout_18"))
        spacerItem10 = QtWidgets.QSpacerItem(85, 3, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_18.addItem(spacerItem10)
        self.refresh_intfacebutton = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.refresh_intfacebutton.sizePolicy().hasHeightForWidth())
        self.refresh_intfacebutton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(font_setting)
        self.refresh_intfacebutton.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("%s/resources/PNG-Refresh.png-256x256.png"%(os.getcwd()))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.refresh_intfacebutton.setIcon(icon2)
        self.refresh_intfacebutton.setIconSize(QtCore.QSize(24, 23))
        self.refresh_intfacebutton.setObjectName(_fromUtf8("refresh_intfacebutton"))
        self.verticalLayout_18.addWidget(self.refresh_intfacebutton)
        self.horizontalLayout_5.addLayout(self.verticalLayout_18)
        spacerItem11 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem11)
        spacerItem12 = QtWidgets.QSpacerItem(13, 36, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout_5.addItem(spacerItem12)
        self.verticalLayout_20.addLayout(self.horizontalLayout_5)
        self.mon_label = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mon_label.sizePolicy().hasHeightForWidth())
        self.mon_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(font_setting)
        self.mon_label.setFont(font)
        self.mon_label.setObjectName(_fromUtf8("mon_label"))
        self.verticalLayout_20.addWidget(self.mon_label)
        self.verticalLayout_27.addLayout(self.verticalLayout_20)
        self.verticalLayout_19 = QtWidgets.QVBoxLayout()
        self.verticalLayout_19.setObjectName(_fromUtf8("verticalLayout_19"))
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        spacerItem13 = QtWidgets.QSpacerItem(168, 2, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_8.addItem(spacerItem13)
        self.scan_button = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scan_button.sizePolicy().hasHeightForWidth())
        self.scan_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(font_setting)
        self.scan_button.setFont(font)
        self.scan_button.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("%s/resources/radio-wireless-signal-icone-5919-128.png"%(os.getcwd()))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.scan_button.setIcon(icon3)
        self.scan_button.setIconSize(QtCore.QSize(40, 42))
        self.scan_button.setObjectName(_fromUtf8("scan_button"))
        self.verticalLayout_8.addWidget(self.scan_button)
        self.horizontalLayout_4.addLayout(self.verticalLayout_8)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        spacerItem14 = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem14)
        spacerItem15 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem15)
        self.label_7 = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(font_setting)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout.addWidget(self.label_7)
        spacerItem16 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem16)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_19.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        spacerItem17 = QtWidgets.QSpacerItem(168, 2, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_10.addItem(spacerItem17)
        self.wep_button = QtWidgets.QPushButton(Dialog)
        self.wep_button.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wep_button.sizePolicy().hasHeightForWidth())
        self.wep_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(font_setting)
        font.setBold(True)
        font.setWeight(75)
        self.wep_button.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("%s/resources/wifi_2.png"%(os.getcwd()))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.wep_button.setIcon(icon4)
        self.wep_button.setIconSize(QtCore.QSize(67, 62))
        self.wep_button.setObjectName(_fromUtf8("wep_button"))
        self.verticalLayout_10.addWidget(self.wep_button)
        self.horizontalLayout_8.addLayout(self.verticalLayout_10)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        spacerItem18 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem18)
        self.wep_clientlabel = QtWidgets.QLabel(Dialog)
        self.wep_clientlabel.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(font_setting)
        self.wep_clientlabel.setFont(font)
        self.wep_clientlabel.setObjectName(_fromUtf8("wep_clientlabel"))
        self.verticalLayout_2.addWidget(self.wep_clientlabel)
        spacerItem19 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem19)
        self.verticalLayout_11.addLayout(self.verticalLayout_2)
        self.horizontalLayout_8.addLayout(self.verticalLayout_11)
        self.verticalLayout_19.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName(_fromUtf8("verticalLayout_12"))
        spacerItem20 = QtWidgets.QSpacerItem(168, 2, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_12.addItem(spacerItem20)
        self.wpa_button = QtWidgets.QPushButton(Dialog)
        self.wpa_button.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wpa_button.sizePolicy().hasHeightForWidth())
        self.wpa_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(font_setting)
        font.setBold(True)
        font.setWeight(75)
        self.wpa_button.setFont(font)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8("%s/resources/wifi_6.png"%(os.getcwd()))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.wpa_button.setIcon(icon5)
        self.wpa_button.setIconSize(QtCore.QSize(67, 62))
        self.wpa_button.setObjectName(_fromUtf8("wpa_button"))
        self.verticalLayout_12.addWidget(self.wpa_button)
        self.horizontalLayout_9.addLayout(self.verticalLayout_12)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName(_fromUtf8("verticalLayout_13"))
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        spacerItem21 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem21)
        self.wpa_clientlabel = QtWidgets.QLabel(Dialog)
        self.wpa_clientlabel.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(font_setting)
        self.wpa_clientlabel.setFont(font)
        self.wpa_clientlabel.setObjectName(_fromUtf8("wpa_clientlabel"))
        self.verticalLayout_3.addWidget(self.wpa_clientlabel)
        spacerItem22 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem22)
        self.verticalLayout_13.addLayout(self.verticalLayout_3)
        self.horizontalLayout_9.addLayout(self.verticalLayout_13)
        self.verticalLayout_19.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName(_fromUtf8("verticalLayout_14"))
        spacerItem23 = QtWidgets.QSpacerItem(168, 2, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_14.addItem(spacerItem23)
        self.database_button = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.database_button.sizePolicy().hasHeightForWidth())
        self.database_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(font_setting)
        font.setBold(True)
        font.setWeight(75)
        self.database_button.setFont(font)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8("%s/resources/Database-64.png"%(os.getcwd()))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.database_button.setIcon(icon6)
        self.database_button.setIconSize(QtCore.QSize(67, 62))
        self.database_button.setObjectName(_fromUtf8("database_button"))
        self.verticalLayout_14.addWidget(self.database_button)
        self.horizontalLayout_10.addLayout(self.verticalLayout_14)
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName(_fromUtf8("verticalLayout_15"))
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        spacerItem24 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem24)
        self.label_16 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(font_setting)
        self.label_16.setFont(font)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.verticalLayout_4.addWidget(self.label_16)
        spacerItem25 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem25)
        self.verticalLayout_15.addLayout(self.verticalLayout_4)
        self.horizontalLayout_10.addLayout(self.verticalLayout_15)
        self.verticalLayout_19.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setObjectName(_fromUtf8("verticalLayout_16"))
        spacerItem26 = QtWidgets.QSpacerItem(168, 2, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_16.addItem(spacerItem26)
        self.tool_button = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tool_button.sizePolicy().hasHeightForWidth())
        self.tool_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(font_setting)
        font.setBold(True)
        font.setWeight(75)
        self.tool_button.setFont(font)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8("%s/resources/1295905972_tool_kit.png"%(os.getcwd()))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tool_button.setIcon(icon7)
        self.tool_button.setIconSize(QtCore.QSize(67, 62))
        self.tool_button.setObjectName(_fromUtf8("tool_button"))
        self.verticalLayout_16.addWidget(self.tool_button)
        self.horizontalLayout_11.addLayout(self.verticalLayout_16)
        self.verticalLayout_17 = QtWidgets.QVBoxLayout()
        self.verticalLayout_17.setObjectName(_fromUtf8("verticalLayout_17"))
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        spacerItem27 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem27)
        self.label_13 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(font_setting)
        self.label_13.setFont(font)
        self.label_13.setText(_fromUtf8(""))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.verticalLayout_5.addWidget(self.label_13)
        spacerItem28 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem28)
        self.verticalLayout_17.addLayout(self.verticalLayout_5)
        self.horizontalLayout_11.addLayout(self.verticalLayout_17)
        self.verticalLayout_19.addLayout(self.horizontalLayout_11)
        self.verticalLayout_27.addLayout(self.verticalLayout_19)
        self.verticalLayout_25.addLayout(self.verticalLayout_27)
        self.horizontalLayout_7.addLayout(self.verticalLayout_25)
        self.verticalLayout_29.addLayout(self.horizontalLayout_7)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(font_setting)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout_6.addWidget(self.label_6)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.label_90 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_90.sizePolicy().hasHeightForWidth())
        self.label_90.setSizePolicy(sizePolicy)
        self.label_90.setObjectName(_fromUtf8("label_90"))
        self.horizontalLayout_12.addWidget(self.label_90)
        spacerItem29 = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem29)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_12.addWidget(self.label)
        self.verticalLayout_6.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13.addLayout(self.verticalLayout_6)
        spacerItem30 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem30)
        self.verticalLayout_7.addLayout(self.horizontalLayout_13)
        self.verticalLayout_29.addWidget(self.groupBox)
        self.verticalLayout_30.addLayout(self.verticalLayout_29)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        pythonver = str(sys.version)
        display = str(subprocess.getstatusoutput('aircrack-ng'))
        Dialog.setWindowTitle(QtWidgets.QApplication.translate("Dialog", "Fern WIFI Cracker", None, 0))
        self.update_label.setText(QtWidgets.QApplication.translate("Dialog", "Latest update is installed:  Revision 10", None, 0))
        self.py_version_label.setText(QtWidgets.QApplication.translate("Dialog", "Python Version: <font color=green>%s</font>"%(pythonver[0:14].replace('(',(''))), None, 0))
        self.air_version.setText(QtWidgets.QApplication.translate("Dialog", "Aircrack Version: <font color=green>%s</font>"%(display[11:33]), None, 0))
        self.qt_version.setText(QtWidgets.QApplication.translate("Dialog", "Qt Version: <font color=green>%s</font>"%(QtCore.PYQT_VERSION_STR), None, 0))
        self.refresh_intfacebutton.setText(QtWidgets.QApplication.translate("Dialog", " Refresh", None, 0))
        self.mon_label.setText(QtWidgets.QApplication.translate("Dialog", "Monitor Mode enabled on wlan0", None, 0))
        self.label_7.setText(QtWidgets.QApplication.translate("Dialog", "Scan for Access points", None, 0))
        self.wep_button.setText(QtWidgets.QApplication.translate("Dialog", "WEP", None, 0))
        self.wep_clientlabel.setText(QtWidgets.QApplication.translate("Dialog", "Detection Status", None, 0))
        self.wpa_button.setText(QtWidgets.QApplication.translate("Dialog", "WPA", None, 0))
        self.wpa_clientlabel.setText(QtWidgets.QApplication.translate("Dialog", "Detection Status", None, 0))
        self.database_button.setText(QtWidgets.QApplication.translate("Dialog", "Key Database", None, 0))
        self.label_16.setText(QtWidgets.QApplication.translate("Dialog", "No Key Entries", None, 0))
        self.tool_button.setText(QtWidgets.QApplication.translate("Dialog", "ToolBox", None, 0))
        self.label_13.setText(QtWidgets.QApplication.translate("Dialog", "", None, 0))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("Dialog", "About Fern WIFI Cracker", None, 0))
        self.label_6.setText(QtWidgets.QApplication.translate("Dialog", "GUI suite for wireless  encryption strength testing of 802.11 wireless encryption standard access points", None, 0))
        self.label_90.setText(QtWidgets.QApplication.translate("Dialog", "Written by Saviour Emmanuel Ekiko", None, 0))
        self.label.setText(QtWidgets.QApplication.translate("Dialog", " Report Bugs at :  savioboyz@rocketmail.com", None, 0))
