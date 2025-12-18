
import sys
from PyQt5.QtWidgets import QApplication
from ui.login_window import LoginWindow
app=QApplication(sys.argv)
w=LoginWindow()
w.show()
sys.exit(app.exec_())
