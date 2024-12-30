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
                        print(f"Menge des ersten Verarbeitendegebäudes ist: {int (menge_verarbeitendegebaeude_1)}")
                        print(f"Menge des zweiten Verarbeitendegebäudes ist: {int (menge_verarbeitendegebaeude_2)}")
                        break
                menge_herstellendergebaeude += 1
            erneut = input ("Möchtest du diese Rechnung für eine weiter Produktionskette durchführen? Y/N: ")
            if erneut != "Y":
                break

def drei_Verarbeitendegebaeude ():
     while True:
            dauer_herstellendesgebaeude = int(input("Gib die Dauer des Herstellendengebäudes in Sekunden an: "))
            dauer_verarbeitendesgebaeude_1 = int(input("Gib die Dauer des ersten Verarbeitendengebäudes in Sekunden an: "))
            dauer_verarbeitendesgebaeude_2 = int(input("Gib die Dauer des zweiten Verarbeitendengebäudes in Sekunden an: "))
            dauer_verarbeitendesgebaeude_3 = int(input("Gib die Dauer des dritten Verarbeitendengebäudes in Sekunden an: "))
            menge_verarbeitendegebaeude_1 = None
            menge_verarbeitendegebaeude_2 = None
            menge_verarbeitendegebaeude_3 = None
            menge_herstellendergebaeude = int (input ("Gib die Anzahl des Herstellendengebäudes ein für die die Berechnung durchgeführt werden soll. "))

            while True:
                durchlaufzeit_1 = dauer_herstellendesgebaeude / dauer_verarbeitendesgebaeude_1
                menge_verarbeitendegebaeude_1 = durchlaufzeit_1 * menge_herstellendergebaeude
                if menge_verarbeitendegebaeude_1.is_integer():
                    durchlaufzeit_2 = dauer_verarbeitendesgebaeude_1 / dauer_verarbeitendesgebaeude_2
                    menge_verarbeitendegebaeude_2 = durchlaufzeit_2 * menge_verarbeitendegebaeude_1
                    if menge_verarbeitendegebaeude_2.is_integer():
                        durchlaufzeit_3 = dauer_verarbeitendesgebaeude_2 / dauer_verarbeitendesgebaeude_3
                        menge_verarbeitendegebaeude_3 = durchlaufzeit_3 * menge_verarbeitendegebaeude_2
                        if menge_verarbeitendegebaeude_3.is_integer ():
                            print(f"Menge Herstellendesgebäude ist: {int(menge_herstellendergebaeude)}")
                            print(f"Menge des ersten Verarbeitendegebäudes ist: {int (menge_verarbeitendegebaeude_1)}")
                            print(f"Menge des zweiten Verarbeitendegebäudes ist: {int (menge_verarbeitendegebaeude_2)}")
                            print(f"Menge des dritten Verarbeitendengebäudes ist: {int (menge_verarbeitendegebaeude_3)}")

                            break
                menge_herstellendergebaeude += 1
            erneut = input ("Möchtest du diese Rechnung für eine weiter Produktionskette durchführen? Y/N: ")
            if erneut != "Y":
                break

def vier_Verarbeitendegebaeude ():
    while True:
            dauer_herstellendesgebaeude = int(input("Gib die Dauer des Herstellendengebäudes in Sekunden an: "))
            dauer_verarbeitendesgebaeude_1 = int(input("Gib die Dauer des ersten Verarbeitendengebäudes in Sekunden an: "))
            dauer_verarbeitendesgebaeude_2 = int(input("Gib die Dauer des zweiten Verarbeitendengebäudes in Sekunden an: "))
            dauer_verarbeitendesgebaeude_3 = int(input("Gib die Dauer des dritten Verarbeitendengebäudes in Sekunden an: "))
            dauer_verarbeitendesgebaeude_4 = int(input("Gib die Dauer des vierten Verarbeitendengebäudes in Sekunden an: "))
            menge_verarbeitendegebaeude_1 = None
            menge_verarbeitendegebaeude_2 = None
            menge_verarbeitendegebaeude_3 = None
            menge_verarbeitendegebaeude_4 = None
            menge_herstellendergebaeude = int (input ("Gib die Anzahl des Herstellendengebäudes ein für die die Berechnung durchgeführt werden soll. "))

            while True:
                durchlaufzeit_1 = dauer_herstellendesgebaeude / dauer_verarbeitendesgebaeude_1
                menge_verarbeitendegebaeude_1 = durchlaufzeit_1 * menge_herstellendergebaeude
                if menge_verarbeitendegebaeude_1.is_integer():
                    durchlaufzeit_2 = dauer_verarbeitendesgebaeude_1 / dauer_verarbeitendesgebaeude_2
                    menge_verarbeitendegebaeude_2 = durchlaufzeit_2 * menge_verarbeitendegebaeude_1
                    if menge_verarbeitendegebaeude_2.is_integer():
                        durchlaufzeit_3 = dauer_verarbeitendesgebaeude_2 / dauer_verarbeitendesgebaeude_3
                        menge_verarbeitendegebaeude_3 = durchlaufzeit_3 * menge_verarbeitendegebaeude_2
                        if menge_verarbeitendegebaeude_3.is_integer ():
                            durchlaufzeit_4 = dauer_verarbeitendesgebaeude_3 / dauer_verarbeitendesgebaeude_4
                            menge_verarbeitendegebaeude_4 = durchlaufzeit_4 * menge_verarbeitendegebaeude_3
                            if menge_verarbeitendegebaeude_4.is_integer ():
                                print(f"Menge Herstellendesgebäude ist: {int(menge_herstellendergebaeude)}")
                                print(f"Menge des ersten Verarbeitendegebäudes ist: {int (menge_verarbeitendegebaeude_1)}")
                                print(f"Menge des zweiten Verarbeitendegebäudes ist: {int (menge_verarbeitendegebaeude_2)}")
                                print(f"Menge des dritten Verarbeitendengebäudes ist: {int (menge_verarbeitendegebaeude_3)}")
                                print(f"Menge des vierten Verarbeitendengebäudes ist: {int (menge_verarbeitendegebaeude_4)}")

                            break
                menge_herstellendergebaeude += 1
            erneut = input ("Möchtest du diese Rechnung für eine weiter Produktionskette durchführen? Y/N: ")
            if erneut != "Y":
                break

