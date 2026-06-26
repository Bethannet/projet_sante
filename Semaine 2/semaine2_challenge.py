# ============================================================
# Rapport comparatif — 3 hôpitaux du Pool
# ============================================================

#CMS Vindza
budget_vindza = 6_800_000
consult_vindza = 923
hosp_vindza = 87
deces_vindza = 2
lits_vindza = 20
lits_occ_vindza = 14
medecins_vindza = 1
population_vindza = 42_000

#Hôpital District de Kinkala
budget_kinkala = 12_500_000
consult_kinkala = 1847
hosp_kinkala = 312
deces_kinkala = 8
lits_kinkala = 45
lits_occ_kinkala = 41
medecins_kinkala = 3
population_kinkala = 85_000

#Hôpital de Kindamba
budget_kindamba = 9_200_000
consult_kindamba = 1234
hosp_kindamba = 201
deces_kindamba = 11
lits_kindamba = 35
lits_occ_kindamba = 33
medecins_kindamba = 2
population_kindamba = 67_000


# Fonction KPI à utiliser pour les 3 hôpitaux
def calculer_kpi(budget, consultations, hospitalisations, deces,
                  lits, lits_occupes, medecins, population):
    # cout moyen par patient, taux d'occupation, densité médicale, taux de mortalité
    cout_patient = round(budget / (consultations + hospitalisations), 2)
    taux_occupation = round((lits_occupes / lits) * 100, 2)
    densite = round((medecins / population) * 1000, 2)
    taux_mortalite = round((deces / hospitalisations) * 100, 2)
    return cout_patient, taux_occupation, densite, taux_mortalite


# Calculs des indicateurs pour chaque hôpital
vindza = calculer_kpi(
    budget_vindza, consult_vindza, hosp_vindza,
    deces_vindza, lits_vindza, lits_occ_vindza,
    medecins_vindza, population_vindza
)  # pour le CMS Vindza

kindamba = calculer_kpi(
    budget_kindamba, consult_kindamba, hosp_kindamba,
    deces_kindamba, lits_kindamba, lits_occ_kindamba,
    medecins_kindamba, population_kindamba
)  # pour l'hôpital de Kindamba

kinkala = calculer_kpi(
    budget_kinkala, consult_kinkala, hosp_kinkala,
    deces_kinkala, lits_kinkala, lits_occ_kinkala,
    medecins_kinkala, population_kinkala
)  # pour l'hôpital de Kinkala


# Fonction d'alerte : explique pourquoi un hôpital est critique
def message_alerte(nom, kpi):
    cout_patient, taux_occupation, densite, taux_mortalite = kpi
    raisons = []
    if taux_mortalite > 2:
        raisons.append(f"taux de mortalité élevé ({taux_mortalite:.2f}%)")
    if densite < 0.05:
        raisons.append(f"densité médicale insuffisante ({densite:.2f} médecin/1000 hab.)")
    if raisons:
        print(f"⚠️  {nom} : SITUATION CRITIQUE — " + " ET ".join(raisons))
    else:
        print(f"✅ {nom} : situation normale")


# ============================================================
# Rapport comparatif des 3 hôpitaux
# ============================================================
print('=' * 60)
print("RAPPORT COMPARATIF DES HOPITAUX DU POOL")
print('=' * 60)

print('-' * 60)
print("CMS VINDZA")
print('-' * 60)
print(f"Coût moyen patient : {vindza[0]:,.2f} FCFA".replace(',', ' '))
print(f"Taux occupation : {vindza[1]:.2f}%")
print(f"Densité médicale : {vindza[2]:.2f}")
print(f"Taux de mortalité : {vindza[3]:.2f}%")

print('-' * 60)
print("HOPITAL DISTRICT KINKALA")
print('-' * 60)
print(f"Coût moyen patient : {kinkala[0]:,.2f} FCFA".replace(',', ' '))
print(f"Taux occupation : {kinkala[1]:.2f}%")
print(f"Densité médicale : {kinkala[2]:.2f}")
print(f"Taux de mortalité : {kinkala[3]:.2f}%")

print('-' * 60)
print("HOPITAL DE KINDAMBA")
print('-' * 60)
print(f"Coût moyen patient : {kindamba[0]:,.2f} FCFA".replace(',', ' '))
print(f"Taux occupation : {kindamba[1]:.2f}%")
print(f"Densité médicale : {kindamba[2]:.2f}")
print(f"Taux de mortalité : {kindamba[3]:.2f}%")

print('-' * 60)
print("ALERTE — Hôpitaux en situation critique")
print("(critère : taux de mortalité > 2% OU densité médicale < 0.05)")
print('-' * 60)
message_alerte("CMS Vindza", vindza)
message_alerte("Hôpital District Kinkala", kinkala)
message_alerte("Hôpital de Kindamba", kindamba)

print('-' * 60)
print("BONUS — Passage à 5 médecins par hôpital")
print('-' * 60)
budget_total = budget_vindza + budget_kindamba + budget_kinkala
nb_medecins_cible = 5
cout_5_medecins = 3 * nb_medecins_cible * 1_200_000

print(f"Budget total des 3 hôpitaux : {budget_total:,.0f} FCFA".replace(',', ' '))
print(f"Coût pour 5 médecins/hôpital : {cout_5_medecins:,.0f} FCFA".replace(',', ' '))

if budget_total >= cout_5_medecins:
    print("✅ Le budget total permet de passer à 5 médecins par hôpital.")
else:
    manque = cout_5_medecins - budget_total
    print(f"❌ Budget insuffisant — il manque {manque:,.0f} FCFA".replace(',', ' '))