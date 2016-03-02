# -*- coding: utf-8 -*-

#!/usr/bin/env python

import sys

from PyQt4.QtGui import QApplication
from src.window import MainWindow


reload(sys)
sys.setdefaultencoding('utf8')

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
