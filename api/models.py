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
    
class Matiere(models.Model):
    id_matiere = models.AutoField(primary_key=True)
    nom_matiere = models.CharField(max_length=100)
    nom_enseignant = models.CharField(max_length=100)
    nb_heures = models.IntegerField()


class Classe(models.Model):
    nom_classe = models.CharField(max_length=100, primary_key=True)
    etudiants = models.ManyToManyField(etudiant, related_name='classes')

class Evaluation(models.Model):
    id_evaluation = models.AutoField(primary_key=True)
    type = models.CharField(max_length=100)
    deadline = models.DateTimeField()
    description = models.TextField()
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE, related_name='evaluations')

class EngagementExtraScolaire(models.Model):
    id_engagement = models.AutoField(primary_key=True)
    type = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    montant_cota = models.DecimalField(max_digits=10, decimal_places=2)
    etudiants = models.ManyToManyField(etudiant, through='Participation')

class Groupe(models.Model):
    id_groupe = models.AutoField(primary_key=True)
    nom_groupe = models.CharField(max_length=100)
    description_groupe = models.TextField()
    date_creation = models.DateField()
    date_fermeture = models.DateField(null=True, blank=True)
    etudiants = models.ManyToManyField(etudiant, through='Appartenance')

class Participation(models.Model):
    etudiant = models.ForeignKey(etudiant, on_delete=models.CASCADE)
    engagement = models.ForeignKey(EngagementExtraScolaire, on_delete=models.CASCADE)
    statut = models.CharField(max_length=100)
    cotisation_payee = models.BooleanField()
    class Meta:
        unique_together = (('etudiant', 'engagement'),)

class Appartenance(models.Model):
    etudiant = models.ForeignKey(etudiant, on_delete=models.CASCADE)
    groupe = models.ForeignKey(Groupe, on_delete=models.CASCADE)
    date_appartenance = models.DateField(auto_now_add=True)
    class Meta:
        unique_together = (('etudiant', 'groupe'),)

