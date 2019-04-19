import re
import sys
from bs4 import BeautifulSoup as bs
import requests

from PySide2.QtWidgets import *
from PySide2.QtCore import *

class MyWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.text = QLabel("Enter Lyrics Below")
        self.textbox = QLineEdit("")
        self.button = QPushButton("Search")
        self.text.setAlignment(Qt.AlignCenter)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.textbox)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

        # Connecting the signal
        self.button.clicked.connect(self.magic)

    @Slot()
    def magic(self):
        self.text.setText("Looking for Lyrics...")
        url = "https://www.google.com/search?q=" + self.textbox.text()
        html = requests.get(url)
        soup = bs(html.text, 'html.parser')
        song_tag = soup.body.findAll(text=re.compile('- YouTube'))
        print(song_tag)

        max = 0
        place = 0

        for i in range(len(song_tag)):
            if len(song_tag[i]) > max:
                max = len(song_tag)
                place = i
        song_name = str(song_tag[place-1])[:-10]
        print(song_name)
        self.text.setText("Song Name: " + song_name)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    widget = MyWidget()
    widget.resize(400, 200)
    widget.show()

    sys.exit(app.exec_())