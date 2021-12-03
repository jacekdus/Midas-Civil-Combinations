### INFORMACJE WSTEPNE
#
# Co ten skrypt robi:
# Zadanie skryptu jest pomoc przy tworzeniu kombinacji w programie Midas Civil. Skrypt pobiera dane wejsciowe w postaci
# zadeklarowanych przypadkow obciazenia, prekombinacji i kombinacji stworzonych w kodzie Python, ktore z koleji
# odpowiadaja zasadom tworzenia kombinacji i prekombinacji recznie w programie Midas Civil. Utworzone kombinacje
# i prekombinacje zamienia na proste przypadki, ktore nie maja juz w sobie zadnych prekombinacji i wyrzuca tak
# przygotowana komende do wklejenia bezposrednio w programie Midas Civil (Zakladka -> Tools, opcja -> MCT Command Shell)
#
# Polecane edytory kodu:
#   - PyCharm - darmowe najlepsze narzedzie do edycji kodu w jezyku Python. Analizuje caly projekt i co w nim jest,
#               podkresla bledy nie tylko syntaktyczne, ale potrafi tez duzo podpowiadac podczas pisania
#   - Notepad++ - prosty edytor/viewer kodu, ktore przede wszystkim koloruje skladnie zeby byla bardziej czytelna
#                 i sprawdza bledy syntaktyczne najlepsze do szybkiego podgladania kodu (do pisania ujdzie).

#### INSTRUKCJA

# 0. Tu sa linijki kodu, ktore importuja podstawowe klasy, z ktorych korzysta aplikacja. Tutaj nie nalezy nic zmieniac.

from App.Application import LoadCombination
from App.CombinationTree.LoadCase import LoadCase

# 1. Przypadki i prekombinacje
#   Tutaj wypisz wszystkie przypadki obciążenia (LoadCase) i kombinacje (LoadCombination) bez ostatecznej
#   (ta zostanie zadeklarowana w pkt 2)

#   Zasada tworzenia kombinacji i prekombinacji zostala zaadoptowana bezposrednio z programu Midas Civil.

#   Deklaracji przypadku obciazenia (LoadCase)
#       Schemat:
#           nazwa_przypadku = LoadCase('NAZWA_PRZYPADKU', 'TYP')
#       Przyklady:
#           g1 = LoadCase('G1')

#           lm1 = LoadCase('LM1', 'MV') - jezeli przypadek nie jest typu 'ST', wowczas nalezy podac tez typ

#   Deklaracja kombinacji (LoadCombination)
#       Schemat:
#           nazwa_kombinacji = LoadCombination('NAZWA_KOMBINACJI', [
#               [przypadek/kombinacja_1, wspolczynnik_1],
#               [przypadek/kombinacja_2, wspolczynnik_2]
#           ], envelope=True/False)

#       Przyklady:
#           - Kombinacja typu Add. Wszystkie przypadki sa ze soba zsumowane
#           sls_comb = LoadCombination('SLS_COMB', [
#               [g1_comb, 1.00],
#               [g2_comb, 1.00],
#               [lm1_comb, 1.00]
#           ])

#           - Kombinacja typu Envelope. Wybierany jest jeden przypadek z wybranych. Nalezy dopisac: envelope=True
#           lm1_comb = LoadCombination('LM1_COMB', [
#               [lm1_1, 1.35],
#               [lm1_2, 1.35]
#           ], envelope=True)

temp_plus = LoadCase('temp+', 'ST')
temp_minus = LoadCase('temp-', 'ST')
gradient_temp_plus = LoadCase('gradient temp+', 'ST')
gradient_temp_minus = LoadCase('gradient temp-', 'ST')

temp_1 = LoadCombination('temp_1', [
    [temp_plus, 0.35],
    [gradient_temp_plus, 1.00]])

temp_2 = LoadCombination('temp_2', [
    [temp_plus, 0.35],
    [gradient_temp_minus, 1.00]])

temp_3 = LoadCombination('temp_3', [
    [temp_minus, 0.35],
    [gradient_temp_plus, 1.00]])

temp_4 = LoadCombination('temp_4', [
    [temp_minus, 0.35],
    [gradient_temp_minus, 1.00]])

