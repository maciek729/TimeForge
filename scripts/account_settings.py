# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'account_settings.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1394, 930)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.str_konto_srodek = QtWidgets.QFrame(Form)
        self.str_konto_srodek.setMinimumSize(QtCore.QSize(700, 0))
        self.str_konto_srodek.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.str_konto_srodek.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.str_konto_srodek.setFrameShadow(QtWidgets.QFrame.Raised)
        self.str_konto_srodek.setObjectName("str_konto_srodek")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.str_konto_srodek)
        self.verticalLayout_7.setContentsMargins(0, 10, 60, 30)
        self.verticalLayout_7.setSpacing(20)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.ustawienia_konta = QtWidgets.QFrame(self.str_konto_srodek)
        self.ustawienia_konta.setMinimumSize(QtCore.QSize(0, 100))
        self.ustawienia_konta.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ustawienia_konta.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ustawienia_konta.setObjectName("ustawienia_konta")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.ustawienia_konta)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(5)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.lb_ustawienia_konta = QtWidgets.QLabel(self.ustawienia_konta)
        self.lb_ustawienia_konta.setMinimumSize(QtCore.QSize(400, 100))
        self.lb_ustawienia_konta.setMaximumSize(QtCore.QSize(400, 100))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.lb_ustawienia_konta.setFont(font)
        self.lb_ustawienia_konta.setObjectName("lb_ustawienia_konta")
        self.verticalLayout_9.addWidget(self.lb_ustawienia_konta)
        self.settings_imie = QtWidgets.QFrame(self.ustawienia_konta)
        self.settings_imie.setMinimumSize(QtCore.QSize(0, 100))
        self.settings_imie.setMaximumSize(QtCore.QSize(16777215, 100))
        self.settings_imie.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.settings_imie.setFrameShadow(QtWidgets.QFrame.Raised)
        self.settings_imie.setObjectName("settings_imie")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.settings_imie)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lb_ikona_imie = QtWidgets.QLabel(self.settings_imie)
        self.lb_ikona_imie.setMinimumSize(QtCore.QSize(30, 30))
        self.lb_ikona_imie.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lb_ikona_imie.setFont(font)
        self.lb_ikona_imie.setText("")
        self.lb_ikona_imie.setPixmap(QtGui.QPixmap("../icons/icons_blue/user.svg"))
        self.lb_ikona_imie.setScaledContents(True)
        self.lb_ikona_imie.setObjectName("lb_ikona_imie")
        self.horizontalLayout_2.addWidget(self.lb_ikona_imie)
        self.lb_imie = QtWidgets.QLabel(self.settings_imie)
        self.lb_imie.setMinimumSize(QtCore.QSize(0, 45))
        self.lb_imie.setMaximumSize(QtCore.QSize(16777215, 45))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lb_imie.setFont(font)
        self.lb_imie.setObjectName("lb_imie")
        self.horizontalLayout_2.addWidget(self.lb_imie)
        self.le_imie = QtWidgets.QLineEdit(self.settings_imie)
        self.le_imie.setMinimumSize(QtCore.QSize(0, 45))
        self.le_imie.setMaximumSize(QtCore.QSize(350, 45))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.le_imie.setFont(font)
        self.le_imie.setToolTip("")
        self.le_imie.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.le_imie.setReadOnly(False)
        self.le_imie.setPlaceholderText("")
        self.le_imie.setObjectName("le_imie")
        self.horizontalLayout_2.addWidget(self.le_imie)
        self.btn_imie_edit = QtWidgets.QPushButton(self.settings_imie)
        self.btn_imie_edit.setMinimumSize(QtCore.QSize(45, 45))
        self.btn_imie_edit.setMaximumSize(QtCore.QSize(45, 45))
        self.btn_imie_edit.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icons/icons_blue/edit.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_imie_edit.setIcon(icon)
        self.btn_imie_edit.setIconSize(QtCore.QSize(25, 25))
        self.btn_imie_edit.setObjectName("btn_imie_edit")
        self.horizontalLayout_2.addWidget(self.btn_imie_edit)
        self.btn_imie_accept = QtWidgets.QPushButton(self.settings_imie)
        self.btn_imie_accept.setMinimumSize(QtCore.QSize(45, 45))
        self.btn_imie_accept.setMaximumSize(QtCore.QSize(45, 45))
        self.btn_imie_accept.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../icons/icons_blue/check.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_imie_accept.setIcon(icon1)
        self.btn_imie_accept.setIconSize(QtCore.QSize(25, 25))
        self.btn_imie_accept.setObjectName("btn_imie_accept")
        self.horizontalLayout_2.addWidget(self.btn_imie_accept)
        self.btn_imie_cancel = QtWidgets.QPushButton(self.settings_imie)
        self.btn_imie_cancel.setMinimumSize(QtCore.QSize(45, 45))
        self.btn_imie_cancel.setMaximumSize(QtCore.QSize(45, 45))
        self.btn_imie_cancel.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../icons/icons_blue/x.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_imie_cancel.setIcon(icon2)
        self.btn_imie_cancel.setIconSize(QtCore.QSize(25, 25))
        self.btn_imie_cancel.setObjectName("btn_imie_cancel")
        self.horizontalLayout_2.addWidget(self.btn_imie_cancel)
        self.verticalLayout_9.addWidget(self.settings_imie)
        self.pole_imie_nie_moze = QtWidgets.QFrame(self.ustawienia_konta)
        self.pole_imie_nie_moze.setMinimumSize(QtCore.QSize(0, 30))
        self.pole_imie_nie_moze.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pole_imie_nie_moze.setFont(font)
        self.pole_imie_nie_moze.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pole_imie_nie_moze.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pole_imie_nie_moze.setObjectName("pole_imie_nie_moze")
        self.lb_pole_imie_nie_moze = QtWidgets.QLabel(self.pole_imie_nie_moze)
        self.lb_pole_imie_nie_moze.setGeometry(QtCore.QRect(30, 0, 400, 31))
        self.lb_pole_imie_nie_moze.setMinimumSize(QtCore.QSize(400, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lb_pole_imie_nie_moze.setFont(font)
        self.lb_pole_imie_nie_moze.setObjectName("lb_pole_imie_nie_moze")
        self.lb_ikona_pole_imie_nie_moze = QtWidgets.QLabel(self.pole_imie_nie_moze)
        self.lb_ikona_pole_imie_nie_moze.setGeometry(QtCore.QRect(0, 0, 30, 31))
        self.lb_ikona_pole_imie_nie_moze.setSizeIncrement(QtCore.QSize(25, 25))
        self.lb_ikona_pole_imie_nie_moze.setBaseSize(QtCore.QSize(25, 25))
        self.lb_ikona_pole_imie_nie_moze.setText("")
        self.lb_ikona_pole_imie_nie_moze.setPixmap(QtGui.QPixmap("../icons/icons_red/alert-octagon.svg"))
        self.lb_ikona_pole_imie_nie_moze.setObjectName("lb_ikona_pole_imie_nie_moze")
        self.verticalLayout_9.addWidget(self.pole_imie_nie_moze)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_9.addItem(spacerItem)
        self.settings_nazwisko = QtWidgets.QFrame(self.ustawienia_konta)
        self.settings_nazwisko.setMinimumSize(QtCore.QSize(0, 100))
        self.settings_nazwisko.setMaximumSize(QtCore.QSize(16777215, 100))
        self.settings_nazwisko.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.settings_nazwisko.setFrameShadow(QtWidgets.QFrame.Raised)
        self.settings_nazwisko.setObjectName("settings_nazwisko")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.settings_nazwisko)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lb_ikona_nazwisko = QtWidgets.QLabel(self.settings_nazwisko)
        self.lb_ikona_nazwisko.setMinimumSize(QtCore.QSize(30, 30))
        self.lb_ikona_nazwisko.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lb_ikona_nazwisko.setFont(font)
        self.lb_ikona_nazwisko.setText("")
        self.lb_ikona_nazwisko.setPixmap(QtGui.QPixmap("../icons/icons_blue/user.svg"))
        self.lb_ikona_nazwisko.setScaledContents(True)
        self.lb_ikona_nazwisko.setObjectName("lb_ikona_nazwisko")
        self.horizontalLayout_3.addWidget(self.lb_ikona_nazwisko)
        self.lb_nazwisko = QtWidgets.QLabel(self.settings_nazwisko)
        self.lb_nazwisko.setMinimumSize(QtCore.QSize(0, 45))
        self.lb_nazwisko.setMaximumSize(QtCore.QSize(16777215, 45))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lb_nazwisko.setFont(font)
        self.lb_nazwisko.setObjectName("lb_nazwisko")
        self.horizontalLayout_3.addWidget(self.lb_nazwisko)
        self.le_nazwisko = QtWidgets.QLineEdit(self.settings_nazwisko)
        self.le_nazwisko.setMinimumSize(QtCore.QSize(0, 45))
        self.le_nazwisko.setMaximumSize(QtCore.QSize(350, 45))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.le_nazwisko.setFont(font)
        self.le_nazwisko.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.le_nazwisko.setObjectName("le_nazwisko")
        self.horizontalLayout_3.addWidget(self.le_nazwisko)
        self.btn_nazwisko_edit = QtWidgets.QPushButton(self.settings_nazwisko)
        self.btn_nazwisko_edit.setMinimumSize(QtCore.QSize(45, 45))
        self.btn_nazwisko_edit.setMaximumSize(QtCore.QSize(45, 45))
        self.btn_nazwisko_edit.setText("")
        self.btn_nazwisko_edit.setIcon(icon)
        self.btn_nazwisko_edit.setIconSize(QtCore.QSize(25, 25))
        self.btn_nazwisko_edit.setObjectName("btn_nazwisko_edit")
        self.horizontalLayout_3.addWidget(self.btn_nazwisko_edit)
        self.btn_nazwisko_accept = QtWidgets.QPushButton(self.settings_nazwisko)
        self.btn_nazwisko_accept.setMinimumSize(QtCore.QSize(45, 45))
        self.btn_nazwisko_accept.setMaximumSize(QtCore.QSize(45, 45))
        self.btn_nazwisko_accept.setText("")
        self.btn_nazwisko_accept.setIcon(icon1)
        self.btn_nazwisko_accept.setIconSize(QtCore.QSize(25, 25))
        self.btn_nazwisko_accept.setObjectName("btn_nazwisko_accept")
        self.horizontalLayout_3.addWidget(self.btn_nazwisko_accept)
        self.btn_nazwisko_cancel = QtWidgets.QPushButton(self.settings_nazwisko)
        self.btn_nazwisko_cancel.setMinimumSize(QtCore.QSize(45, 45))
        self.btn_nazwisko_cancel.setMaximumSize(QtCore.QSize(45, 45))
        self.btn_nazwisko_cancel.setText("")
        self.btn_nazwisko_cancel.setIcon(icon2)
        self.btn_nazwisko_cancel.setIconSize(QtCore.QSize(25, 25))
        self.btn_nazwisko_cancel.setObjectName("btn_nazwisko_cancel")
        self.horizontalLayout_3.addWidget(self.btn_nazwisko_cancel)
        self.verticalLayout_9.addWidget(self.settings_nazwisko)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_9.addItem(spacerItem1)
        self.settings_login = QtWidgets.QFrame(self.ustawienia_konta)
        self.settings_login.setMinimumSize(QtCore.QSize(0, 100))
        self.settings_login.setMaximumSize(QtCore.QSize(16777215, 100))
        self.settings_login.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.settings_login.setFrameShadow(QtWidgets.QFrame.Raised)
        self.settings_login.setObjectName("settings_login")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.settings_login)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.lb_ikona_login = QtWidgets.QLabel(self.settings_login)
        self.lb_ikona_login.setMinimumSize(QtCore.QSize(30, 30))
        self.lb_ikona_login.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lb_ikona_login.setFont(font)
        self.lb_ikona_login.setText("")
        self.lb_ikona_login.setPixmap(QtGui.QPixmap("../icons/icons_blue/user.svg"))
        self.lb_ikona_login.setScaledContents(True)
        self.lb_ikona_login.setObjectName("lb_ikona_login")
        self.horizontalLayout_7.addWidget(self.lb_ikona_login)
        self.lb_login = QtWidgets.QLabel(self.settings_login)
        self.lb_login.setMinimumSize(QtCore.QSize(0, 45))
        self.lb_login.setMaximumSize(QtCore.QSize(16777215, 45))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lb_login.setFont(font)
        self.lb_login.setObjectName("lb_login")
        self.horizontalLayout_7.addWidget(self.lb_login)
        self.le_login = QtWidgets.QLineEdit(self.settings_login)
        self.le_login.setMinimumSize(QtCore.QSize(0, 45))
        self.le_login.setMaximumSize(QtCore.QSize(400, 45))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.le_login.setFont(font)
        self.le_login.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.le_login.setObjectName("le_login")
        self.horizontalLayout_7.addWidget(self.le_login)
        self.verticalLayout_9.addWidget(self.settings_login)
        spacerItem2 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_9.addItem(spacerItem2)
        self.settings_haslo = QtWidgets.QFrame(self.ustawienia_konta)
        self.settings_haslo.setMinimumSize(QtCore.QSize(0, 100))
        self.settings_haslo.setMaximumSize(QtCore.QSize(16777215, 100))
        self.settings_haslo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.settings_haslo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.settings_haslo.setObjectName("settings_haslo")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.settings_haslo)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lb_ikona_haslo = QtWidgets.QLabel(self.settings_haslo)
        self.lb_ikona_haslo.setMinimumSize(QtCore.QSize(30, 30))
        self.lb_ikona_haslo.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lb_ikona_haslo.setFont(font)
        self.lb_ikona_haslo.setText("")
        self.lb_ikona_haslo.setPixmap(QtGui.QPixmap("../icons/icons_blue/lock.svg"))
        self.lb_ikona_haslo.setScaledContents(True)
        self.lb_ikona_haslo.setObjectName("lb_ikona_haslo")
        self.horizontalLayout_4.addWidget(self.lb_ikona_haslo)
        self.lb_haslo = QtWidgets.QLabel(self.settings_haslo)
        self.lb_haslo.setMinimumSize(QtCore.QSize(0, 45))
        self.lb_haslo.setMaximumSize(QtCore.QSize(16777215, 45))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lb_haslo.setFont(font)
        self.lb_haslo.setObjectName("lb_haslo")
        self.horizontalLayout_4.addWidget(self.lb_haslo)
        self.le_haslo = QtWidgets.QLineEdit(self.settings_haslo)
        self.le_haslo.setMinimumSize(QtCore.QSize(0, 45))
        self.le_haslo.setMaximumSize(QtCore.QSize(350, 45))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.le_haslo.setFont(font)
        self.le_haslo.setEchoMode(QtWidgets.QLineEdit.Password)
        self.le_haslo.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.le_haslo.setReadOnly(True)
        self.le_haslo.setObjectName("le_haslo")
        self.horizontalLayout_4.addWidget(self.le_haslo)
        self.btn_haslo_edit = QtWidgets.QPushButton(self.settings_haslo)
        self.btn_haslo_edit.setMinimumSize(QtCore.QSize(45, 45))
        self.btn_haslo_edit.setMaximumSize(QtCore.QSize(45, 45))
        self.btn_haslo_edit.setText("")
        self.btn_haslo_edit.setIcon(icon)
        self.btn_haslo_edit.setIconSize(QtCore.QSize(25, 25))
        self.btn_haslo_edit.setObjectName("btn_haslo_edit")
        self.horizontalLayout_4.addWidget(self.btn_haslo_edit)
        self.verticalLayout_9.addWidget(self.settings_haslo)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem3)
        self.app_usun_konto = QtWidgets.QFrame(self.ustawienia_konta)
        self.app_usun_konto.setMinimumSize(QtCore.QSize(0, 180))
        self.app_usun_konto.setMaximumSize(QtCore.QSize(16777215, 220))
        self.app_usun_konto.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.app_usun_konto.setFrameShadow(QtWidgets.QFrame.Raised)
        self.app_usun_konto.setObjectName("app_usun_konto")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.app_usun_konto)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.lb_usun_konto = QtWidgets.QLabel(self.app_usun_konto)
        self.lb_usun_konto.setMinimumSize(QtCore.QSize(0, 50))
        self.lb_usun_konto.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lb_usun_konto.setFont(font)
        self.lb_usun_konto.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lb_usun_konto.setObjectName("lb_usun_konto")
        self.verticalLayout_10.addWidget(self.lb_usun_konto)
        self.lb_spowoduje = QtWidgets.QLabel(self.app_usun_konto)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lb_spowoduje.setFont(font)
        self.lb_spowoduje.setObjectName("lb_spowoduje")
        self.verticalLayout_10.addWidget(self.lb_spowoduje)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem4)
        self.btn_usun_konto = QtWidgets.QPushButton(self.app_usun_konto)
        self.btn_usun_konto.setMinimumSize(QtCore.QSize(180, 60))
        self.btn_usun_konto.setMaximumSize(QtCore.QSize(180, 60))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn_usun_konto.setFont(font)
        self.btn_usun_konto.setObjectName("btn_usun_konto")
        self.verticalLayout_10.addWidget(self.btn_usun_konto)
        self.verticalLayout_9.addWidget(self.app_usun_konto)
        self.verticalLayout_7.addWidget(self.ustawienia_konta)
        self.verticalLayout.addWidget(self.str_konto_srodek)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lb_ustawienia_konta.setText(_translate("Form", "Ustawienia konta"))
        self.lb_imie.setText(_translate("Form", "Imię"))
        self.lb_pole_imie_nie_moze.setText(_translate("Form", "Pole imię nie może być puste!"))
        self.lb_nazwisko.setText(_translate("Form", "Nazwisko"))
        self.lb_login.setText(_translate("Form", "Login"))
        self.lb_haslo.setText(_translate("Form", "Hasło"))
        self.lb_usun_konto.setText(_translate("Form", "Usuń konto"))
        self.lb_spowoduje.setText(_translate("Form", "Spowoduje to trwałe usunięcie wszystkich danych. \n"
"Czynność nie może zostać cofnięta."))
        self.btn_usun_konto.setText(_translate("Form", "Usuń konto"))
