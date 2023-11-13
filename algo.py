auta = {
    'BMW X5': 2022,
    'Toyota Camry': 2021,
    'Ford Mustang': 2020,
    'Honda Civic': 2019,
    'Chevrolet Tahoe': 2018
}

for auto, rok in auta.items():
    print(f'Model: {auto}, Rok výroby: {rok}')

delka_slovniku = len(auta)
print(f'Délka slovníku: {delka_slovniku}')

auta['BMW X5'] = 2023
auta['Toyota Camry'] = 2022

# Vypsání aktualizovaných informací
for auto, rok in auta.items():
    print(f'Model: {auto}, Nový rok výroby: {rok}')
