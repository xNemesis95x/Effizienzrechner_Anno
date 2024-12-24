while True:
    Anzahl_Verarbeitendergebaeude = int (input("Wie viele Verarbeitendegebäude enthält deine Produktionskette? "))

    if Anzahl_Verarbeitendergebaeude == 1:
        while True:
            dauer_herstellendesgebaeude = int(input("Gib die Dauer des Herstellendengebäudes in Sekunden an: "))
            dauer_verarbeitendesgebaeude = int(input("Gib die Dauer des Verarbeitendengebäudes in Sekunden an: "))
            menge_verarbeitendegebaeude = None
            menge_herstellendergebaeude = 1

            while True:
                durchlaufzeit = dauer_herstellendesgebaeude / dauer_verarbeitendesgebaeude
                menge_verarbeitendegebaeude = durchlaufzeit * menge_herstellendergebaeude
                if menge_verarbeitendegebaeude.is_integer():
                    print(f"Menge Herstellendesgebäude ist: {menge_herstellendergebaeude}")
                    print(f"Menge Verarbeitendegebäude ist: {int(menge_verarbeitendegebaeude)}")
                    break
                menge_herstellendergebaeude += 1
            erneut = input ("Möchtest du diese Rechnung für eine weiter Produktionskette durchführen? Y/N: ")
            if erneut != "Y":
                break
    erneut = input ("Möchtest du die Rechnung für eine weiter Produktionskette durchführen? Y/N: ")
    if erneut != "Y":
        break
