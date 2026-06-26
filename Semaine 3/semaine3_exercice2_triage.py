# ============================================================
# AKIENI ACADEMY — Projet Sante Publique
# Semaine 3 — Exercice 2 : Triage Patient Urgences CHU Brazzaville
# Notions S2 : variables, types, input(), f-strings, conversion
# Notions S3 : if/elif/else, conditions composees or/and/not
# ============================================================
print('=== SYSTEME DE TRIAGE — URGENCES CHU BRAZZAVILLE ===')
print('Protocole Manchester adapte — DSS Congo 2026')
print()
# --- SAISIE DES DONNEES PATIENT (S2 reutilise : input(), conversion) --
nom_patient   = input('Nom du patient : ')
age_patient   = int(input('Age (annees) : '))
temperature   = float(input('Temperature (degres C, ex: 38.4) : '))
spo2          = float(input('Saturation O2 en % (ex: 96.0) : '))
tension_syst  = int(input('Tension systolique en mmHg (ex: 135) : '))
douleur       = int(input('Douleur /10 (0=aucune, 10=insupportable) : '))
# --- VALIDATION DES PLAGES (S2 + S3 : conditions simples) --
# Verifier que la temperature est dans une plage physiologiquement possible
if temperature < 35.0 or temperature > 43.0:
    print('ERREUR : Valeur de temperature impossible — verifier la saisie')
    # Dans une version avancee, on redemanderait la saisie ici
# TODO : Valider spo2, tension_syst, douleur, age de la meme facon
if spo2 < 50.0 or spo2 > 100.0:
    print('ERREUR : Spo2 hors plage - verifier le capteur')
if tension_syst < 50 or tension_syst > 250:
    print('ERREUR : Tension hors plage — verifier le brassard')
if douleur < 0 or douleur > 10:
    print('ERREUR : Douleur doit etre entre 0 et 10')
if age_patient < 0 or age_patient > 120:
    print('ERREUR : Age invalide — verifier la saisie')

# --- TRIAGE (S3 nouveau : conditions composees avec or) --
# Niveau 1 : IMMEDIAT — au moins UNE condition critique suffit (or)
if temperature > 39.5 or spo2 < 90 or tension_syst > 180:
    niveau_triage  = '1 — IMMEDIAT'
    couleur_triage = '[ROUGE]'
    delai_pec      = '0 minute'
    action_triage  = 'Medecin present immediatement — code ROUGE active'
    if temperature > 39.5:
        motif_triage = f'Temperature {temperature:.1f} C > seuil 39.5 C'
    elif spo2 < 90:
        motif_triage = f'Spo2 {spo2:.1f} % < seuil 90 %'
    else:
        motif_triage = f'Tension systolique {tension_syst} mmHg > seuil 180 mmHg'
# Niveau 2 : URGENT — conditions moins critiques mais toujours urgentes
elif temperature > 38.5 or spo2 < 94 or tension_syst > 140:
    niveau_triage  = '2 — URGENT'
    couleur_triage = '[ORANGE]'
    delai_pec      = '10 minutes'
    action_triage  = 'Appel medecin senior — code ORANGE active'
    if temperature > 38.5:
        motif_triage = f'Temperature {temperature:.1f} C > seuil 38.5 C'
    elif spo2 < 94:
        motif_triage = f'Spo2 {spo2:.1f} % < seuil 94 %'
    else:
        motif_triage = f'Tension systolique {tension_syst} mmHg > seuil 140 mmHg'
# Niveau 3 : URGENT DIFFERE
elif temperature > 37.5 or douleur > 6:
    niveau_triage  = '3 — URGENT DIFFERE'
    couleur_triage = '[JAUNE]'
    delai_pec      = '30 minutes'
    action_triage  = 'Infirmier-Surveillance — code JAUNE active'
    if temperature > 37.5:
        motif_triage = f'Temperature {temperature:.1f} C > seuil 37.5 C'
    else:
        motif_triage = f'Douleur {douleur}/10 > seuil 6/10'
# Niveau 4 : MOINS URGENT (cas par defaut)
else:
    niveau_triage  = '4 — MOINS URGENT'
    couleur_triage = '[VERT]'
    delai_pec      = '120 minutes'
    action_triage  = "File d'attente standard — code VERT active"
    motif_triage   = 'Aucun parametre alarmant — situation stable'
# Etat
etat_temp = "[ANORMAL]" if temperature > 37.5 else "[NORMAL]"
etat_spo2 = "[ANORMAL]" if spo2 < 94 else "[NORMAL]"
etat_tension = "[ANORMAL]" if tension_syst > 140 else "[NORMAL]"
etat_douleur = "[ANORMAL]" if douleur > 6 else "[NORMAL]"
# --- AFFICHAGE FICHE TRIAGE (S2 reutilise : f-strings) --
print()
print('=' * 55) 
print(f'  RESULTAT TRIAGE — {nom_patient.upper()}')
print('=' * 55)
# TODO : Afficher tous les parametres vitaux et le resultat du triage
print(f"PARAMETRES VITAUX")
print(f"Temperature : {temperature:.1f} C        {etat_temp}")
print(f"Saturation O2 : {spo2:.1f} %             {etat_spo2}")
print(f"Tension systol : {tension_syst} mmHg     {etat_tension}")
print(f"Douleur : {douleur}/10                   {etat_douleur}")
print()
print('-'*55)
print(f"NIVEAU DE TRIAGE : {niveau_triage}")
print(f"COULEUR : {couleur_triage}")
print(f"PRISE EN CHARGE : {delai_pec}")
print(f"ACTION : {action_triage}")
print('-'*55)
print(f"Motif principal : {motif_triage}")