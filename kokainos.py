
with open("snooker.txt") as f:    elso_sor = f.readline();    lista = [sor.strip().split(";") for sor in f];   print(f"3.feladat: A világranglistán {len(lista)} versenyző szerepel \n4.feladat: A versenyzők {sum([int(sor[3]) for sor in lista]) / len(lista):.2f} fontot kerestek \n5.feladat: A legjobban kereső kínai versenyző: \nHelyezés: {[sor for sor in [sor for sor in lista if sor[2] == 'Kína'] if int(sor[3]) == max([int(sor[3]) for sor in [sor for sor in lista if sor[2] == 'Kína']])][0][0]} \nNév: {[sor for sor in [sor for sor in lista if sor[2] == 'Kína'] if int(sor[3]) == max([int(sor[3]) for sor in [sor for sor in lista if sor[2] == 'Kína']])][0][1]} \nország:: {[sor for sor in [sor for sor in lista if sor[2] == 'Kína'] if int(sor[3]) == max([int(sor[3]) for sor in [sor for sor in lista if sor[2] == 'Kína']])][0][2]} \nNyeremény összege: {int([sor for sor in [sor for sor in lista if sor[2] == 'Kína'] if int(sor[3]) == max([int(sor[3]) for sor in [sor for sor in lista if sor[2] == 'Kína']])][0][3])*380} \n6.feladat: A versenyzők között {'van' if [True for sor in lista if sor[2] == 'Norvégia'] else 'nincs'} norvég versenyző");from collections import Counter;print("7.feladat: Statisztika  \n{}".format('\n'.join([f'{orszag} - {db} fő' for orszag, db in [Counter(sor[2] for sor in lista)][0].items() if db > 4])))