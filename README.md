Proje Adı      : STM32 Ultrasonik Mesafe & 4-Digit Display Uygulaması
Dosya Adı      : main.c
Platform        : STM32F4 Serisi (ör. STM32F407 Discovery)
Geliştirme Ortamı: STM32CubeIDE (HAL tabanlı), VSC (Python)

Açıklama
--------
Bu proje, HC-SR04 ultrasonik mesafe sensöründen ölçüm alır, mesafeyi UART üzerinden gönderir
ve aynı zamanda TM1637 tabanlı 4-haneli 7-segment ekranda hem UART ile gelen değeri hem de
oldukça basit bir aralık kontrolüne göre LED’leri sürer. Bu süreci python ile yazdığımız kullanıcı arayüzü ile izleyebilir
ve kontrol edebilirsiniz.

Özellikler
----------
  • HC-SR04 ile mikro saniye hassasiyetinde mesafe ölçümü  
  • Ölçülen mesafeyi UART3 üzerinden ASCII formatında gönderme  
  • UART üzerinden gelen “.” karakteri ile biten sayısal veriyi parse edip 4-digit ekranda gösterme  
  • Gelen değere göre GPIOD üzerindeki 12, 13, 14 no’lu LED’leri seviye aralıklarına göre yakma  
  • TM1637 kütüphanesi ile display kontrolü  
  • DWT ile mikro saniye hassasiyetli delay

Donanım Bağlantıları
--------------------
  HC-SR04:
  
    • TRIG -> PA1  
    • ECHO -> PA2  

  TM1637 4-digit Display:
  
    • CLK  -> PC0  
    • DIO  -> PC1  

  UART3 (Kesme ile RX/TX):
  
    • TX   -> PD8  
    • RX   -> PD9  

  LED’ler (GPIOD):
  
    • Mesafe  1–10 cm arası: PD13  
    • Mesafe 11–20 cm arası: PD14  
    • Mesafe 21–30 cm arası: PD12  

Yazılım Bağımlılıkları
----------------------
  • STM32 HAL Kütüphaneleri  
  • dwt_stm32_delay.h (DWT mikro saniye delay)  
  • stm32_tm1637.h (TM1637 display sürücüsü)  
  • stdio.h, stdlib.h, string.h  
  • Python kütüphaneleri PyQt5, Serial, time, sys

Kurulum & Derleme
-----------------
1. STM32CubeIDE ile yeni bir STM32F4 projesi oluşturun.  
2. `main.c`, `dwt_stm32_delay.c/.h`, `stm32_tm1637.c/.h` dosyalarını proje klasörüne ekleyin.  
3. CubeMX yapılandırmasında:
     - USART3 alt yapısını (PD8/PD9, 115200 baud, RX kesmesi) aktif edin.  
     - TIM1’i temel zamanlayıcı olarak bırakın.  
     - GPIOD 12,13,14 pinlerini GPIO Output şeklinde ayarlayın.  
     - PA1 ve PA2 pinlerini GPIO Output/Input olarak ayarlayın.  
     - PC0 ve PC1 pinlerini GPIO Output olarak ayarlayın.  
4. Projeyi derleyin ve STM32 üzerine yükleyin.
5. Python Lunch.py dosyasını VSC ile çalıştırın.

Çalıştırma
----------
1. MCU resetlendikten sonra ekran “1111” gösterir.  
2. HC-SR04 sensörü aracılığıyla mesafe ölçümü başlar.  
3. Ölçülen mesafe cm cinsinden UART3 üzerinden gönderilir.  
4. Harici bir terminal programı (115200 baud, 8N1) ile gelen değerleri izleyebilirsiniz.  
5. UART üzerinden “1234.” (nokta ile biten) veri gönderirseniz,  
   - 1–10 arası ise PD13  
   - 11–20 arası ise PD14  
   - 21–30 arası ise PD12 LED’i yanar,  
   ve gelen sayı 4-digit ekranda gösterilir.
6. VSC ile python kodunu çalıştırıp tasarlanan arayüzle haberleşmeyi yapabilirsiniz.

Dosya Yapısı
------------
  ├── Src/  
  │   ├ main.c  
  │   ├ dwt_stm32_delay.c  
  │   └ stm32_tm1637.c  
  └── Inc/  
      ├ main.h  
      ├ dwt_stm32_delay.h  
      └ stm32_tm1637.h