def fuenf_Verarbeitendegebaeude ():
     while True:
            dauer_herstellendesgebaeude = int(input("Gib die Dauer des Herstellendengebäudes in Sekunden an: "))
            dauer_verarbeitendesgebaeude_1 = int(input("Gib die Dauer des ersten Verarbeitendengebäudes in Sekunden an: "))
            dauer_verarbeitendesgebaeude_2 = int(input("Gib die Dauer des zweiten Verarbeitendengebäudes in Sekunden an: "))
            dauer_verarbeitendesgebaeude_3 = int(input("Gib die Dauer des dritten Verarbeitendengebäudes in Sekunden an: "))
            dauer_verarbeitendesgebaeude_4 = int(input("Gib die Dauer des vierten Verarbeitendengebäudes in Sekunden an: "))
            dauer_verarbeitendesgebaeude_5 = int(input("Gib die Dauer des fünften Verarbeitendengebäudes in Sekunden an: "))
            menge_verarbeitendegebaeude_1 = None
            menge_verarbeitendegebaeude_2 = None
            menge_verarbeitendegebaeude_3 = None
            menge_verarbeitendegebaeude_4 = None
            menge_verarbeitendegebaeude_5 = None
            menge_herstellendergebaeude = int (input ("Gib die Anzahl des Herstellendengebäudes ein für die die Berechnung durchgeführt werden soll. "))

            while True:
                durchlaufzeit_1 = dauer_herstellendesgebaeude / dauer_verarbeitendesgebaeude_1
                menge_verarbeitendegebaeude_1 = durchlaufzeit_1 * menge_herstellendergebaeude
                if menge_verarbeitendegebaeude_1.is_integer():
                    durchlaufzeit_2 = dauer_verarbeitendesgebaeude_1 / dauer_verarbeitendesgebaeude_2
                    menge_verarbeitendegebaeude_2 = durchlaufzeit_2 * menge_verarbeitendegebaeude_1
                    if menge_verarbeitendegebaeude_2.is_integer():
                        durchlaufzeit_3 = dauer_verarbeitendesgebaeude_2 / dauer_verarbeitendesgebaeude_3
                        menge_verarbeitendegebaeude_3 = durchlaufzeit_3 * menge_verarbeitendegebaeude_2
                        if menge_verarbeitendegebaeude_3.is_integer ():
                            durchlaufzeit_4 = dauer_verarbeitendesgebaeude_3 / dauer_verarbeitendesgebaeude_4
                            menge_verarbeitendegebaeude_4 = durchlaufzeit_4 * menge_verarbeitendegebaeude_3
                            if menge_verarbeitendegebaeude_4.is_integer ():
                                durchlaufzeit_5 = dauer_verarbeitendesgebaeude_4 / dauer_verarbeitendesgebaeude_5
                                menge_verarbeitendegebaeude_5 = durchlaufzeit_5 * menge_verarbeitendegebaeude_4
                                if menge_verarbeitendegebaeude_5.is_integer ():
                                    print(f"Menge Herstellendesgebäude ist: {int(menge_herstellendergebaeude)}")
                                    print(f"Menge des ersten Verarbeitendegebäudes ist: {int (menge_verarbeitendegebaeude_1)}")
                                    print(f"Menge des zweiten Verarbeitendegebäudes ist: {int (menge_verarbeitendegebaeude_2)}")
                                    print(f"Menge des dritten Verarbeitendengebäudes ist: {int (menge_verarbeitendegebaeude_3)}")
                                    print(f"Menge des vierten Verarbeitendengebäudes ist: {int (menge_verarbeitendegebaeude_4)}")
                                    print(f"Menge des fünften Verarbeitendengebäudes ist: {int (menge_verarbeitendegebaeude_5)}")

                            break
                menge_herstellendergebaeude += 1
            erneut = input ("Möchtest du diese Rechnung für eine weiter Produktionskette durchführen? Y/N: ")
            if erneut != "Y":
                break

