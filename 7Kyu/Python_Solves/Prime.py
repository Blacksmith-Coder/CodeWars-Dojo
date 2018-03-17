#                        _ _         _   _  _____ __  __   ______
#       /\              (_) |       | \ | |/ ____|  \/  | |____  |
#      /  \   __ _ _   _ _| | __ _  |  \| | |    | \  / |     / /
#     / /\ \ / _` | | | | | |/ _` | | . ` | |    | |\/| |    / /
#    / ____ \ (_| | |_| | | | (_| | | |\  | |____| |  | |   / /
#   /_/    \_\__, |\__,_|_|_|\__,_| |_| \_|\_____|_|  |_|  /_/
#               | |
#               |_| Blacksmith-Coder :: CopyLeft 2018 GNU GPL
#
# See ../../Licence.md or https://opensource.org/licenses/GPL-3.0

###################################
# calcul naif de nombres premiers #
###################################


def is_prime(n):
    if n < 7:
        if n in (2, 3, 5):
            return True
        else:
            return False
    # si n est pair et >2 (=2: cas traité ci-dessus), il ne peut pas être premier
    if n & 1 == 0:
        return False
    # autres cas
    k = 3
    r = lrac2(n)
    while k <= r:
        if n % k == 0:
            return False
        k += 2
    return True


def lrac2(n):
    """Racine carrée entière d'un nombre entier n de taille quelconque
           (méthode de Heron d'Alexandrie).
       Génère un exception "ValueError" si n est négatif.
    """
    #  traitement des cas particuliers
    if n < 2:
        if n < 0:
            raise ValueError("Erreur: racine carrée d'un nb négatif")
        else:
            return n  # ici, n = 0 ou 1

    # trouve une valeur approchée de la racine (important pour les grds nb)
    rac1, i = n, 0  # i = compteur du nb de positions binaires utilisées
    while rac1 != 0:
        rac1 >>= 1
        i += 1
    rac1 = 1 << (i >> 1)

    # calcule la racine en partant de la racine approchée rac1
    delta = n
    while True:
        rac2 = (rac1 + n // rac1) >> 1
        if delta <= 1 and rac2 >= rac1:
            return rac1
        delta = abs(rac2 - rac1)  # on garde pour la prochaine boucle
        rac1 = rac2


def premiers(n, p=[ 2, 3, 5]):
    """Retourne la liste des nombres premiers <= n (méthode=division)"""
    k = p[-1]+2
    if n < k:
        return [x for x in p if x <= n]
    while k <= n:
        i = 0
        while i < len(p):
            if p[i]*p[i] > k:
                p.append(k)
                break
            if (k % p[i]) == 0:
                break
            i += 1
        k += 2
    return p

