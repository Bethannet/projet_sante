# ============================================================
# MODULE FONDATEUR — Projet Sante Publique / Akieni Academy
# Ce fichier centralise toutes les constantes et variables metier
# Il sera enrichi chaque semaine jusqu'a S24
# ============================================================

# =========================================================
# === SECTION A : CONSTANTES NATIONALES ET NORMES OMS =====
# =========================================================
TAUX_EUR_FCFA = 655.957
TAUX_USD_FCFA = 600.0

SEUIL_OMS_DENSITE_MEDICALE = 2.3      # medecins pour 1000 habitants
SEUIL_OMS_COUVERTURE_VACCIN = 95.0    # pourcentage minimum OMS
SEUIL_MORTALITE_ALERTE = 2.0          # % deces / hospitalisations
SEUIL_RUPTURE_STOCK_JOURS = 30        # jours minimum de stock

# Seuils de couverture vaccinale OMS (classification a 4 niveaux)
SEUIL_VACCIN_CRITIQUE = 50.0   # < 50%  => ZONE CRITIQUE
SEUIL_VACCIN_A_RISQUE = 80.0   # < 80%  => ZONE A RISQUE
# >= SEUIL_OMS_COUVERTURE_VACCIN (95%) => ZONE CONFORME

# Seuils d'occupation hospitaliere (classification a 4 niveaux)
SEUIL_OCCUPATION_SOUS_UTILISE = 60.0   # < 60%        => SOUS-UTILISE
SEUIL_OCCUPATION_OPTIMAL = 85.0        # 60% - 85%    => OPTIMAL
SEUIL_OCCUPATION_ELEVE = 95.0          # 85% - 95%    => ELEVE
# >= SEUIL_OCCUPATION_ELEVE (95%)      => CRITIQUE

DEPARTEMENTS_CONGO = [                 # 12 departements officiels
    'Brazzaville', 'Pointe-Noire', 'Bouenza', 'Cuvette',
    'Cuvette-Ouest', 'Kouilou', 'Lekoumou', 'Likouala',
    'Niari', 'Plateaux', 'Pool', 'Sangha'
]


# =========================================================
# === SECTION B : VARIABLES DES 5 HOPITAUX =================
# =========================================================

# Hopital 1 — CHU de Brazzaville
h1_nom              = 'CHU de Brazzaville'
h1_ville             = 'Brazzaville'
h1_departement       = 'Brazzaville'
h1_type              = 'CHU'
h1_nb_lits           = 320
h1_nb_lits_occupes   = 284
h1_nb_medecins       = 47
h1_nb_infirmiers     = 123
h1_population_zone   = 1_800_000

# Hopital 2 — Hopital General de Pointe-Noire
h2_nom               = 'Hopital General de Pointe-Noire'
h2_ville             = 'Pointe-Noire'
h2_departement       = 'Pointe-Noire'
h2_type              = 'Hopital General'
h2_nb_lits           = 210
h2_nb_lits_occupes   = 201
h2_nb_medecins       = 28
h2_nb_infirmiers     = 96
h2_population_zone   = 1_100_000

# Hopital 3 — Hopital de Dolisie
h3_nom               = 'Hopital de Dolisie'
h3_ville             = 'Dolisie'
h3_departement       = 'Niari'
h3_type              = 'Hopital Departemental'
h3_nb_lits           = 95
h3_nb_lits_occupes   = 60
h3_nb_medecins       = 9
h3_nb_infirmiers      = 34
h3_population_zone   = 260_000

# Hopital 4 — Hopital de district d'Owando
h4_nom               = "Hopital de district d'Owando"
h4_ville             = 'Owando'
h4_departement       = 'Cuvette'
h4_type              = 'Hopital de district'
h4_nb_lits           = 60
h4_nb_lits_occupes   = 21
h4_nb_medecins       = 4
h4_nb_infirmiers     = 17
h4_population_zone   = 95_000

# Hopital 5 — Centre de sante d'Impfondo
h5_nom               = 'Centre de sante de Impfondo'
h5_ville             = 'Impfondo'
h5_departement       = 'Likouala'
h5_type              = 'Centre de sante'
h5_nb_lits           = 30
h5_nb_lits_occupes   = 29
h5_nb_medecins       = 2
h5_nb_infirmiers     = 11
h5_population_zone   = 48_000


# =========================================================
# === SECTION C : VARIABLES DES 5 MEDICAMENTS ==============
# =========================================================

# Medicament 1 — Artemether-Lumefantrine (antipaludeen)
m1_nom               = 'Artemether-Lumefantrine'
m1_quantite_dispo    = 4200
m1_seuil_rupture     = 1500
m1_cout_unitaire     = 850.0

# Medicament 2 — Amoxicilline
m2_nom               = 'Amoxicilline'
m2_quantite_dispo    = 6000
m2_seuil_rupture     = 2000
m2_cout_unitaire     = 320.0

# Medicament 3 — Paracetamol
m3_nom               = 'Paracetamol'
m3_quantite_dispo    = 1200
m3_seuil_rupture     = 2500
m3_cout_unitaire     = 90.0

# Medicament 4 — SRO (Sels de Rehydratation Orale)
m4_nom               = 'SRO'
m4_quantite_dispo    = 3000
m4_seuil_rupture     = 1000
m4_cout_unitaire     = 150.0

# Medicament 5 — Vaccin antipaludeen
m5_nom               = 'Vaccin antipaludeen'
m5_quantite_dispo    = 800
m5_seuil_rupture     = 1000
m5_cout_unitaire     = 4500.0


# =========================================================
# === SECTION D : CALCULS D'INITIALISATION =================
# =========================================================

# --- KPI 1 : Densite medicale nationale (medecins / 1000 habitants) ---
TOTAL_MEDECINS = (h1_nb_medecins + h2_nb_medecins + h3_nb_medecins
                   + h4_nb_medecins + h5_nb_medecins)
TOTAL_POPULATION = (h1_population_zone + h2_population_zone
                     + h3_population_zone + h4_population_zone
                     + h5_population_zone)

densite_medicale_nationale = (TOTAL_MEDECINS / TOTAL_POPULATION) * 1000

# --- KPI 2 : Taux d'occupation moyen (%) ---
TOTAL_LITS = h1_nb_lits + h2_nb_lits + h3_nb_lits + h4_nb_lits + h5_nb_lits
TOTAL_LITS_OCCUPES = (h1_nb_lits_occupes + h2_nb_lits_occupes
                       + h3_nb_lits_occupes + h4_nb_lits_occupes
                       + h5_nb_lits_occupes)

taux_occupation_moyen = (TOTAL_LITS_OCCUPES / TOTAL_LITS) * 100

# --- KPI 3 : Valeur totale du stock de medicaments (FCFA) ---
valeur_stock_m1 = m1_quantite_dispo * m1_cout_unitaire
valeur_stock_m2 = m2_quantite_dispo * m2_cout_unitaire
valeur_stock_m3 = m3_quantite_dispo * m3_cout_unitaire
valeur_stock_m4 = m4_quantite_dispo * m4_cout_unitaire
valeur_stock_m5 = m5_quantite_dispo * m5_cout_unitaire

valeur_totale_stock = (valeur_stock_m1 + valeur_stock_m2 + valeur_stock_m3
                        + valeur_stock_m4 + valeur_stock_m5)


# =========================================================
# === SECTION E : RAPPORT D'INVENTAIRE (INITIAL) ===========
# =========================================================

def afficher_rapport_inventaire():
    print("=" * 60)
    print("RAPPORT D'INVENTAIRE INITIAL - SYSTEME DE SANTE")
    print("=" * 60)

    print("\n--- HOPITAUX ---")
    print(f"{h1_nom} ({h1_ville}) : {h1_nb_lits_occupes}/{h1_nb_lits} lits, "
          f"{h1_nb_medecins} medecins")
    print(f"{h2_nom} ({h2_ville}) : {h2_nb_lits_occupes}/{h2_nb_lits} lits, "
          f"{h2_nb_medecins} medecins")
    print(f"{h3_nom} ({h3_ville}) : {h3_nb_lits_occupes}/{h3_nb_lits} lits, "
          f"{h3_nb_medecins} medecins")
    print(f"{h4_nom} ({h4_ville}) : {h4_nb_lits_occupes}/{h4_nb_lits} lits, "
          f"{h4_nb_medecins} medecins")
    print(f"{h5_nom} ({h5_ville}) : {h5_nb_lits_occupes}/{h5_nb_lits} lits, "
          f"{h5_nb_medecins} medecins")

    print("\n--- MEDICAMENTS ---")
    print(f"{m1_nom} : {m1_quantite_dispo} unites (seuil {m1_seuil_rupture}) "
          f"- valeur {valeur_stock_m1:,.0f} FCFA")
    print(f"{m2_nom} : {m2_quantite_dispo} unites (seuil {m2_seuil_rupture}) "
          f"- valeur {valeur_stock_m2:,.0f} FCFA")
    print(f"{m3_nom} : {m3_quantite_dispo} unites (seuil {m3_seuil_rupture}) "
          f"- valeur {valeur_stock_m3:,.0f} FCFA")
    print(f"{m4_nom} : {m4_quantite_dispo} unites (seuil {m4_seuil_rupture}) "
          f"- valeur {valeur_stock_m4:,.0f} FCFA")
    print(f"{m5_nom} : {m5_quantite_dispo} unites (seuil {m5_seuil_rupture}) "
          f"- valeur {valeur_stock_m5:,.0f} FCFA")

    print("\n--- KPIs GLOBAUX INITIAUX ---")
    print(f"Densite medicale nationale : {densite_medicale_nationale:.2f} "
          f"medecins / 1000 habitants (seuil OMS : {SEUIL_OMS_DENSITE_MEDICALE})")
    print(f"Taux d'occupation moyen des hopitaux : {taux_occupation_moyen:.1f}%")
    print(f"Valeur totale du stock de medicaments : {valeur_totale_stock:,.0f} FCFA")
    print("=" * 60)


