from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMessageBox
import ObslugaBazyDanych as odb
from Zalogowany_użytkownik import zalogowanyUzytkownik
import startowa_strona as start
import toolbar_impl as sidebar

class DlgMain(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = start.Ui_TimeForge()
        self.ui.setupUi(self)

        # Ustawienia okna autoryzacji
        pixmap = QPixmap('../resources/TimeForge_icon0000.ico')
        self.ui.lb_ikona_aplikacji_logowanie_2.setPixmap(pixmap)
        self.setWindowIcon(QtGui.QIcon('../resources/TimeForge_icon0000.ico'))
        self.ui.strony.setCurrentWidget(self.ui.str_witaj)
        self.setWindowTitle("Timeforge")

        self.imie = ''
        self.lista_uzytkownikow = []

        # Strona Witaj Zdarzenia
        self.ui.btn_kontynuuj.clicked.connect(self.evt_btn_kontynuuj)
        self.ui.le_wprowadz.textChanged.connect(self.evt_le_wprowadz_changed)
        self.ui.btn_posiadasz.clicked.connect(self.evt_btn_posiadasz)
        self.ui.pole_nie_moze.hide()

        # Strona Zarejestruj Zdarzenia
        self.ui.btn_zaloz_konto.clicked.connect(self.evt_btn_zaloz_konto)
        self.ui.btn_posiadasz_rejestracja.clicked.connect(self.evt_btn_posiadasz_rejestracja)
        self.ui.le_wprowadz_login.textChanged.connect(self.evt_le_wprowadz_login)
        self.ui.le_wprowadz_haslo.textChanged.connect(self.evt_le_wprowadz_haslo)
        self.ui.pole_nie_moze_login_rejestracja.hide()
        self.ui.pole_nie_moze_haslo_rejestracja.hide()
        self.ui.haslo_musi_zawierac.hide()
        self.ui.btn_pokaz_haslo.clicked.connect(self.evt_btn_pokaz_haslo)

        # Strona Zaloguj Zdarzenia
        self.ui.btn_zaloguj.clicked.connect(self.evt_btn_zaloguj)
        self.ui.btn_nie_posiadasz.clicked.connect(self.evt_btn_nie_posiadasz)
        self.ui.btn_pokaz_haslo_logowanie.clicked.connect(self.evt_pokaz_haslo_logowanie)
        self.ui.niepoprawny_login.hide()


    # ===== STRONA POWITALNA OBSLUGA ZDARZEN

    # Button kontynnuj - jezeli posiada tekst to wówczas pozwala uruchomic aplikacje,
    # w przeciwnym przypadku pokazuje informacje, ze pole nie moze byc puste
    def evt_btn_kontynuuj(self):
        if self.ui.le_wprowadz.text():
            self.imie = self.ui.le_wprowadz.text()
            self.ui.strony.setCurrentWidget(self.ui.str_rejestracja)
        else:
            self.ui.pole_nie_moze.show()


    # LineEdit, gdy jest pusty pokazuje sie informacja, ze pole nie moze byc puste
    # jesli nie jest pusty to znika informacja, ze pole nie moze byc puste
    def evt_le_wprowadz_changed(self):
        if self.ui.le_wprowadz.text():
            self.ui.pole_nie_moze.hide()
        else:
            self.ui.pole_nie_moze.show()


    # Przycisk Posiadasz juz konto? Zaloguj sie
    # przenosi na strone logowania sie
    def evt_btn_posiadasz(self):
        self.ui.strony.setCurrentWidget(self.ui.str_logowanie)




    # ===== REJESTRACJA OBSLUGA ZDARZEN

    # jezeli login i haslo nie jest puste to pozwala utworzyc konto, w przeciwnym wypadku
    # pokazuje informacje ze pole nie moze byc puste
    def evt_btn_zaloz_konto(self):
        self.ui.le_wprowadz_email_logowanie.setText("")
        self.ui.le_wprowadz_haslo_logowanie.setText("")
        self.ui.btn_pokaz_haslo_logowanie.setChecked(False)
        self.ui.le_wprowadz_haslo_logowanie.setEchoMode(QtWidgets.QLineEdit.Password)

        theme = "jasny"
        if self.ui.le_wprowadz_login.text() and self.ui.le_wprowadz_haslo.text():
            if len(self.ui.le_wprowadz_haslo.text()) >= 8:
                imie = self.imie
                login = self.ui.le_wprowadz_login.text()
                haslo = self.ui.le_wprowadz_haslo.text()

                if odb.register_user(imie, login, haslo, theme):
                    # Redirect to login page after successful registration
                    self.ui.strony.setCurrentWidget(self.ui.str_logowanie)
                    self.ui.le_wprowadz_email_logowanie.setFocus(True)
                else:
                    QMessageBox.warning(self, "Rejestracja nie powiodła się",
                                        "Login już istnieje!")
            else:
                self.ui.haslo_musi_zawierac.show()
        else:
            if not self.ui.le_wprowadz_login.text():
                self.ui.pole_nie_moze_login_rejestracja.show()
            if not self.ui.le_wprowadz_haslo.text():
                self.ui.pole_nie_moze_haslo_rejestracja.show()

    # Przycisk Posiadasz juz konto? zaloguj sie!
    # Gdy wcisniety przenosi na strone logowania
    def evt_btn_posiadasz_rejestracja(self):
        self.ui.strony.setCurrentWidget(self.ui.str_logowanie)
        self.ui.le_wprowadz_email_logowanie.clear()
        self.ui.le_wprowadz_haslo_logowanie.clear()
        self.ui.le_wprowadz_haslo.clear()
        self.ui.le_wprowadz_login.clear()
        self.ui.pole_nie_moze_login_rejestracja.hide()
        self.ui.pole_nie_moze_haslo_rejestracja.hide()
        self.ui.le_wprowadz_haslo_logowanie.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ui.btn_pokaz_haslo_logowanie.setChecked(False)

    # zmiana zawartosci LineEdit login
    # gdy pole jest puste pojawia sie komunikat ze Pole nie moze byc puste
    def evt_le_wprowadz_login(self):
        if self.ui.le_wprowadz_login.text():
            self.ui.pole_nie_moze_login_rejestracja.hide()
        else:
            self.ui.pole_nie_moze_login_rejestracja.show()

    # zmiana zawartosci LineEdit haslo
    # gdy pole jest puste pojawia sie komunikat ze Pole nie moze byc puste
    def evt_le_wprowadz_haslo(self):
        if self.ui.le_wprowadz_haslo.text():
            self.ui.pole_nie_moze_haslo_rejestracja.hide()
        else:
            self.ui.pole_nie_moze_haslo_rejestracja.show()

    def evt_btn_pokaz_haslo(self):
        current_echo_mode = self.ui.le_wprowadz_haslo.echoMode()
        # Sprawdź aktualny tryb echo
        if current_echo_mode == QtWidgets.QLineEdit.Password:
            # Jeśli aktualny tryb to Password, zmień na Normal
            self.ui.le_wprowadz_haslo.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            # Jeśli aktualny tryb to inny niż Password, zmień na Password
            self.ui.le_wprowadz_haslo.setEchoMode(QtWidgets.QLineEdit.Password)




    # ===== LOGOWANIE OBSLUGA ZDARZEN
    # Button Zaloguj, jesli uzytkownika dane sie zgadzaja to nastapi
    # przekierowanie do aplikacji glownej
    def evt_btn_zaloguj(self):
        # Get the login and password from the input fields
        login = self.ui.le_wprowadz_email_logowanie.text()
        haslo = self.ui.le_wprowadz_haslo_logowanie.text()


        print("Login:", login)  # Debug print
        print("Password:", haslo)  # Debug print

        user_info = odb.get_user_info(login)
        print("User Info:", user_info)  # Debug print

        # Check if the login and password exist in the database
        if odb.validate_user(login, haslo):
            print("User validated")  # Debug print
            self.logged_user_id = user_info['user_id']
            self.logged_user_name = user_info['first_name']
            self.logged_user_login = user_info['login']  # Corrected key name
            self.logged_user_password = user_info['password_hash']
            self.logged_user_nazwisko = user_info['last_name']  # Debug statement
            zalogowany_uzytkownik = zalogowanyUzytkownik.get_instance()
            zalogowany_uzytkownik.set_zalogowany_id(self.logged_user_id)

            self.sidebar_window = sidebar.DlgMain()  # Tworzenie instancji okna bocznego
            self.sidebar_window.show()  # Wyświetlenie okna bocznego
            self.close()
        else:
            self.ui.lb_niepoprawny_login.show()
            # If login or password is incorrect, show a warning message
            print("Login failed")  # Debug print
            QMessageBox.warning(self, "Logowanie nie powiodło się",
                                "Niepoprawny login lub haslo. Spróbuj ponownie.")


    # Przycisk nie posiadasz, przekierowuje do rejestracji
    def evt_btn_nie_posiadasz(self):
        self.ui.strony.setCurrentWidget(self.ui.str_rejestracja)
        self.ui.le_wprowadz_login.clear()
        self.ui.le_wprowadz_haslo.clear()
        self.ui.btn_pokaz_haslo.setChecked(False)
        self.ui.le_wprowadz_haslo.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ui.pole_nie_moze_login_rejestracja.hide()
        self.ui.pole_nie_moze_haslo_rejestracja.hide()
        self.ui.haslo_musi_zawierac.hide()

    def evt_pokaz_haslo_logowanie(self):
        current_echo_mode = self.ui.le_wprowadz_haslo_logowanie.echoMode()
        # Sprawdź aktualny tryb echo
        if current_echo_mode == QtWidgets.QLineEdit.Password:
            # Jeśli aktualny tryb to Password, zmień na Normal
            self.ui.le_wprowadz_haslo_logowanie.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            # Jeśli aktualny tryb to inny niż Password, zmień na Password
            self.ui.le_wprowadz_haslo_logowanie.setEchoMode(QtWidgets.QLineEdit.Password)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            current_widget = self.ui.strony.currentWidget()
            if current_widget == self.ui.str_logowanie:
                self.ui.btn_zaloguj.click()
            elif current_widget == self.ui.str_rejestracja:
                self.ui.btn_zaloz_konto.click()
            elif current_widget == self.ui.str_witaj:
                self.ui.btn_kontynuuj.click()

    # Uruchomienie okna głównego aplikacji
    def uruchom_aplikacje(self):
        self.sidebar_window = sidebar.DlgMain()
        self.sidebar_window.show()
        self.close()