def sechs_Verarbeitendegebaeude ():
    while True:
            dauer_herstellendesgebaeude = int(input("Gib die Dauer des Herstellendengebäudes in Sekunden an: "))
            dauer_verarbeitendesgebaeude_1 = int(input("Gib die Dauer des ersten Verarbeitendengebäudes in Sekunden an: "))
            dauer_verarbeitendesgebaeude_2 = int(input("Gib die Dauer des zweiten Verarbeitendengebäudes in Sekunden an: "))
            dauer_verarbeitendesgebaeude_3 = int(input("Gib die Dauer des dritten Verarbeitendengebäudes in Sekunden an: "))
            dauer_verarbeitendesgebaeude_4 = int(input("Gib die Dauer des vierten Verarbeitendengebäudes in Sekunden an: "))
            dauer_verarbeitendesgebaeude_5 = int(input("Gib die Dauer des fünften Verarbeitendengebäudes in Sekunden an: "))
            dauer_verarbeitendesgebaeude_6 = int(input("Gib die Dauer des sechsten Verarbeitendengebäudes in Sekunden an: "))
            menge_verarbeitendegebaeude_1 = None
            menge_verarbeitendegebaeude_2 = None
            menge_verarbeitendegebaeude_3 = None
            menge_verarbeitendegebaeude_4 = None
            menge_verarbeitendegebaeude_5 = None
            menge_verarbeitendegebaeude_6 = None
            menge_herstellendergebaeude = int (input ("Gib die Anzahl des Herstellendengebäudes ein für die die Berechnung durchgeführt werden soll. "))

            while True:
                durchlaufzeit_1 = dauer_herstellendesgebaeude / dauer_verarbeitendesgebaeude_1
                menge_verarbeitendegebaeude_1 = durchlaufzeit_1 * menge_herstellendergebaeude
                if menge_verarbeitendegebaeude_1.is_integer():
                    durchlaufzeit_2 = dauer_verarbeitendesgebaeude_1 / dauer_verarbeitendesgebaeude_2
                    menge_verarbeitendegebaeude_2 = durchlaufzeit_2 * menge_verarbeitendegebaeude_1
                    if menge_verarbeitendegebaeude_2.is_integer():
                        durchlaufzeit_3 = dauer_verarbeitendesgebaeude_2 / dauer_verarbeitendesgebaeude_3
                        menge_verarbeitendegebaeude_3 = durchlaufzeit_3 * menge_verarbeitendegebaeude_2
                        if menge_verarbeitendegebaeude_3.is_integer ():
                            durchlaufzeit_4 = dauer_verarbeitendesgebaeude_3 / dauer_verarbeitendesgebaeude_4
                            menge_verarbeitendegebaeude_4 = durchlaufzeit_4 * menge_verarbeitendegebaeude_3
                            if menge_verarbeitendegebaeude_4.is_integer ():
                                durchlaufzeit_5 = dauer_verarbeitendesgebaeude_4 / dauer_verarbeitendesgebaeude_5
                                menge_verarbeitendegebaeude_5 = durchlaufzeit_5 * menge_verarbeitendegebaeude_4
                                if menge_verarbeitendegebaeude_5.is_integer ():
                                    durchlaufzeit_6 = dauer_verarbeitendesgebaeude_5 / dauer_verarbeitendesgebaeude_6
                                    menge_verarbeitendegebaeude_6 = durchlaufzeit_6 * menge_verarbeitendegebaeude_5
                                    if menge_verarbeitendegebaeude_6.is_integer ():
                                        print(f"Menge Herstellendesgebäude ist: {int(menge_herstellendergebaeude)}")
                                        print(f"Menge des ersten Verarbeitendegebäudes ist: {int (menge_verarbeitendegebaeude_1)}")
                                        print(f"Menge des zweiten Verarbeitendegebäudes ist: {int (menge_verarbeitendegebaeude_2)}")
                                        print(f"Menge des dritten Verarbeitendengebäudes ist: {int (menge_verarbeitendegebaeude_3)}")
                                        print(f"Menge des vierten Verarbeitendengebäudes ist: {int (menge_verarbeitendegebaeude_4)}")
                                        print(f"Menge des fünften Verarbeitendengebäudes ist: {int (menge_verarbeitendegebaeude_5)}")
                                        print(f"Menge des sechsten Verarbeitendengebäudes ist: {int (menge_verarbeitendegebaeude_6)}")

                            break
                menge_herstellendergebaeude += 1
            erneut = input ("Möchtest du diese Rechnung für eine weiter Produktionskette durchführen? Y/N: ")
            if erneut != "Y":
                break

