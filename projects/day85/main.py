from PySide6.QtWidgets import (
                                QApplication, 
                                QMainWindow, 
                                QLabel, 
                                QWidget, 
                                QVBoxLayout,
                                QPushButton, QLineEdit,
                                QFileDialog
                            )
from PySide6.QtCore import Qt
import os

from image_processing import add_watermark_overlay

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

        browse_btn = QPushButton("Browse") # botton component
        browse_btn.clicked.connect(self.get_file)
        self.imported_file_path=None # the variable that stores the imported file path
        

        proceed_btn = QPushButton("Proceed") # botton component
        proceed_btn.clicked.connect(self.imageprocessing)

        self.line_edit = QLineEdit("Watermarked Text") # one line text box
        


        layout.addWidget(label)
        layout.addWidget(self.line_edit)
        layout.addWidget(browse_btn)
        layout.addWidget(proceed_btn)

    def get_file(self):
        file_filter = 'Image File (*.png *.jpg)'
        response = QFileDialog.getOpenFileName(
            parent=self,
            caption='Select a image file',
            filter=file_filter,
        )

        #print(f"the file address : {response[0]}")
        self.imported_file_path = response[0]

    def imageprocessing(self):
        watermarked_text = self.line_edit.text()
        if self.imported_file_path != None:
            add_watermark_overlay(self.imported_file_path,"output.png",watermarked_text)
        else:
            print(3)




app = QApplication()

window = MainWindow()
window.show()

app.exec()
