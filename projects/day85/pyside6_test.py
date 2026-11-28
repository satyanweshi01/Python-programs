from PySide6.QtWidgets import (
                                QApplication, 
                                QMainWindow, 
                                QLabel, 
                                QWidget, 
                                QGridLayout, QVBoxLayout, QHBoxLayout,
                                QPushButton, QLineEdit, QComboBox, QListWidget, QCheckBox, QRadioButton
                            )
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Image Watermarking app")

        container = QWidget() # widget object
        self.setCentralWidget(container)

        layout = QVBoxLayout(container) # Layout for a widget conponent

        # UI component
        label = QLabel('Image to Watermarked Image') # label component
        label.setAlignment(Qt.AlignCenter)

        button = QPushButton("Browse") # botton component
        button.clicked.connect(self.printsome)





        line_edit = QLineEdit() # one line text box

        combobox = QComboBox() # drop down menu component
        combobox.addItems(['Op1','Op2','Op3'])

        listwidget = QListWidget()
        listwidget.addItems(['Op1','Op2','Op3'])
        
        # subwidget (inside a widget)
        inner_widget = QWidget()
        inner_container = QHBoxLayout(inner_widget)

        checkbox1 = QCheckBox('Op1')
        checkbox2 = QCheckBox('Op2')
        checkbox3 = QCheckBox('Op3')
        inner_container.addWidget(checkbox1)
        inner_container.addWidget(checkbox2)
        inner_container.addWidget(checkbox3)

        # subwidget (inside a widget)
        inner_widget2 = QWidget()
        inner_container2 = QHBoxLayout(inner_widget2)

        radiobutton1 = QRadioButton('Op1')
        radiobutton2 = QRadioButton('Op2')
        radiobutton3 = QRadioButton('Op3')
        inner_container2.addWidget(radiobutton1)
        inner_container2.addWidget(radiobutton2)
        inner_container2.addWidget(radiobutton3)


        layout.addWidget(label)
        layout.addWidget(line_edit)
        layout.addWidget(button)
        layout.addWidget(combobox)
        layout.addWidget(listwidget)

        layout.addWidget(inner_widget) # adding inner widget the main widget
        layout.addWidget(inner_widget2)

        # layout1 = QHBoxLayout(container) # horizontal layout

        # label1 = QLabel('PDF')
        # label1.setAlignment(Qt.AlignCenter)

        # label2 = QLabel('One')
        # label2.setAlignment(Qt.AlignCenter)

        # label3 = QLabel('Two')
        # label3.setAlignment(Qt.AlignCenter)

        # layout1.addWidget(label1)
        # layout1.addWidget(label2)
        # layout1.addWidget(label3)

    def printsome(self):
        print('some')




app = QApplication()

window = MainWindow()
window.show()

app.exec()