temp_komb = LoadCombination('temp_komb', [
  [temp_1, 1.0],
  [temp_2, 1.0],
  [temp_3, 1.0],
  [temp_4, 1.0],
], envelop=True)

hamowanie_1 = LoadCase('hamowanie_1', 'ST')
hamowanie_2 = LoadCase('hamowanie_2', 'ST')
hamowanie_3 = LoadCase('hamowanie_3', 'ST')
hamowanie_4 = LoadCase('hamowanie_4', 'ST')
hamowanie_5 = LoadCase('hamowanie_5', 'ST')
hamowanie_6 = LoadCase('hamowanie_6', 'ST')
hamowanie_minus_1 = LoadCase('hamowanie_-1', 'ST')
hamowanie_minus_2 = LoadCase('hamowanie_-2', 'ST')
hamowanie_minus_3 = LoadCase('hamowanie_-3', 'ST')
hamowanie_minus_4 = LoadCase('hamowanie_-4', 'ST')
hamowanie_minus_5 = LoadCase('hamowanie_-5', 'ST')
hamowanie_minus_6 = LoadCase('hamowanie_-6', 'ST')

hamowanie_komb = LoadCombination('hamowanie_komb', [
  [hamowanie_1, 1.0],
  [hamowanie_2, 1.0],
  [hamowanie_3, 1.0],
  [hamowanie_4, 1.0],
  [hamowanie_5, 1.0],
  [hamowanie_6, 1.0],
  [hamowanie_minus_1, 1.0],
  [hamowanie_minus_2, 1.0],
  [hamowanie_minus_3, 1.0],
  [hamowanie_minus_4, 1.0],
  [hamowanie_minus_5, 1.0],
  [hamowanie_minus_6, 1.0]
], envelop=True)


dg_izolacja = LoadCase('dg_izolacja', 'CS')
dg_nawierzchnia = LoadCase('dg_nawierzchnia', 'CS')

dg_izolacja08 = LoadCombination('dg_izolacja08', [
    [dg_izolacja, 0.8]
])
dg_izolacja0140 = LoadCombination('dg_izolacja0140', [
    [dg_izolacja, 1.4]
])

dg_nawierzchnia08 = LoadCombination('dg_nawierzchnia08', [
    [dg_nawierzchnia, 0.8]
])
dg_nawierzchnia0140 = LoadCombination('dg_nawierzchnia0140', [
    [dg_nawierzchnia, 1.4]
])
# dg_izolacja0140 = LoadCase('dg_izolacja', 'CS')
# dg_nawierzchnia08 = LoadCase('dg_nawierzchnia', 'CS')
# dg_nawierzchnia0140 = LoadCase('dg_nawierzchnia', 'CS')
dg = LoadCase('dg', 'CS')



dg_izo_komb = LoadCombination('dg_izo_komb', [
  [dg_izolacja08, 1.0],
  [dg_izolacja0140, 1.0],
], envelop=True)

dg_naw_komb = LoadCombination('dg_naw_komb', [
  [dg_nawierzchnia08, 1.0],
  [dg_nawierzchnia0140, 1.0],
], envelop=True)

dg_naw_izol = LoadCombination('dg_naw_izol', [
    [dg_izo_komb, 1.0],
    [dg_naw_komb, 1.0],
], envelop=False)

dg_ = LoadCombination('dg_', [
    [dg, 1.0],
    [dg_naw_izol, 1.0],
], envelop=False)

gr1a = LoadCase('LM1+piesi', 'MV')
gr1a_psi = LoadCase('LM1+piesi#psi', 'MV')
LM1 = LoadCase('LM1', 'MV')
LM1_psi = LoadCase('LM1#psi', 'MV')
gr1b = LoadCase('LM2', 'MV')
gr1b_psi = LoadCase('LM2#psi', 'MV')
Piesi = LoadCase('Piesi', 'MV')
Piesi_psi = LoadCase('Piesi#psi', 'MV')

gr2 = LoadCombination('gr1a', [
    [hamowanie_komb, 1.0],
    [LM1_psi, 1.0],
], envelop=False)

