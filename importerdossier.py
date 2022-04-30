#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 17:59:55 2022

@author: LKorenfeld
"""

import dbm
import sys

from PyQt5.QtWidgets import (QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout,
                             QApplication, QMainWindow, QWidget, QTextEdit, QLabel)
from PyQt5 import QtGui, QtCore


class View4(QWidget):
    
    def __init__(self, fprec):
        super().__init__()
        
        self.fp = fprec
        self.btRetour = QPushButton("Retour")
    
    def init_ui2(self):
        
        v_box = QVBoxLayout()
        v_box.addWidget(self.btRetour)
        
        self.setLayout(v_box)
        self.setWindowTitle('Aide médicaments')
        
        self.btRetour.clicked.connect(self.btn1_click) 
        
    def ouvrir(self):
        self.fichier = QtGui.QFileDialog.getOpenFileName(self, 
                     u"Sélectionnez le fichier", 
                     u"toto.txt", 
                     u"Fichier texte (*.txt);;Tous (*.*)")
        
    def btn1_click(self): 
        self.hide()
        self.fp.show()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    view4 = View4()
    sys.exit(app.exec_())