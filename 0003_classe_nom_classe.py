# Generated by Django 4.0.4 on 2022-06-09 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emploi', '0002_alter_cours_jour'),
    ]

    operations = [
        migrations.AddField(
            model_name='classe',
            name='nom_classe',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
