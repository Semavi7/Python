def yasKontrol(isim: str, yas: int):
    if yas > 0 and yas < 13:
        print(isim+", bu filmi izlemek için yaşınız 13'den büyük olmalı")
    elif yas <= 0:
        print(isim+", hatalı değer girdiniz.")
    else:
        print(isim+", bu filmi izleyebilirsiniz")

kisininYasi = input("Yaşınız kaç?")
yasKontrol("Burçhan", int(kisininYasi))    