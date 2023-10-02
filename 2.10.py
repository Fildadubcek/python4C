zamestnanci = {
    "zamestnanec1": {
        "jméno": "Jan",
        "příjmení": "Novák",
        "pozice": "Manažer",
        "email": "jan.novak@email.com",
        "kancelář": "A101"
    },
    "zamestnanec2": {
        "jméno": "Eva",
        "příjmení": "Svobodová",
        "pozice": "Asistentka",
        "email": "eva.svobodova@email.com",
        "kancelář": "B202"
    },
    "zamestnanec3": {
        "jméno": "Petr",
        "příjmení": "Kovář",
        "pozice": "Programátor",
        "email": "petr.kovar@email.com",
        "kancelář": "A101"
    },
    "zamestnanec4": {
        "jméno": "Lucie",
        "příjmení": "Novotná",
        "pozice": "Designér",
        "email": "lucie.novotna@email.com",
        "kancelář": "C303"
    }
}
print("Úkol 2")
for zamestnanec, informace in zamestnanci.items():
    print(f"Zaměstnanec {zamestnanec}:")
    for atribut, hodnota in informace.items():
        print(f"{atribut}: {hodnota}")
    print()


print("Úkol 3a")
for zamestnanec, informace in zamestnanci.items():
    print(f"{informace['jméno']} {informace['příjmení']}, Email: {informace['email']}")

print("Úkol 3b")
zamestnanec_konkretni = "zamestnanec1"  # Můžete si vybrat jiného zaměstnance podle potřeby
informace_konkretni = zamestnanci.get(zamestnanec_konkretni)
if informace_konkretni:
    print(f"{informace_konkretni['jméno']} {informace_konkretni['příjmení']}, Pozice: {informace_konkretni['pozice']}")
else:
    print("Zaměstnanec neexistuje.")

print("Úkol 4")
kancelar = "A101"
for zamestnanec, informace in zamestnanci.items():
    if(informace["kancelář"] == kancelar):
        print(f"{informace['jméno']} {informace['příjmení']}, Pozice: {informace['pozice']}")
