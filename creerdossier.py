#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 09:58:38 2022

@author: LKorenfeld
"""
import dbm
import sys
import paramiko

from PyQt5.QtWidgets import (QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout,
                             QApplication, QMainWindow, QWidget, QTextEdit, QLabel, QRadioButton)
from PyQt5 import QtGui, QtCore

from historiquedossier import View3


class View2(QWidget):
    
    def __init__(self, fprec):
        super().__init__()
        self
        self.fp = fprec
        self.f3 = View3(self)
         
        self.lbl2 = QLabel('Nom')
        self.nom = QLineEdit('')
        self.lbl3 = QLabel('Prénom')
        self.prenom = QLineEdit('')
        self.lbl4 = QLabel('Age')
        self.age = QLineEdit('')
        self.lbl5 = QLabel('Sexe')
        self.homme = QRadioButton('H')
        self.femme = QRadioButton('F')
        self.enregistrer = QPushButton("Enregistrer")
        self.historique = QPushButton("Historique")
        self.btRetour = QPushButton("Retour")
        self.symptomes = QTextEdit('')
        self.medicaments = QTextEdit('')
        self.lbl6 = QLabel('Symptômes')
        self.lbl7 = QLabel('Medicaments proposés')
        
        
        self.nom.setDisabled(False)
        self.prenom.setDisabled(False)
        self.age.setDisabled(False)
        self.medicaments.setDisabled(True)
        
        
        self.repertoire = {'Doliprane':['douleurs','douleur','fièvre', 'antalgique'],
                      'Efferalgan':['douleurs','douleur','fièvre', 'antalgique'], 
                      'Dafalgan':['douleurs','douleur','fièvre', 'antalgique'],
                      'Kardegic':['vasculaire','cérébral','cérébraux', 'cardiaque', 'cardiages', 'prévenir'],
                      'Spasfon':['douleurs','spasmodiques','douleur', 'spasmodique', 'biliaires', 'vessie', 'utérus'],
                      'Gaviscon':['brûlures','estomac','indigestion'],
                      'Dexeryl':['irritations','cutané','cutanées', 'irritation', 'crème'],
                      'MeteoSpasmy':['douleurs', 'douleur','intestinales','intestins', 'ventre'],
                      'Biseptine':['antisepsie','peau','plaie', 'infection'],
                      'Eludril':['bouche','antiseptique','douleur', 'douleurs', 'dents', 'gencives']}
       
        self.init_ui2()  
        self.show()    
        
       
    def init_ui2(self):
        
        self.f3.hide()
        h_box = QHBoxLayout()

        h_box.addWidget(self.lbl5)
        h_box.addWidget(self.homme)
        h_box.addWidget(self.femme)
        
        h1_box = QHBoxLayout()
        h1_box.addWidget(self.lbl6)
        h1_box.addWidget(self.lbl7)
        
        h2_box = QHBoxLayout()
        h2_box.addWidget(self.symptomes)       
        h2_box.addWidget(self.medicaments)
        
        h3_box = QHBoxLayout()
        h3_box.addWidget(self.enregistrer)
        h3_box.addWidget(self.historique)
        h3_box.addWidget(self.btRetour)

        v_box = QVBoxLayout()
        v_box.addWidget(self.lbl2)
        v_box.addWidget(self.nom) 
        v_box.addWidget(self.lbl3)
        v_box.addWidget(self.prenom)
        v_box.addWidget(self.lbl4)
        v_box.addWidget(self.age)
        v_box.addLayout(h_box)
        
        v_box.addLayout(h1_box)
        v_box.addLayout(h2_box)
        v_box.addLayout(h3_box)
        
        
        self.setLayout(v_box)
        self.setWindowTitle('Aide médicaments')
        
        self.btRetour.clicked.connect(self.btn1_click) 
        self.historique.clicked.connect(self.btn2_click)
        self.enregistrer.clicked.connect(self.btn3_click)
        
        

    def btn1_click(self): 
        self.hide()
        # self.prenom.setText('')
        # self.nom.setText('')
        # self.age.setText('')
        self.medicaments.setText('')
        self.symptomes.setText('')
        self.fp.show() 
        
    def btn2_click(self): 
        self.hide()
        self.f3.show()
               
    def btn3_click(self): 
        
        if self.homme.isChecked() :
            self.sexe ='H'
        elif self.femme.isChecked() :
            self.sexe ='F'
        self.n=self.nom.text()
        self.p=self.prenom.text()
        self.a=self.age.text()
        self.f3.nom.setText(self.n) 
        self.f3.prenom.setText(self.p)
        self.f3.age.setText(self.a)         
        self.s=str(self.symptomes.toPlainText())
        self.f3.symptomes.setText(self.s) 
        self.addP(self.n, self.p, self.a, self.sexe, self.s)

        self.aideordonnance(self.n, self.p, self.a, self.sexe, self.s)
        self.prenom.setText('')
        self.nom.setText('')
        self.age.setText('')
        #self.symptomes.setText('')

#fonction qui sert à l'enregistrement :
    def addP(self, n, p, a, sexe, s): #les arguments sont : Nom Prénom age sexe symptômes
       
        self.titre = n+'_'+p+'_'+a+'_'+sexe+'.txt'
        self.f = open(self.titre, 'a')

        print(s)
        self.f.write(s+'\n')  #ajout des informations sur une même ligne
         #considérons que deux patients n'auront pas même nom et prénom
           
         #print("Le patient a déjà un dossier. Vous pouvez cliquer sur Historique pour le consulter")
         #affichier le message sur l'interface
         #self.aux2=self.aideordonnance(self.n, self.p, self.a, self.sexe)
        
        self.f.close()

        
    def showHist(self, n, p, a, sexe):  
        self.titre = n+'_'+p+'_'+a+'_'+sexe+'.txt'
        self.f = open(self.titre, 'a')
        self.f.close()
        
    def aideordonnance(self,n, p, a, sexe,s) :
        self.titre = n+'_'+p+'_'+a+'_'+sexe+'.txt'
        self.f = open(self.titre, 'r') #ouverture du fichier en mode lecture
        #self.sympt=str(self.f.read())
        self.listsymptomes = self.s.split() #récupération des symptômes dans une liste
        print(self.listsymptomes)
       
        self.correspondance = {} #création d'un dictionnaire qui va indiquer le plus grand nombre de symptômes communs 
                                #entre le texte rentré par le médecin et les symptômes associés à chaque médicaments        
        for i in self.listsymptomes :
            
            for e in self.repertoire.keys() :
                self.nbsympt = 0
                for j in self.repertoire[e]:
                    if j == i :
                        self.nbsympt +=1                 
                self.correspondance[e]=self.nbsympt                  
        self.maxi=''
        for k,v in self.correspondance.items():
            if v==max(self.correspondance.values()):
                print(v)
                self.maxi+=k+' ' #self.maxi est une chaîne de caractère qui montre les médicaments qui matchent
        self.f.close()
        self.fi = open(self.titre, 'a')
        self.fi.write('Proposition de médicaments : ' + str(self.maxi))
        self.medicaments.setText(self.maxi)       
        self.fi.close()
        self.fic=open(self.titre, 'r')
        self.f3.symptomes.setText(self.fic.read())
        self.fic.close()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    view2 = View2()
    sys.exit(app.exec_())