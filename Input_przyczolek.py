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
#               podkresla bledy nie tylko syntaktyczne, ale patrzy tez na strukture calego projektu
#   - Notepad++ - prosty edytor/viewer kodu, ktore przede wszystkim koloruje skladnie zeby byla bardziej czytelna
#                 najlepsze do szybkiego podgladania kodu (do pisania malo uzyteczna).

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
#           - Kombinacja typu Add. Wszystkie przypadki sa ze soba sumowane
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

zerowanie = LoadCase('ZEROWANIE')
g1 = LoadCase('G1')
g2 = LoadCase('G2')
e = LoadCase('E_G2')

e_ts_korp_l = LoadCase('E_TS_KORP_L')
e_udl_korp_l = LoadCase('E_UDL_KORP_L')
e_ts_korp_p = LoadCase('E_TS_KORP_P')
e_udl_korp_p = LoadCase('E_UDL_KORP_P')

r1 = LoadCase('REAKCJA OBL 1')
r2 = LoadCase('REAKCJA OBL 2')
r3 = LoadCase('REAKCJA OBL 3')
r4 = LoadCase('REAKCJA OBL 4')

naziom_ts_k_l1 = LoadCase('NAZIOM TS K_L1')
naziom_ts_k_l2 = LoadCase('NAZIOM TS K_L2')
naziom_ts_k_p1 = LoadCase('NAZIOM TS K_P1')
naziom_ts_k_p2 = LoadCase('NAZIOM TS K_P2')

naziom_udl_l = LoadCase('NAZIOM UDL_L')
naziom_udl_p = LoadCase('NAZIOM UDL_P')


g1_max = LoadCombination('G1_max', [[g1, 1.35]])
g1_min = LoadCombination('G1_min', [[g1, 1.00]])
g1_comb = LoadCombination('G1_COMB', [[g1_max, 1.00], [g1_min, 1.00]], envelop=True)

g2_max = LoadCombination('G2_max', [[g2, 1.35]])
g2_min = LoadCombination('G2_min', [[g2, 1.00]])
g2_comb = LoadCombination('G2_COMB', [[g2_max, 1.00], [g2_min, 1.00]], envelop=True)

e_max = LoadCombination('E_max', [[e, 1.35]])
e_min = LoadCombination('E_min', [[e, 1.00]])
e_comb = LoadCombination('E_COMB', [[e_max, 1.00], [e_min, 1.00]], envelop=True)

r_comb = LoadCombination('R_OBL_COMB', [[r1, 1.00], [r2, 1.00], [r3, 1.00], [r4, 1.00]], envelop=True)

ts_k_l1 = LoadCombination('TS_K_L1', [[naziom_ts_k_l1, 1.00], [e_ts_korp_l, 1.00]])
ts_k_l2 = LoadCombination('TS_K_L1', [[naziom_ts_k_l1, 1.00], [e_ts_korp_l, 1.00]])
ts_k_p1 = LoadCombination('TS_K_P1', [[naziom_ts_k_p1, 1.00], [e_ts_korp_p, 1.00]])
ts_k_p2 = LoadCombination('TS_K_P2', [[naziom_ts_k_p2, 1.00], [e_ts_korp_p, 1.00]])
ts_k = LoadCombination('TS_K_COMB', [[ts_k_l1, 1.00], [ts_k_l2, 1.00], [ts_k_p1, 1.00], [ts_k_p2, 1.00]], envelop=True)

udl_k_l = LoadCombination('UDL_K_L', [[naziom_udl_l, 1.00], [e_udl_korp_l, 1.00]])
udl_k_p = LoadCombination('UDL_K_P', [[naziom_udl_p, 1.00], [e_udl_korp_p, 1.00]])
udl_k = LoadCombination('UDL_K_COMB', [[udl_k_l, 1.00], [udl_k_p, 1.00], [zerowanie, 1.00]], envelop=True)

ts_udl_k = LoadCombination('TS+UDL_K_COMB', [[ts_k, 1.00], [udl_k, 1.00]])

ts_udl = LoadCombination('TS+UDL_COMB', [[ts_udl_k, 1.00]])

# 2. Kombinacja ostateczna
#   Kombinacja podstawowa main_comb (nie zmieniac nazwy zmiennej)

main_comb = LoadCombination('ULS', [[g1_comb, 1.00], [g2_comb, 1.00], [e_comb, 1.00], [r_comb, 1.00], [ts_udl, 1.00]])
