# Generated by Django 4.0.1 on 2022-06-07 21:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Classe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('effectif_classe', models.IntegerField(verbose_name='Effectif')),
                ('date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Enseignant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricule', models.CharField(max_length=7, unique=True)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='enseignant', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Filiere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_filiere', models.CharField(max_length=30, unique=True)),
                ('date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Niveau',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_niveau', models.CharField(max_length=10, unique=True)),
                ('date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Salle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_salle', models.CharField(max_length=50, unique=True)),
                ('capacite_salle', models.IntegerField(verbose_name='capacite')),
                ('date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='UniteEnseignement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100, unique=True)),
                ('intitule', models.CharField(max_length=100, unique=True)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('classe', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='emploi.classe')),
                ('enseignant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='emploi.enseignant')),
            ],
        ),
        migrations.CreateModel(
            name='Specialite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_specialite', models.CharField(max_length=30, unique=True)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('classe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emploi.classe')),
            ],
        ),
        migrations.CreateModel(
            name='Cours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jour', models.CharField(choices=[('lundi', 'lundi'), ('mardi', 'mardi'), ('mercredi', 'mercredi'), ('jeudi', 'jeudi'), ('vendredi', 'vendredi'), ('samedi', 'samedi'), ('dimanche', 'dimanche')], max_length=20)),
                ('type', models.CharField(choices=[('CM', 'CM'), ('TD', 'TD')], max_length=20)),
                ('heure', models.CharField(max_length=12)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('groupe', multiselectfield.db.fields.MultiSelectField(choices=[('G1', 'G1'), ('G2', 'G2'), ('G3', 'G3'), ('G4', 'G4')], max_length=11)),
                ('salle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emploi.salle')),
                ('ue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emploi.uniteenseignement')),
            ],
        ),
        migrations.AddField(
            model_name='classe',
            name='filiere',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emploi.filiere'),
        ),
        migrations.AddField(
            model_name='classe',
            name='niveau',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emploi.niveau'),
        ),
    ]
