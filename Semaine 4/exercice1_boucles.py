# ============================================================
# RAPPORT NATIONAL MPOX 2025 - SUIVI PAR DISTRICT
# ============================================================

# Compteurs nationaux 
total_suspects  = 0
total_confirmes = 0
total_deces     = 0
total_actifs    = 0

# Compteurs de zones d'alerte 
zones_vertes    = 0
zones_jaunes    = 0
zones_oranges   = 0
zones_rouges    = 0

# Nombre total de districts a analyser
nb_districts    = 9

# Boucle : on traite chaque district un par un (de 1 a 9 inclus)
for i in range(1, nb_districts + 1):
    print('--- District', i, '---')

    # --- Saisie des donnees du district ---
    nom_district = input('Nom du district  : ')
    suspects     = int(input('Cas suspects     : '))
    confirmes    = int(input('Cas confirmes    : '))
    deces        = int(input('Deces            : '))

    # TODO 1 : Cas actifs = cas confirmes qui ne sont pas (encore) decedes
    cas_actifs = confirmes - deces

    # TODO 2 : Taux de letalite = pourcentage de deces parmi les cas confirmes
    # On verifie d'abord que confirmes > 0 pour eviter une division par zero
    if confirmes > 0:
        letalite = (deces / confirmes) * 100
    else:
        letalite = 0

    #  Classification du niveau d'alerte selon le nombre de cas confirmes 
    if confirmes >= 10:
        alerte = 'ROUGE'
        # TODO 3 : on incremente le compteur de zones rouges pour ce district
        zones_rouges = zones_rouges + 1
    elif confirmes >= 5:
        alerte = 'ORANGE'
        # TODO 4 : on incremente le compteur de zones oranges
        zones_oranges = zones_oranges + 1
    elif confirmes >= 2:
        alerte = 'JAUNE'
        # TODO 5 : on incremente le compteur de zones jaunes
        zones_jaunes = zones_jaunes + 1
    else:
        alerte = 'VERT'
        zones_vertes = zones_vertes + 1

    # Mise a jour des totaux nationaux (on cumule a chaque tour de boucle) 
    total_suspects  = total_suspects  + suspects

    # TODO 6 : on ajoute les cas confirmes de ce district au total national
    total_confirmes = total_confirmes + confirmes

    # TODO 7 : on ajoute les deces de ce district au total national
    total_deces     = total_deces + deces

    # TODO 8 : on ajoute les cas actifs de ce district au total national
    total_actifs    = total_actifs + cas_actifs

    #  Affichage du resume de ce district 
    print('  Alerte   :', alerte)
    print('  Actifs   :', cas_actifs)
    print('  Letalite :', round(letalite, 1), '%')
    print()

# RAPPORT FINAL - SYNTHESE NATIONALE 
print('=======================================')
print('      RAPPORT NATIONAL MPOX 2025       ')
print('=======================================')
print('Districts analyses   :', nb_districts)
print('Total suspects       :', total_suspects)
print('Total confirmes      :', total_confirmes)
print('Total deces          :', total_deces)
print('Total cas actifs     :', total_actifs)
print('Zones VERTES         :', zones_vertes)
print('Zones JAUNES         :', zones_jaunes)
print('Zones ORANGES        :', zones_oranges)
print('Zones ROUGES         :', zones_rouges)
print('=======================================')