print("OSOBO ZADEJ ČÍSLO:")
cislo = int(input())
if cislo >= 0:
    for i in range(cislo, 1, -1):
        print('-' * i + '+' + '-' *(cislo -i -1))
else:
    print("Tento program pracuje pouze pro nezáporná čísla.")