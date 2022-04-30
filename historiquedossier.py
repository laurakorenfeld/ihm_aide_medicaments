#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 10:56:43 2022

@author: LKorenfeld
"""

import dbm
import sys

from PyQt5.QtWidgets import (QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout,
                             QApplication, QMainWindow, QWidget, QTextEdit, QLabel)
from PyQt5 import QtGui, QtCore


class View3(QWidget):
    
    def __init__(self, fprec):
        super().__init__()
        
        self.fp = fprec
         
        self.lbl2 = QLabel('Nom')
        self.nom = QLineEdit('')
        self.lbl3 = QLabel('Prénom')
        self.prenom = QLineEdit('')
        self.lbl4 = QLabel('Age')
        self.age = QLineEdit('')
        self.symptomes = QTextEdit('')       
        self.btRetour = QPushButton("Retour")
        
        self.nom.setDisabled(True)
        self.prenom.setDisabled(True)
        self.age.setDisabled(True)
        self.symptomes.setDisabled(True)
        
        self.init_ui2()  
        self.show()    
        
       
    def init_ui2(self):
        
        v_box = QVBoxLayout()
        v_box.addWidget(self.lbl2)
        v_box.addWidget(self.nom) 
        v_box.addWidget(self.lbl3)
        v_box.addWidget(self.prenom)
        v_box.addWidget(self.lbl4)
        v_box.addWidget(self.age)
        v_box.addWidget(self.symptomes)
        v_box.addWidget(self.btRetour)
        
        self.setLayout(v_box)
        self.setWindowTitle('Aide médicaments')
        
        self.btRetour.clicked.connect(self.btn1_click) 
        
        
    
    def btn1_click(self): 
        self.hide()
        
        self.fp.show()
        #self.f2.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    view3 = View3()
    sys.exit(app.exec_())
    