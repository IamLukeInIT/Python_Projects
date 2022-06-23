cat1 = "Kosmos"
cat2 = "Polityka"
cat3 = "Geografia"
cat4 = "Muzyka"
cat5 = "Sport"
cat6 = "Chemia"
cat7 = "Technologia"
cat8 = "Zwierzęta"
cat9 = "Zagadki"
cat10 = "Religia"

print("Aby wygrać quiz trzeba odpowiedzieć na 10 pytań. W każdej rundzie są do wyboru dwie kategorie.\n")
print("Etap 1\n Kategorie:\n    "   + cat1  + " | " + cat2)
category = input("Którą kategorię wybierasz?\n")
if category == cat1:
    print("Pytanie z kategori" + cat1)
    print("Asteryzm Wielkiego Wozu jest cześcią jakiego gwiazdozbioru?")
    answer = input("a) Rysia    b) Hydry    c) Wielkiej Niedźwiedzicy   d) Kompasu\n")
    if answer != "c":
        print("PRZEGRANA. \nNieprawidłowa odpowiedź.")
        exit()
    else:
        print('Prawidłowa odpowiedź.\nPrzechodzisz do następnego etapu.')    
else:
    print("Pytanie z kategori" + cat2)
    print(""""Pieniądze nie spadają z nieba, muszą być zarobione na Ziemi" stwierdziła:""")
    answer = input("a) Hillary Clinton    b) Margaret Thatcher  c) Beata Szydło       d) Indira Gandhi\n")
    if answer != "b":
        print("PRZEGRANA. \nNieprawidłowa odpowiedź.")
        exit()
    else:
        print('Prawidłowa odpowiedź.\nPrzechodzisz do następnego etapu.') 

print("Etap 2\n Kategorie:\n    " + cat3 + " | " + cat4)
category = input("Którą kategorię wybierasz?\n")
if category == cat3:
    print("Pytanie z kategori" + cat3)
    print("Stolicą Azerbejdżanu jest:")
    answer = input("a) Damaszek    b) Bagdad    c) Islamabad   d) Baku\n")
    if answer != "d":
        print("PRZEGRANA. \nNieprawidłowa odpowiedź.")
        exit()
    else:
        print('Prawidłowa odpowiedź.\nPrzechodzisz do następnego etapu.')    
else:
    print("Pytanie z kategori" + cat4)
    print("Autorem słów i muzyki piosenki „Samotni ludzie” jest Stanisław Staszewski. Piosenka znalazła się na płycie „Tata 2”. Który zespół wykonuje ten utwór?")
    answer = input("a) Kult    b) T.Love    c) Dżem     d) Republika\n")
    if answer != "a":
        print("PRZEGRANA. \nNieprawidłowa odpowiedź.")
        exit()
    else:
        print('Prawidłowa odpowiedź.\nPrzechodzisz do następnego etapu.') 

print("Etap 3\n Kategorie:\n    "+ cat5 + " | " + cat6)
category = input("Którą kategorię wybierasz?\n")
if category == cat5:
    print("Pytanie z kategori" + cat5)
    print("W której z dyscyplin gra jest przerywana, kiedy piłka dotknie boiska?")
    answer = input("a) Tenis ziemny    b) Rugby    c) Piłka ręczna   d) Siatkówka\n")
    if answer != "d":
        print("PRZEGRANA. \nNieprawidłowa odpowiedź.")
        exit()
    else:
        print('Prawidłowa odpowiedź.\nPrzechodzisz do następnego etapu.')    
else:
    print("Pytanie z kategori" + cat6)
    print("NaCl to wzór chemiczny:")
    answer = input("a) Chlorku sodu    b) Kwasu siarkowego    c) Wodorotlenku sodu     d) Tlenku węgla\n")
    if answer != "a":
        print("PRZEGRANA. \nNieprawidłowa odpowiedź.")
        exit()
    else:
        print('Prawidłowa odpowiedź.\nPrzechodzisz do następnego etapu.') 

print("Etap 4\n Kategorie:\n    "+ cat7 + " | " + cat8)
category = input("Którą kategorię wybierasz?\n")
if category == cat7:
    print("Pytanie z kategori" + cat7)
    print("W którym roku powstał pierwszy protopy komputra?")
    answer = input("a) w 30 p.n.e    b) W 300 p.n.e    c) W 3000 p.n.e   d) W 30 n.e\n")
    if answer != "c":
        print("PRZEGRANA. \nNieprawidłowa odpowiedź.")
        exit()
    else:
        print('Prawidłowa odpowiedź.\nPrzechodzisz do następnego etapu.')    
else:
    print("Pytanie z kategori" + cat8)
    print("Psi pysk to inaczej:")
    answer = input("a) Chrapa    b) Kufa    c) Stop     d) Fafel\n")
    if answer != "b":
        print("PRZEGRANA. \nNieprawidłowa odpowiedź.")
        exit()
    else:
        print('Prawidłowa odpowiedź.\nPrzechodzisz do następnego etapu.') 

print("Etap 5\n Kategorie:\n    "+ cat9 + " | " + cat10)
category = input("Którą kategorię wybierasz?\n")
if category == cat9:
    print("Pytanie z kategori" + cat9)
    print("X + X + X = 60\nX + Y + Y = 30\nY + Z = 3\nZ + X + Y = ?")
    answer = input("a) 26    b) 27    c) 102   d) 81\n")
    if answer != "d":
        print("PRZEGRANA. \nNieprawidłowa odpowiedź.")
        exit()
    else:
        print('Prawidłowa odpowiedź.\nPrzechodzisz do następnego etapu.')    
else:
    print("Pytanie z kategori" + cat10)
    print("""Bądź pochwalony, Rozdawco cierpienia! Ręceż mi przekłuł i nogi I krew mi cieknie z głowy" to incipit wiersza Jana Kasprowicza - "Hymn Św. Franciszka z:""")
    answer = input("a) Padwy    b) Asyżu    c) Gandawy     d) Pontu\n")
    if answer != "b":
        print("PRZEGRANA. \nNieprawidłowa odpowiedź.")
        exit()
    else:
        print('Prawidłowa odpowiedź.\nPrzechodzisz do następnego etapu.') 

print("Brawo! Odpowiedziałeś poprawnie na wszystkie pytania.")
