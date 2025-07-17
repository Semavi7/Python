import json
from difflib import get_close_matches as yakin_sonuclari_getir

def veritabani_yukle():
    with open("D:/Project/Python/yapayzeka/veritabani.json", "r", encoding='utf-8') as dosya:
        return json.load(dosya)
    
def veriTabanina_yaz(veriler):
    with open("D:/Project/Python/yapayzeka/veritabani.json", "w", encoding='utf-8') as dosya:
        json.dump(veriler, dosya, indent=2, ensure_ascii=False)

def yakin_sonuc_bul(soru, sorular):
    eslesen = yakin_sonuclari_getir(soru, sorular, n=1, cutoff=0.6)
    return eslesen[0] if eslesen else None

def cevabini_bul(soru, veritabani):
    for soru_cevaplar in veritabani["sorular"]:
        if soru_cevaplar["soru"] == soru:
            return soru_cevaplar["cevap"]
 
    return None

def chat_bot():
    veritabani = veritabani_yukle()

    while True:
        soru = input("Siz: ")

        if soru == 'çık':
            break
    
        gelen_sonuc = yakin_sonuc_bul(soru, [soru_cevaplar["soru"] for soru_cevaplar in veritabani["sorular"]])

        if gelen_sonuc:
            verilecek_cevap = cevabini_bul(gelen_sonuc, veritabani)
            print(f"Bot: {verilecek_cevap}")
        else:
            print("Bot: Bunu nasıl cevaplayacağımı bilmiyorum. Öğretir misin?")
            yeni_cevap = input("Öğretmek için yazabilir veya 'geç' diyabilirsin")

            if yeni_cevap != 'geç':
                veritabani["sorular"].append({
                    "soru": soru,
                    "cevap": yeni_cevap
                })
                veriTabanina_yaz(veritabani)
                print("Bot: Teşekkürler, sayende yeni bir şey öğrendim.")

if __name__ == '__main__':
    chat_bot()