cw = LoadCase('cw', 'CS')
Tendon_Primary = LoadCase('Tendon Primary', 'CS')
Tendon_Secondary = LoadCase('Tendon Secondary', 'CS')
Creep_Secondary = LoadCase('Creep Secondary', 'CS')
Shrinkage_Secondary = LoadCase('Shrinkage Secondary', 'CS')
set_komb = LoadCase('A+B+C', 'SM')

G_ch_1 = LoadCombination('G_ch_1', [
    [cw, 1.0],
    [Tendon_Primary, 1.0],
    [Tendon_Secondary, 1.0],
    [Creep_Secondary, 1.],
    [Shrinkage_Secondary, 1.0],
    [dg_, 1.0]
], envelop=False)

G_ch_2 = LoadCombination('G_ch_2', [
    [G_ch_1, 1.0],
    [set_komb, 1.0],
], envelop=False)

G_ch_komb = LoadCombination('G_ch_komb', [
    [G_ch_1, 1.0],
    [G_ch_2, 1.0],
], envelop=True)

Q_ch_1a = LoadCombination('Q_ch_1a', [
    [gr1a, 1.0],
    [temp_komb, 0.6]
], envelop=False)

Q_ch_temp = LoadCombination('Q_ch_temp', [
    [temp_komb, 1.0],
    [gr1a_psi, 1.0]
    ], envelop=False)

Q_ch_komb = LoadCombination('Q_ch_komb', [
    [Q_ch_1a, 1.0],
    [Q_ch_temp, 1.0]
    ], envelop=True)

CHARAKT_KOMB = LoadCombination('CHARAKT_KOMB', [
    [G_ch_komb, 1.0],
    [Q_ch_komb, 1.0],
], envelop=False)

Q_cz_1 = LoadCombination ('Q_cz_1', [
    [temp_komb, 0.5],
    [LM1_psi, 1.0]
], envelop=False)

Q_cz_2 = LoadCombination('Q_cz_2', [
    [temp_komb, 0.5],
    [gr1b_psi, 1.0]
], envelop=False)

Q_cz_3 = LoadCombination('Q_cz_3', [
    [temp_komb, 0.5],
    [Piesi_psi, 1.0]
], envelop=False)

Q_cz_komb = LoadCombination('Q_cz_komb', [
    [Q_cz_1, 1.0],
    [Q_cz_2, 1.0],
    [Q_cz_3, 1.0],
    [temp_komb, 0.6]
    ], envelop=True)

CZESTA_komb = LoadCombination('CZESTA_komb', [
    [G_ch_komb, 1.0],
    [Q_cz_komb, 1.0],
], envelop=False)

QUASI_S_komb = LoadCombination('QUASI_S_komb', [
    [G_ch_komb, 1.0],
    [temp_komb, 0.5],
], envelop=False)

G_obl_1 = LoadCombination('G_obl_1', [
    [set_komb, 1.2]
], envelop=False)

G_obl_2 = LoadCombination('G_obl_2', [
    [cw, 1.35],
    [Tendon_Primary, 1.0],
    [Tendon_Secondary, 1.0],
    [Creep_Secondary, 1.35],
    [Shrinkage_Secondary, 1.35],
    [dg_, 1.35]
], envelop=False)

G_obl_3 = LoadCombination('G_obl_3', [
    [cw, 1.0],
    [Tendon_Primary, 1.0],
    [Tendon_Secondary, 1.0],
    [Creep_Secondary, 1.0],
    [Shrinkage_Secondary, 1.0],
    [dg_, 1.0]
], envelop=False)

G_obl_1_2 = LoadCombination('G_obl_1_2', [
    [G_obl_1, 1.0],
    [G_obl_2, 1.0]
], envelop=False)

G_obl_1_3 = LoadCombination('G_obl_1_3', [
    [G_obl_1, 1.0],
    [G_obl_3, 1.0]
], envelop=False)

G_obl_komb = LoadCombination('G_obl_komb ', [
    [G_obl_2, 1.0],
    [G_obl_3, 1.0],
    [G_obl_1_2, 1.0],
    [G_obl_1_3, 1.0]
], envelop=True)
