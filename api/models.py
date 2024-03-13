from django.db import models

# Create your models here.
class etudiant(models.Model):
    SEXES = [
        ("M", "Masculin"),
        ("F", "Feminin")
    ]
    STATUTS = [
        ("Etu","Etudiant simple"),
        ("Del", "Delegue classe"),
        ("Ext","Responsable extrascolaire")
    ]
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    statut = models.CharField(max_length=3,choices=STATUTS)
    sexe = models.CharField(max_length=1,choices=SEXES)
    nationalite = models.CharField(max_length=30)
    numero_telephone = models.CharField(max_length=15)
    afficher_numero = models.BooleanField(max_length=30)
    anniversaire = models.DateField(max_length=30)
    #