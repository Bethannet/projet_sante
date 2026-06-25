# ============================================================ 
# AKIENI ACADEMY — Projet Sante Publique 
# Semaine 2 — Exercice 2 : KPIs Sanitaires OMS 
# ============================================================ 
 
# --- DONNEES BRUTES --- 
budget_fcfa          = 87_4500_00   # underscore pour lisibilite des grands nombres 
nb_consultations_ext = 4823 
nb_hospitalisations  = 1247 
nb_deces             = 18 
nb_lits_total        = 180 
nb_lits_occupes      = 143 
nb_medecins          = 22 
nb_infirmiers        = 58 
population_dept      = 128_000 
taux_eur_fcfa        = 655.957 
taux_usd_fcfa        = 600.0 
 
# --- A COMPLETER --- 
# 1. Conversions devises 
budget_eur = budget_fcfa / taux_eur_fcfa 
budget_usd = budget_fcfa / taux_usd_fcfa 
 
# 2. Indicateurs OMS 
densite_medicale     = nb_medecins / population_dept * 1000 
taux_mortalite       = nb_deces / nb_hospitalisations * 100 
taux_occupation      = nb_lits_occupes / nb_lits_total * 100 
 
# 3. Division entiere et modulo 
budget_medicaments   = round(budget_fcfa * 0.35) 
cout_journalier_meds = 450_000 
jours_stock          = budget_medicaments // cout_journalier_meds   # division entiere // 
jours_restants       = budget_medicaments % cout_journalier_meds   # modulo % 
#operateur modulo
reste_consultations  = nb_consultations_ext % 2
parite_consultations = "paire" if reste_consultations == 0 else "impaire"

# 4. Puissance pour projection 
budget_n_plus_2 =87450000 * (1.08**2)  #** pour la puissance 
 
# --- AFFICHAGE RAPPORT --- 
print(f'=== RAPPORT TRIMESTRIEL Q4 2025 - Hopital General Pointe-Noire ===')
print(f"BUDGET") 
# ... completez l'affichage 
print(f"Depenses Q4 : {budget_fcfa:,.0f} FCFA".replace(',', ' '))
print(f"En euros : {budget_eur:,.2f} EUR".replace(',', ' '))
print(f"En dollars : {budget_usd:,.2f} USD".replace(',', ' '))
print(f"INDICATEURS OMS")
print(f"Densite medicale : {densite_medicale:.1f} medecins / 1000 hab   [Norme OMS : >= 2.3]           ")
print(f"Taux mortalite : {taux_mortalite:.1f}%                   [Seuil alerte : > 2%]")
print(f"Taux occupation : {taux_occupation:.1f}%                       [Optimal : 70-85%]")
print(f"ANALYSE PHARMACIE")
print(f"Budget medicaments : {budget_medicaments:,.0f} FCFA".replace(',', ' '))
print(f"Jours de stock : {jours_stock} jours")
print(f"Jours depassement : {jours_restants} jours")

# --- AFFICHAGE RAPPORT --- 
print(f'=== RAPPORT TRIMESTRIEL Q4 2025 - Hopital General Pointe-Noire ===') 
# ... completez l'affichage
print(f"PROJECTION") 
print(f"Budget N+2 (8%/an) : {budget_n_plus_2:,.1f} FCFA".replace(',', ' '))
print(f"ALERTE: Densite medicale CRITIQUE ({densite_medicale:.1f} pour 1000 hab - norme OMS : 2.3)")
