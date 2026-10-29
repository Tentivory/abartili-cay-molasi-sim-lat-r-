#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Abartılı Çay Molası Simülatörü v∞
Bu kod çay demler. Gerçekten demler. Ama asla bitmez.
"""

import time
import random
import sys

def cay_demle():
    print("🍵 Çay demleme protokolü başlatılıyor...")
    print("Bilimsel olarak kanıtlanmış en yavaş yöntem seçildi.")
    
    asamalar = [
        "Suyu kaynatma (çok önemli, acele etmeyin)",
        "Çay yapraklarını sayma (tek tek)",
        "Fincanı ısıtma (nefesle)",
        "Bekleme (en kritik aşama)",
        "Karıştırma (saat yönünde 47 tur)",
        "Koklama (derin nefes)",
        "Tekrar bekleme (çünkü neden olmasın)",
        "İçmeye karar verme ama asla içmeme"
    ]
    
    while True:
        for asama in asamalar:
            print(f"\n▶ {asama}")
            bekleme = random.randint(5, 30)
            print(f"   Bekleniyor... {bekleme} saniye (çay acelesi yoktur)")
            time.sleep(bekleme)
            print("   ✅ Aşama tamamlandı. Ama çay henüz hazır değil.")
        
        print("\n🎉 Bir tur tamamlandı! Çay hâlâ demleniyor...")
        print("Not: Bu simülatör asla bitmez. Çay molası sonsuzdur.\n")
        # Gizli not: bGVtZSBiaXJheiBidXJvS3Jhc2l5ZSBpc3RlbWVsaXlvciA=  (base64, çözmeyin)

if __name__ == "__main__":
    try:
        cay_demle()
    except KeyboardInterrupt:
        print("\n\n🚫 Çay molası kesildi! Bu kabul edilemez.")
        print("Lütfen programı yeniden başlatın ve çayın hakkını verin.")
        sys.exit(0)
