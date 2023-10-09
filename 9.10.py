def precti_jmena_a_pridej_do_souboru():
    # Otevření souboru names.txt pro čtení
    with open('names.txt', 'r') as soubor:
        jmena = soubor.readlines()  # Přečtení jmen ze souboru

    # Vypsání jmen
    print("Jména ve souboru:")
    for jmeno in jmena:
        print(jmeno.strip())


def pocet_slov_v_souboru():
    with open('names.txt', 'r') as soubor:
        obsah = soubor.read()
        slova = obsah.split()
        pocet_slov = len(slova)
        print(f"Počet slov v souboru: {pocet_slov}")

def vytvor_a_zapis_slovnik():
    slovnik = {
        "Jméno": "Jaroslav",
        "Příjmení": "Melichar",
        "Věk": "12"
    }

    with open('slovnik.txt', 'w') as soubor:
        for klic, hodnota in slovnik.items():
            soubor.write(f"{klic}: {hodnota}\n")




precti_jmena_a_pridej_do_souboru()
pocet_slov_v_souboru()
vytvor_a_zapis_slovnik()
