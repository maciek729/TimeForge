import sys
from PyQt5 import QtGui
from PyQt5 import QtWidgets

from PyQt5.QtCore import QSize, Qt, QPropertyAnimation
import Zmiana_Motywow
import toolbar
import strona_glowna
import kalendarz
import account_settings
import settings
import run
import new_shortcuts as shortcuts
import zmiana_hasla
from Zalogowany_użytkownik import zalogowanyUzytkownik
import ObslugaBazyDanych as obd

class DlgMain(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = toolbar.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('../resources/TimeForge_icon0000.ico'))

        self.ui.pasek_zwiniety.setMinimumSize(QSize(70, 0))
        self.ui.pasek_zwiniety.setMaximumSize(QSize(70, 16777215))

        # !!!! Przypisanie ekranów do okna
        # Przypisanie ekranu strony głównej
        self.str_glowna = strona_glowna.DlgMain()
        self.ui.zawartosc_okna.addWidget(self.str_glowna)

        # Przypisanie ekranu kalendarz
        self.str_kalendarz = kalendarz.DlgMain()
        self.ui.zawartosc_okna.addWidget(self.str_kalendarz)

        # Przypisanie ekranu ustawienia konta
        self.str_ustawienia_konta = QtWidgets.QWidget()
        self.str_ustawienia_konta_ui = account_settings.Ui_Form()
        self.str_ustawienia_konta_ui.setupUi(self.str_ustawienia_konta)
        self.ui.zawartosc_okna.addWidget(self.str_ustawienia_konta)

        # Przypisanie ekranu ustawienia aplikacji
        self.str_ustawienia_aplikacji = QtWidgets.QWidget()
        self.str_ustawienia_aplikacji_ui = settings.Ui_Form()
        self.str_ustawienia_aplikacji_ui.setupUi(self.str_ustawienia_aplikacji)
        self.ui.zawartosc_okna.addWidget(self.str_ustawienia_aplikacji)

        # Przypisanie ekranu skrótów klawiszowych
        self.str_skroty_klawiszowe = QtWidgets.QWidget()
        self.str_skroty_klawiszowe_ui = shortcuts.Ui_Form()
        self.str_skroty_klawiszowe_ui.setupUi(self.str_skroty_klawiszowe)
        self.ui.zawartosc_okna.addWidget(self.str_skroty_klawiszowe)

        # Przypisanie ekranu zmiana hasła
        self.str_zmiana_hasla = QtWidgets.QWidget()
        self.str_zmiana_hasla_ui = zmiana_hasla.Ui_Form()
        self.str_zmiana_hasla_ui.setupUi(self.str_zmiana_hasla)
        self.ui.zawartosc_okna.addWidget(self.str_zmiana_hasla)

        # Ustawienia Aplikacji Uruchomionej
        self.setMinimumSize(1250, 780)
        self.resize(1400,800)
        self.ui.zawartosc_okna.setCurrentWidget(self.str_glowna)
        self.ui.btn_sidebar_zwin_calosc.hide()
        self.ui.pasek_hover.show()
        self.ui.pasek.hide()
        self.ui.btn_strona_glowna.setChecked(True)
        self.ui.btn_strona_glowna_3.setChecked(True)



        # Btn Strona startowa zdarzenia
        self.ui.btn_strona_glowna.clicked.connect(self.evt_btn_strona_glowna_clicked)
        self.ui.btn_strona_glowna_3.clicked.connect(self.evt_btn_strona_glowna_clicked)

        # Btn Kalendarz zdarzenia
        self.ui.btn_kalendarz.clicked.connect(self.evt_btn_kalendarz_clicked)
        self.ui.btn_kalendarz_3.clicked.connect(self.evt_btn_kalendarz_clicked)

        # Btn konto zdarzenia
        self.ui.btn_konto.clicked.connect(self.evt_btn_konto_clicked)
        self.ui.btn_konto_3.clicked.connect(self.evt_btn_konto_clicked)

        # Btn ustawienia zdarzenia
        self.ui.btn_ustawienia.clicked.connect(self.evt_btn_ustawienia_clicked)
        self.ui.btn_ustawienia_3.clicked.connect(self.evt_btn_ustawienia_clicked)

        # Btn wyloguj clicked zdarzenia
        self.ui.btn_wyloguj.clicked.connect(self.evt_btn_wyloguj_clicked)
        self.ui.btn_wyloguj_3.clicked.connect(self.evt_btn_wyloguj_clicked)

        """
        # Pasek Zadan (dynamicznie rozwijany i zwijany, zakomentowane, gdyż denerwował niektóre osoby)
        def evt_pasek_hover_hide():
            self.ui.pasek_hover.hide()

        def evt_pasek_hovered():
            if not (self.ui.pasek.isHidden() and self.ui.pasek_hover.isHidden()):
                self.ui.pasek_hover.show()
                self.ui.pasek.hide()

        def evt_pasek_not_hovered():
            if not (self.ui.pasek.isHidden() and self.ui.pasek_hover.isHidden()):
                self.ui.pasek_hover.hide()
                self.ui.pasek.show()
        """
        # self.ui.srodek.enterEvent = lambda event: evt_pasek_hover_hide()
        # self.ui.pasek.enterEvent = lambda event: evt_pasek_hovered()
        # self.ui.pasek_hover.leaveEvent = lambda event: evt_pasek_not_hovered()



        # Wykrywanie zdarzen
        # Strona glowna zdarzenia
        # - znajduja sie w pliku strona_glowna.py wraz z ich obsluga

        # Kalendarz zdarzenia
        # - znajduja sie w pliku kalendarz.py wraz z ich obsluga

        # # Ustawienia zdarzenia
        # 0) Ukrycie komunikatow (stan poczatkowy ekranu)
        self.str_ustawienia_aplikacji_ui.zmiany_zostaly_zapisane.hide()
        self.str_ustawienia_aplikacji_ui.zmiany_nie_zostaly.hide()
        self.str_ustawienia_aplikacji_ui.przywrocono_domyslne_ustawienia.hide()

        # 1) wciśnięcie klawisza skróty klawiszowe
        # - przeniesienie na str_skroty_klawiszowe, ktora wyswietla skroty_klawiszowe
        self.str_ustawienia_aplikacji_ui.btn_skroty_klawiszowe.clicked.connect(
            lambda event: self.ui.zawartosc_okna.setCurrentWidget(self.str_skroty_klawiszowe))

        # 2) wcisniecie przycisku powrót na stronie sktóry klawiszowe
        # - przeniesienie z powrotem na stronę ustawień
        self.str_skroty_klawiszowe_ui.btn_powrot_skroty_klawiszowe.clicked.connect(
            lambda event: self.ui.zawartosc_okna.setCurrentWidget(self.str_ustawienia_aplikacji))

        # 3) Uzytkownik zmienil motyw w combo motyw
        # - wyswietli sie komunikat o niezapisanych ustawieniach
        # - komunikat zniknie po zapisaniu lub po kliknieciu anuluj
        # lub po kliknieciu przywroc ustawienia domyslne
        self.str_ustawienia_aplikacji_ui.combo_motyw.currentIndexChanged.connect(
            lambda event: self.str_ustawienia_aplikacji_ui.zmiany_nie_zostaly.show())

        # 4) wcisnięcie przycisku "Przejdź do ustawień konta"
        # - przeniesienie użytkownika na stronę ustawień konta
        self.str_ustawienia_aplikacji_ui.btn_ustawienia_konta.clicked.connect(
            self.evt_ustawienia_btn_ustawienia_konta_clicked)

        # 5) Wcisniecie przycisku "Zapisz zmiany"
        # - zapis zmian do bazy danych
        # - komunikat o tym ze zmiany zostaly zapisane
        # - znikniecie komunikatu o niezapisanych danych
        self.str_ustawienia_aplikacji_ui.btn_zapisz_zmiany.clicked.connect(self.evt_btn_zapisz_zmiany_clicked)

        # 6) Wcisniecie przycisku "Anuluj"
        # - pobranie obecnych zmian z bazy danych
        # - wczytanie je do comboBoxow
        # - znikniecie komunikatu o niezapisanych danych
        self.str_ustawienia_aplikacji_ui.btn_anuluj_zmiany.clicked.connect(self.evt_btn_anuluj_zmiany_clicked)

        # 7) Wcisniecie przycisku "Przywroc domyslne ustawienia"
        # - ustawienie domyslnych ustawien
        # - zapis ustawien do bazy danych
        # - komunikat o tym ze Przywrocono domyslne ustawienia
        # - znikniecie komunikatu o niezapisanych danych
        self.str_ustawienia_aplikacji_ui.btn_przywroc_domyslne_ustawienia.clicked.connect(
            self.evt_btn_przywroc_domyslne_ustawienia_clicked)

        # Ustawienia konta zdarzenia
        # stan poczatkowy strony (ukrycie przycisków zatwierdzających/anulujących, komunikatów)
        self.str_ustawienia_konta_ui.btn_imie_edit.show()
        self.str_ustawienia_konta_ui.btn_imie_cancel.hide()
        self.str_ustawienia_konta_ui.btn_imie_accept.hide()

        self.str_ustawienia_konta_ui.btn_nazwisko_edit.show()
        self.str_ustawienia_konta_ui.btn_nazwisko_cancel.hide()
        self.str_ustawienia_konta_ui.btn_nazwisko_accept.hide()
        self.str_ustawienia_konta_ui.pole_imie_nie_moze.hide()

        # pobranie zalogowanego uzytkownika
        zalogowany_uzytkownik = zalogowanyUzytkownik.get_instance()
        self.logged_user_id = zalogowany_uzytkownik.get_zalogowany_id()
        self.user_info = obd.get_user_info_by_id(self.logged_user_id)  # Retrieve user information from the database
        # wypelnienie pol tekstowych danymi zalogowanego uzytkownika
        self.str_ustawienia_konta_ui.le_imie.setText(self.user_info["first_name"])
        self.str_ustawienia_konta_ui.le_nazwisko.setText(self.user_info["last_name"])
        self.str_ustawienia_konta_ui.le_login.setText(self.user_info["login"])
        self.str_ustawienia_konta_ui.le_haslo.setText(self.user_info["password"])
        # ustawienie motywu wykorzystywanego przez uzytkownika
        self.motyw = self.user_info["theme"]
        self.user_motyw = self.motyw
        self.str_ustawienia_aplikacji_ui.combo_motyw.setCurrentText(self.user_motyw)

        # Funkcja ktora wprowadzi te ustawienia w zycie
        # - dzieki niej przy uruchomieniu aplikacji ponownie po zmianie na tryb ciemny faktycznie bd tryb ciemny
        self.wprowadz_ustawienia(self.user_motyw)

        print(type(self.motyw))
        # Set QLineEdit widgets as read-only
        self.str_ustawienia_konta_ui.le_imie.setReadOnly(True)
        self.str_ustawienia_konta_ui.le_nazwisko.setReadOnly(True)
        self.str_ustawienia_konta_ui.le_login.setReadOnly(True)
        self.str_ustawienia_konta_ui.le_haslo.setReadOnly(True)

        # Edytowanie imienia i nazwiska
        self.str_ustawienia_konta_ui.btn_imie_edit.clicked.connect(self.evt_btn_imie_edit_clicked)
        self.str_ustawienia_konta_ui.btn_nazwisko_edit.clicked.connect(self.evt_btn_nazwisko_edit_clicked)

        # Akceptacja imienia i nazwiska (zapis)
        self.str_ustawienia_konta_ui.btn_imie_accept.clicked.connect(self.evt_btn_imie_accept_clicked)
        self.str_ustawienia_konta_ui.btn_nazwisko_accept.clicked.connect(self.evt_btn_nazwisko_accept_clicked)

        # Anulowanie zmiany imienia i nazwiska
        self.str_ustawienia_konta_ui.btn_imie_cancel.clicked.connect(self.evt_btn_imie_cancel_clicked)
        self.str_ustawienia_konta_ui.btn_nazwisko_cancel.clicked.connect(self.evt_btn_nazwisko_cancel_clicked)

        # Usuwanie Konta
        self.str_ustawienia_konta_ui.btn_usun_konto.clicked.connect(self.evt_btn_usun_konto)

        # Zmiana hasla
        self.str_ustawienia_konta_ui.btn_haslo_edit.clicked.connect(
            lambda event: self.ui.zawartosc_okna.setCurrentWidget(self.str_zmiana_hasla))



        # Ekran Zmiana hasla zdarzenia
        # -------------------------------
        # 1) Ukrycie Komunikatow o Bledach
        #  "Podano błędne bieżące hasło"
        self.str_zmiana_hasla_ui.podano_bledne_biezace_haslo.hide()

        #  "Nowe hasło nie może być takie samo jak bieżące hasło"
        self.str_zmiana_hasla_ui.nowe_haslo_nie_moze.hide()

        #  "Hasła nie są takie same" (Nowe hasło i Powtórz nowe hasło)
        self.str_zmiana_hasla_ui.hasla_nie_sa_takie.hide()

        #  "Nowe hasło musi zawierać co najmniej 8 znaków!"
        self.str_zmiana_hasla_ui.nowe_haslo_musi.hide()

        # -----------------------------------------------
        # 2) Włączenie echoMode w miejscu wpisywania haseł
        # - echoMode powoduje, że tekst wpisywany w LineEdit
        #   będzie widoczny w postaci *
        #   zamiast "haslo" będzie widoczne "*****"
        self.str_zmiana_hasla_ui.le_biezace_haslo.setEchoMode(QtWidgets.QLineEdit.Password)
        self.str_zmiana_hasla_ui.le_nowe_haslo.setEchoMode(QtWidgets.QLineEdit.Password)
        self.str_zmiana_hasla_ui.le_potwierdz_nowe_haslo.setEchoMode(QtWidgets.QLineEdit.Password)

        # ---------------------------------------------------------------
        # 3) Event: Uzytkownik Przełącza Tryb Widoczności Hasła (echoMode)
        # - czyli zamiast "*****" będzie widoczne "haslo"
        #   lub zamiast "haslo" będzie widoczne "*****"
        #   w zależności od tego jak użytkownik będzie chciał

        # Zmiana trybu widoczności pola "Bieżące hasło"
        self.str_zmiana_hasla_ui.btn_biezace_haslo_pokaz.clicked.connect(self.evt_echoMode_changed_le_biezace_haslo)

        # Zmiana trybu widoczności pola "Nowe Hasło"
        self.str_zmiana_hasla_ui.btn_nowe_haslo_pokaz.clicked.connect(self.evt_echoMode_changed_le_nowe_haslo)

        # Zmiana trybu widoczności pola "Potwierdź Nowe Hasło"
        self.str_zmiana_hasla_ui.btn_potwierdz_nowe_haslo.clicked.connect(
            self.evt_echoMode_changed_le_potwierdz_nowe_haslo)

        # -------------------------------------------------
        # 4) Event: Użytkownik klika na przycisk powrot [<]
        # - po wciśnięciu przycisku powrót użytkownik wraca na stronę ustawień konta
        self.str_zmiana_hasla_ui.btn_powrot.clicked.connect(self.evt_btn_powrot_clicked)

        # --------------------------------------------------
        # 5) Event: Użytkownik klika na przycisk "
        self.str_zmiana_hasla_ui.btn_zmien_haslo.clicked.connect(self.evt_zmien_moje_haslo)

    # Przelaczanie ekranow
    def evt_btn_strona_glowna_clicked(self):
        self.ui.zawartosc_okna.setCurrentWidget(self.str_glowna)

    def evt_btn_kalendarz_clicked(self):
        self.ui.zawartosc_okna.setCurrentWidget(self.str_kalendarz)

    def evt_btn_konto_clicked(self):
        self.ui.zawartosc_okna.setCurrentWidget(self.str_ustawienia_konta)

    def evt_btn_ustawienia_clicked(self):
        self.ui.zawartosc_okna.setCurrentWidget(self.str_ustawienia_aplikacji)
        self.str_ustawienia_aplikacji_ui.zmiany_nie_zostaly.hide()

    def evt_btn_wyloguj_clicked(self):
        self.run = run.DlgMain()
        self.run.ui.strony.setCurrentWidget(self.run.ui.str_logowanie)
        self.run.show()
        self.close()


    # USTAWIENIA KONTA OBSLUGA ZDARZEN
    # wcisniecie przycisku edytowania dla kazdego z pola
    def evt_btn_imie_edit_clicked(self):
        konto = self.str_ustawienia_konta_ui
        konto.le_imie.setReadOnly(False)
        konto.btn_imie_edit.hide()
        konto.btn_imie_accept.show()
        konto.btn_imie_cancel.show()

    def evt_btn_nazwisko_edit_clicked(self):
        konto = self.str_ustawienia_konta_ui
        konto.le_nazwisko.setReadOnly(False)
        konto.btn_nazwisko_edit.hide()
        konto.btn_nazwisko_accept.show()
        konto.btn_nazwisko_cancel.show()

    # wcisniecie przycisku accept dla kazdego z pol
    def evt_btn_imie_accept_clicked(self):
        # Sprawdzam czy pole nie jest puste
        if self.str_ustawienia_konta_ui.le_imie.text():
            self.str_ustawienia_konta_ui.btn_imie_edit.show()
            self.str_ustawienia_konta_ui.btn_imie_accept.hide()
            self.str_ustawienia_konta_ui.btn_imie_cancel.hide()
            self.str_ustawienia_konta_ui.le_imie.setReadOnly(True)
            self.str_ustawienia_konta_ui.pole_imie_nie_moze.hide()

            # Przypisanei nowego imienia
            imie = self.str_ustawienia_konta_ui.le_imie.text()
            self.str_ustawienia_konta_ui.le_imie.setText(imie)
            obd.save_new_first_name(self.logged_user_id, imie)


    def evt_btn_nazwisko_accept_clicked(self):
        self.str_ustawienia_konta_ui.btn_nazwisko_edit.show()
        self.str_ustawienia_konta_ui.btn_nazwisko_accept.hide()
        self.str_ustawienia_konta_ui.btn_nazwisko_cancel.hide()
        self.str_ustawienia_konta_ui.le_nazwisko.setReadOnly(True)

        nazwisko = self.str_ustawienia_konta_ui.le_nazwisko.text()
        self.str_ustawienia_konta_ui.le_nazwisko.setText(nazwisko)
        obd.save_new_last_name(self.logged_user_id, nazwisko)


    # wcisniecie przycisku anuluj dla kazdego z pol
    def evt_btn_imie_cancel_clicked(self):
        self.str_ustawienia_konta_ui.pole_imie_nie_moze.hide()
        self.str_ustawienia_konta_ui.le_imie.setReadOnly(True)
        self.str_ustawienia_konta_ui.btn_imie_edit.show()
        self.str_ustawienia_konta_ui.btn_imie_accept.hide()
        self.str_ustawienia_konta_ui.btn_imie_cancel.hide()
        updated_user_info = obd.get_user_info_by_id(self.logged_user_id)
        # Przywrocenie domyslnego imienia z bazy danych
        self.str_ustawienia_konta_ui.le_imie.setText(updated_user_info["first_name"])

    def evt_btn_nazwisko_cancel_clicked(self):
        self.str_ustawienia_konta_ui.le_nazwisko.setReadOnly(True)
        self.str_ustawienia_konta_ui.btn_nazwisko_edit.show()
        self.str_ustawienia_konta_ui.btn_nazwisko_accept.hide()
        self.str_ustawienia_konta_ui.btn_nazwisko_cancel.hide()
        updated_user_info = obd.get_user_info_by_id(self.logged_user_id)

        # Przywrocenie domyslnego nazwiska z bazy danych
        self.str_ustawienia_konta_ui.le_nazwisko.setText(updated_user_info["last_name"])



    # ZMIEN HASLO OBSLUGA ZDARZEN
    # ----------------------------------------------------
    # 1) Kliknięcie na przycisk <- (Powrót)
    def evt_btn_powrot_clicked(self):
        # - zmiana strony z powrotem na stronę ustawienia konta
        self.ui.zawartosc_okna.setCurrentWidget(self.str_ustawienia_konta)

        # Przywrócenie pustych wartości
        self.str_zmiana_hasla_ui.btn_biezace_haslo_pokaz.setChecked(False)
        self.str_zmiana_hasla_ui.le_biezace_haslo.setEchoMode(QtWidgets.QLineEdit.Password)
        self.str_zmiana_hasla_ui.btn_nowe_haslo_pokaz.setChecked(False)
        self.str_zmiana_hasla_ui.le_nowe_haslo.setEchoMode(QtWidgets.QLineEdit.Password)
        self.str_zmiana_hasla_ui.btn_potwierdz_nowe_haslo.setChecked(False)
        self.str_zmiana_hasla_ui.le_potwierdz_nowe_haslo.setEchoMode(QtWidgets.QLineEdit.Password)

        self.str_zmiana_hasla_ui.podano_bledne_biezace_haslo.hide()
        self.str_zmiana_hasla_ui.nowe_haslo_nie_moze.hide()
        self.str_zmiana_hasla_ui.hasla_nie_sa_takie.hide()
        self.str_zmiana_hasla_ui.nowe_haslo_musi.hide()

        self.str_zmiana_hasla_ui.le_biezace_haslo.setText("")
        self.str_zmiana_hasla_ui.le_nowe_haslo.setText("")
        self.str_zmiana_hasla_ui.le_potwierdz_nowe_haslo.setText("")


    # ------------------------------------------------------
    # 2) Zmiana widoczności haseł
    # - umożliwia przełączanie między widocznością haseł
    # - po wciśnięciu przycisku zamiast "****" zobaczymy "abcd"
    # - albo zamiast "abcd" zobaczymy "****"
    def evt_echoMode_changed_le_biezace_haslo(self):
        # Przypisanie bieżącego trybu widoczności
        current_echo_mode = self.str_zmiana_hasla_ui.le_biezace_haslo.echoMode()

        # Jeżeli tryb jest Trybem Hasła (****) to zmieniamy na Tryb Normalny (abcd)
        if current_echo_mode == QtWidgets.QLineEdit.Password:
            self.str_zmiana_hasla_ui.le_biezace_haslo.setEchoMode(QtWidgets.QLineEdit.Normal)
        # W przeciwnym wypadku zmieniamy na tryb hasła (****)
        else:
            self.str_zmiana_hasla_ui.le_biezace_haslo.setEchoMode(QtWidgets.QLineEdit.Password)

    def evt_echoMode_changed_le_nowe_haslo(self):
        current_echo_mode = self.str_zmiana_hasla_ui.le_nowe_haslo.echoMode()
        if current_echo_mode == QtWidgets.QLineEdit.Password:
            self.str_zmiana_hasla_ui.le_nowe_haslo.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.str_zmiana_hasla_ui.le_nowe_haslo.setEchoMode(QtWidgets.QLineEdit.Password)

    def evt_echoMode_changed_le_potwierdz_nowe_haslo(self):
        current_echo_mode = self.str_zmiana_hasla_ui.le_potwierdz_nowe_haslo.echoMode()
        if current_echo_mode == QtWidgets.QLineEdit.Password:
            self.str_zmiana_hasla_ui.le_potwierdz_nowe_haslo.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.str_zmiana_hasla_ui.le_potwierdz_nowe_haslo.setEchoMode(QtWidgets.QLineEdit.Password)

    # ----------------------------------------------------
    # 3) Naciśnięcie na przycisk Zmień Hasło
    # - zmiana hasła + walidacja
    # - w przypadku niepowodzeń wyświetlenie odpowiednich komunikatów
    # (np. że nowe hasło nie może być takie jak bieżące hasło)
        biezace_haslo = self.user_info["password"]
        # self.str_zmiana_hasla_ui.le_biezace_haslo.setText(biezace_haslo)
    def evt_zmien_moje_haslo(self):
        try:
            self.user_info = obd.get_user_info_by_id(self.logged_user_id)
            #Pobranie danych z LineEditów (z Pól danych/Inputów)
            biezace_haslo = self.str_zmiana_hasla_ui.le_biezace_haslo.text()
            #Set the password text
            nowe_haslo = self.str_zmiana_hasla_ui.le_nowe_haslo.text()
            potwierdz_nowe_haslo = self.str_zmiana_hasla_ui.le_potwierdz_nowe_haslo.text()

            #Tutaj powinno zostac przypisane z bazy danych użytkownika hasło
            #- ja tutaj na razie przypisałem "admin"
            poprawne_haslo = self.user_info["password"]

            # Sprawdzam czy biezace_haslo jest zgodne z hasłem użytkownika (poprawne_haslo)
            if biezace_haslo == poprawne_haslo:

                # Ukrywam komunikat "Podano Błędne Bieżące Hasło"
                self.str_zmiana_hasla_ui.podano_bledne_biezace_haslo.hide()

                # Następnie przechodzę dalej i sprawdzam czy Nowe Hasło
                # oraz Potwierdz Nowe Hasło są takie same
                if nowe_haslo == potwierdz_nowe_haslo:

                    # Ukrywam komunikat "Hasła nie są takie same"
                    self.str_zmiana_hasla_ui.hasla_nie_sa_takie.hide()

                    # Sprawdzam czy Nowe Hasło ma więcej lub równo 8 znaków
                    if len(nowe_haslo) >= 8:

                        # Ukrywam komunikat "Nowe Hasło Musi Zawierać Co Najmniej 8 Znaków"
                        self.str_zmiana_hasla_ui.nowe_haslo_musi.hide()

                        # Sprawdzam czy przypadkiem użytkownik nie podał nowego hasła
                        # takiego samego jak hasło wcześniejsze użytkownika (poprawne_haslo)
                        if poprawne_haslo != nowe_haslo:

                            # Wyświetlenie komunikatu "Pomyślnie zmieniono hasło"
                            QtWidgets.QMessageBox.information(self, "Sukces!", "Pomyślnie zmieniono hasło!")

                            # Zapis do bazy danych tutaj powinien byc
                            # - zapis hasła

                            # Ustawienie w stronie ustawienia konta nowego hasla
                            self.str_ustawienia_konta_ui.le_haslo.setText(nowe_haslo)

                            #Zmiana hasla w bazie danych

                            obd.save_new_password(self.logged_user_id,nowe_haslo)

                            # Przejście do strony ustawień konta
                            self.ui.zawartosc_okna.setCurrentWidget(self.str_ustawienia_konta)

                            # Zresetowanie wartości w stronie zmien haslo
                            self.str_zmiana_hasla_ui.le_biezace_haslo.setText("")
                            self.str_zmiana_hasla_ui.le_nowe_haslo.setText("")
                            self.str_zmiana_hasla_ui.le_potwierdz_nowe_haslo.setText("")

                            self.str_zmiana_hasla_ui.hasla_nie_sa_takie.hide()
                            self.str_zmiana_hasla_ui.nowe_haslo_musi.hide()
                            self.str_zmiana_hasla_ui.nowe_haslo_nie_moze.hide()
                            self.str_zmiana_hasla_ui.podano_bledne_biezace_haslo.hide()

                            self.str_zmiana_hasla_ui.btn_biezace_haslo_pokaz.setChecked(False)
                            self.str_zmiana_hasla_ui.btn_nowe_haslo_pokaz.setChecked(False)
                            self.str_zmiana_hasla_ui.btn_potwierdz_nowe_haslo.setChecked(False)

                            self.str_zmiana_hasla_ui.le_biezace_haslo.setEchoMode(QtWidgets.QLineEdit.Password)
                            self.str_zmiana_hasla_ui.le_nowe_haslo.setEchoMode(QtWidgets.QLineEdit.Password)
                            self.str_zmiana_hasla_ui.le_potwierdz_nowe_haslo.setEchoMode(QtWidgets.QLineEdit.Password)

                        # Przypadek gdy użytkownik podał takie samo nowe hasło jak
                        # poprzednie hasło użytkownika
                        else:
                            # Wyswietlenie komunikatu "Nowe Hasło Nie Może Być Takie Samo Jak Bieżące Hasło"
                            self.str_zmiana_hasla_ui.nowe_haslo_nie_moze.show()

                    # Przypadek gdy nowe hasło nie zawiera 8 znaków
                    else:
                        # Wyswietlenie komunikatu "Nowe Hasło Musi Zawierać Co Najmniej 8 Znaków"
                        self.str_zmiana_hasla_ui.nowe_haslo_musi.show()

                # Przypadek gdy nowe hasło i potwierdź nowe hasło nie są takie same
                else:
                    # Komunikat "Hasla Nie Sa Takie Same"
                    self.str_zmiana_hasla_ui.hasla_nie_sa_takie.show()

            # Przypadek gdy biezace_haslo nie jest poprawne (nie jest to haslo uzytkownika)
            else:
                # Komunikat "Podano Bledne Biezace Haslo"
                self.str_zmiana_hasla_ui.podano_bledne_biezace_haslo.show()

        except Exception as e:
            # Display the error message for debugging purposes
            QtWidgets.QMessageBox.critical(self, "Błąd", f"Wystąpił błąd: {str(e)}")
            print(f"Error: {str(e)}")

    # wcisniecie przycisku usun konto
    def evt_btn_usun_konto(self):
        msg_box = QtWidgets.QMessageBox(self)
        msg_box.setWindowTitle("Usunięcie konta")
        msg_box.setText(
            "Czy jesteś pewien, że chcesz usunąć konto?\nUsuwając konto nigdy nie odzyskasz jego danych z powrotem.")
        tak_button = msg_box.addButton("Tak", QtWidgets.QMessageBox.YesRole)
        nie_button = msg_box.addButton("Nie", QtWidgets.QMessageBox.NoRole)
        msg_box.setDefaultButton(nie_button)  # Ustawienie domyślnego przycisku na "Nie"
        msg_box.setStyleSheet("""
                QLabel {
                    font-size: 18px;
                    font-weight: 400;
                }
                """)

        msg_box.exec()

        if msg_box.clickedButton() == tak_button:
            print(f"Deleting user with ID: {self.logged_user_id}")
            try:
                obd.delete_user_from_db(self.logged_user_id)
                print("User deleted successfully.")
            except Exception as e:
                print(f"Error deleting user: {e}")
                QtWidgets.QMessageBox.critical(self, 'Błąd', f'Wystąpił błąd podczas usuwania konta: {e}')
                return

            print("Reinitializing the main dialog (DlgMain).")
            self.run = run.DlgMain()  # Assuming run.DlgMain() is correctly imported and implemented
            self.run.show()
            print("DlgMain shown successfully.")
            self.close()
            print("Current dialog closed successfully.")
        else:
            print("User chose not to delete the account.")
            return


    # USTAWIENIA APLIKACJI OBSLUGA ZDARZEN
    # Zmiana Motywow + ich definicje
    def zmien_motyw(self, index):
        motyw = Zmiana_Motywow.ZmianaMotywow()
        if index == 0:
            # Ustawienie jasnego motywu
            self.setStyleSheet(motyw.pobierz_styl_jasny())
            self.str_glowna.setStyleSheet(motyw.pobierz_styl_jasny())
            self.str_kalendarz.setStyleSheet(motyw.pobierz_styl_jasny())
            self.str_ustawienia_konta_ui.app_usun_konto.setStyleSheet(motyw.pobierz_styl_jasny())
        elif index == 1:
            # Ustawienie ciemnego motywu
            self.setStyleSheet(motyw.pobierz_styl_ciemny())
            self.str_glowna.setStyleSheet(motyw.pobierz_styl_ciemny())
            self.str_kalendarz.setStyleSheet(motyw.pobierz_styl_ciemny())
            self.str_ustawienia_konta_ui.app_usun_konto.setStyleSheet("""
                #app_usun_konto {
                    border-style:solid;
                    border-radius:15px;
                    border-width:2px;
                    border-color: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #1565C0, stop:1 #9C27B0);
                }
                """)

    # Wciśnięcie przycisku "Przejdź do ustawień konta"
    # - przeniesienie na strone ustawien konta
    # - ustawienie na pasku zadan przyciskow Ustawienia_Konta na podswietlane na bialo
    # zeby uzytkownik wiedzial gdzie jest
    def evt_ustawienia_btn_ustawienia_konta_clicked(self):
        self.ui.zawartosc_okna.setCurrentWidget(self.str_ustawienia_konta)
        self.ui.btn_konto.setChecked(True)
        self.ui.btn_konto_3.setChecked(True)

    # Wciśnięcie przypisku Zapisz Zmiany
    def evt_btn_zapisz_zmiany_clicked(self):
        # Pobranie wybranych przez uzytkownika ustawien
        # - wartosci sa w jako string, wiec mozna je od razu zapisywac do bazy danych
        motyw = self.str_ustawienia_aplikacji_ui.combo_motyw.currentText()

        # Zmiana motywu
        index_motyw = self.str_ustawienia_aplikacji_ui.combo_motyw.currentIndex()
        self.zmien_motyw(index_motyw)

        # Sprawdzenie czy faktycznie dobrze pobiera i czy faktycznie sa w string
        # print(motyw,powiadomienia,type(motyw),type(powiadomienia))

        # Zapis do bazy danych
        obd.save_new_theme(self.logged_user_id, motyw)

        # Wyswietlenie komunikatu o poprawnym zapisie ustawien
        # - wraz z niedziałająca na razie animacją xd, później zrobię
        # - a także ukrycie komunikatu o niezapisanych ustawieniach
        self.str_ustawienia_aplikacji_ui.zmiany_zostaly_zapisane.show()
        self.hide_message_gradually(self.str_ustawienia_aplikacji_ui.zmiany_zostaly_zapisane)
        self.str_ustawienia_aplikacji_ui.zmiany_nie_zostaly.hide()
        self.str_ustawienia_aplikacji_ui.przywrocono_domyslne_ustawienia.hide()

        # ukrycie komunikatu o niezapisanych ustawieniach i o przywroceniu domyslnych ustawien
        self.str_ustawienia_aplikacji_ui.zmiany_nie_zostaly.hide()
        self.str_ustawienia_aplikacji_ui.przywrocono_domyslne_ustawienia.hide()

    # Wcisniecie przypisku Anuluj
    def evt_btn_anuluj_zmiany_clicked(self):
        # - przywraca tekst jaki byl w bazie danych

        self.str_ustawienia_aplikacji_ui.combo_motyw.setCurrentText(obd.get_user_theme(self.logged_user_id))
        #self.str_ustawienia_aplikacji_ui.combo_motyw.setCurrentText(self.user_powiadomienia)

        # - ukrywa komunikat o niezapisanych ustawieniach i o domyslnych ustawieniach
        self.str_ustawienia_aplikacji_ui.zmiany_nie_zostaly.hide()
        self.str_ustawienia_aplikacji_ui.przywrocono_domyslne_ustawienia.hide()

    # Wcisniecie przycisku Przywroc domyslne ustawienia
    def evt_btn_przywroc_domyslne_ustawienia_clicked(self):
        domyslny_motyw_index = 0  # 0 - jasny, 1 - ciemny

        # przywrocenie domyslnych ustawien
        self.str_ustawienia_aplikacji_ui.combo_motyw.setCurrentIndex(domyslny_motyw_index)
        self.zmien_motyw(domyslny_motyw_index)

        # zapis do bazy danych
        obd.default_theme(self.logged_user_id, "jasny")

        # ukrycie komunikatu o niezapisanych ustawieniach
        self.str_ustawienia_aplikacji_ui.zmiany_nie_zostaly.hide()

        # pokazanie komunikatu o przywroceniu domyslnych ustawien
        self.str_ustawienia_aplikacji_ui.przywrocono_domyslne_ustawienia.show()
        self.hide_message_gradually(self.str_ustawienia_aplikacji_ui.przywrocono_domyslne_ustawienia)
        self.str_ustawienia_aplikacji_ui.zmiany_nie_zostaly.hide()
        self.str_ustawienia_aplikacji_ui.zmiany_zostaly_zapisane.hide()

    # Funkcja przywracajaca ustawienia uzytkownika przy uruchomieniu aplikacji
    def wprowadz_ustawienia(self, motyw):
        # Jezeli user mial motyw jasny to przywroci sie motyw jasny
        # jesli user mial motyw ciemny to przywroci sie ciemny
        #obd.get_user_theme(self.logged_user_id)

        if motyw == "ciemny":
            self.zmien_motyw(1)
        else:
            self.zmien_motyw(0)

    # To mialabyc animacja zanikania komunikatow o zapisie, przywroceniu domyslnych ustawien i o niezapisanych zmianach
    # jednak tutaj zle sa obslugiwane animacje, nie bylo juz czasu zeby poprawic
    def hide_message_gradually(self, komunikat):
        # Utwórz animację przejścia
        self.animation = QPropertyAnimation(komunikat, b"opacity")
        self.animation.setDuration(1500)  # Czas trwania animacji w milisekundach (2 sekundy)
        self.animation.setStartValue(1.0)  # Początkowa wartość przeźroczystości (pełna widoczność)
        self.animation.setEndValue(0.0)  # Końcowa wartość przeźroczystości (całkowicie przezroczyste)

        # Funkcja, która będzie wywoływana w trakcie trwania animacji
        self.animation.valueChanged.connect(self.update_opacity)

        self.animation.finished.connect(lambda: komunikat.hide())
        self.animation.start()

    def update_opacity(self, value):
        # Aktualizacja przezroczystości w trakcie trwania animacji
        self.str_ustawienia_aplikacji_ui.zmiany_zostaly_zapisane.setWindowOpacity(value)

    # Wykrywanie skrotow klawiszowych wcisnietych i ich obsluga
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_1 and event.modifiers() & Qt.ControlModifier:
            self.ui.btn_strona_glowna.click()
        elif event.key() == Qt.Key_2 and event.modifiers() & Qt.ControlModifier:
            self.ui.btn_kalendarz.click()
        elif event.key() == Qt.Key_3 and event.modifiers() & Qt.ControlModifier:
            self.ui.btn_konto.click()
        elif event.key() == Qt.Key_4 and event.modifiers() & Qt.ControlModifier:
            self.ui.btn_ustawienia.click()
        elif event.key() == Qt.Key_5 and event.modifiers() & Qt.ControlModifier:
            self.ui.btn_wyloguj.click()

""" DO TESTOWANIA
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = DlgMain()
    ui.show()
    sys.exit(app.exec_())
"""