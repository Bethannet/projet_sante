# ============================================================
# CHALLENGE ENTREPRISE — RAPPORT D'ETAT SANITAIRE DEPARTEMENTAL
# Demande du Ministre — Conseil des Ministres du 17 janvier 2026
# ============================================================

# ============================================================
# === IMPORT / DECLARATION DES VARIABLES DES 5 HOPITAUX =====
# ============================================================
# (Variables redeclarees ici depuis sante_variables.py, avec
#  les donnees specifiques fournies par le Ministere pour ce
#  rapport : lits, lits occupes, medecins, ruptures, alertes)

# --- Hopital 1 : CHU Brazzaville ---
h1_nom            = 'CHU Brazzaville'
h1_nb_lits        = 320
h1_nb_lits_occupes = 298
h1_nb_medecins    = 47
h1_nb_ruptures    = 2
h1_medocs_rupture = "SRO, Vaccin"
h1_nb_alertes     = 2
h1_medocs_alerte  = "Artemether, Amoxi"

# --- Hopital 2 : Hopital Pointe-Noire ---
h2_nom            = 'Hopital Pointe-Noire'
h2_nb_lits        = 180
h2_nb_lits_occupes = 143
h2_nb_medecins    = 22
h2_nb_ruptures    = 0
h2_medocs_rupture = ""
h2_nb_alertes     = 1
h2_medocs_alerte  = "Amoxicilline"

# --- Hopital 3 : Hopital Dolisie ---
h3_nom            = 'Hopital Dolisie'
h3_nb_lits        = 95
h3_nb_lits_occupes = 91
h3_nb_medecins    = 8
h3_nb_ruptures    = 1
h3_medocs_rupture = "SRO"
h3_nb_alertes     = 2
h3_medocs_alerte  = "Artemether, Vaccin"

# --- Hopital 4 : Hopital Owando ---
h4_nom            = 'Hopital Owando'
h4_nb_lits        = 45
h4_nb_lits_occupes = 32
h4_nb_medecins    = 3
h4_nb_ruptures    = 3
h4_medocs_rupture = "SRO, Vaccin, Artemether"
h4_nb_alertes     = 0
h4_medocs_alerte  = ""

# --- Hopital 5 : CMS Impfondo ---
h5_nom            = 'CMS Impfondo'
h5_nb_lits        = 20
h5_nb_lits_occupes = 19
h5_nb_medecins    = 1
h5_nb_ruptures    = 2
h5_medocs_rupture = "SRO, Amoxi"
h5_nb_alertes     = 1
h5_medocs_alerte  = "Vaccin"


# ============================================================
#  SEUILS DE CLASSIFICATION (regles du Ministere) =========
# ============================================================
SEUIL_OCCUPATION_CRITIQUE = 95.0      # > 95% => CRITIQUE
SEUIL_OCCUPATION_PREOCCUPANT = 85.0   # > 85% => PREOCCUPANT
SEUIL_RUPTURE_CRITIQUE = 2            # >= 2 ruptures => CRITIQUE
SEUIL_RUPTURE_PREOCCUPANT = 1         # >= 1 rupture  => PREOCCUPANT
SEUIL_ALERTES_PREOCCUPANT = 2         # >= 2 alertes ET medecins < 5 => PREOCCUPANT
SEUIL_MEDECINS_CRITIQUE_RH = 5
COUT_COMMANDE_EXPRESS = 450_000.0     # FCFA, cout unitaire moyen d'une commande urgente


# ============================================================
# FONCTIONS DE CALCUL 
# ============================================================

def calculer_taux_occupation(nb_lits_occupes, nb_lits):
    """S2 : calcul simple du taux d'occupation en %."""
    return (nb_lits_occupes / nb_lits) * 100


def classer_niveau_triage_occupation(taux):
    """Etiquette courte utilisee dans le tableau de bord : [CRI] [ALT] [OK]"""
    if taux > SEUIL_OCCUPATION_CRITIQUE:
        return 'CRI'
    elif taux > SEUIL_OCCUPATION_PREOCCUPANT:
        return 'ALT'
    else:
        return 'OK'


def classer_niveau_alerte_global(nb_ruptures, taux_occupation, nb_alertes, nb_medecins):
    """
    Regles officielles du Ministere (if/elif/else, conditions composees) :
      CRITIQUE    : nb_ruptures >= 2 OU taux_occupation > 95%
      PREOCCUPANT : nb_ruptures >= 1 OU taux_occupation > 85%
                    OU (nb_alertes >= 2 ET nb_medecins < 5)
      SATISFAISANT: sinon
    """
    if nb_ruptures >= SEUIL_RUPTURE_CRITIQUE or taux_occupation > SEUIL_OCCUPATION_CRITIQUE:
        return 'CRITIQUE'
    elif (nb_ruptures >= SEUIL_RUPTURE_PREOCCUPANT
          or taux_occupation > SEUIL_OCCUPATION_PREOCCUPANT
          or (nb_alertes >= SEUIL_ALERTES_PREOCCUPANT and nb_medecins < SEUIL_MEDECINS_CRITIQUE_RH)):
        return 'PREOCCUPANT'
    else:
        return 'SATISFAISANT'


