# INFORMACJE WSTEPNE

# Polecane edytory kodu:
#   - PyCharm - darmowe najlepsze narzedzie do edycji kodu w jezyku Python. Analizuje caly projekt i co w nim jest,
#               podkresla bledy nie tylko syntaktyczne, ale potrafi tez duzo podpowiadac podczas pisania
#   - Notepad++ - prosty edytor/viewer kodu, ktore przede wszystkim koloruje skladnie zeby byla bardziej czytelna
#                 i sprawdza bledy syntaktyczne najlepsze do szybkiego podgladania kodu (do pisania ujdzie).

# INSTRUKCJA

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


# TUTAJ ZACZNIJ PISAC TWOJE PRZYPADKI KOMBINACJE

g = LoadCase('g')
temp_normal_plus = LoadCase('temp_normal_plus')
temp_gradient_plus = LoadCase('temp_gradient_plus')

temp_1 = LoadCombination('temp_1', [
    [temp_normal_plus, 0.35],
    [temp_gradient_plus, 1.00]
])

temp_2 = LoadCombination('temp_2', [
    [temp_normal_plus, 1.00],
    [temp_gradient_plus, 0.35]
])

temp = LoadCombination('temp', [
    [temp_1, 1.00],
    [temp_2, 1.00]
], envelop=True)

# 2. Kombinacja ostateczna
#   Kombinacja podstawowa main_comb (nie zmieniac nazwy zmiennej)

main_comb = LoadCombination('main', [
    [g, 1.00],
    [temp, 0.60]
])
