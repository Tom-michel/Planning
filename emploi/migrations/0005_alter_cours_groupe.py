# Generated by Django 4.0.1 on 2022-06-07 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emploi', '0004_alter_cours_groupe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cours',
            name='groupe',
            field=models.IntegerField(default=1),
        ),
    ]