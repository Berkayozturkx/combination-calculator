#!/usr/bin/env python
# coding: utf-8

# In[1]:


from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

class CombinationCalculator(QWidget):
    
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        self.setWindowTitle("Kombinasyon Hesaplayıcı")
        
        grid = QGridLayout()
        
        grid.addWidget(QLabel("Eleman Sayısı (n):"),1,0)
        grid.addWidget(QLabel("Seçim Sayısı (r):"),2,0)
        
        self.elemanSayisi = QLineEdit()
        self.secimSayisi = QLineEdit()
        
        grid.addWidget(self.elemanSayisi,1,1,1,2)
        grid.addWidget(self.secimSayisi,2,1,1,2)
        
        self.buton = QPushButton("Hesapla")
        self.buton.clicked.connect(self.hesapla)
        grid.addWidget(self.buton,3,2,1,1)
        
        self.sonuc = QLabel("")
        
        
        h_box = QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(grid)
        h_box.addStretch()
        
        v_box = QVBoxLayout()
        v_box.addStretch()
        v_box.addLayout(h_box)
        v_box.addStretch()
        
        
        v_box.addWidget(self.sonuc)
        
        self.setLayout(v_box)
        self.resize(300,300)
        self.show()
        
        
    def hesapla(self):
        eleman = 0
        try: eleman = int(self.elemanSayisi.text())
        except: pass
        
        secim = 0
        try: secim = int(self.secimSayisi.text())
        except: pass
        
        fark = eleman-secim
        
        sonucEleman = 1
        sonucSecim = 1
        sonucFark = 1
        if(secim > 0 and eleman > 0):
            if(secim < eleman):
                for i in range(1,eleman+1):
                    sonucEleman *= i
                for i in range(1,secim+1):
                    sonucSecim *= i
                for i in range(1,fark+1):
                    sonucFark *= i

                sonuc = int(sonucEleman/(sonucSecim*sonucFark))

                self.sonuc.setText("C({},{}): {}".format(eleman,secim,sonuc))
            else:
                self.sonuc.setText("Eleman sayısından küçük bir seçim sayısı giriniz.")
        else:
            self.sonuc.setText("Hatalı veri girişi, pozitif sayı giriniz")
    
uygulama = QApplication(sys.argv)
pencere = CombinationCalculator()
sys.exit(uygulama.exec_())


# In[ ]:




