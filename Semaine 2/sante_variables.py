# ============================================================ 
# MODULE FONDATEUR — Projet Sante Publique / Akieni Academy 
# Ce fichier centralise toutes les constantes et variables metier 
# Il sera enrichi chaque semaine jusqu'a S24 
# ============================================================ 
# === SECTION A : CONSTANTES NATIONALES ET NORMES OMS ======== 
TAUX_EUR_FCFA = 655.957 
TAUX_USD_FCFA = 600.0 
SEUIL_OMS_DENSITE_MEDICALE = 2.3    
# medecins pour 1000 habitants 
SEUIL_OMS_COUVERTURE_VACCIN = 95.0  # pourcentage minimum OMS 
SEUIL_MORTALITE_ALERTE = 2.0        # % deces / hospitalisations 
SEUIL_RUPTURE_STOCK_JOURS = 30      # jours minimum de stock 
DEPARTEMENTS_CONGO = [              # 12 departements officiels 
    'Brazzaville', 'Pointe-Noire', 'Bouenza', 'Cuvette', 
    'Cuvette-Ouest', 'Kouilou', 'Lekoumou', 'Likouala', 
    'Niari', 'Plateaux', 'Pool', 'Sangha' 
] 
 

# === SECTION B : VARIABLES DES 5 HOPITAUX =================== 
# Hopital 1 — CHU de Brazzaville 
h1_nom              = 'CHU de Brazzaville' 
h1_ville            = 'Brazzaville' 
h1_departement      = 'Brazzaville' 
h1_type             = 'CHU' 
h1_nb_lits          = 320 
h1_nb_lits_occupes  = 298 
h1_nb_medecins      = 47 
h1_nb_infirmiers    = 123 #
h1_population_zone  = 1_800_000 
# Hopital 2 - Hopital general Pointe-Noire
h2_nom              = 'Hopital General Pointe-Noire'
h2_ville            = 'Pointe-Noire'
h2_departement      = 'Pointe-Noire'
h2_type             = 'Hopital General'
h2_nb_lits          = 180
h2_nb_lits_occupes  = 143
h2_nb_medecins      = 22
h2_nb_infirmiers    = 150 #
h2_population_zone  = 1_123_342
# Hopital 3 - Hopital de Dolisie
h3_nom              = 'Hopital de Dolisie'
h3_ville            = 'Dolisie'
h3_departement      = 'Niari'
h3_type             = 'Hopital'
h3_nb_lits          = 95
h3_nb_lits_occupes  = 91
h3_nb_medecins      = 8
h3_nb_infirmiers    = 34  #
h3_population_zone  = 456_698
# Hopital 4 - Hopital de district Owando
h4_nom              = 'Hopital de district Owando'
h4_ville            = 'Owando'
h4_departement      = 'Cuvette'
h4_type             = 'Hopital de district'
h4_nb_lits          = 45
h4_nb_lits_occupes  = 32
h4_nb_medecins      = 3
h4_nb_infirmiers    = 42 #
h4_population_zone  = 987_765
# Hopital 5 - Centre de sante de Impfondo 
h5_nom              = 'Centre de sante de Impfondo'
h5_ville            = 'Impfondo'
h5_departement      = 'Likouala'
h5_type             = 'Centre de sante'
h5_nb_lits          = 20
h5_nb_lits_occupes  = 19
h5_nb_medecins      = 1
h5_nb_infirmiers    = 30  #
h5_population_zone  = 1_000_123

 
# === SECTION C : VARIABLES DES 5 MEDICAMENTS ================ 
# TODO : Declarer les 5 medicaments essentiels
#Medicament 1 - Artemether-Lumefantrine (antipaludeen)
m1_nom                  = 'Artemether-Lumefantrine'
m1_categorie            = 'Antipaludeen'
m1_quantite_disponible  = 4_200      # int : nombre de boites en stock
m1_seuil_rupture        = 1_000      # int : seuil minimum avant alerte
m1_cout_unitaire        = 1_250.0    # float : cout en FCFA par boite
 
# Medicament 2 - Amoxicilline (antibiotique)
m2_nom                  = 'Amoxicilline'
m2_categorie            = 'Antibiotique'
m2_quantite_disponible  = 6_800
m2_seuil_rupture        = 1_500
m2_cout_unitaire        = 850.0
 
# Medicament 3 - Paracetamol (antalgique)
m3_nom                  = 'Paracetamol'
m3_categorie            = 'Antalgique'
m3_quantite_disponible  = 12_500
m3_seuil_rupture        = 3_000
m3_cout_unitaire        = 150.0
 
# Medicament 4 - SRO (Sels de Rehydratation Orale)
m4_nom                  = 'SRO'
m4_categorie            = 'Rehydratation'
m4_quantite_disponible  = 3_400
m4_seuil_rupture        = 1_200
m4_cout_unitaire        = 300.0
 
# Medicament 5 - Vaccin antipaludeen
m5_nom                  = 'Vaccin antipaludeen'
m5_categorie            = 'Vaccin'
m5_quantite_disponible  = 950
m5_seuil_rupture        = 500
m5_cout_unitaire         = 18_500.0 
 
# === SECTION D : CALCULS D'INITIALISATION =================== 
# TODO : Calculer les KPIs globaux initiaux 
#--KPIs hopitaux --
total_lits = (h1_nb_lits + h2_nb_lits + h3_nb_lits
              + h4_nb_lits + h5_nb_lits)
total_lits_occupes = (h1_nb_lits_occupes + h2_nb_lits_occupes
                       + h3_nb_lits_occupes + h4_nb_lits_occupes
                       + h5_nb_lits_occupes)