# =========================================================
# === SECTION F : CLASSIFICATION STATUT DES MEDICAMENTS ===
# =========================================================
# Regle : on compare la quantite disponible au seuil de rupture
#   quantite <= seuil               => RUPTURE
#   quantite <= seuil * 1.5         => CRITIQUE
#   sinon                           => STOCK OK

def classer_statut_medicament(quantite_dispo, seuil_rupture):
    if quantite_dispo <= seuil_rupture:
        return 'RUPTURE'
    elif quantite_dispo <= seuil_rupture * 1.5:
        return 'CRITIQUE'
    else:
        return 'STOCK OK'

m1_statut = classer_statut_medicament(m1_quantite_dispo, m1_seuil_rupture)
m2_statut = classer_statut_medicament(m2_quantite_dispo, m2_seuil_rupture)
m3_statut = classer_statut_medicament(m3_quantite_dispo, m3_seuil_rupture)
m4_statut = classer_statut_medicament(m4_quantite_dispo, m4_seuil_rupture)
m5_statut = classer_statut_medicament(m5_quantite_dispo, m5_seuil_rupture)


# =========================================================
# === SECTION G : CLASSIFICATION OCCUPATION DES HOPITAUX ===
# =========================================================
# Utilise les constantes SEUIL_OCCUPATION_* de la SECTION A
#   < SOUS_UTILISE (60%)                      => SOUS-UTILISE
#   SOUS_UTILISE <= taux < OPTIMAL (85%)      => OPTIMAL
#   OPTIMAL <= taux < ELEVE (95%)             => ELEVE
#   >= ELEVE (95%)                            => CRITIQUE

def classer_occupation_hopital(nb_lits_occupes, nb_lits):
    taux = (nb_lits_occupes / nb_lits) * 100
    if taux < SEUIL_OCCUPATION_SOUS_UTILISE:
        return 'SOUS-UTILISE', taux
    elif taux < SEUIL_OCCUPATION_OPTIMAL:
        return 'OPTIMAL', taux
    elif taux < SEUIL_OCCUPATION_ELEVE:
        return 'ELEVE', taux
    else:
        return 'CRITIQUE', taux

h1_statut_occupation, h1_taux_occupation = classer_occupation_hopital(h1_nb_lits_occupes, h1_nb_lits)
h2_statut_occupation, h2_taux_occupation = classer_occupation_hopital(h2_nb_lits_occupes, h2_nb_lits)
h3_statut_occupation, h3_taux_occupation = classer_occupation_hopital(h3_nb_lits_occupes, h3_nb_lits)
h4_statut_occupation, h4_taux_occupation = classer_occupation_hopital(h4_nb_lits_occupes, h4_nb_lits)
h5_statut_occupation, h5_taux_occupation = classer_occupation_hopital(h5_nb_lits_occupes, h5_nb_lits)


# =========================================================
# === SECTION H : CLASSIFICATION COUVERTURE VACCINALE ======
# =========================================================
# Donnees officielles (tableau fourni) — 4 departements
# Utilise les constantes SEUIL_VACCIN_* / SEUIL_OMS_COUVERTURE_VACCIN

d1_departement        = 'Brazzaville'
d1_population_cible   = 450000
d1_personnes_vaccinees = 418500
d1_taux_couverture    = (d1_personnes_vaccinees / d1_population_cible) * 100

d2_departement        = 'Pointe-Noire'
d2_population_cible   = 280000
d2_personnes_vaccinees = 229600
d2_taux_couverture    = (d2_personnes_vaccinees / d2_population_cible) * 100

