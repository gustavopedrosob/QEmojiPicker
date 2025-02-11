import sys

from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout

from widgets.color_responsive_button import QColorResponsiveButton
from widgets.utils import get_icon


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Color Responsive Button Test")

        widget = QWidget()

        layout = QVBoxLayout()

        button = QColorResponsiveButton()
        button.setIcon(get_icon("face-smile-solid.svg"))

        layout.addWidget(button)

        widget.setLayout(layout)

        self.setCentralWidget(widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())