# Generated by Django 4.0.1 on 2022-06-07 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emploi', '0003_remove_cours_classe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cours',
            name='groupe',
            field=models.IntegerField(),
        ),
    ]
