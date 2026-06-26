# ============================================================
# Rapport PNA — Pharmacie Nationale d'Approvisionnement
# Suivi de stock de 3 medicaments essentiels
# ============================================================

# Medicament 1 : Artemether-Lumefantrine ---
m1_nom              = "Artemether-Lumefantrine"
m1_stock            = 8_450
m1_seuil_rupture    = 2_000
m1_prix_unitaire    = 3_500
m1_conso_mensuelle  = 1_200

# Medicament 2 : Amoxicilline 500mg ---
m2_nom              = "Amoxicilline 500mg"
m2_stock            = 3_200
m2_seuil_rupture    = 800
m2_prix_unitaire    = 850
m2_conso_mensuelle  = 650

# Medicament 3 : Serum de rehydratation ---
m3_nom              = "Serum de rehydratation"
m3_stock            = 15_600
m3_seuil_rupture    = 5_000
m3_prix_unitaire    = 125
m3_conso_mensuelle  = 3_800


# Fonction de calcul des indicateurs pour un medicament 
def calculer_indicateurs(stock, prix, conso_mensuelle):
    """Calcule la valeur du stock, les mois restants et le statut."""
    valeur_stock = stock * prix
    mois_restants = round(stock / conso_mensuelle, 1)

    if mois_restants > 2:
        statut = "OK"
    elif mois_restants >= 1:
        statut = "ALERTE"
    else:
        statut = "RUPTURE"

    return valeur_stock, mois_restants, statut


# Calculs pour chaque medicament ---
m1_valeur, m1_mois, m1_statut = calculer_indicateurs(m1_stock, m1_prix_unitaire, m1_conso_mensuelle)
m2_valeur, m2_mois, m2_statut = calculer_indicateurs(m2_stock, m2_prix_unitaire, m2_conso_mensuelle)
m3_valeur, m3_mois, m3_statut = calculer_indicateurs(m3_stock, m3_prix_unitaire, m3_conso_mensuelle)

# Valeur totale des 3 stocks combines ---
valeur_totale = m1_valeur + m2_valeur + m3_valeur

# Medicament le plus critique = celui qui a le moins de mois restants ---
medicaments = [
    (m1_nom, m1_mois, m1_stock, m1_conso_mensuelle),
    (m2_nom, m2_mois, m2_stock, m2_conso_mensuelle),
    (m3_nom, m3_mois, m3_stock, m3_conso_mensuelle),
]
nom_critique, mois_critique, stock_critique, conso_critique = min(medicaments, key=lambda x: x[1])

# Jours restants avant rupture (consommation journaliere = conso mensuelle / 30)
conso_journaliere_critique = conso_critique / 30
jours_stock_critique = int(stock_critique // conso_journaliere_critique)


# ============================================================
# AFFICHAGE DU RAPPORT
# ============================================================
print("=" * 60)
print(f"RAPPORT DE STOCK — PHARMACIE NATIONALE D'APPROVISIONNEMENT")
print("=" * 60)

print("-" * 60)
print(f"{m1_nom}")
print("-" * 60)
print(f"Stock actuel        : {m1_stock} unites")
print(f"Valeur du stock      : {m1_valeur:,.0f} FCFA".replace(',', ' '))
print(f"Mois de stock restant : {m1_mois} mois")
print(f"Statut               : {m1_statut}")

print("-" * 60)
print(m2_nom)
print("-" * 60)
print(f"Stock actuel        : {m2_stock} unites")
print(f"Valeur du stock      : {m2_valeur:,.0f} FCFA".replace(',', ' '))
print(f"Mois de stock restant : {m2_mois} mois")
print(f"Statut               : {m2_statut}")

print("-" * 60)
print(m3_nom)
print("-" * 60)
print(f"Stock actuel        : {m3_stock} unites")
print(f"Valeur du stock      : {m3_valeur:,.0f} FCFA".replace(',', ' '))
print(f"Mois de stock restant : {m3_mois} mois")
print(f"Statut               : {m3_statut}")

print("-" * 60)
print(f"SYNTHESE GLOBALE")
print("-" * 60)
print(f"Valeur totale des 3 stocks : {valeur_totale:,.0f} FCFA".replace(',', ' '))
print(f"Medicament le plus critique : {nom_critique} ({mois_critique} mois de stock)")
print(f"Jours avant rupture estimes : {jours_stock_critique} jours")
print("=" * 60)