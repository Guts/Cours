# -*- coding: UTF-8 -*-
#! python3

"""
    DataGouvFr Browser - Standalone launcher

    Purpose:     Get datas from https://data.gouv.fr
    Author:      ENSG
    Python:      3.6.x
"""

# #############################################################################
# ########## Libraries #############
# ##################################

# standard library
import logging
import platform
from datetime import datetime
from functools import partial
from logging.handlers import RotatingFileHandler
from os import listdir, path
import pathlib  # TO DO: replace os.path by pathlib

from PyQt5.QtCore import (QLocale, QSettings, QThread, QTranslator,
                          pyqtSignal, pyqtSlot)
from PyQt5.QtGui import QCloseEvent, QIcon
from PyQt5.QtWidgets import (QApplication, QComboBox, QMainWindow,
                             QMessageBox, QStyleFactory)


# submodules
from modules import udata_client_datagouvfr
from modules import ui_windowtitle_setter
from modules.ui.py_searchForm import Ui_mainForm

# vars
app_dir = path.realpath(path.dirname(__file__))
current_locale = QLocale()


# #############################################################################
# ########## Classes ###############
# ##################################
class DataGouvFrBrowser_Main(QMainWindow):


    def __init__(self):
        super().__init__()
        # load search form and build its ui
        self.searchform = Ui_mainForm()
        self.searchform.setupUi(self)
        # load datagouv client
        self.client_dg = udata_client_datagouvfr.DataGouvFr()
        self.winTitler = ui_windowtitle_setter

        # build  & launch main window
        self.initUI()


    def initUI(self):
        """Start UI display and widgets signals and slots.
        """
        # change Windo Title
        self.setWindowTitle("Viva ENSG !")
        # connect woidgets to methds
        self.searchform.btn_download.pressed.connect(partial(self.toto))
        self.searchform.comboBox.activated.connect(partial(self.udata_search))
        # display main application
        self.show()

    ## METHODS
    def toto(self):
        print("Ceci est la méthode toto de l'application principale")

    def udata_search(self):
        print("Ceci est la recherche DatGouv")
        orgas = {"ign": "534fff80a3a7292c64a77e41",
             "insee": "534fff81a3a7292c64a77e5c",
             "isogeo": "54a13044c751df096c04805a",
             }
        org = "ign"
        org_ds = self.client_dg.org_datasets(org_id=orgas.get(org))

        self.winTitler(window=self, new_title="{} results on {}".format(org_ds.get("total"), org))
        pass


# #############################################################################
# ##### Stand alone program ########
# ##################################
if __name__ == "__main__":
    import sys
    # create the application and the main window
    app = QApplication(sys.argv)
    # languages
    locale_path = path.join(app_dir,
                            'i18n',
                            'datagouvfrbrowser_{}.qm'.format(current_locale.system().name()))
    translator = QTranslator()
    translator.load(path.realpath(locale_path))
    app.installTranslator(translator)
    # ui execution
    searchForm = DataGouvFrBrowser_Main()
    sys.exit(app.exec_())
