import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtCore import pyqtSlot, QFile, QTextStream, QEasingCurve, QAbstractAnimation, QSize
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QPropertyAnimation
  # Import the generated UI code
from PyQt5.QtWidgets import QMenu
class Mainwindow(QMainWindow):
    def __init__(self):
        super(Mainwindow, self).__init__()
        
        # Set up the UI from the generated code
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connect menu button click to show/hide menu
        self.ui.menuButton.clicked.connect(self.toggle_menu)
        
        # Create a menu and add items
        self.menu = QMenu(self)
        self.menu.addAction("Item 1")
        self.menu.addAction("Item 2")
        self.menu.addAction("Item 3")
        
        # Set up animation for menu
        self.menu_animation = QPropertyAnimation(self.menu, b"geometry", self)
        self.menu_animation.setDuration(300)
        self.menu_animation.setEasingCurve(QEasingCurve.OutCubic)

    @pyqtSlot()
    def toggle_menu(self):
        if self.menu.isVisible():
            end_geometry = QRect(self.width(), 0, 0, self.height())
        else:
            end_geometry = QRect(self.width() - 150, 0, 150, self.height())
            
        self.menu_animation.setStartValue(self.menu.geometry())
        self.menu_animation.setEndValue(end_geometry)
        self.menu_animation.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Mainwindow()
    window.show()
    sys.exit(app.exec_())