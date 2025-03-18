import sys
from Zalogowany_użytkownik import zalogowanyUzytkownik
from PyQt5.QtGui import QTextCharFormat, QColor
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTime, QDate
import ObslugaBazyDanych as obd
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TimeForge")

        # Create calendar widget
        self.calendarWidget = QCalendarWidget(self)
        #self.calendarWidget.setStyleSheet(self.sStyle)
        self.calendarWidget.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        min_date = QDate.currentDate().addDays(-365)  # Example: one year ago from today
        max_date = QDate.currentDate().addDays(365)  # Example: one year from today
        self.calendarWidget.setMinimumDate(min_date)
        self.calendarWidget.setMaximumDate(max_date)
        self.calendarWidget.setGridVisible(True)
        self.calendarWidget.setNavigationBarVisible(True)
        self.calendarWidget.selectionChanged.connect(self.update_date_label)

        # Layout for calendar widget
        self.lyCalendar = QVBoxLayout()
        self.lyCalendar.addWidget(self.calendarWidget)

        # Labels with name and date
        self.lblN = QLabel("Witaj $Imie, ")
        self.lblD = QLabel(QDate.currentDate().toString("yyyy-MM-dd"))

        """lblD i lblN trzeba wpisac do stylesheets zamiast wstep_label"""
        self.lblD.setObjectName("wstep_label_2")
        self.lblN.setObjectName("wstep_label")

        self.lblD.setAlignment(Qt.AlignRight)  # Align date label to the right

        # QPushButton to add a task and save changes
        self.pshBtnDodaj = QPushButton("Dodaj")
        self.pshBtnDodaj.setFixedHeight(50)

        """Dodac nalezy connecty"""
        self.pshBtnDodaj.clicked.connect(self.evt_pshBtnDodaj_clicked)

        self.pshBtnUsun = QPushButton("Usuń")
        self.pshBtnUsun.setFixedHeight(50)

        """to tez trzeba dodac"""
        self.pshBtnUsun.clicked.connect(self.delete_selected_row)

        # ComboBox for categories
        self.cmbStates = QComboBox(self)
        self.cmbStates.addItem("Wybierz Kategorie", userData=None)
        self.cmbStates.addItem("Praca")
        self.cmbStates.addItem("Szkoła")
        self.cmbStates.addItem("Studia")
        self.cmbStates.addItem("Rekreacja")
        self.cmbStates.setFixedHeight(50)

        # Input for task name
        self.leTaskName = QLineEdit(self)
        self.leTaskName.setPlaceholderText("Nazwa zadania")

        # Input for task description
        self.leTaskDescription = QTextEdit(self)
        self.leTaskDescription.setPlaceholderText("Opis zadania")

        """Dodac  tutaj connecta"""
        self.leTaskDescription.textChanged.connect(self.evt_leTaskDescription_tChanged)

        #self.leTaskDescription.setStyleSheet(self.sStyle)
        self.leTaskDescription.setFixedHeight(80)

        # Inputs for task start and end time and labels for them
        self.timeStart = QTimeEdit(self)
        self.lblSrt = QLabel("Rozpoczęcie zadania:")
        self.timeEnd = QTimeEdit(self)
        self.lblEnd = QLabel("Koniec zadania:")

        """Connecty dodac"""
        self.timeStart.timeChanged.connect(self.evt_timeStart_tChanged)
        self.timeEnd.editingFinished.connect(self.evt_timeEnd_tChanged)

        self.timeEnd.setFixedHeight(50)
        self.timeStart.setFixedHeight(50)

        # Create widget QTableWidget
        self.tblWidget = QTableWidget(self)
        self.tblWidget.setColumnCount(5)  # 4 columns: Time, Task, Description, Done?
        self.tblWidget.setHorizontalHeaderLabels(["Czas", "Nazwa", "Opis", "Kategoria", "Zrobione?"])
        self.setFixedHeight(500)

        # Adjust column widths
        self.tblWidget.setColumnWidth(0, 80)  # Time
        self.tblWidget.setColumnWidth(1, 100)  # Task
        self.tblWidget.setColumnWidth(2, 350)  # Description
        self.tblWidget.setColumnWidth(3, 100)
        self.tblWidget.setColumnWidth(4, 100)
        self.tblWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        header = self.tblWidget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)
        # Center align labels in QTableWidget and change header font
        # header = self.tblWidget.horizontalHeader()
        # for i in range(5):
        #     header.setDefaultAlignment(Qt.AlignCenter)
        #     header.setStyleSheet("""
        #         font-weight: bold;
        #         font-size: 20px; /* Change font size */
        #         color: #2c2c84;
        #         border:none;"""
        #                          )

        # Layout for button, combobox, and pushbutton
        self.hbox = QHBoxLayout()

        self.hbox.addWidget(self.leTaskName)

        # Layout for time input
        self.hbox2 = QHBoxLayout()
        self.hbox2.addWidget(self.lblSrt)
        self.hbox2.addWidget(self.timeStart)
        self.hbox2.addWidget(self.lblEnd)
        self.hbox2.addWidget(self.timeEnd)

        # Layout for labels: name
        self.hbox3 = QHBoxLayout()
        self.hbox3.addWidget(self.lblN)
        self.hbox3.setContentsMargins(0, 0, 0, 20)

        # layout for buttons
        self.hbox4 = QHBoxLayout()
        self.hbox4.addWidget(self.pshBtnDodaj)
        self.hbox4.addWidget(self.pshBtnUsun)

        # layout for labels: date
        self.hbox5 = QHBoxLayout()
        self.hbox5.addWidget(self.lblD)
        self.hbox5.setContentsMargins(0, 0, 0, 20)

        # calendar layout
        self.lyCalendar = QVBoxLayout()
        self.lyCalendar.addLayout(self.hbox3)
        self.lyCalendar.addWidget(self.calendarWidget)
        self.lyCalendar.setContentsMargins(0, 30, 0, 10)

        # zadania  layout
        self.lyZadania = QVBoxLayout()
        self.lyZadania.addLayout(self.hbox5)
        self.lyZadania.addLayout(self.hbox)
        self.lyZadania.addWidget(self.leTaskDescription)
        self.lyZadania.addWidget(self.cmbStates)
        self.lyZadania.addLayout(self.hbox2)
        self.lyZadania.addLayout(self.hbox4)
        self.lyZadania.addWidget(self.tblWidget)
        self.lyZadania.setContentsMargins(30, 30, 30, 10)

        self.lyMain = QVBoxLayout()

        # Podzielilem layout na 2 osobne zeby sie wysrodkowalo
        self.lyZadaniaKalendarz = QHBoxLayout()
        self.lyZadaniaKalendarz.addLayout(self.lyCalendar, 5)
        self.lyZadaniaKalendarz.addLayout(self.lyZadania, 1)

        # self.lyMain.addLayout(self.lyTop)
        self.lyMain.addLayout(self.lyZadaniaKalendarz)
        self.setLayout(self.lyMain)
        self.setMinimumSize(800, 700)
        self.setContentsMargins(0, 30, 20, 50)
        self.setMaximumSize(16777215, 16777215)

    #Po wejsciu w aplikacje dane z dzisiejszego dnia odrazu się pokazują w zakladce kalendarz
    def showEvent(self, event):
        super().showEvent(event)
        self.update_date_label()
        self.paint_cells()

    def paint_cells(self):
        zalogowany_uzytkownik = zalogowanyUzytkownik.get_instance()
        logged_user_id = zalogowany_uzytkownik.get_zalogowany_id()
        tasks_by_date = obd.get_tasks_for_user(logged_user_id)

        max_tasks = 20  # Maximum number of tasks for the darkest red
        max_red_value = 100  # Maximum red value for the darkest red (adjust this to your preference)
        min_red_value = 50  # Minimum red value for the palest red

        # Reset all dates to the default color first
        default_format = QTextCharFormat()
        self.calendarWidget.setDateTextFormat(QDate(), default_format)

        for date, tasks in tasks_by_date.items():
            task_count = len(tasks)

            # Skip if there are no tasks
            if task_count == 0:
                continue

            # Calculate the shade of red based on the number of tasks
            if task_count * 4 >= max_tasks:
                red_value = 0  # Minimum red for the highest number of tasks
            else:
                # Linearly interpolate between max_red_value (pale red) and min_red_value (dark red)
                red_value = max_red_value - int((max_red_value - min_red_value) * (task_count * 4 / max_tasks))

            color = QColor(255, red_value, red_value)  # Pure red with varying intensity

            # Create a QTextCharFormat object and set its background color
            char_format = QTextCharFormat()
            char_format.setBackground(color)

            # Convert the string date to a QDate object
            date_format = "yyyy-MM-dd"  # Adjust this according to your date format
            date_obj = QDate.fromString(date, date_format)

            # Set the text format (including color) for the given date
            self.calendarWidget.setDateTextFormat(date_obj, char_format)

    def update_date_label(self):
        selected_date = self.calendarWidget.selectedDate()
        self.lblD.setText(selected_date.toString("yyyy-MM-dd"))

        # Fetch tasks from the database for the selected date
        zalogowany_uzytkownik = zalogowanyUzytkownik.get_instance()
        logged_user_id = zalogowany_uzytkownik.get_zalogowany_id()

        selected_date_str = selected_date.toString("yyyy-MM-dd")
        tasks = obd.get_tasks_for_date(logged_user_id, selected_date_str)
        self.paint_cells()

        tasks.sort(key=lambda x: x['start_time'])

        # Populate the table with fetched tasks
        self.tblWidget.setRowCount(0)
        for task in tasks:
            try:
                row_position = self.tblWidget.rowCount()
                self.tblWidget.insertRow(row_position)
                start_time_str = task['start_time'][:5]  # Keep only HH:mm
                end_time_str = task['end_time'][:5]  # Keep only HH:mm

                start_time = QTime.fromString(start_time_str, "HH:mm")
                end_time = QTime.fromString(end_time_str, "HH:mm")

                self.tblWidget.setItem(row_position, 0, QTableWidgetItem(
                    start_time.toString("HH:mm") + " - " + end_time.toString("HH:mm")))
                self.tblWidget.setItem(row_position, 1, QTableWidgetItem(task['task_name']))

                description_item = QTableWidgetItem(task['task_description'])
                description_item.setFlags(description_item.flags() ^ Qt.ItemIsEditable)
                description_item.setTextAlignment(Qt.AlignTop | Qt.AlignLeft)
                description_item.setFlags(description_item.flags() | Qt.ItemIsSelectable)
                self.tblWidget.setItem(row_position, 2, description_item)

                self.tblWidget.setItem(row_position, 3, QTableWidgetItem(task['category_name']))

                chkbox = QCheckBox()
                chkbox.setChecked(task['status'])
                self.tblWidget.setCellWidget(row_position, 4, chkbox)

                task_id = task['task_id']
                category_id = obd.get_category_id(task["category_name"])

                # Connect the checkbox state change to update the status in the database
                chkbox.stateChanged.connect(self.create_checkbox_callback(task_id, category_id, row_position))

                if task['status']:
                    self.highlight_row_on_checkbox_change(row_position, Qt.Checked)

            except Exception as e:
                print("Error populating table row:", e)

        user_name = obd.get_user_name(logged_user_id)

        if user_name:
            self.lblN.setText(f"Witaj {user_name}")
        else:
            self.lblN.setText("Witaj")

        self.tblWidget.resizeRowsToContents()

    def create_checkbox_callback(self, task_id, category_id, row_position):
        def callback(state):
            self.update_status(task_id, category_id, state == Qt.Checked)
            self.highlight_row_on_checkbox_change(row_position, state)

        return callback

    def is_dark_color(self, color):
        luminance = (0.299 * color.red() + 0.587 * color.green() + 0.114 * color.blue()) / 255
        return 'dark' if luminance < 0.5 else 'light'

    def highlight_row_on_checkbox_change(self, row, state):
        table_palette = self.tblWidget.palette()
        window_background_color = table_palette.color(table_palette.Base)
        is_dark_bg = self.is_dark_color(window_background_color)

        theme_background_color = QColor(255, 255, 255)
        if is_dark_bg == 'dark':
            theme_background_color = window_background_color

        for column in range(self.tblWidget.columnCount()):
            item = self.tblWidget.item(row, column)
            if item is not None:
                if state == Qt.Checked:
                    item.setBackground(QColor(144, 238, 144))  # Light green color
                    font = item.font()
                    font.setStrikeOut(True)
                    item.setFont(font)
                    if is_dark_bg == 'dark':
                        item.setForeground(QColor(0, 0, 0))
                else:
                    item.setBackground(theme_background_color)
                    font = item.font()
                    font.setStrikeOut(False)
                    item.setFont(font)
                    if is_dark_bg == 'dark':
                        item.setForeground(QColor(187, 222, 251))
                    else:
                        item.setForeground(QColor(44, 44, 132))

    def delete_selected_row(self):
        selected_row = self.tblWidget.currentRow()

        if selected_row < 0:
            QMessageBox.warning(self, 'Ostrzeżenie', 'Proszę zaznaczyć konkretny wiersz zadania.')
            return

        zalogowany_uzytkownik = zalogowanyUzytkownik.get_instance()
        logged_user_id = zalogowany_uzytkownik.get_zalogowany_id()
        conn = obd.get_connection()
        cursor = conn.cursor()
        cursor.execute("""
                       SELECT TOP 1 zadanie_id 
                       FROM Zadania 
                       WHERE uzytkownik_id = ? 
                       ORDER BY zadanie_id DESC
                   """, (logged_user_id,))
        task_id = cursor.fetchone()[0]
        cursor.close()
        conn.close()

        msg_box = QtWidgets.QMessageBox(self)
        msg_box.setWindowTitle("Usunięcie konta")
        msg_box.setText(
            "Czy jesteś pewien, że chcesz usunąć zadanie?.")
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
            obd.delete_task_from_db(task_id)
            self.tblWidget.removeRow(selected_row)



    def evt_leTaskDescription_tChanged(self):
        if self.leTaskDescription.toPlainText():
            #self.leTaskDescription.setTextColor(Qt.black)
            pass

    def evt_timeStart_tChanged(self):
        start_time = self.timeStart.time()
        self.timeEnd.setTime(start_time)

    def evt_timeEnd_tChanged(self):
        start_time = self.timeStart.time()
        end_time = self.timeEnd.time()

        if end_time < start_time:
            # Show a warning message box
            QMessageBox.warning(self, "Ostrzeżenie", "Czas zakończenia zadania nie może być mniejszy od czasu jego rozpoczęcia")
            self.timeEnd.setTime(start_time)

    def evt_pshBtnDodaj_clicked(self):
        task_name = self.leTaskName.text()
        task_description = self.leTaskDescription.toPlainText()
        start_time = self.timeStart.time()
        end_time = self.timeEnd.time()
        category = self.cmbStates.currentText()
        date = self.lblD.text()

        # Ensure all fields are filled
        if not task_name or not task_description or category == "Kategorie":
            QMessageBox.warning(self, "Ostrzeżenie", "Żadne pole nie może być puste.")
            return



        # Get category and status IDs
        category_id = obd.get_category_id(category)
        if category_id is None:
            QMessageBox.warning(self, "Ostrzeżenie", "Nieprawidłowa kategoria.")
            return

        # Initial status is assumed to be False (unchecked)
        status_id = obd.get_status_id(False)
        if status_id is None:
            QMessageBox.warning(self, "Ostrzeżenie", "Nieprawidłowy status.")
            return

        # Insert task-category-status mapping initially
        zalogowany_uzytkownik = zalogowanyUzytkownik.get_instance()
        logged_user_id = zalogowany_uzytkownik.get_zalogowany_id()
        print(logged_user_id)

        obd.insert_task(logged_user_id, task_name, task_description, date, start_time, end_time)

        conn = obd.get_connection()
        cursor = conn.cursor()
        cursor.execute("""
                       SELECT TOP 1 zadanie_id 
                       FROM Zadania 
                       WHERE uzytkownik_id = ? 
                       ORDER BY zadanie_id DESC
                   """, (logged_user_id,))
        task_id = cursor.fetchone()[0]
        cursor.close()
        conn.close()
        obd.insert_task_category_status(task_id, category_id, status_id)

        # Check for time overlap with existing tasks
        for row in range(self.tblWidget.rowCount()):
            task_time_str = self.tblWidget.item(row, 0).text()
            task_start_str, task_end_str = task_time_str.split(" - ")
            task_start = QTime.fromString(task_start_str, "HH:mm")
            task_end = QTime.fromString(task_end_str, "HH:mm")

            if (start_time >= task_start and start_time <= task_end) or \
                    (end_time >= task_start and end_time <= task_end) or \
                    (start_time <= task_start and end_time >= task_end):
                QMessageBox.warning(self, "Ostrzeżenie", "Czasy zadań nie mogą się pokrywać.")
                return

        row_position = self.tblWidget.rowCount()
        for row in range(self.tblWidget.rowCount()):
            task_time_str = self.tblWidget.item(row, 0).text().split(" - ")[0]
            task_start = QTime.fromString(task_time_str, "HH:mm")
            if start_time < task_start:
                row_position = row
                break

        self.tblWidget.insertRow(row_position)
        self.tblWidget.setItem(row_position, 0, QTableWidgetItem(
            start_time.toString("HH:mm") + " - " + end_time.toString("HH:mm")))
        self.tblWidget.setItem(row_position, 1, QTableWidgetItem(task_name))

        # Set text wrapping for description column
        description_item = QTableWidgetItem(task_description)
        description_item.setFlags(description_item.flags() ^ Qt.ItemIsEditable)
        description_item.setTextAlignment(Qt.AlignTop | Qt.AlignLeft)
        description_item.setFlags(description_item.flags() | Qt.ItemIsSelectable)
        self.tblWidget.setItem(row_position, 2, description_item)

        self.tblWidget.setItem(row_position, 3, QTableWidgetItem(category))

        chkbox = QCheckBox()
        chkbox.setChecked(False)
        self.tblWidget.setCellWidget(row_position, 4, chkbox)

        # Now determine the status based on the checkbox state
        chkbox.stateChanged.connect(self.create_checkbox_callback(task_id, category_id, row_position))

        self.tblWidget.resizeRowToContents(row_position)
        self.tblWidget.sortItems(0, Qt.AscendingOrder)

        # Reset all fields after adding the task
        self.leTaskName.setText("")
        self.leTaskDescription.setText("")
        self.cmbStates.setCurrentIndex(0)
        self.timeStart.setTime(QTime(0, 0))
        self.timeEnd.setTime(QTime(0, 0))

    def update_status(self, task_id, category_id, is_checked):
        status_id = obd.get_status_id(is_checked)
        if status_id is None:
            QMessageBox.warning(self, "Ostrzeżenie", "Nieprawidłowy status.")
            return

        conn = obd.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                SELECT COUNT(*)
                FROM kategoria_zadania_status_mapowanie
                WHERE zadanie_id = ? AND kategoria_id = ?
            """, (task_id, category_id))
            count = cursor.fetchone()[0]

            if count > 0:
                cursor.execute("""
                    UPDATE kategoria_zadania_status_mapowanie
                    SET status_id = ?
                    WHERE zadanie_id = ? AND kategoria_id = ?
                """, (status_id, task_id, category_id))
            else:
                cursor.execute("""
                    INSERT INTO kategoria_zadania_status_mapowanie (zadanie_id, kategoria_id, status_id)
                    VALUES (?, ?, ?)
                """, (task_id, category_id, status_id))

            conn.commit()
        except Exception as e:
            QMessageBox.warning(self, "Błąd", f"Error updating task status: {e}")
        finally:
            cursor.close()
            conn.close()

    def update_task_list(self):
        self.tblWidget.setRowCount(0)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            event.ignore()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter or event.key() == Qt.Key_F6:
            self.pshBtnDodaj.click()
        elif event.key() == Qt.Key_Delete or event.key() == Qt.Key_F7:
            self.pshBtnUsun.click()
        elif event.key() == Qt.Key_F1:
            self.leTaskName.setFocus()
        elif event.key() == Qt.Key_F2:
            self.leTaskDescription.setFocus()
        elif event.key() == Qt.Key_F3:
            self.cmbStates.showPopup()
        elif event.key() == Qt.Key_F4:
            self.timeStart.setFocus()
        elif event.key() == Qt.Key_F5:
            self.timeEnd.setFocus()
        elif event.key() == Qt.Key_F8:
            self.calendarWidget.setFocus()
        elif event.key() == Qt.Key_F9:
            self.tblWidget.setFocus()

""" Używane do testowania
if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    #dlgMain.update_table_widget()
    dlgMain.show()
    sys.exit(app.exec_())
"""