def sieben_Verarbeitendegebaeude ():
    while True:
            dauer_herstellendesgebaeude = int(input("Gib die Dauer des Herstellendengebäudes in Sekunden an: "))
            dauer_verarbeitendesgebaeude_1 = int(input("Gib die Dauer des ersten Verarbeitendengebäudes in Sekunden an: "))
            dauer_verarbeitendesgebaeude_2 = int(input("Gib die Dauer des zweiten Verarbeitendengebäudes in Sekunden an: "))
            dauer_verarbeitendesgebaeude_3 = int(input("Gib die Dauer des dritten Verarbeitendengebäudes in Sekunden an: "))
            dauer_verarbeitendesgebaeude_4 = int(input("Gib die Dauer des vierten Verarbeitendengebäudes in Sekunden an: "))
            dauer_verarbeitendesgebaeude_5 = int(input("Gib die Dauer des fünften Verarbeitendengebäudes in Sekunden an: "))
            dauer_verarbeitendesgebaeude_6 = int(input("Gib die Dauer des sechsten Verarbeitendengebäudes in Sekunden an: "))
            dauer_verarbeitendesgebaeude_7 = int(input("Gib die Dauer des siebten Verarbeitendengebäudes in Sekunden an: "))
            menge_verarbeitendegebaeude_1 = None
            menge_verarbeitendegebaeude_2 = None
            menge_verarbeitendegebaeude_3 = None
            menge_verarbeitendegebaeude_4 = None
            menge_verarbeitendegebaeude_5 = None
            menge_verarbeitendegebaeude_6 = None
            menge_verarbeitendegebaeude_7 = None
            menge_herstellendergebaeude = int (input ("Gib die Anzahl des Herstellendengebäudes ein für die die Berechnung durchgeführt werden soll. "))

            while True:
                durchlaufzeit_1 = dauer_herstellendesgebaeude / dauer_verarbeitendesgebaeude_1
                menge_verarbeitendegebaeude_1 = durchlaufzeit_1 * menge_herstellendergebaeude
                if menge_verarbeitendegebaeude_1.is_integer():
                    durchlaufzeit_2 = dauer_verarbeitendesgebaeude_1 / dauer_verarbeitendesgebaeude_2
                    menge_verarbeitendegebaeude_2 = durchlaufzeit_2 * menge_verarbeitendegebaeude_1
                    if menge_verarbeitendegebaeude_2.is_integer():
                        durchlaufzeit_3 = dauer_verarbeitendesgebaeude_2 / dauer_verarbeitendesgebaeude_3
                        menge_verarbeitendegebaeude_3 = durchlaufzeit_3 * menge_verarbeitendegebaeude_2
                        if menge_verarbeitendegebaeude_3.is_integer ():
                            durchlaufzeit_4 = dauer_verarbeitendesgebaeude_3 / dauer_verarbeitendesgebaeude_4
                            menge_verarbeitendegebaeude_4 = durchlaufzeit_4 * menge_verarbeitendegebaeude_3
                            if menge_verarbeitendegebaeude_4.is_integer ():
                                durchlaufzeit_5 = dauer_verarbeitendesgebaeude_4 / dauer_verarbeitendesgebaeude_5
                                menge_verarbeitendegebaeude_5 = durchlaufzeit_5 * menge_verarbeitendegebaeude_4
                                if menge_verarbeitendegebaeude_5.is_integer ():
                                    durchlaufzeit_6 = dauer_verarbeitendesgebaeude_5 / dauer_verarbeitendesgebaeude_6
                                    menge_verarbeitendegebaeude_6 = durchlaufzeit_6 * menge_verarbeitendegebaeude_5
                                    if menge_verarbeitendegebaeude_6.is_integer ():
                                        durchlaufzeit_7 = dauer_verarbeitendesgebaeude_6 / dauer_verarbeitendesgebaeude_7
                                        menge_verarbeitendegebaeude_7 = durchlaufzeit_7 * menge_verarbeitendegebaeude_6
                                        if menge_verarbeitendegebaeude_7.is_integer ():
                                            print(f"Menge Herstellendesgebäude ist: {int(menge_herstellendergebaeude)}")
                                            print(f"Menge des ersten Verarbeitendegebäudes ist: {int (menge_verarbeitendegebaeude_1)}")
                                            print(f"Menge des zweiten Verarbeitendegebäudes ist: {int (menge_verarbeitendegebaeude_2)}")
                                            print(f"Menge des dritten Verarbeitendengebäudes ist: {int (menge_verarbeitendegebaeude_3)}")
                                            print(f"Menge des vierten Verarbeitendengebäudes ist: {int (menge_verarbeitendegebaeude_4)}")
                                            print(f"Menge des fünften Verarbeitendengebäudes ist: {int (menge_verarbeitendegebaeude_5)}")
                                            print(f"Menge des sechsten Verarbeitendengebäudes ist: {int (menge_verarbeitendegebaeude_6)}")
                                            print(f"Menge des siebten Verarbeitendengebäudes ist: {int (menge_verarbeitendegebaeude_7)}")

                            break
                menge_herstellendergebaeude += 1
            erneut = input ("Möchtest du diese Rechnung für eine weiter Produktionskette durchführen? Y/N: ")
            if erneut != "Y":
                break

