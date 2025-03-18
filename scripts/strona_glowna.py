import sys
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QTime, QDate

from Zalogowany_użytkownik import zalogowanyUzytkownik
import ObslugaBazyDanych as obd

class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TimeForge")

        self.lblTasks = QLabel("Zadania na dziś")
        self.lblTasks.setObjectName("lblTasks")
        self.test = []

        # Create widget QTableWidget
        self.tblWidget = QTableWidget(self)
        self.tblWidget.setColumnCount(5)  # 4 columns: Time, Task, Description, Done?
        self.tblWidget.setHorizontalHeaderLabels(["   Czas", "Nazwa", "Opis", "Kategoria", "Zrobione?"])

        # Adjust column widths
        self.tblWidget.setColumnWidth(0, 100)  # Time
        self.tblWidget.setColumnWidth(1, 100)  # Task
        self.tblWidget.setColumnWidth(2, 750)  # Description
        self.tblWidget.setColumnWidth(3, 100)
        self.tblWidget.setColumnWidth(4, 150)
        self.tblWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        header = self.tblWidget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)

        # Center align labels in QTableWidget and change header font
        # header = self.tblWidget.horizontalHeader()
        # for i in range(5):
        #     header.setDefaultAlignment(Qt.AlignCenter)
        #     header.setStyleSheet("""
        #                   font-weight: bold;
        #                   font-size: 20px; /* Change font size */
        #                   color: #2c2c84;
        #                   border:none;""")

        # mainlayout
        self.lyMain = QVBoxLayout()
        self.lyMain.addWidget(self.lblTasks)  # Add label
        self.lyMain.setSpacing(40)
        self.lyMain.addWidget(self.tblWidget)
        self.setLayout(self.lyMain)
        self.lyMain.setContentsMargins(5, 100, 80, 100)
        # self.setFixedSize(1600, 800)
        # self.setMinimumSize(1000, 700)


    def update_table_widget(self):
        selected_date = QDate.currentDate()
        # Use current date instead of selected date from calendar widget

        # Fetch tasks from the database for the selected date
        zalogowany_uzytkownik = zalogowanyUzytkownik.get_instance()
        logged_user_id = zalogowany_uzytkownik.get_zalogowany_id()

        selected_date_str = selected_date.toString("yyyy-MM-dd")
        # Pass the selected_date to the get_tasks_for_date() function
        tasks = obd.get_tasks_for_date(logged_user_id, selected_date_str)
        tasks.sort(key=lambda x: x['start_time'])
        # Populate the table with fetched tasks
        self.tblWidget.setRowCount(0)
        # Clear existing rows first
        if not tasks:
            # No tasks to insert, exit the method
            return
        print(tasks)
        for task in tasks:
            try:
                row_position = self.tblWidget.rowCount()
                self.tblWidget.insertRow(row_position)
                start_time_str = task['start_time'][:5]  # Keep only HH:mm
                end_time_str = task['end_time'][:5]  # Keep only HH:mm

                # Parse the truncated time strings to QTime
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

        self.tblWidget.resizeRowsToContents()

    def showEvent(self, event):
        super().showEvent(event)
        self.update_table_widget()

    def create_checkbox_callback(self, task_id, category_id, row_position):
        def callback(state):
            self.update_status(task_id, category_id, state == Qt.Checked)
            self.highlight_row_on_checkbox_change(row_position, state)

        return callback

    def is_dark_color(self, color):
        # Calculate the luminance of the color
        luminance = (0.299 * color.red() + 0.587 * color.green() + 0.114 * color.blue()) / 255
        # Return 'dark' if the luminance is below the threshold (0.5), indicating a dark color
        return 'dark' if luminance < 0.5 else 'light'

    def highlight_row_on_checkbox_change(self, row, state):
        table_palette = self.tblWidget.palette()
        window_background_color = table_palette.color(table_palette.Base)
        is_dark_bg = self.is_dark_color(window_background_color)
        print("Window Background Color (RGB):", window_background_color.red(), window_background_color.green(),
              window_background_color.blue())
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
                    # Apply strikeout effect to the text
                    item.setFont(font)
                    if is_dark_bg == 'dark':
                        item.setForeground(QColor(0, 0, 0))



                else:
                    item.setBackground(theme_background_color)
                    font = item.font()
                    font.setStrikeOut(False)  # Apply strikeout effect to the text
                    item.setFont(font)
                    # White color (default)
                    if is_dark_bg == 'dark':
                        item.setForeground(QColor(187, 222, 251))
                    else:
                        item.setForeground(QColor(44, 44, 132))

    def update_status(self, task_id, category_id, is_checked):
        status_id = obd.get_status_id(is_checked)
        if status_id is None:
            QMessageBox.warning(self, "Ostrzeżenie", "Nieprawidłowy status.")
            return

        conn = obd.get_connection()
        cursor = conn.cursor()
        try:
            # Check if the mapping already exists
            cursor.execute("""
                SELECT COUNT(*)
                FROM kategoria_zadania_status_mapowanie
                WHERE zadanie_id = ? AND kategoria_id = ?
            """, (task_id, category_id))
            count = cursor.fetchone()[0]

            if count > 0:
                # Update the existing mapping
                cursor.execute("""
                    UPDATE kategoria_zadania_status_mapowanie
                    SET status_id = ?
                    WHERE zadanie_id = ? AND kategoria_id = ?
                """, (status_id, task_id, category_id))
            else:
                # Insert new mapping (fallback, should not typically occur in this flow)
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

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            event.ignore()

""" Uzywane do testowania
if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.update_table_widget()
    # print("error")
    dlgMain.show()
    sys.exit(app.exec_())
"""