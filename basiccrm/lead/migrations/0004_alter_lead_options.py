# Generated by Django 4.1.7 on 2023-03-16 04:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0003_lead_team'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lead',
            options={'ordering': ('name',)},
        ),
    ]