def acht_Verarbeitendegebaeude ():
    while True:
            dauer_herstellendesgebaeude = int(input("Gib die Dauer des Herstellendengebäudes in Sekunden an: "))
            dauer_verarbeitendesgebaeude_1 = int(input("Gib die Dauer des ersten Verarbeitendengebäudes in Sekunden an: "))
            dauer_verarbeitendesgebaeude_2 = int(input("Gib die Dauer des zweiten Verarbeitendengebäudes in Sekunden an: "))
            dauer_verarbeitendesgebaeude_3 = int(input("Gib die Dauer des dritten Verarbeitendengebäudes in Sekunden an: "))
            dauer_verarbeitendesgebaeude_4 = int(input("Gib die Dauer des vierten Verarbeitendengebäudes in Sekunden an: "))
            dauer_verarbeitendesgebaeude_5 = int(input("Gib die Dauer des fünften Verarbeitendengebäudes in Sekunden an: "))
            dauer_verarbeitendesgebaeude_6 = int(input("Gib die Dauer des sechsten Verarbeitendengebäudes in Sekunden an: "))
            dauer_verarbeitendesgebaeude_7 = int(input("Gib die Dauer des siebten Verarbeitendengebäudes in Sekunden an: "))
            dauer_verarbeitendesgebaeude_8 = int(input("Gib die Dauer des achten Verarbeitendengebäudes in Sekunden an: "))
            menge_verarbeitendegebaeude_1 = None
            menge_verarbeitendegebaeude_2 = None
            menge_verarbeitendegebaeude_3 = None
            menge_verarbeitendegebaeude_4 = None
            menge_verarbeitendegebaeude_5 = None
            menge_verarbeitendegebaeude_6 = None
            menge_verarbeitendegebaeude_7 = None
            menge_verarbeitendegebaeude_8 = None
            menge_herstellendergebaeude = int (input ("Gib die Anzahl des Herstellendengebäudes ein für die die Berechnung durchgeführt werden soll. "))

            while True:
                durchlaufzeit_1 = dauer_herstellendesgebaeude / dauer_verarbeitendesgebaeude_1
                menge_verarbeitendegebaeude_1 = durchlaufzeit_1 * menge_herstellendergebaeude
                if menge_verarbeitendegebaeude_1.is_integer():
                    durchlaufzeit_2 = dauer_verarbeitendesgebaeude_1 / dauer_verarbeitendesgebaeude_2
                    menge_verarbeitendegebaeude_2 = durchlaufzeit_2 * menge_verarbeitendegebaeude_1
                    if menge_verarbeitendegebaeude_2.is_integer():
                        durchlaufzeit_3 = dauer_verarbeitendesgebaeude_2 / dauer_verarbeitendesgebaeude_3
                        menge_verarbeitendegebaeude_3 = durchlaufzeit_3 * menge_verarbeitendegebaeude_2
                        if menge_verarbeitendegebaeude_3.is_integer ():
                            durchlaufzeit_4 = dauer_verarbeitendesgebaeude_3 / dauer_verarbeitendesgebaeude_4
                            menge_verarbeitendegebaeude_4 = durchlaufzeit_4 * menge_verarbeitendegebaeude_3
                            if menge_verarbeitendegebaeude_4.is_integer ():
                                durchlaufzeit_5 = dauer_verarbeitendesgebaeude_4 / dauer_verarbeitendesgebaeude_5
                                menge_verarbeitendegebaeude_5 = durchlaufzeit_5 * menge_verarbeitendegebaeude_4
                                if menge_verarbeitendegebaeude_5.is_integer ():
                                    durchlaufzeit_6 = dauer_verarbeitendesgebaeude_5 / dauer_verarbeitendesgebaeude_6
                                    menge_verarbeitendegebaeude_6 = durchlaufzeit_6 * menge_verarbeitendegebaeude_5
                                    if menge_verarbeitendegebaeude_6.is_integer ():
                                        durchlaufzeit_7 = dauer_verarbeitendesgebaeude_6 / dauer_verarbeitendesgebaeude_7
                                        menge_verarbeitendegebaeude_7 = durchlaufzeit_7 * menge_verarbeitendegebaeude_6
                                        if menge_verarbeitendegebaeude_7.is_integer ():
                                            durchlaufzeit_8 = dauer_verarbeitendesgebaeude_7 / dauer_verarbeitendesgebaeude_8
                                            menge_verarbeitendegebaeude_8 = durchlaufzeit_8 * menge_verarbeitendegebaeude_7
                                            if menge_verarbeitendegebaeude_8.is_integer ():
                                                print(f"Menge Herstellendesgebäude ist: {int(menge_herstellendergebaeude)}")
                                                print(f"Menge des ersten Verarbeitendegebäudes ist: {int (menge_verarbeitendegebaeude_1)}")
                                                print(f"Menge des zweiten Verarbeitendegebäudes ist: {int (menge_verarbeitendegebaeude_2)}")
                                                print(f"Menge des dritten Verarbeitendengebäudes ist: {int (menge_verarbeitendegebaeude_3)}")
                                                print(f"Menge des vierten Verarbeitendengebäudes ist: {int (menge_verarbeitendegebaeude_4)}")
                                                print(f"Menge des fünften Verarbeitendengebäudes ist: {int (menge_verarbeitendegebaeude_5)}")
                                                print(f"Menge des sechsten Verarbeitendengebäudes ist: {int (menge_verarbeitendegebaeude_6)}")
                                                print(f"Menge des siebten Verarbeitendengebäudes ist: {int (menge_verarbeitendegebaeude_7)}")
                                                print(f"Menge des achten Verarbeitendengebäudes ist: {int (menge_verarbeitendegebaeude_8)}")

                            break
                menge_herstellendergebaeude += 1
            erneut = input ("Möchtest du diese Rechnung für eine weiter Produktionskette durchführen? Y/N: ")
            if erneut != "Y":
                break