total_medecins = (h1_nb_medecins + h2_nb_medecins + h3_nb_medecins
                   + h4_nb_medecins + h5_nb_medecins)
total_population = (h1_population_zone + h2_population_zone
                     + h3_population_zone + h4_population_zone
                     + h5_population_zone)
 
# Densite medicale nationale : medecins pour 1000 habitants
densite_medicale_nationale = round((total_medecins / total_population) * 1000, 2)
 
# Taux d'occupation moyen des lits (sur l'ensemble du parc)
taux_occupation_moyen = round((total_lits_occupes / total_lits) * 100, 2)
 
# -- KPI medicaments --
# Valeur totale du stock = somme(quantite * cout unitaire) pour chaque medicament
valeur_stock_m1 = m1_quantite_disponible * m1_cout_unitaire
valeur_stock_m2 = m2_quantite_disponible * m2_cout_unitaire
valeur_stock_m3 = m3_quantite_disponible * m3_cout_unitaire
valeur_stock_m4 = m4_quantite_disponible * m4_cout_unitaire
valeur_stock_m5 = m5_quantite_disponible * m5_cout_unitaire
 
valeur_totale_stock = round(
    valeur_stock_m1 + valeur_stock_m2 + valeur_stock_m3
    + valeur_stock_m4 + valeur_stock_m5, 2
)
 
# === SECTION E : RAPPORT D'INVENTAIRE ======================= 
# TODO : Afficher le rapport initial du systeme de sante
def afficher_rapport():
    """Affiche le rapport initial du systeme de sante (lisible, sans code)."""
    print('=' * 60)
    print("RAPPORT D'INVENTAIRE INITIAL — SYSTEME DE SANTE")
    print('=' * 60)
 
    print('-' * 60)
    print("NORMES OMS DE REFERENCE")
    print('-' * 60)
    print(f"Seuil densite medicale OMS    : {SEUIL_OMS_DENSITE_MEDICALE} medecins/1000 hab.")
    print(f"Seuil couverture vaccinale    : {SEUIL_OMS_COUVERTURE_VACCIN}%")
    print(f"Seuil d'alerte mortalite      : {SEUIL_MORTALITE_ALERTE}%")
    print(f"Stock minimum (jours)         : {SEUIL_RUPTURE_STOCK_JOURS} jours")
    print(f"Nombre de departements suivis : {len(DEPARTEMENTS_CONGO)}")
 
    print('-' * 60)
    print("HOPITAUX RECENSES")
    print('-' * 60)
    for nom, ville, lits, lits_occ, medecins in [
        (h1_nom, h1_ville, h1_nb_lits, h1_nb_lits_occupes, h1_nb_medecins),
        (h2_nom, h2_ville, h2_nb_lits, h2_nb_lits_occupes, h2_nb_medecins),
        (h3_nom, h3_ville, h3_nb_lits, h3_nb_lits_occupes, h3_nb_medecins),
        (h4_nom, h4_ville, h4_nb_lits, h4_nb_lits_occupes, h4_nb_medecins),
        (h5_nom, h5_ville, h5_nb_lits, h5_nb_lits_occupes, h5_nb_medecins),
    ]:
        taux_occ = round((lits_occ / lits) * 100, 2)
        print(f"{nom} ({ville}) : {lits} lits, {medecins} medecins, "
              f"taux occupation {taux_occ}%")
 
    print('-' * 60)
    print("KPIs GLOBAUX NATIONAUX")
    print('-' * 60)
    print(f"Total lits (5 hopitaux)        : {total_lits}")
    print(f"Total medecins (5 hopitaux)    : {total_medecins}")
    print(f"Population totale couverte    : {total_population:,}".replace(',', ' '))
    print(f"Densite medicale nationale     : {densite_medicale_nationale} medecins/1000 hab.")
    print(f"Taux d'occupation moyen        : {taux_occupation_moyen}%")
 
    if densite_medicale_nationale < SEUIL_OMS_DENSITE_MEDICALE:
        print(f"⚠️  ALERTE : densite medicale sous le seuil OMS "
              f"({SEUIL_OMS_DENSITE_MEDICALE})")
    else:
        print("✅ Densite medicale conforme au seuil OMS")
 
    print('-' * 60)
    print("STOCK DE MEDICAMENTS ESSENTIELS")
    print('-' * 60)
    for nom, qte, seuil, cout, valeur in [
        (m1_nom, m1_quantite_disponible, m1_seuil_rupture, m1_cout_unitaire, valeur_stock_m1),
        (m2_nom, m2_quantite_disponible, m2_seuil_rupture, m2_cout_unitaire, valeur_stock_m2),
        (m3_nom, m3_quantite_disponible, m3_seuil_rupture, m3_cout_unitaire, valeur_stock_m3),
        (m4_nom, m4_quantite_disponible, m4_seuil_rupture, m4_cout_unitaire, valeur_stock_m4),
        (m5_nom, m5_quantite_disponible, m5_seuil_rupture, m5_cout_unitaire, valeur_stock_m5),
    ]:
        alerte = " ⚠️ RISQUE DE RUPTURE" if qte < seuil else ""
        valeur_fmt = f"{valeur:,.2f}".replace(',', ' ')
        print(f"{nom} : {qte} unites (seuil {seuil}), "
              f"valeur {valeur_fmt} FCFA{alerte}")
 
    print('-' * 60)
    print(f"VALEUR TOTALE DU STOCK : {valeur_totale_stock:,.2f} FCFA".replace(',', ' '))
    print('=' * 60)
 
 
# Le fichier doit etre executable directement et afficher le rapport
if __name__ == '__main__':
    afficher_rapport()
  