d3_departement        = 'Pool'
d3_population_cible   = 120000
d3_personnes_vaccinees = 54000
d3_taux_couverture    = (d3_personnes_vaccinees / d3_population_cible) * 100

d4_departement        = 'Sangha'
d4_population_cible   = 85000
d4_personnes_vaccinees = 35700
d4_taux_couverture    = (d4_personnes_vaccinees / d4_population_cible) * 100


def classer_couverture_vaccinale(taux):
    if taux < SEUIL_VACCIN_CRITIQUE:
        return 'ZONE CRITIQUE'
    elif taux < SEUIL_VACCIN_A_RISQUE:
        return 'ZONE A RISQUE'
    elif taux < SEUIL_OMS_COUVERTURE_VACCIN:
        return 'ZONE INSUFFISANTE'
    else:
        return 'ZONE CONFORME'

d1_statut_vaccinal = classer_couverture_vaccinale(d1_taux_couverture)
d2_statut_vaccinal = classer_couverture_vaccinale(d2_taux_couverture)
d3_statut_vaccinal = classer_couverture_vaccinale(d3_taux_couverture)
d4_statut_vaccinal = classer_couverture_vaccinale(d4_taux_couverture)


# =========================================================
# === SECTION I : RAPPORT D'ETAT GLOBAL AVEC ALERTES =======
# =========================================================

def afficher_rapport_etat_global():
    print("\n" + "=" * 60)
    print("RAPPORT D'ETAT GLOBAL - SEMAINE 3 - ALERTES")
    print("=" * 60)

    # --- Bloc medicaments ---
    print("\n--- STATUT DES STOCKS DE MEDICAMENTS ---")
    medicaments = [
        (m1_nom, m1_quantite_dispo, m1_statut),
        (m2_nom, m2_quantite_dispo, m2_statut),
        (m3_nom, m3_quantite_dispo, m3_statut),
        (m4_nom, m4_quantite_dispo, m4_statut),
        (m5_nom, m5_quantite_dispo, m5_statut),
    ]
    nb_ruptures = 0
    for nom, qte, statut in medicaments:
        print(f"  {nom:30s} : {qte:5d} unites -> {statut}")
        if statut == 'RUPTURE':
            nb_ruptures += 1

    # --- Bloc hopitaux ---
    print("\n--- NIVEAU D'OCCUPATION DES HOPITAUX ---")
    hopitaux = [
        (h1_nom, h1_taux_occupation, h1_statut_occupation),
        (h2_nom, h2_taux_occupation, h2_statut_occupation),
        (h3_nom, h3_taux_occupation, h3_statut_occupation),
        (h4_nom, h4_taux_occupation, h4_statut_occupation),
        (h5_nom, h5_taux_occupation, h5_statut_occupation),
    ]
    nb_saturation = 0
    for nom, taux, statut in hopitaux:
        print(f"  {nom:35s} : {taux:5.1f}% -> {statut}")
        if statut == 'CRITIQUE':
            nb_saturation += 1

    # --- Bloc couverture vaccinale ---
    print("\n--- COUVERTURE VACCINALE PAR DEPARTEMENT ---")
    departements_vaccin = [
        (d1_departement, d1_taux_couverture, d1_statut_vaccinal),
        (d2_departement, d2_taux_couverture, d2_statut_vaccinal),
        (d3_departement, d3_taux_couverture, d3_statut_vaccinal),
        (d4_departement, d4_taux_couverture, d4_statut_vaccinal),
    ]
    nb_zones_critiques = 0
    for dep, taux, statut in departements_vaccin:
        print(f"  {dep:15s} : {taux:5.1f}% -> {statut}")
        if statut == 'ZONE CRITIQUE':
            nb_zones_critiques += 1

    # --- Resume executif ---
    print("\n--- RESUME EXECUTIF ---")
    print(f"  Alertes ruptures medicament   : {nb_ruptures}")
    print(f"  Hopitaux en saturation (CRITIQUE) : {nb_saturation}")
    print(f"  Zones vaccinales critiques     : {nb_zones_critiques}")

    total_alertes = nb_ruptures + nb_saturation + nb_zones_critiques
    if total_alertes == 0:
        print(f"  STATUT GLOBAL : SYSTEME STABLE - aucune alerte critique")
    elif total_alertes <= 2:
        print(f"  STATUT GLOBAL : VIGILANCE - quelques points a surveiller")
    else:
        print("  STATUT GLOBAL : ALERTE - intervention urgente recommandee")

    print("=" * 60)


# =========================================================
# === EXECUTION DU MODULE ==================================
# =========================================================
if __name__ == '__main__':
    afficher_rapport_inventaire()
    afficher_rapport_etat_global()