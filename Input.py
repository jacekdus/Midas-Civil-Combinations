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

g1 = LoadCase('G1', 'CS')
g1_max = LoadCombination('G1_MAX', [[g1, 1.00]])
g1_min = LoadCombination('G1_MIN', [[g1, 1.00]])

g2_kapy = LoadCase('G2_KAPY', 'CS')
g2_kapy_max = LoadCombination('G2_KAPY_MAX', [[g2_kapy, 1.00]])
g2_kapy_min = LoadCombination('G2_KAPY_MIN', [[g2_kapy, 1.00]])

g2_nawierz = LoadCase('G2_NAWIERZ', 'CS')
g2_nawierz_max = LoadCombination('G2_NAWIERZ_MAX', [[g2_nawierz, 1.40]])
g2_nawierz_min = LoadCombination('G2_NAWIERZ_MIN', [[g2_nawierz, 0.80]])

g2_izol = LoadCase('G2_IZOL', 'CS')
g2_izol_max = LoadCombination('G2_NAWIERZ_MAX', [[g2_izol, 1.40]])
g2_izol_min = LoadCombination('G2_NAWIERZ_MIN', [[g2_izol, 0.80]])

g2_kapy_ch_comb = LoadCombination('G2_KAPY_CH_COMB', [[g2_kapy_max, 1.00], [g2_kapy_min, 1.00]], envelop=True)
g2_nawierz_ch_comb = LoadCombination('G2_NAWIERZ_CH_COMB', [g2_nawierz_max, 1.00], [g2_nawierz_min, 1.00], envelop=True)
g2_izol_ch_comb = LoadCombination('G2_IZOL_CH_COMB', [[g2_izol_max, 1.00], [g2_izol_min, 1.00]], envelop=True)

g2_kapy_str_comb = LoadCombination('G2_KAPY_STR_COMB', [[g2_kapy_max, 1.35], [g2_kapy_min, 1.00]], envelop=True)
g2_nawierz_str_comb = LoadCombination('G2_NAWIERZ_STR_COMB', [[g2_nawierz_max, 1.35, g2_nawierz_min, 1.00]], envelop=True)
g2_izol_str_comb = LoadCombination('G2_IZOL_STR_COMB', [[g2_izol_max, 1.35], [g2_izol_min, 1.00]], envelop=True)

tendon_secondary = LoadCase('Tendon Secondary', 'CS')
ps_str_max = LoadCombination('PS_STR_MAX', [[tendon_secondary, 1.00]])
ps_str_min = LoadCombination('PS_STR_MIN', [[tendon_secondary, 1.00]])

tendon_primary = LoadCase('Tendon Primary', 'CS')
ps_sls_max = LoadCombination('PS_SLS_MAX', [[tendon_primary, 1.00], [tendon_secondary, 1.00]])
ps_sls_min = LoadCombination('PS_SLS_MIN', [[tendon_primary, 1.00], [tendon_secondary, 1.00]])

creep_secondary = LoadCase('Creep Secondary', 'CS')
crp_max = LoadCombination('CRP_MAX', [[creep_secondary, 1.00]])
crp_min = LoadCombination('CRP_MIN', [[creep_secondary, 1.00]])
shrinkage_secondary = LoadCase('Shrinkage Secondary', 'CS')
shr_max = LoadCombination('SHR_MAX', [[shrinkage_secondary, 1.00]])
shr_min = LoadCombination('SHR_MIN', [[shrinkage_secondary, 1.00]])

zerowanie = LoadCase('ZEROWANIE')
lm1_l_psi = LoadCase('LM1_L#PSI', 'MV')
lm1_p_psi = LoadCase('LM1_P#PSI', 'MV')
q_gr2_lm1_comb = LoadCombination('Q_gr2_LM1_COMB', [[zerowanie, 1.00], [lm1_l_psi, 1.00], [lm1_p_psi, 1.00]], envelop=True)

