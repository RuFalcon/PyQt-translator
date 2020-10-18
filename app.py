from PyQt5.QtWidgets import (
    QWidget,
    QPushButton,
    QLabel,
    QApplication,
    QMainWindow,
    QTextEdit,
    )
from PyQt5 import uic
from PyQt5.QtGui import QIcon
import sys
import string
import googletrans
from googletrans import Translator
import pyttsx3

translator = Translator()

engine = pyttsx3.init()
engine.setProperty('rate', 125)
engine.setProperty('volume',1.0)
voices = engine.getProperty('voices')



class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('word_changer.ui', self)

        self.setWindowIcon(QIcon('images/word.svg'))

        self.setFixedHeight(542)
        self.setFixedWidth(1280)

        self.button_upper = self.findChild(QPushButton, "button_upper")
        self.button_upper.clicked.connect(self.to_upper)

        self.button_capwords = self.findChild(QPushButton, "button_capwords")
        self.button_capwords.clicked.connect(self.to_capwords)

        self.button_lower = self.findChild(QPushButton, "button_lower")
        self.button_lower.clicked.connect(self.to_lower)

        self.eng_block = self.findChild(QTextEdit, "eng_block")
        self.eng_block.textChanged.connect(self.length_eng)
        self.eng_block.textChanged.connect(self.ru_translate)

        self.ru_block = self.findChild(QTextEdit, "ru_block")
        self.ru_block.textChanged.connect(self.length_ru)
        
        self.button_translate = self.findChild(QPushButton, "button_translate")
        self.button_translate.clicked.connect(self.eng_translate)

        self.eng_length = self.findChild(QLabel, "eng_length")
        self.ru_length = self.findChild(QLabel, "ru_length")

        self.eng_sound = self.findChild(QPushButton, "eng_sound")
        self.eng_sound.clicked.connect(self.eng_audio)

        self.ru_sound = self.findChild(QPushButton, "ru_sound")
        self.ru_sound.clicked.connect(self.ru_audio)

        self.length_eng()
        self.length_ru()
        self.ru_translate()
        

    def to_upper(self):
        self.eng_block.setPlainText(self.eng_block.toPlainText().upper())

    def to_capwords(self):
        self.eng_block.setPlainText(string.capwords(self.eng_block.toPlainText()))
        self.ru_block.setPlainText(string.capwords(self.ru_block.toPlainText()))

    def to_lower(self):
        self.eng_block.setPlainText(self.eng_block.toPlainText().lower())

    def length_eng(self):
        self.eng_length.setText(str(len(self.eng_block.toPlainText())))

    def length_ru(self):
        self.ru_length.setText(str(len(self.ru_block.toPlainText())))

    def ru_translate(self):
         self.ru_block.setPlainText(translator.translate(self.eng_block.toPlainText(), src='en', dest='ru').text)

    def eng_translate(self):
         self.eng_block.setPlainText(translator.translate(self.ru_block.toPlainText(), src='ru', dest='en').text)

    def eng_audio(self):
        engine.setProperty('voice', voices[3].id)
        engine.say(self.eng_block.toPlainText())
        engine.runAndWait()
        engine.stop()

    def ru_audio(self):
        engine.setProperty('voice', voices[0].id)
        engine.say(self.ru_block.toPlainText())
        engine.runAndWait()
        engine.stop()






app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
