class ZmianaMotywow:
    def __init__(self):
        self.styl_jasny = """
        QMainWindow {
	        background-color: white;
        }
        #powiadomienia, #app_usun_konto, #usun_konto, #motyw, #pasek_boczny #skroty_klawiszowe, #skrot_kalendarz, #skrot_strona_glowna, #skrot_ustawienia_konta, #skrot_ustawienia, #skrot_wyloguj,
         #settings_imie, #settings_nazwisko, #settings_haslo, #settings_login, #pasek_boczny, #skroty_klawiszowe, #ustawienia_konta_app, #usun_konto,
         #potwierdz_nowe_haslo, #nowe_haslo, #biezace_haslo,
         #skrot_kalendarz_f1, #skrot_kalendarz_f2, #skrot_kalendarz_f3,
         #skrot_kalendarz_f4,
         #skrot_kalendarz_f5, #skrot_kalendarz_f6, #skrot_kalendarz_f7,
         #skrot_kalendarz_f8, #skrot_kalendarz_f9{
            border-style:solid;
            border-radius:15px;
            border-width:2px;
            border-color: #C9F7FF;
            background-color: white;
        }
        QFrame#pasek, QFrame#pasek_hover {
            background-color: #019bff;
        }
        QPushButton#btn_sidebar_zwin_calosc {
            background-color:transparent;
        }
        QPushButton {
            font-size:18px;
            font-weight:400;
            background-color: #019bff; /* Kolor tła */
            border: none; /* Brak obramowania */
            color: white; /* Kolor czcionki */
            padding: 10px 20px; /* Wielkość przycisku */
            border-radius: 15px; /* Zaokrąglenie krawędzi */
            height:33px;
        }
        QPushButton:hover {
            background-color: #1565C0; /* Kolor tła po najechaniu myszką */
        }
        QPushButton:pressed {
            background-color: #0D47A1; /* Kolor tła po kliknięciu */
        }
        QPushButton:checked {
            background-color: white;
            color: #019bff;
        }
        QLabel, #lblSrt, #lblEnd {
            color: #2c2c84;
            font-size:22px;
            font-weight:700;
            border-color:#019bff;
        }     
        #lblN, #lblD {
            font-weight: bold;
            font-size: 35px;
            border-color:#019bff;
        }
        QTextEdit, #leTaskDescription {
            padding: 10px 20px; /* Wielkość przycisku */
            border-radius: 15px; /* Zaokrąglenie krawędzi */
            font-size: 20px;
            background-color: palette(base);
            color: black;
            border: 2px solid qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #1565C0, stop:1 #9C27B0); /* Border with gradient color */
        }
        QLineEdit, #leTaskName {
            color: black;
            font-size: 20px;
            padding: 10px 20px; /* Wielkość przycisku */
            border-radius: 15px; /* Zaokrąglenie krawędzi */
            border: 2px solid qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #1565C0, stop:1 #9C27B0); /* Border with gradient color */
        }
        #leTaskName:pressed{
            color: black;
        }
        QComboBox {
            padding: 10px 40px 10px 20px; /* Adjust padding as needed */
            border-radius: 15px; /* Round the corners */
            border:none;
            font-size: 20px;
            color: white;
            height:33px;
            font-weight:400;
            background: #019bff;
            background-image: url("../resources/chevron-down.svg"); /* Set the background image */
            background-repeat: no-repeat; /* Prevent image from repeating */
            background-position: right center; /* Position the arrow on the right side */
        }
        QComboBox:hover {
            background-color: #1565C0;
            background-image: url("../resources/chevron-down.svg"); /* Set the background image */
            background-repeat: no-repeat; /* Prevent image from repeating */
            background-position: right center; /* Position the arrow on the right side */
        }
        QComboBox:pressed {
            background-color: #0D47A1;
            background-image: url("../resources/chevron-down.svg"); /* Set the background image */
            background-repeat: no-repeat; /* Prevent image from repeating */
            background-position: right center; /* Position the arrow on the right side */
        }  
        QComboBox QAbstractItemView {
            background: #019bff;
            color: white;
            padding:10px;
            border: 2px solid white;
            border-radius:15px;
        }
        QComboBox::drop-down {
            width: 0px;
        }
        QTimeEdit::up-button,
        QTimeEdit::down-button {
            width: 0px;
        }
        QTableWidget {
            padding: 10px 20px; /* Wielkość przycisku */
            border-radius: 15px; /* Zaokrąglenie krawędzi */
            background-color: palette(base);;
            border: 2px solid qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #1565C0, stop:1 #9C27B0); /* Border with gradient color */
            color: #2c2c84;
            font-size: 15px;
        }
        QCalendarWidget {
            padding: 10px 20px; /* Wielkość przycisku */
            border-radius: 15px; /* Zaokrąglenie krawędzi */
            background-color: palette(base);;
            border: 2px solid qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #1565C0, stop:1 #9C27B0); /* Border with gradient color */
        }
        QTableWidget QHeaderView::section {
            font-weight: bold;
            font-size: 20px; /* Change font size */
            color: #2c2c84; /* Change font color */
        }
        QTimeEdit {
            padding: 10px 20px; /* Wielkość przycisku */
            border-radius: 15px; /* Zaokrąglenie krawędzi */
            font-size: 20px;
            border: 2px solid qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #1565C0, stop:1 #9C27B0); /* Border with gradient color */
            color:black;
        }
        #btn_skroty_klawiszowe {
            border-style:solid;
            border-width:2px;
            border-color:#019bff;
            color:#019bff;
        }
        QFrame#lewo, QFrame#prawo {
	        background-color: #E4FFFC;
        }
        QPushButton#btn_usun_konto, #btn_zmien_haslo {
	        background-color: #ff4d4d;
	        color: white;
	        font-weight:500;
        }
        QPushButton:hover#btn_usun_konto, #btn_zmien_haslo:hover {
	        background-color: #cc3333;
        }
        QPushButton:pressed#btn_usun_konto, #btn_zmien_haslo:pressed {
	        background-color: #993333;
        }
        #btn_zmien_haslo {
            font-size:28px;
            font-weight:600;
        }
        #btn_powrot_skroty_klawiszowe, #btn_powrot {
            background-color: white; /* Kolor tła */
            border: none; /* Brak obramowania */
            color: white; /* Kolor czcionki */
            padding: 10px 20px; /* Wielkość przycisku */
            border-radius: 15px; /* Zaokrąglenie krawędzi */
        }
        #btn_powrot_skroty_klawiszowe:hover, #btn_powrot:hover {
            background-color: #E6E6FF; /* Kolor tła po najechaniu myszką */
        }
        #btn_powrot_skroty_klawiszowe:pressed, #btn_powrot:pressed {
            background-color: #CCCCFF; /* Kolor tła po kliknięciu */
        }
        #btn_imie_edit,#btn_imie_cancel,#btn_imie_accept,#btn_haslo_edit,#btn_nazwisko_edit,#btn_nazwisko_cancel,#btn_nazwisko_accept{
            background-color: white; /* Kolor tła */
            border: none; /* Brak obramowania */
            color: white; /* Kolor czcionki */
            padding: 10px 20px; /* Wielkość przycisku */
            border-radius: 15px; /* Zaokrąglenie krawędzi */
        }
        #btn_imie_edit:hover,#btn_imie_cancel:hover,#btn_imie_accept:hover,#btn_haslo_edit:hover,#btn_nazwisko_edit:hover,#btn_nazwisko_cancel:hover,#btn_nazwisko_accept:hover{
            background-color: #E6E6FF; /* Kolor tła po najechaniu myszką */
        }
        #btn_imie_edit:pressed,#btn_imie_cancel:pressed,#btn_imie_accept:pressed,#btn_haslo_edit:pressed,#btn_nazwisko_edit:pressed,#btn_nazwisko_cancel:pressed,#btn_nazwisko_accept:pressed {
            background-color: #CCCCFF; /* Kolor tła po kliknięciu */
        }
        #le_imie, #le_nazwisko, #le_login, #le_haslo, #le_biezace_haslo, #le_nowe_haslo, #le_potwierdz_nowe_haslo {
            border-style:solid;
            border-radius:15px;
            border-width:2px;
            padding-left:10px;
            padding-right:10px;
            border-color:#4db8ff;
            color: #2c2c84;
            font-size: 18px;
        }
        #le_imie:focus, #le_nazwisko:focus, #le_login:focus, #le_haslo:focus {
            border-color: #019bff;
        }
        #usun_konto {
            border:none;
        }
        #lb_pole_imie_nie_moze,#lb_podano_bledne, #lb_nowe_haslo_nie_moze, #lb_nowe_haslo_musi, #lb_hasla_nie_sa_takie {
	        color: #ff4d4d;
	        font-size:18px;
	        font-weight:400;
        }
        #lb_spowoduje {
            font-size: 20px;
            font-weight:400;
        }
        QPushButton#btn_usun_konto {
            background-color: #ff4d4d;
            color: white;
        }
        QPushButton:hover#btn_usun_konto {
            background-color: #cc3333;
        }
        QPushButton:pressed#btn_usun_konto {
            background-color: #993333;
        }      
        QPushButton#btn_usun_konto_2 {
            background-color: #ff4d4d;
            color: white;
        }
        QPushButton:hover#btn_usun_konto_2 {
            background-color: #cc3333;
        }
        QPushButton:pressed#btn_usun_konto_2 {
            background-color: #993333;
        }
        #lb_nowe_haslo_nie_moze, #lb_hasla_nie_sa_takie, #lb_nowe_haslo_musi,#lb_podano_bledne {
            color: #ff4d4d;
        }
        /* Style dla komunikatów */
        #zmiany_zostaly_zapisane, #lb_zmiany_zostaly_zapisane {
            background-color: #32CD32;
            color: white;
            font-size:18px;
        }
        #zmiany_nie_zostaly, #lb_zmiany_nie_zostaly {
            background-color: #FF8C00;
            color: white;
            font-size:18px;
        }
        #przywrocono_domyslne_ustawienia, #lb_przywrocono_domyslne_ustawienia {
            background-color: #1E90FF;
            color: white;
            font-size:18px;
        }

        /* Style dla przycisków */
        #btn_zapisz_zmiany {
            background-color: #32CD32;
            font-weight: 800;
            font-size: 19px;
            color: white;
            border: none;
            padding: 10px 20px;
            cursor: pointer;
        }
        #btn_anuluj_zmiany {
            background-color: white;
            border-color: #1E90FF;
            border-style: solid;
            border-width: 2px;
            font-weight: 800;
            font-size: 19px;
            color: #1E90FF;
            padding: 10px 20px;
            cursor: pointer;
        }
        #btn_przywroc_domyslne_ustawienia {
            background-color: #1E90FF;
            font-weight: 800;
            font-size: 19px;
            color: white;
            border: none;
            padding: 10px 20px;
            cursor: pointer;
        }

        /* Efekty hover */
        #zmiany_zostaly_zapisane:hover, #lb_zmiany_zostaly_zapisane:hover {
            background-color: #28a745; /* Darker green */
        }
        #zmiany_nie_zostaly:hover, #lb_zmiany_nie_zostaly:hover {
            background-color: #e07b00; /* Darker orange */
        }
        #przywrocono_domyslne_ustawienia:hover, #lb_przywrocono_domyslne_ustawienia:hover {
            background-color: #1c86ee; /* Darker blue */
        }
        #btn_zapisz_zmiany:hover {
            background-color: #28a745; /* Darker green */
        }
        #btn_anuluj_zmiany:hover {
            background-color: #f0f0f0;
            color: #1E90FF;
        }
        #btn_przywroc_domyslne_ustawienia:hover {
            background-color: #1c86ee; /* Darker blue */
        }

        /* Efekty pressed */
        #btn_zapisz_zmiany:pressed {
            background-color: #228B22; /* Even darker green */
        }
        #btn_anuluj_zmiany:pressed {
            background-color: #dcdcdc;
            color: #1E90FF;
        }
        #btn_przywroc_domyslne_ustawienia:pressed {
            background-color: #1a78d2; /* Even darker blue */
        }

        #wstep_label, #wstep_label_2, #lblTasks, #lb_ustawienia_konta, #lb_ustawienia_aplikacji, #lb_zmien_haslo, #lb_skroty_skroty_klawiszowe, #lb_skroty_kalendarz_tekst {
            font-weight: bold;
            font-size: 35px;
            border-color: #1E88E5;
        }
        #btn_ustawienia_konta, #btn_skroty_klawiszowe, #combo_motyw{
            color: #019bff;
            background-color: white;
            border: 2px solid #019bff;
        }
        #btn_ustawienia_konta:hover, 
        #btn_skroty_klawiszowe:hover, 
        #combo_motyw:hover {
            background-color:#E6E6FF;
        }
        #btn_ustawienia_konta:pressed, 
        #btn_skroty_klawiszowe:pressed, 
        #combo_motyw:pressed {
            background-color: #CCCCFF;
        }
        #combo_motyw QAbstractItemView {
            background: white;
            color: #019bff;
            padding:10px;
            border: 2px solid #019bff;
            border-radius:15px;
        }
        #leTaskDescription {
            color:black;
        }
        #btn_powrot, #btn_powrot_skroty_klawiszowe, #btn_biezace_haslo_pokaz,
        #btn_nowe_haslo_pokaz, #btn_potwierdz_nowe_haslo{
            background-color: transparent;
        }
        #btn_powrot:hover, 
        #btn_powrot_skroty_klawiszowe:hover, 
        #btn_biezace_haslo_pokaz:hover, 
        #btn_nowe_haslo_pokaz:hover, 
        #btn_potwierdz_nowe_haslo:hover {
            background-color: #E6E6FF;
        }
        #btn_powrot:pressed, 
        #btn_powrot_skroty_klawiszowe:pressed, 
        #btn_biezace_haslo_pokaz:pressed, 
        #btn_nowe_haslo_pokaz:pressed, 
        #btn_potwierdz_nowe_haslo:pressed {
            background-color: #CCCCFF;
        }
        #btn_strona_glowna_3, #btn_kalendarz_3, #btn_konto_3, #btn_ustawienia_3, #btn_wyloguj_3 {
            font-weight:400;
        }

        """

        self.styl_ciemny = """
        QMainWindow {
            background-color: #2E2E2E; /* Ciemne tło */
        }
        QFrame#pasek, QFrame#pasek_hover {
            background-color: #262626; /* Ciemniejszy odcień niebieskiego */
        }
        QPushButton#btn_sidebar_zwin_calosc {
            background-color: transparent;
        }
        #btn_kalendarz, #btn_konto, #btn_strona_glowna, #btn_ustawienia, #btn_wyloguj,
        #btn_kalendarz_3, #btn_konto_3, #btn_strona_glowna_3, #btn_ustawienia_3, #btn_wyloguj_3, #btn_sidebar_zwin, #btn_sidebar_zwin_2{
            background-color: #262626;
            border:none;
        }
        #btn_kalendarz:hover, #btn_konto:hover, #btn_strona_glowna:hover, #btn_ustawienia:hover, #btn_wyloguj:hover,
        #btn_kalendarz_3:hover, #btn_konto_3:hover, #btn_strona_glowna_3:hover, #btn_ustawienia_3:hover, #btn_wyloguj_3:hover, #btn_sidebar_zwin:hover,#btn_sidebar_zwin_2:hover {
            background-color: #363636; /* Kolor ciemniejszy niż #262626 */
        }
        #btn_kalendarz:pressed, #btn_konto:pressed, #btn_strona_glowna:pressed, #btn_ustawienia:pressed, #btn_wyloguj:pressed,#btn_sidebar_zwin:pressed,#btn_sidebar_zwin_2:pressed,
        #btn_kalendarz_3:pressed, #btn_konto_3:pressed, #btn_strona_glowna_3:pressed, #btn_ustawienia_3:pressed, #btn_wyloguj_3:pressed {
            background-color: #1e1e1e; /* Kolor jeszcze ciemniejszy */
        }
        #btn_kalendarz:checked, #btn_konto:checked, #btn_strona_glowna:checked, #btn_ustawienia:checked, #btn_wyloguj:checked,
        #btn_kalendarz_3:checked, #btn_konto_3:checked, #btn_strona_glowna_3:checked, #btn_ustawienia_3:checked, #btn_wyloguj_3:checked {
            background-color: #1e1e1e; /* Kolor jeszcze ciemniejszy */
            border: 2px solid qlineargradient(x1:1, y1:0, x2:0, y2:0, stop:0 #1565C0, stop:1 #9C27B0);
        }
        QPushButton {
            font-size:18px;
            background-color: qlineargradient(x1:1, y1:0, x2:0, y2:0, stop:0 #1565C0, stop:1 #9C27B0); /* Gradientowy kolor przycisków */
            border: none;
            color: white;
            padding: 10px 20px;
            border-radius: 15px;
        }
        QPushButton:hover {
            background-color: qlineargradient(x1:1, y1:0, x2:0, y2:0, stop:0 #1E88E5, stop:1 #BA68C8); /* Jaśniejszy gradient przy hover */
        }

        QPushButton:pressed {
            background-color: qlineargradient(x1:1, y1:0, x2:0, y2:0, stop:0 #0D47A1, stop:1 #7B1FA2); /* Ciemniejszy gradient przy pressed */
        }
        QPushButton:checked {
            background-color: #2E2E2E; /* Tło przycisku w kolorze tła */
            color: #1E88E5;
        }
        QLabel, #lblSrt, #lblEnd, #lblTasks, #lb_ustawienia_konta, #lb_nazwisko,#lb_imie,#lb_login,#lb_haslo {
            color: white;
        }
        #btn_powrot, #btn_powrot_skroty_klawiszowe, #btn_biezace_haslo_pokaz,
        #btn_nowe_haslo_pokaz, #btn_potwierdz_nowe_haslo{
            background-color: transparent;
        }
        #btn_powrot:hover, 
        #btn_powrot_skroty_klawiszowe:hover, 
        #btn_biezace_haslo_pokaz:hover, 
        #btn_nowe_haslo_pokaz:hover, 
        #btn_potwierdz_nowe_haslo:hover {
            border: 2px solid qlineargradient(x1:1, y1:0, x2:0, y2:0, stop:0 #1565C0, stop:1 #9C27B0);
        }
        #btn_powrot:pressed, 
        #btn_powrot_skroty_klawiszowe:pressed, 
        #btn_biezace_haslo_pokaz:pressed, 
        #btn_nowe_haslo_pokaz:pressed, 
        #btn_potwierdz_nowe_haslo:pressed {
            border: 2px solid qlineargradient(x1:1, y1:0, x2:0, y2:0, stop:0 #1565C0, stop:1 #9C27B0);
        }
        #btn_sidebar_zwin_calosc:hover, #btn_sidebar_zwin_calosc:pressed {
            border: 2px solid qlineargradient(x1:1, y1:0, x2:0, y2:0, stop:0 #1565C0, stop:1 #9C27B0);
        }
        #wstep_label, #lblTasks, #wstep_label_2  {
            font-weight: bold;
            font-size: 35px;
            border-color: #1E88E5;
        }
        #wstep_label,#wstep_label_2, #lblTasks, #lb_ustawienia_konta, #lb_ustawienia_aplikacji, #lb_zmien_haslo, #lb_skroty_skroty_klawiszowe, #lb_skroty_kalendarz_tekst {
            font-weight: bold;
            font-size: 35px;
        }
        QLabel, #lblSrt, #lblEnd {
            color: white;
            font-size:22px;
            font-weight:700;
            border-color:#019bff;
        } 
        QTextEdit {
            padding: 10px 20px;
            border-radius: 15px;
            font-size: 20px;
            color: white;
            background-color: #424242; /* Ciemne tło */
            border: 2px solid qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #1565C0, stop:1 #9C27B0);
        }
        QLineEdit, #leTaskName {
            color: white; /* Jasnoszary kolor czcionki */
            font-size: 20px;
            padding: 10px 20px;
            border-radius: 15px;
            background-color: #424242; /* Ciemne tło */
            border: 2px solid qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #1565C0, stop:1 #9C27B0);
        }
        #leTaskName:pressed {
            color: white;
        }
        QComboBox {
            padding: 10px 40px 10px 20px;
            border-radius: 15px;
            border: none;
            font-size: 20px;
            color: white;
            height: 33px;
            background-color: qlineargradient(x1:1, y1:0, x2:0, y2:0, stop:0 #1565C0, stop:1 #9C27B0);
            background-image: url("../resources/chevron-down.svg");
            background-repeat: no-repeat;
            background-position: right center;
        }
        QComboBox:hover {
            background-color: qlineargradient(x1:1, y1:0, x2:0, y2:0, stop:0 #1E88E5, stop:1 #BA68C8);
            background-image: url("../resources/chevron-down.svg");
            background-repeat: no-repeat;
            background-position: right center;
        }
        QComboBox:pressed {
            background-color: qlineargradient(x1:1, y1:0, x2:0, y2:0, stop:0 #0D47A1, stop:1 #7B1FA2);
            background-image: url("../resources/chevron-down.svg");
            background-repeat: no-repeat;
            background-position: right center;
        }
        QComboBox::drop-down {
            width: 0px;
        }
        QComboBox QAbstractItemView {
            background: qlineargradient(x1:1, y1:0, x2:0, y2:0, stop:0 #1565C0, stop:1 #9C27B0);
            color: white;
            padding:10px;
            border: 2px solid transparent;
            border-radius:15px;
        }
        QTimeEdit::up-button,
        QTimeEdit::down-button {
            width: 0px;
        }
        QTableWidget {
            padding: 10px 20px;
            border-radius: 15px;
            background-color: #424242; /* Ciemne tło */
            border: 2px solid qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #1565C0, stop:1 #9C27B0);
            color: #BBDEFB; /* Jasny niebieski */
            font-size: 15px;
        }
        QTableWidget::horizontalHeader, #header {
            background-color: #424242; /* Ustawienie tła dla nagłówków kolumn */
            color: #BBDEFB; /* Ustawienie koloru tekstu dla nagłówków kolumn */
        }
        QTableWidget QHeaderView::section {
            font-weight: bold;
            font-size: 20px;
            background-color: #424242; /* Ciemne tło */
            color: #BBDEFB; /* Jasny niebieski */
        }
        QTableWidget QTableCornerButton::section {
            background-color: #2E2E2E; /* Ciemniejsze tło nagłówków wierszy */
        }
        QScrollBar:vertical {
            background: #2E2E2E; /* Ciemniejsze tło paska przewijania */
        }
        QScrollBar::handle:vertical {
            background: #1E88E5; /* Kolor uchwytu paska przewijania */
        }
        QScrollBar::add-line:vertical,
        QScrollBar::sub-line:vertical {
            background: #1E88E5; /* Kolor przycisków na pasku przewijania */
        }
        QScrollBar:horizontal {
            background: #2E2E2E; /* Ciemniejsze tło paska przewijania */
        }
        QScrollBar::handle:horizontal {
            background: #1E88E5; /* Kolor uchwytu paska przewijania */
        }
        QScrollBar::add-line:horizontal,
        QScrollBar::sub-line:horizontal {
            background: #1E88E5; /* Kolor przycisków na pasku przewijania */
        }
        QPushButton#btn_usun_konto, #btn_zmien_haslo {
            font-size:20px;
            background-color: qlineargradient(x1:1, y1:0, x2:0, y2:0, stop:0 #8B0000, stop:1 #FF0000); /* Gradientowy ciemnoczerwony */
            color: #FFFFFF; /* Biały kolor czcionki */
            border:none;
        }
        #lb_pole_imie_nie_moze,#lb_podano_bledne, #lb_nowe_haslo_nie_moze, #lb_nowe_haslo_musi, #lb_hasla_nie_sa_takie {
	        color: #ff4d4d;
	        font-size:18px;
	        font-weight:400;
        }
        #btn_zmien_haslo {
            font-size:25px;
        }
        QPushButton:hover#btn_usun_konto, #btn_zmien_haslo:hover {
            background-color: qlineargradient(x1:1, y1:0, x2:0, y2:0, stop:0 #B22222, stop:1 #FF6347); /* Gradientowy jaśniejszy czerwony */
            border:none;
        }
        QPushButton:pressed#btn_usun_konto, #btn_zmien_haslo:pressed {
            background-color: qlineargradient(x1:1, y1:0, x2:0, y2:0, stop:0 #A52A2A, stop:1 #FA8072); /* Gradientowy ciemniejszy czerwony */
            border:none;
        }
        #powiadomienia, #motyw, #skroty_klawiszowe, #imie, #nazwisko, #login, #haslo, #usun_konto,
        #skrot_kalendarz, #skrot_strona_glowna, #skrot_ustawienia, #skrot_ustawienia_konta,
        #skrot_wyloguj, #biezace_haslo, #nowe_haslo, #potwierdz_nowe_haslo, #pasek_zadan, #ustawienia_konta_app, #pasek_boczny,
        #settings_imie,#settings_nazwisko,#settings_login,#settings_haslo,
        #skrot_kalendarz_f1, #skrot_kalendarz_f2, #skrot_kalendarz_f3,
        #skrot_kalendarz_f4,
        #skrot_kalendarz_f5, #skrot_kalendarz_f6, #skrot_kalendarz_f7,
        #skrot_kalendarz_f8, #skrot_kalendarz_f9 {
            border-style: solid;
            border-radius: 15px;
            border-width: 2px;
            border-color: qlineargradient(x1:1, y1:0, x2:0, y2:0, stop:0 #1565C0, stop:1 #9C27B0);
            background: transparent;
        }
        QFrame#lewo, QFrame#prawo {
            background-color: #37474F; /* Ciemniejsze tło */
        }
        QCalendarWidget {
            padding: 10px 20px;
            border-radius: 15px;
            background-color: #424242; /* Ciemne tło */
            border: 2px solid qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #1565C0, stop:1 #9C27B0);
            color: #E0E0E0; /* Jasnoszary kolor czcionki */
        }
        QMessageBox QLabel {
            color: #white;
            
        }
        QMessageBox{
        background-color: #424242;
        }
        QCalendarWidget QWidget {
            background-color: #424242; /* Ciemne tło */
        }
        QCalendarWidget QToolButton {
            color: #E0E0E0; /* Kolor czcionki */
            background: none; /* Brak tła */
            border: none; /* Brak obramowania */
        }
        QCalendarWidget QToolButton:hover {
            color: #FFFFFF; /* Kolor czcionki po najechaniu */
        }
        QCalendarWidget QToolButton::menu-indicator {
            image: none; /* Brak wskaźnika menu */
        }
        QCalendarWidget QToolButton#qt_calendar_prevmonth, QCalendarWidget QToolButton#qt_calendar_nextmonth {
            border: none; /* Brak obramowania przycisków zmiany miesiąca */
            border-radius: 5px; /* Zaokrąglenie krawędzi */
        }
        QCalendarWidget QToolButton#qt_calendar_prevmonth:hover, QCalendarWidget QToolButton#qt_calendar_nextmonth:hover {
            background-color: #616161; /* Kolor tła po najechaniu */
        }
        QCalendarWidget QMenu {
            background-color: #424242; /* Tło menu */
            color: #E0E0E0; /* Kolor czcionki menu */
        }
        QCalendarWidget QSpinBox {
            background: none; /* Brak tła */
            color: #E0E0E0; /* Kolor czcionki */
            selection-background-color: #1565C0; /* Kolor tła zaznaczenia */
            selection-color: #FFFFFF; /* Kolor czcionki zaznaczenia */
        }
        QCalendarWidget QSpinBox::up-button, QCalendarWidget QSpinBox::down-button {
            border: none; /* Brak obramowania */
            background: none; /* Brak tła */
        }
        QCalendarWidget QSpinBox::up-arrow, QCalendarWidget QSpinBox::down-arrow {
            border: none; /* Brak obramowania */
        }
        QCalendarWidget QTableView {
            background-color: #424242; /* Tło tabeli */
            alternate-background-color: #616161; /* Naprzemienne tło */
        }
        QCalendarWidget QHeaderView::section {
            background-color: #424242; /* Tło nagłówków */
            color: #E0E0E0; /* Kolor czcionki nagłówków */
            padding: 5px;
            border: none; /* Brak obramowania */
        }
        QCalendarWidget QHeaderView::section:horizontal {
            color: #E0E0E0; /* Kolor czcionki nagłówków poziomych */
        }
        QCalendarWidget QHeaderView::section:vertical {
            color: #E0E0E0; /* Kolor czcionki nagłówków pionowych */
        }
        QTimeEdit {
            padding: 10px 20px;
            border-radius: 15px;
            font-size: 20px;
            background-color: #424242; /* Ciemne tło */
            border: 2px solid qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #1565C0, stop:1 #9C27B0);
            color: white; /* Jasnoszary kolor czcionki */
        }

        /* Style dla komunikatów */
        #zmiany_zostaly_zapisane, #lb_zmiany_zostaly_zapisane {
            background-color: #32CD32;
            color: white;
            font-size:18px;
        }
        #zmiany_nie_zostaly, #lb_zmiany_nie_zostaly {
            background-color: #FF8C00;
            color: white;
            font-size:18px;
        }
        #przywrocono_domyslne_ustawienia, #lb_przywrocono_domyslne_ustawienia {
            background-color: #1E90FF;
            color: white;
            font-size:18px;
        }
        #leTaskDescription {
            color: white;
        }
        /* Style dla przycisków */
        #btn_zapisz_zmiany {
            background-color: #32CD32;
            font-weight: 800;
            font-size: 19px;
            color: white;
            border: none;
            padding: 10px 20px;
            cursor: pointer;
        }
        #btn_anuluj_zmiany {
            background-color: white;
            border-color: #1E90FF;
            border-style: solid;
            border-width: 2px;
            font-weight: 800;
            font-size: 19px;
            color: #1E90FF;
            padding: 10px 20px;
            cursor: pointer;
        }
        #btn_przywroc_domyslne_ustawienia {
            background-color: #1E90FF;
            font-weight: 800;
            font-size: 19px;
            color: white;
            border: none;
            padding: 10px 20px;
            cursor: pointer;
        }

        /* Efekty hover */
        #zmiany_zostaly_zapisane:hover, #lb_zmiany_zostaly_zapisane:hover {
            background-color: #28a745; /* Darker green */
        }
        #zmiany_nie_zostaly:hover, #lb_zmiany_nie_zostaly:hover {
            background-color: #e07b00; /* Darker orange */
        }
        #przywrocono_domyslne_ustawienia:hover, #lb_przywrocono_domyslne_ustawienia:hover {
            background-color: #1c86ee; /* Darker blue */
        }
        #btn_zapisz_zmiany:hover {
            background-color: #28a745; /* Darker green */
        }
        #btn_anuluj_zmiany:hover {
            background-color: #f0f0f0;
            color: #1E90FF;
        }
        #btn_przywroc_domyslne_ustawienia:hover {
            background-color: #1c86ee; /* Darker blue */
        }
        #btn_zapisz_zmiany:pressed {
            background-color: #228B22; /* Even darker green */
        }
        #btn_anuluj_zmiany:pressed {
            background-color: #dcdcdc;
            color: #1E90FF;
        }
        #btn_przywroc_domyslne_ustawienia:pressed {
            background-color: #1a78d2; /* Even darker blue */
        }
        #lb_spowoduje {
            font-size: 20px;
            font-weight:400;
        }
        #btn_zapisz_zmiany {
            background-color: qlineargradient(x1:1, y1:0, x2:0, y2:0, stop:0 #388E3C, stop:1 #4CAF50);
        }
        #btn_zapisz_zmiany:hover {
            background-color: qlineargradient(x1:1, y1:0, x2:0, y2:0, stop:0 #2E7D32, stop:1 #388E3C); /* Gradientowy średnio ciemny zielony przy hover */
        }

        #btn_zapisz_zmiany:pressed {
            background-color: qlineargradient(x1:1, y1:0, x2:0, y2:0, stop:0 #1B5E20, stop:1 #2E7D32); /* Gradientowy ciemniejszy zielony przy pressed */
        }
         #btn_anuluj_zmiany {
            border: 2px solid qlineargradient(x1:1, y1:0, x2:0, y2:0, stop:0 #1565C0, stop:1 #9C27B0);
            color: qlineargradient(x1:1, y1:0, x2:0, y2:0, stop:0 #1565C0, stop:1 #9C27B0);
            background-color: qlineargradient(x1:1, y1:0, x2:0, y2:0, stop:0 #FFFFFF, stop:1 #E0E0E0); /* Bardziej kontrastowy biały gradient */
        }

        #btn_anuluj_zmiany:hover {
            border: 2px solid qlineargradient(x1:1, y1:0, x2:0, y2:0, stop:0 #1565C0, stop:1 #9C27B0);
            color: qlineargradient(x1:1, y1:0, x2:0, y2:0, stop:0 #1565C0, stop:1 #9C27B0);
            background-color: qlineargradient(x1:1, y1:0, x2:0, y2:0, stop:0 #E0E0E0, stop:1 #C0C0C0); /* Bardziej kontrastowy jasnoszary gradient przy hover */
        }

        #btn_anuluj_zmiany:pressed {
            border: 2px solid qlineargradient(x1:1, y1:0, x2:0, y2:0, stop:0 #1565C0, stop:1 #9C27B0);
            color: qlineargradient(x1:1, y1:0, x2:0, y2:0, stop:0 #1565C0, stop:1 #9C27B0);
            background-color: qlineargradient(x1:1, y1:0, x2:0, y2:0, stop:0 #C0C0C0, stop:1 #A0A0A0); /* Bardziej kontrastowy ciemniejszy szary gradient przy pressed */
        }
        #btn_przywroc_domyslne_ustawienia {
            font-size: 18px;
            background-color: qlineargradient(x1:1, y1:0, x2:0, y2:0, stop:0 #1565C0, stop:1 #9C27B0); /* Gradientowy kolor przycisków */
            border: none;
            color: white;
            padding: 10px 20px;
            border-radius: 15px;
        }

        #btn_przywroc_domyslne_ustawienia:hover {
            background-color: qlineargradient(x1:1, y1:0, x2:0, y2:0, stop:0 #1E88E5, stop:1 #BA68C8); /* Jaśniejszy gradient przy hover */
        }

        #btn_przywroc_domyslne_ustawienia:pressed {
            background-color: qlineargradient(x1:1, y1:0, x2:0, y2:0, stop:0 #0D47A1, stop:1 #7B1FA2); /* Ciemniejszy gradient przy pressed */
        }

        #le_imie, #le_nazwisko, #le_login, #le_haslo, #le_biezace_haslo, #le_nowe_haslo, #le_potwierdz_nowe_haslo {
            font-size: 18px;
        }

        """

    def pobierz_styl_jasny(self):
        return self.styl_jasny

    def pobierz_styl_ciemny(self):
        return self.styl_ciemny