def neun_Verarbeitendegebaeude ():
    while True:
            dauer_herstellendesgebaeude = int(input("Gib die Dauer des Herstellendengebäudes in Sekunden an: "))
            dauer_verarbeitendesgebaeude_1 = int(input("Gib die Dauer des ersten Verarbeitendengebäudes in Sekunden an: "))
            dauer_verarbeitendesgebaeude_2 = int(input("Gib die Dauer des zweiten Verarbeitendengebäudes in Sekunden an: "))
            dauer_verarbeitendesgebaeude_3 = int(input("Gib die Dauer des dritten Verarbeitendengebäudes in Sekunden an: "))
            dauer_verarbeitendesgebaeude_4 = int(input("Gib die Dauer des vierten Verarbeitendengebäudes in Sekunden an: "))
            dauer_verarbeitendesgebaeude_5 = int(input("Gib die Dauer des fünften Verarbeitendengebäudes in Sekunden an: "))
            dauer_verarbeitendesgebaeude_6 = int(input("Gib die Dauer des sechsten Verarbeitendengebäudes in Sekunden an: "))
            dauer_verarbeitendesgebaeude_7 = int(input("Gib die Dauer des siebten Verarbeitendengebäudes in Sekunden an: "))
            dauer_verarbeitendesgebaeude_8 = int(input("Gib die Dauer des achten Verarbeitendengebäudes in Sekunden an: "))
            dauer_verarbeitendesgebaeude_9 = int(input("Gib die Dauer des neunten Verarbeitendengebäudes in Sekunden an: "))
            menge_verarbeitendegebaeude_1 = None
            menge_verarbeitendegebaeude_2 = None
            menge_verarbeitendegebaeude_3 = None
            menge_verarbeitendegebaeude_4 = None
            menge_verarbeitendegebaeude_5 = None
            menge_verarbeitendegebaeude_6 = None
            menge_verarbeitendegebaeude_7 = None
            menge_verarbeitendegebaeude_8 = None
            menge_verarbeitendegebaeude_9 = None
            menge_herstellendergebaeude = int (input ("Gib die Anzahl des Herstellendengebäudes ein für die die Berechnung durchgeführt werden soll. "))

            while True:
                durchlaufzeit_1 = dauer_herstellendesgebaeude / dauer_verarbeitendesgebaeude_1
                menge_verarbeitendegebaeude_1 = durchlaufzeit_1 * menge_herstellendergebaeude
                if menge_verarbeitendegebaeude_1.is_integer():
                    durchlaufzeit_2 = dauer_verarbeitendesgebaeude_1 / dauer_verarbeitendesgebaeude_2
                    menge_verarbeitendegebaeude_2 = durchlaufzeit_2 * menge_verarbeitendegebaeude_1
                    if menge_verarbeitendegebaeude_2.is_integer():
                        durchlaufzeit_3 = dauer_verarbeitendesgebaeude_2 / dauer_verarbeitendesgebaeude_3
                        menge_verarbeitendegebaeude_3 = durchlaufzeit_3 * menge_verarbeitendegebaeude_2
                        if menge_verarbeitendegebaeude_3.is_integer ():
                            durchlaufzeit_4 = dauer_verarbeitendesgebaeude_3 / dauer_verarbeitendesgebaeude_4
                            menge_verarbeitendegebaeude_4 = durchlaufzeit_4 * menge_verarbeitendegebaeude_3
                            if menge_verarbeitendegebaeude_4.is_integer ():
                                durchlaufzeit_5 = dauer_verarbeitendesgebaeude_4 / dauer_verarbeitendesgebaeude_5
                                menge_verarbeitendegebaeude_5 = durchlaufzeit_5 * menge_verarbeitendegebaeude_4
                                if menge_verarbeitendegebaeude_5.is_integer ():
                                    durchlaufzeit_6 = dauer_verarbeitendesgebaeude_5 / dauer_verarbeitendesgebaeude_6
                                    menge_verarbeitendegebaeude_6 = durchlaufzeit_6 * menge_verarbeitendegebaeude_5
                                    if menge_verarbeitendegebaeude_6.is_integer ():
                                        durchlaufzeit_7 = dauer_verarbeitendesgebaeude_6 / dauer_verarbeitendesgebaeude_7
                                        menge_verarbeitendegebaeude_7 = durchlaufzeit_7 * menge_verarbeitendegebaeude_6
                                        if menge_verarbeitendegebaeude_7.is_integer ():
                                            durchlaufzeit_8 = dauer_verarbeitendesgebaeude_7 / dauer_verarbeitendesgebaeude_8
                                            menge_verarbeitendegebaeude_8 = durchlaufzeit_8 * menge_verarbeitendegebaeude_7
                                            if menge_verarbeitendegebaeude_8.is_integer ():
                                                durchlaufzeit_9 = dauer_verarbeitendesgebaeude_8 / dauer_verarbeitendesgebaeude_9
                                                menge_verarbeitendegebaeude_9 = durchlaufzeit_9 * menge_verarbeitendegebaeude_8
                                                if menge_verarbeitendegebaeude_9.is_integer ():
                                                    print(f"Menge Herstellendesgebäude ist: {int(menge_herstellendergebaeude)}")
                                                    print(f"Menge des ersten Verarbeitendegebäudes ist: {int (menge_verarbeitendegebaeude_1)}")
                                                    print(f"Menge des zweiten Verarbeitendegebäudes ist: {int (menge_verarbeitendegebaeude_2)}")
                                                    print(f"Menge des dritten Verarbeitendengebäudes ist: {int (menge_verarbeitendegebaeude_3)}")
                                                    print(f"Menge des vierten Verarbeitendengebäudes ist: {int (menge_verarbeitendegebaeude_4)}")
                                                    print(f"Menge des fünften Verarbeitendengebäudes ist: {int (menge_verarbeitendegebaeude_5)}")
                                                    print(f"Menge des sechsten Verarbeitendengebäudes ist: {int (menge_verarbeitendegebaeude_6)}")
                                                    print(f"Menge des siebten Verarbeitendengebäudes ist: {int (menge_verarbeitendegebaeude_7)}")
                                                    print(f"Menge des achten Verarbeitendengebäudes ist: {int (menge_verarbeitendegebaeude_8)}")
                                                    print(f"Menge des neunten Verarbeitendengebäudes ist: {int (menge_verarbeitendegebaeude_9)}")

                            break
                menge_herstellendergebaeude += 1
            erneut = input ("Möchtest du diese Rechnung für eine weiter Produktionskette durchführen? Y/N: ")
            if erneut != "Y":
                break