ham_1p = LoadCase('HAMOWANIE_1+')
ham_1m = LoadCase('HAMOWANIE_1-')
ham_2p = LoadCase('HAMOWANIE_2+')
ham_2m = LoadCase('HAMOWANIE_2-')
ham_3p = LoadCase('HAMOWANIE_3+')
ham_3m = LoadCase('HAMOWANIE_3-')
ham_4p = LoadCase('HAMOWANIE_4+')
ham_4m = LoadCase('HAMOWANIE_4-')
ham_5p = LoadCase('HAMOWANIE_5+')
ham_5m = LoadCase('HAMOWANIE_5-')
ham_6p = LoadCase('HAMOWANIE_6+')
ham_6m = LoadCase('HAMOWANIE_6-')
q_gr2_brk_comb = LoadCombination('Q_gr2_BRK_COMB', [
    [ham_1p, 1.00], [ham_1m, 1.00],
    [ham_2p, 1.00], [ham_2m, 1.00],
    [ham_3p, 1.00], [ham_3m, 1.00],
    [ham_4p, 1.00], [ham_4m, 1.00],
    [ham_5p, 1.00], [ham_5m, 1.00],
    [ham_6p, 1.00], [ham_6m, 1.00],
    [zerowanie, 1.00]
], envelop=True)

ods_1 = LoadCase('ODŚRODKOWA_1')
ods_2 = LoadCase('ODŚRODKOWA_2')
ods_3 = LoadCase('ODŚRODKOWA_3')
ods_4 = LoadCase('ODŚRODKOWA_4')
ods_5 = LoadCase('ODŚRODKOWA_5')
ods_6 = LoadCase('ODŚRODKOWA_6')
q_gr2_cf_comb = LoadCombination('Q_gr2_CF_COMB', [
    [ods_1, 1.00], [ods_2, 1.00], [ods_3, 1.00], [ods_4, 1.00], [ods_5, 1.00], [ods_6, 1.00],
    [zerowanie, 1.00]
], envelop=True)

lm1_l = LoadCase('LM1_L', 'MV')
lm1_p = LoadCase('LM1_P', 'MV')
q_gr1a_comb = LoadCombination('Q_gr1a_COMB', [[zerowanie, 1.00], [lm1_l, 1.00], [lm1_p, 1.00]], envelop=True)
q_gr1a_psi_comb = LoadCombination('Q_gr1a_psi_COMB', [[zerowanie, 1.00], [lm1_l_psi, 1.00], [lm1_p, 1.00]], envelop=True)

q_gr2_comb = LoadCombination('Q_gr2_COMB', [[q_gr2_brk_comb, 1.00], [q_gr2_cf_comb, 1.00], [q_gr2_lm1_comb, 1.00]])

mlc_x1 = LoadCase('MLC_x1', 'MV')
mlc_x2 = LoadCase('MLC_x2', 'MV')
q_gr5_comb = LoadCombination('Q_gr5_COMB', [[zerowanie, 1.00], [mlc_x1, 1.00], [mlc_x2, 1.00]], envelop=True)

q2k = LoadCase('Q2k', 'MV')
q2k_comb = LoadCombination('Q2k_comb', [[zerowanie, 1.00], [q2k, 1.00]], envelop=True)

uderz_1_1p = LoadCase('UDERZENIE_1_1+')
uderz_1_1m = LoadCase('UDERZENIE_1_1-')
uderz_1_2p = LoadCase('UDERZENIE_1_2+')
uderz_1_2m = LoadCase('UDERZENIE_1_2-')
uderz_1_3p = LoadCase('UDERZENIE_1_3+')
uderz_1_3m = LoadCase('UDERZENIE_1_3-')
uderz_2_1p = LoadCase('UDERZENIE_2_1+')
uderz_2_1m = LoadCase('UDERZENIE_2_1-')
uderz_2_2p = LoadCase('UDERZENIE_2_2+')
uderz_2_2m = LoadCase('UDERZENIE_2_2-')
uderz_2_3p = LoadCase('UDERZENIE_2_3+')
uderz_2_3m = LoadCase('UDERZENIE_2_3-')
imp_comb = LoadCombination('IMP_COMB', [
    [uderz_1_1p, 1.00], [uderz_2_1p, 1.00],
    [uderz_1_1m, 1.00], [uderz_2_1m, 1.00],
    [uderz_1_2p, 1.00], [uderz_2_2p, 1.00],
    [uderz_1_2m, 1.00], [uderz_2_2m, 1.00],
    [uderz_1_3p, 1.00], [uderz_2_3p, 1.00],
    [uderz_1_3m, 1.00], [uderz_2_3m, 1.00]
], envelop=True)

g1_ch_comb = LoadCombination('G1_CH_COMB', [[g1_max, 1.00], [g1_min, 1.00]], envelop=True)
g2_ch_comb = LoadCombination('G2_CH_COMB', [[g2_kapy_ch_comb, 1.00], [g2_nawierz_ch_comb, 1.00], [g2_izol_ch_comb, 1.00]])

