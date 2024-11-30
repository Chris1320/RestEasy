from PySide6.QtWidgets import QMainWindow, QPushButton


class Dashboard(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("RestEasy")

        button = QPushButton("RestEasy (WIP)")
        _ = button.pressed.connect(self.close)

        self.setCentralWidget(button)
        self.show()
