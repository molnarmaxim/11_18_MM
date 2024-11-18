def feladat_1():
    megadott_mondat = str(input("Kérlek adj meg egy mondatot írásjellel a végén!\nA mondat: "))

    if megadott_mondat[-1] == '.':
        print("Ez a mondat kijelentő.")
    elif megadott_mondat[-1] == "!":
        print("Ez a mondat felkiáltó / felszólító / óhajtó.")
    elif megadott_mondat[-1] == "?":
        print("Ez a mondat kérdő.")
    else: print("A mondat amit megadtál nem értelmezhető, mivel nincs mondatvégi írásjele...")

feladat_1()