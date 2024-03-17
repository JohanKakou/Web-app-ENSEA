# Generated by Django 4.2 on 2024-03-17 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appartenance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_appartenance', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='EngagementExtraScolaire',
            fields=[
                ('id_engagement', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=100)),
                ('nom', models.CharField(max_length=100)),
                ('montant_cota', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='etudiant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('prenom', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('statut', models.CharField(choices=[('Etu', 'Etudiant simple'), ('Del', 'Delegue classe'), ('Ext', 'Responsable extrascolaire')], max_length=3)),
                ('sexe', models.CharField(choices=[('M', 'Masculin'), ('F', 'Feminin')], max_length=1)),
                ('nationalite', models.CharField(max_length=30)),
                ('numero_telephone', models.CharField(max_length=15)),
                ('afficher_numero', models.BooleanField(max_length=30)),
                ('anniversaire', models.DateField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Matiere',
            fields=[
                ('id_matiere', models.AutoField(primary_key=True, serialize=False)),
                ('nom_matiere', models.CharField(max_length=100)),
                ('nom_enseignant', models.CharField(max_length=100)),
                ('nb_heures', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Participation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statut', models.CharField(max_length=100)),
                ('cotisation_payee', models.BooleanField()),
                ('engagement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.engagementextrascolaire')),
                ('etudiant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.etudiant')),
            ],
            options={
                'unique_together': {('etudiant', 'engagement')},
            },
        ),
        migrations.CreateModel(
            name='Groupe',
            fields=[
                ('id_groupe', models.AutoField(primary_key=True, serialize=False)),
                ('nom_groupe', models.CharField(max_length=100)),
                ('description_groupe', models.TextField()),
                ('date_creation', models.DateField()),
                ('date_fermeture', models.DateField(blank=True, null=True)),
                ('etudiants', models.ManyToManyField(through='api.Appartenance', to='api.etudiant')),
            ],
        ),
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id_evaluation', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=100)),
                ('deadline', models.DateTimeField()),
                ('description', models.TextField()),
                ('matiere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='evaluations', to='api.matiere')),
            ],
        ),
        migrations.AddField(
            model_name='engagementextrascolaire',
            name='etudiants',
            field=models.ManyToManyField(through='api.Participation', to='api.etudiant'),
        ),
        migrations.CreateModel(
            name='Classe',
            fields=[
                ('nom_classe', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('etudiants', models.ManyToManyField(related_name='classes', to='api.etudiant')),
            ],
        ),
        migrations.AddField(
            model_name='appartenance',
            name='etudiant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.etudiant'),
        ),
        migrations.AddField(
            model_name='appartenance',
            name='groupe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.groupe'),
        ),
        migrations.AlterUniqueTogether(
            name='appartenance',
            unique_together={('etudiant', 'groupe')},
        ),
    ]
