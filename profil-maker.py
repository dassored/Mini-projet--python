def creer_profil():
    prenom = input("Entrez le prénom : ")
    nom = input("Entrez le nom : ")
    age = input("Entrez l'âge : ")
    telephone = input("Entrez le numéro de téléphone : ")
    email = input("Entrez l'adresse email : ")
    registre_national = input("Entrez le registre national : ")
    commentaire = input("Entrez un commentaire : ")
    return (prenom, nom, age, telephone, email, registre_national, commentaire)

# Demander à l'utilisateur de saisir un nom de fichier pour enregistrer le profil
nom_fichier = input("Entrez un nom de fichier pour enregistrer le profil : ")

# Créer le profil
profil = creer_profil()

# Écrire les informations du profil dans le fichier
with open(nom_fichier, 'w') as fichier:
    fichier.write("Prénom : " + profil[0] + "\n")
    fichier.write("Nom : " + profil[1] + "\n")
    fichier.write("Âge : " + profil[2] + "\n")
    fichier.write("Numéro de téléphone : " + profil[3] + "\n")
    fichier.write("Email : " + profil[4] + "\n")
    fichier.write("Registre national : " + profil[5] + "\n")
    fichier.write("Commentaire : " + profil[6] + "\n")

print("Le profil a été enregistré avec succès dans le fichier texte !")