def definir_recommandation(niveau_global, nb_ruptures, taux_occupation):
    """Recommandation d'action prioritaire en une phrase, selon le niveau global."""
    if niveau_global == 'CRITIQUE':
        if nb_ruptures >= SEUIL_RUPTURE_CRITIQUE:
            return "Mobiliser la reserve nationale PNA"
        else:
            return "Activer le plan de delestage des patients vers etablissements voisins"
    elif niveau_global == 'PREOCCUPANT':
        return "Renforcer le suivi des stocks et anticiper une commande de reapprovisionnement"
    else:
        return "Maintenir la surveillance de routine, aucune action urgente requise"


# ============================================================
#  CALCULS POUR LES 5 HOPITAUX 
# ============================================================

hopitaux = [
    (h1_nom, h1_nb_lits, h1_nb_lits_occupes, h1_nb_medecins, h1_nb_ruptures, h1_nb_alertes),
    (h2_nom, h2_nb_lits, h2_nb_lits_occupes, h2_nb_medecins, h2_nb_ruptures, h2_nb_alertes),
    (h3_nom, h3_nb_lits, h3_nb_lits_occupes, h3_nb_medecins, h3_nb_ruptures, h3_nb_alertes),
    (h4_nom, h4_nb_lits, h4_nb_lits_occupes, h4_nb_medecins, h4_nb_ruptures, h4_nb_alertes),
    (h5_nom, h5_nb_lits, h5_nb_lits_occupes, h5_nb_medecins, h5_nb_ruptures, h5_nb_alertes),
]

resultats = []  # une entree par hopital : dict avec toutes les infos calculees

for nom, nb_lits, nb_lits_occupes, nb_medecins, nb_ruptures, nb_alertes in hopitaux:
    taux_occupation = calculer_taux_occupation(nb_lits_occupes, nb_lits)
    niveau_triage = classer_niveau_triage_occupation(taux_occupation)
    niveau_global = classer_niveau_alerte_global(nb_ruptures, taux_occupation, nb_alertes, nb_medecins)
    recommandation = definir_recommandation(niveau_global, nb_ruptures, taux_occupation)

    resultats.append({
        'nom': nom,
        'taux_occupation': taux_occupation,
        'niveau_triage': niveau_triage,
        'nb_ruptures': nb_ruptures,
        'nb_alertes': nb_alertes,
        'niveau_global': niveau_global,
        'recommandation': recommandation,
    })


# ============================================================
# === BILAN NATIONAL (BONUS) ==================================
# ============================================================

nb_hopitaux_critiques = sum(1 for r in resultats if r['niveau_global'] == 'CRITIQUE')
total_ruptures_nationales = sum(r['nb_ruptures'] for r in resultats)
cout_total_commandes_urgentes = total_ruptures_nationales * COUT_COMMANDE_EXPRESS

# Recommandation prioritaire nationale = celle de l'hopital le plus critique
# (priorite : plus de ruptures, puis plus forte occupation)
hopital_plus_critique = max(
    resultats,
    key=lambda r: (r['nb_ruptures'], r['taux_occupation'])
)
recommandation_nationale = hopital_plus_critique['recommandation']


# ============================================================
# AFFICHAGE DU TABLEAU DE BORD 
# ============================================================

def afficher_tableau_de_bord():
    print("=" * 62)
    print("  TABLEAU DE BORD SANITAIRE - MINISTERE DE LA SANTE")
    print("  Date : 16 janvier 2026  |  Pour le Conseil des Ministres")
    print("=" * 62)
    print(f"  {'HOPITAL':<22}{'OCCUPATION':<14}{'ALERTES':<10}{'NIVEAU GLOBAL'}")

    for r in resultats:
        occupation_str = f"{r['taux_occupation']:.1f}% [{r['niveau_triage']}]"
        alertes_str = f"{r['nb_ruptures']}R + {r['nb_alertes']}A"
        print(f"  {r['nom']:<22}{occupation_str:<14}{alertes_str:<10}[{r['niveau_global']}]")

    print("-" * 62)
    print(f"  {nb_hopitaux_critiques} hopitaux sur {len(resultats)} en situation CRITIQUE")
    print(f"  {total_ruptures_nationales} ruptures de stock identifiees a l'echelle nationale")
    print(f"  RECOMMANDATION PRIORITAIRE : {recommandation_nationale}")
    print("=" * 62)


if __name__ == '__main__':
    afficher_tableau_de_bord()