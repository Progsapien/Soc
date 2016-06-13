import sys
from PyQt5.QtWidgets import QApplication
from ui import Ui

app = QApplication(sys.argv)
ui = Ui()
ui.show()
sys.exit(app.exec_())