#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 14:33:45 2022

@author: LKorenfeld
"""

import dbm
import sys

from PyQt5.QtWidgets import (QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout,
                             QApplication, QMainWindow, QWidget, QTextEdit, QLabel, QToolTip)
from PyQt5 import QtGui, QtCore

from creerdossier import View2
from historiquedossier import View3
from importerdossier import View4

class View(QWidget):
    
    def __init__(self):
        super().__init__()
        
     
        self.f2 = View2(self)        
        self.f4 = View4(self)        

        self.lbl0 = QLabel("Bienvenue sur cette plateforme d'aide à la prescription de médicaments")
        #self.lbl1 = QLabel('¡ La plataforma !') # nom de la plateforme
        self.creer = QPushButton('Créer un dossier')

        self.creer.resize(150,50)
        #self.importer = QPushButton('Importer un dossier')    
        #self.importer.resize(150,50)
        self.app = QApplication(sys.argv)
        self.w = QWidget()
        self.im = QLabel(self.w)
        self.pixmap = QtGui.QPixmap('logo')
        self.im.setPixmap(self.pixmap.scaled(100,100))
        self.im.setAlignment(QtCore.Qt.AlignCenter)
        #self.im.setGeometry(1000, 10, 50, 20)   
        #self.im.move(10000,90)
    
        self.init_ui1()  
        self.show()    
    
    def init_ui1(self):

        #h_box = QHBoxLayout() #h horizontal
        self.f2.hide()        
        self.f4.hide()
        
        v_box = QVBoxLayout() #v vertical
        v_box.addWidget(self.im)
        v_box.addWidget(self.lbl0)
        #v_box.addWidget(self.lbl1) 
        #v_box.addLayout(h_box)
        v_box.addWidget(self.creer) 

        #self.creer.toolTip("Cliquez ici pour créer ou modifier le dossier d'un patient")
        #v_box.addWidget(self.importer) 


        self.setLayout(v_box)
        
        self.setWindowTitle('Aide médicaments')    
        
        self.creer.clicked.connect(self.btn1_click) 
        #self.importer.clicked.connect(self.btn2_click)


    def btn1_click(self): 
        self.hide()
        self.f2.show()

        
    def btn2_click(self):
        self.hide()
        self.f4.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = View()
    sys.exit(app.exec_())





