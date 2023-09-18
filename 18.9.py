muj_list = [1, 2, 3, 4, 4, 4]
soucet = sum(muj_list)

print("Součet čísel:", soucet)


nejmensi = min(muj_list)
nejvetsi = max(muj_list)

print ("Nejmenší číslo:", nejmensi)
print ("Největší číslo:", nejvetsi)

unikatni_list = list(set(muj_list))

print("Tohle je list bez duplikátů:", unikatni_list)

if len(muj_list) > 0:
    print("Seznam není prázdný!")
else:
    print("Seznam je prázdný!")