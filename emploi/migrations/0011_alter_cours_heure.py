# Generated by Django 4.0.4 on 2022-06-08 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emploi', '0010_alter_cours_groupe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cours',
            name='heure',
            field=models.CharField(choices=[('7h-9h55', '7h-9h55'), ('10h05-12h55', '10h05-12h55'), ('13h05-15h55', '13h05-15h55'), ('16h05-18h55', '16h05-18h55'), ('19h05-21h55', '19h05-21h55'), ('8h-10h', '8h-10h'), ('10h-12h', '10h-12h'), ('12h-14h', '12h-14h'), ('14h-16h', '14h-16h'), ('16h-18h', '16h-18h')], max_length=12),
        ),
    ]
