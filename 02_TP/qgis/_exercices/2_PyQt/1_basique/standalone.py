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
from PyQt5.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QVBoxLayout, QMainWindow,
                             QMessageBox, QPushButton, QStyleFactory, QTableWidget, QTableWidgetItem, QWidget)


# submodules
from modules import udata_client_datagouvfr

# vars
app_dir = path.realpath(path.dirname(__file__))
current_locale = QLocale()


# #############################################################################
# ########## Classes ###############
# ##################################
class DataGouvFrBrowser_Main(QMainWindow):

    def __init__(self):
        super().__init__()  # link current object to the QMainWindow instanciated
        # load datagouv client
        self.client_dg = udata_client_datagouvfr.DataGouvFr()

        # build  & launch main window
        self.initUI()


    def initUI(self):
        """Start UI display and widgets signals and slots.
        """
        # change Window Title
        self.setWindowTitle("Viva Open Data !")

        # DROPDOWN LIST #############################
        # create combobox list
        self.cbb_orgs = QComboBox(self)
        self.cbb_orgs.addItem("IGN")
        self.cbb_orgs.addItem("INSEE")
        self.cbb_orgs.addItem("Isogeo")
        self.cbb_orgs.addItem("Paris")

        # BUTTON #############################
        # create button
        self.btn_download = QPushButton("Search on uData", self)
        self.btn_download.resize(self.btn_download.sizeHint())
        self.btn_download.setToolTip("Télécharger la liste des données ouvertes de l'organisation")
        # connect button to function
        self.btn_download.pressed.connect(partial(self.udata_search))

        # # connect combobox
        # self.comboBox.activated.connect(partial(self.udata_search))
        # create table
        self.tab_results = QTableWidget(self)
        self.tab_results.setColumnCount(2)  # set column count
        # self.tab_results.setRowCount(1)  # set row count

        # organize
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addWidget(self.cbb_orgs)
        vbox.addWidget(self.btn_download)
        vbox.addWidget(self.tab_results)
        w = QWidget()
        w.setLayout(vbox)
        self.setCentralWidget(w)

        # display main application
        self.setGeometry(200,300,500,250)
        self.statusBar().showMessage('Choisir son organisation...')
        self.show()

    ## EXECUTIVE METHODS #####################################################
    def udata_search(self):
        print("Ceci est la fonction qui lance la recherche DatGouv")
        orgas = {
            "ign": "534fff80a3a7292c64a77e41",
            "insee": "534fff81a3a7292c64a77e5c",
            "isogeo": "54a13044c751df096c04805a",
            "paris": "534fff89a3a7292c64a77eb7"
            }
        # get choosen organization
        org = self.cbb_orgs.currentText()

        # launch udata search
        org_ds = self.client_dg.org_datasets(org_id=orgas.get(org.lower()))

        # update status bar
        self.statusBar().showMessage("{} results on {}".format(org_ds.get("total"), org))

        # fill table
        self.tab_results.setRowCount(org_ds.get("total"))
        i = 0
        for ds in org_ds.get("data"):
            self.tab_results.setItem(i, 0, QTableWidgetItem(ds.get("title")))
            self.tab_results.setItem(i, 1, QTableWidgetItem(ds.get("license")))
            i += 1



# #############################################################################
# ##### Stand alone program ########
# ##################################
if __name__ == "__main__":
    import sys
    # create the application and the main window
    app = QApplication(sys.argv)
    # ui execution
    searchForm = DataGouvFrBrowser_Main()
    sys.exit(app.exec_())