def zehn_Verarbeitendegebaeude ():
    while True:
            dauer_herstellendesgebaeude = int(input("Gib die Dauer des Herstellendengebäudes in Sekunden an: "))
            dauer_verarbeitendesgebaeude_1 = int(input("Gib die Dauer des ersten Verarbeitendengebäudes in Sekunden an: "))
            dauer_verarbeitendesgebaeude_2 = int(input("Gib die Dauer des zweiten Verarbeitendengebäudes in Sekunden an: "))
            dauer_verarbeitendesgebaeude_3 = int(input("Gib die Dauer des dritten Verarbeitendengebäudes in Sekunden an: "))
            dauer_verarbeitendesgebaeude_4 = int(input("Gib die Dauer des vierten Verarbeitendengebäudes in Sekunden an: "))
            dauer_verarbeitendesgebaeude_5 = int(input("Gib die Dauer des fünften Verarbeitendengebäudes in Sekunden an: "))
            dauer_verarbeitendesgebaeude_6 = int(input("Gib die Dauer des sechsten Verarbeitendengebäudes in Sekunden an: "))
            dauer_verarbeitendesgebaeude_7 = int(input("Gib die Dauer des siebten Verarbeitendengebäudes in Sekunden an: "))
            dauer_verarbeitendesgebaeude_8 = int(input("Gib die Dauer des achten Verarbeitendengebäudes in Sekunden an: "))
            dauer_verarbeitendesgebaeude_9 = int(input("Gib die Dauer des neunten Verarbeitendengebäudes in Sekunden an: "))
            dauer_verarbeitendesgebaeude_10 = int(input("Gib die Dauer des zehnten Verarbeitendengebäudes in Sekunden an: "))
            menge_verarbeitendegebaeude_1 = None
            menge_verarbeitendegebaeude_2 = None
            menge_verarbeitendegebaeude_3 = None
            menge_verarbeitendegebaeude_4 = None
            menge_verarbeitendegebaeude_5 = None
            menge_verarbeitendegebaeude_6 = None
            menge_verarbeitendegebaeude_7 = None
            menge_verarbeitendegebaeude_8 = None
            menge_verarbeitendegebaeude_9 = None
            menge_verarbeitendegebaeude_10 = None
            menge_herstellendergebaeude = int (input ("Gib die Anzahl des Herstellendengebäudes ein für die die Berechnung durchgeführt werden soll. "))

            while True:
                durchlaufzeit_1 = dauer_herstellendesgebaeude / dauer_verarbeitendesgebaeude_1
                menge_verarbeitendegebaeude_1 = durchlaufzeit_1 * menge_herstellendergebaeude
                if menge_verarbeitendegebaeude_1.is_integer():
                    durchlaufzeit_2 = dauer_verarbeitendesgebaeude_1 / dauer_verarbeitendesgebaeude_2
                    menge_verarbeitendegebaeude_2 = durchlaufzeit_2 * menge_verarbeitendegebaeude_1
                    if menge_verarbeitendegebaeude_2.is_integer():
                        durchlaufzeit_3 = dauer_verarbeitendesgebaeude_2 / dauer_verarbeitendesgebaeude_3
                        menge_verarbeitendegebaeude_3 = durchlaufzeit_3 * menge_verarbeitendegebaeude_2
                        if menge_verarbeitendegebaeude_3.is_integer ():
                            durchlaufzeit_4 = dauer_verarbeitendesgebaeude_3 / dauer_verarbeitendesgebaeude_4
                            menge_verarbeitendegebaeude_4 = durchlaufzeit_4 * menge_verarbeitendegebaeude_3
                            if menge_verarbeitendegebaeude_4.is_integer ():
                                durchlaufzeit_5 = dauer_verarbeitendesgebaeude_4 / dauer_verarbeitendesgebaeude_5
                                menge_verarbeitendegebaeude_5 = durchlaufzeit_5 * menge_verarbeitendegebaeude_4
                                if menge_verarbeitendegebaeude_5.is_integer ():
                                    durchlaufzeit_6 = dauer_verarbeitendesgebaeude_5 / dauer_verarbeitendesgebaeude_6
                                    menge_verarbeitendegebaeude_6 = durchlaufzeit_6 * menge_verarbeitendegebaeude_5
                                    if menge_verarbeitendegebaeude_6.is_integer ():
                                        durchlaufzeit_7 = dauer_verarbeitendesgebaeude_6 / dauer_verarbeitendesgebaeude_7
                                        menge_verarbeitendegebaeude_7 = durchlaufzeit_7 * menge_verarbeitendegebaeude_6
                                        if menge_verarbeitendegebaeude_7.is_integer ():
                                            durchlaufzeit_8 = dauer_verarbeitendesgebaeude_7 / dauer_verarbeitendesgebaeude_8
                                            menge_verarbeitendegebaeude_8 = durchlaufzeit_8 * menge_verarbeitendegebaeude_7
                                            if menge_verarbeitendegebaeude_8.is_integer ():
                                                durchlaufzeit_9 = dauer_verarbeitendesgebaeude_8 / dauer_verarbeitendesgebaeude_9
                                                menge_verarbeitendegebaeude_9 = durchlaufzeit_9 * menge_verarbeitendegebaeude_8
                                                if menge_verarbeitendegebaeude_9.is_integer ():
                                                    durchlaufzeit_10 = dauer_verarbeitendesgebaeude_9 / dauer_verarbeitendesgebaeude_10
                                                    menge_verarbeitendegebaeude_10 = durchlaufzeit_10 * menge_verarbeitendegebaeude_9
                                                    if menge_verarbeitendegebaeude_10.is_integer ():
                                                        print(f"Menge Herstellendesgebäude ist: {int(menge_herstellendergebaeude)}")
                                                        print(f"Menge des ersten Verarbeitendegebäudes ist: {int (menge_verarbeitendegebaeude_1)}")
                                                        print(f"Menge des zweiten Verarbeitendegebäudes ist: {int (menge_verarbeitendegebaeude_2)}")
                                                        print(f"Menge des dritten Verarbeitendengebäudes ist: {int (menge_verarbeitendegebaeude_3)}")
                                                        print(f"Menge des vierten Verarbeitendengebäudes ist: {int (menge_verarbeitendegebaeude_4)}")
                                                        print(f"Menge des fünften Verarbeitendengebäudes ist: {int (menge_verarbeitendegebaeude_5)}")
                                                        print(f"Menge des sechsten Verarbeitendengebäudes ist: {int (menge_verarbeitendegebaeude_6)}")
                                                        print(f"Menge des siebten Verarbeitendengebäudes ist: {int (menge_verarbeitendegebaeude_7)}")
                                                        print(f"Menge des achten Verarbeitendengebäudes ist: {int (menge_verarbeitendegebaeude_8)}")
                                                        print(f"Menge des neunten Verarbeitendengebäudes ist: {int (menge_verarbeitendegebaeude_9)}")
                                                        print(f"Menge des zehnten Verarbeitendengebäudes ist: {int (menge_verarbeitendegebaeude_10)}")

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
    elif Anzahl_Verarbeitendergebaeude == 3:
         drei_Verarbeitendegebaeude ()
    elif Anzahl_Verarbeitendergebaeude == 4:
        vier_Verarbeitendegebaeude ()
    elif Anzahl_Verarbeitendergebaeude == 5:
        fuenf_Verarbeitendegebaeude ()
    elif Anzahl_Verarbeitendergebaeude == 6:
        sechs_Verarbeitendegebaeude ()
    elif Anzahl_Verarbeitendergebaeude == 7:
        sieben_Verarbeitendegebaeude ()
    elif Anzahl_Verarbeitendergebaeude == 8:
        acht_Verarbeitendegebaeude ()
    elif Anzahl_Verarbeitendergebaeude == 9:
        neun_Verarbeitendegebaeude ()
    elif Anzahl_Verarbeitendergebaeude == 10:
        zehn_Verarbeitendegebaeude ()
    else:
        print ("Error bitte gib eine Zahl zwischen 1 u. 10 ein.")

    erneut = input ("Möchtest du die Rechnung für eine weiter Produktionskette durchführen? Y/N: ")
    if erneut != "Y":
        break
