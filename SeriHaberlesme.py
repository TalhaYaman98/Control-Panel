import sys, serial, time
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from pencere import Ui_MainWindow

class pencere(QMainWindow):                                 # QMainWindow'dan türetilen GUI için ana sınıf

    def __init__(self):
        super().__init__()                                  
        self.ui = Ui_MainWindow()                           # Kullanıcı arayüzünü başlatma
        self.ui.setupUi(self)                               # Arayüz setup
        self.setToolTip("DevamEt!!")                        # fare sabit kaldığında altında çıkan yazı

        self.ui.pushButton.clicked.connect(self.verial)     # butona basıldığında gidilen fonksiyon
        self.ui.pushButton_2.clicked.connect(self.gonder)   # butona basıldığında gidilen fonksiyon
        self.ui.pushButton_3.clicked.connect(self.oto)      # butona basıldığında gidilen fonksiyon

        self.ser = serial.Serial(       # seri haberleşme
        port='COM4',                    # Linux'ta /dev/ttyUSB4 veya /dev/ttyS4 olabilir
        baudrate=115200,                # veri akış hızı
        timeout=2                       # bekleme
        )
    
        if self.ser.is_open:                                # port açıkmı   
            port = str(self.ser.name)                       # port adını alır
            self.ui.label_2.setText(port)                   # port adını label üzerine yazar

    def verial(self):                                       # tek seferde veri almak için
        self.ser.reset_input_buffer()                       # Giriş tamponunu temizler
        gelen = self.ser.readline().decode('utf-8').strip() # porttan gelen veriyi okur
        self.ui.label.setText(str(gelen))                   # veriyi label üzerine yazar
        print("Gelen veri: " + str(gelen))                  # terminale yazar

    def gonder(self):                                       # tek seferde veri göndermek için
        gonderilen = self.ui.lineEdit.text() + "."          # verinin sonuna . koyar, stm32'in verinin bittiğini anlaması için 
        self.ser.write(gonderilen.encode('utf-8'))          # port üzerinden veriyi gönderir
        print("Veri gönderildi: " + str(gonderilen))        # terminale yazar

    def oto(self):                                               # veri alış verişini otomatik yapar

        while(True):
            self.ser.reset_input_buffer()                        # Giriş tamponunu temizler
            gelen = self.ser.readline().decode('utf-8').strip()  # porttan gelen veriyi okur
            self.ui.label.setText(str(gelen))                    # veriyi label üzerine yazar
            print("Gelen veri: " + str(gelen))                   # terminale yazar
            gonderilen = gelen +  "."                            # gelen veriyi noktalar
            self.ser.write(gonderilen.encode('utf-8'))           # port üzerinden veriyi gönderir
            print("Veri gönderildi: " + str(gonderilen))         # terminale yazar
            time.sleep(0.3)                                      # 0.3 saniye bekler, gözlemleme için

app = QApplication(sys.argv)     # PyQt5 uygulamasını başlatma
win = pencere()                  # Ana pencerenin bir örneğini oluşturma
win.show()                       # main window gösterme
app.exec_()                      # Uygulamanın ana döngüsünü yürütme 