ps_ch_comb = LoadCombination('PS_SLS_MAX', [[ps_sls_max, 1.00], [ps_sls_min, 1.00]], envelop=True)

crp_ch_comb = LoadCombination('CRP_CH_COMB', [[crp_max, 1.00], [crp_min, 1.00]], envelop=True)
shr_ch_comb = LoadCombination('SHR_CH_COMB', [[shr_max, 1.00], [shr_min, 1.00]], envelop=True)

q_ch_comb = LoadCombination('Q_CH_COMB', [[q_gr1a_comb, 1.00], [q_gr2_comb, 1.00], [q_gr5_comb, 1.00]], envelop=True)
q_qp_comb = LoadCombination('Q_QP_COMB', [[q_gr1a_psi_comb, 1.00]], envelop=True)

q_acc_1_comb = LoadCombination('Q_ACC_1_COMB', [[q_gr1a_psi_comb, 1.00], [imp_comb, 1.00]])
q_acc_2_comb = LoadCombination('Q_ACC_2_COMB', [[q2k_comb, 1.00]])
q_acc_comb = LoadCombination('Q_ACC_COMB', [[q_acc_1_comb, 1.00], [q_acc_2_comb, 1.00], [zerowanie, 1.00]], envelop=True)

g1_str_comb = LoadCombination('G1_STR_COMB', [[g1_max, 1.35], [g1_min, 1.00]], envelop=True)
g2_str_comb = LoadCombination('G2_CH_COMB', [[g2_kapy_str_comb, 1.00], [g2_nawierz_str_comb, 1.00], [g2_izol_str_comb, 1.00]])

ps_str_comb = LoadCombination('PS_SLS_MAX', [[ps_str_max, 1.00], [ps_str_min, 1.00]], envelop=True)

crp_str_comb = LoadCombination('CRP_CH_COMB', [[crp_max, 1.35], [crp_min, 1.00]], envelop=True)
shr_str_comb = LoadCombination('SHR_CH_COMB', [[shr_max, 1.35], [shr_min, 1.00]], envelop=True)

q_str_comb = LoadCombination('Q_CH_COMB', [[q_gr1a_comb, 1.35], [q_gr2_comb, 1.35], [q_gr5_comb, 1.35]], envelop=True)

ch_comb = LoadCombination('CH_COMB', [
    [g1_ch_comb, 1.00], [g2_ch_comb, 1.00], [ps_ch_comb, 1.00],
    [crp_ch_comb, 1.00], [shr_ch_comb, 1.00], [q_ch_comb, 1.00]
])

fr_comb = LoadCombination('FR_COMB', [
    [g1_ch_comb, 1.00], [g2_ch_comb, 1.00], [ps_ch_comb, 1.00],
    [crp_ch_comb, 1.00], [shr_ch_comb, 1.00]
])

qp_comb = LoadCombination('QP_COMB', [
    [g1_ch_comb, 1.00], [g2_ch_comb, 1.00], [ps_ch_comb, 1.00],
    [crp_ch_comb, 1.00], [shr_ch_comb, 1.00], [q_qp_comb, 1.00]
])

str_comb = LoadCombination('STR_COMB', [
    [g1_str_comb, 1.00], [g2_str_comb, 1.00], [ps_str_comb, 1.00],
    [crp_str_comb, 1.00], [shr_str_comb, 1.00], [q_str_comb, 1.00]
])

accidental = LoadCase('ACCIDENTAL')
acc_comb = LoadCombination('ACC_COMB', [
    [g1_ch_comb, 1.00], [g2_ch_comb, 1.00], [ps_ch_comb, 1.00],
    [crp_ch_comb, 1.00], [shr_ch_comb, 1.00], [q_acc_comb, 1.00], [accidental, 1.00]
])

fxy_ch_comb = LoadCombination('FXY_CH_COMB', [[q_gr2_comb, 1.00], [q_acc_1_comb, 1.00]], envelop=True)
fxy_str_comb = LoadCombination('FXY_STR_COMB', [[q_gr2_comb, 1.35], [q_acc_1_comb, 1.00]], envelop=True)

ps_1 = LoadCombination('PS-1', [tendon_primary, 1.00])
ps_2 = LoadCombination('PS-2', [tendon_secondary, 1.00])

# 2. Kombinacja ostateczna
#   Kombinacja podstawowa main_comb (nie zmieniac nazwy zmiennej)

main_comb = str_comb
