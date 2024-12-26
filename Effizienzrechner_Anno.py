def ein_Verarbeitendesgebaeude ():
    while True:
            dauer_herstellendesgebaeude = int(input("Gib die Dauer des Herstellendengebäudes in Sekunden an: "))
            dauer_verarbeitendesgebaeude = int(input("Gib die Dauer des Verarbeitendengebäudes in Sekunden an: "))
            menge_verarbeitendegebaeude = None
            menge_herstellendergebaeude = int (input ("Gib die Anzahl des Herstellendengebäudes ein für die die Berechnung durchgeführt werden soll. "))

            while True:
                durchlaufzeit = dauer_herstellendesgebaeude / dauer_verarbeitendesgebaeude
                menge_verarbeitendegebaeude = durchlaufzeit * menge_herstellendergebaeude
                if menge_verarbeitendegebaeude.is_integer():
                    print(f"Menge Herstellendesgebäude ist: {int (menge_herstellendergebaeude)}")
                    print(f"Menge Verarbeitendegebäude ist: {int(menge_verarbeitendegebaeude)}")
                    break
                menge_herstellendergebaeude += 1
            erneut = input ("Möchtest du diese Rechnung für eine weiter Produktionskette durchführen? Y/N: ")
            if erneut != "Y":
                break

def zwei_Verarbeitendegebaeude ():
    while True:
            dauer_herstellendesgebaeude = int(input("Gib die Dauer des Herstellendengebäudes in Sekunden an: "))
            dauer_verarbeitendesgebaeude_1 = int(input("Gib die Dauer des ersten Verarbeitendengebäudes in Sekunden an: "))
            dauer_verarbeitendesgebaeude_2 = int(input("Gib die Dauer des zweiten Verarbeitendengebäudes in Sekunden an: "))
            menge_verarbeitendegebaeude_1 = None
            menge_verarbeitendegebaeude_2 = None
            menge_herstellendergebaeude = int (input ("Gib die Anzahl des Herstellendengebäudes ein für die die Berechnung durchgeführt werden soll. "))

            while True:
                durchlaufzeit_1 = dauer_herstellendesgebaeude / dauer_verarbeitendesgebaeude_1
                menge_verarbeitendegebaeude_1 = durchlaufzeit_1 * menge_herstellendergebaeude
                if menge_verarbeitendegebaeude_1.is_integer():
                    durchlaufzeit_2 = dauer_verarbeitendesgebaeude_1 / dauer_verarbeitendesgebaeude_2
                    menge_verarbeitendegebaeude_2 = durchlaufzeit_2 * menge_verarbeitendegebaeude_1
                    if menge_verarbeitendegebaeude_2.is_integer():
                        print(f"Menge Herstellendesgebäude ist: {int(menge_herstellendergebaeude)}")
                        print(f"Menge der ersten Verarbeitendegebäudes ist: {int (menge_verarbeitendegebaeude_1)}")
                        print(f"Menge der ersten Verarbeitendegebäudes ist: {int (menge_verarbeitendegebaeude_2)}")
                        break
                menge_herstellendergebaeude += 1
            erneut = input ("Möchtest du diese Rechnung für eine weiter Produktionskette durchführen? Y/N: ")
            if erneut != "Y":
                break


while True:
    Anzahl_Verarbeitendergebaeude = int (input("Wie viele Verarbeitendegebäude enthält deine Produktionskette? "))

    if Anzahl_Verarbeitendergebaeude == 1:
        ein_Verarbeitendesgebaeude ()
    elif Anzahl_Verarbeitendergebaeude == 2:
        zwei_Verarbeitendegebaeude ()

    erneut = input ("Möchtest du die Rechnung für eine weiter Produktionskette durchführen? Y/N: ")
    if erneut != "Y":
        break
