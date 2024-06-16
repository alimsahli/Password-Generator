#!/usr/bin/env python3
# This Python file uses the following encoding: utf-8
import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QCheckBox, QLabel, QPushButton, QWidget, QTextEdit, QSpinBox
from PyQt5.QtGui import QIcon

class PasswordGeneratorApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle("Ali Password Generator")
        self.setWindowIcon(QIcon("pic.ico"))

        self.initUI()

    def initUI(self):
        widget = QWidget()
        main_layout = QVBoxLayout()

        # Create layout for checkboxes
        checkbox_layout = QHBoxLayout()
        column1 = QVBoxLayout()
        column2 = QVBoxLayout()

        self.uppercase_checkbox = QCheckBox("Include Uppercase Letters")
        self.lowercase_checkbox = QCheckBox("Include Lowercase Letters")
        self.numbers_checkbox = QCheckBox("Include Numbers")
        self.symbols_checkbox = QCheckBox("Include Symbols")

        column1.addWidget(self.uppercase_checkbox)
        column1.addWidget(self.lowercase_checkbox)
        column2.addWidget(self.numbers_checkbox)
        column2.addWidget(self.symbols_checkbox)

        checkbox_layout.addLayout(column1)
        checkbox_layout.addLayout(column2)

        self.length_input = QSpinBox()
        self.length_input.setRange(1, 100)
        self.length_input.setValue(20)
        self.length_input.setPrefix("Length: ")

        self.amount_input = QSpinBox()
        self.amount_input.setRange(1, 100)
        self.amount_input.setValue(1)
        self.amount_input.setPrefix("Amount: ")

        self.result_text = QTextEdit()
        self.result_text.setReadOnly(True)

        generate_button = QPushButton("Generate Password")
        generate_button.clicked.connect(self.generate_password)

        main_layout.addLayout(checkbox_layout)
        main_layout.addWidget(self.length_input)
        main_layout.addWidget(self.amount_input)
        main_layout.addWidget(generate_button)
        main_layout.addWidget(QLabel("Generated Password(s):"))
        main_layout.addWidget(self.result_text)

        widget.setLayout(main_layout)
        self.setCentralWidget(widget)

    def generate_password(self):
        uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lowercase_letters = uppercase_letters.lower()
        digits = "0123456789"
        symbols = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

        upper = self.uppercase_checkbox.isChecked()
        lower = self.lowercase_checkbox.isChecked()
        nums = self.numbers_checkbox.isChecked()
        syms = self.symbols_checkbox.isChecked()

        all_chars = ""
        if upper:
            all_chars += uppercase_letters
        if lower:
            all_chars += lowercase_letters
        if nums:
            all_chars += digits
        if syms:
            all_chars += symbols

        length = self.length_input.value()
        amount = self.amount_input.value()

        if not all_chars:
            self.result_text.setPlainText("Please select at least one character set.")
            return

        passwords = []
        for _ in range(amount):
            password = ''.join(random.sample(all_chars, length))
            passwords.append(password)

        self.result_text.setPlainText("\n".join(passwords))

def main():
    app = QApplication(sys.argv)
    win = PasswordGeneratorApp()
    win.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
