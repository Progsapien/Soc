import sys
from PyQt5.QtWidgets import QApplication
from ui import Ui
from socman import SocMan

app = QApplication(sys.argv)
socman = SocMan()
ui = Ui(socman)
ui.show()
sys.exit(app.exec_())