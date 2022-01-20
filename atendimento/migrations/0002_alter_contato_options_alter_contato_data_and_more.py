# Generated by Django 4.0.1 on 2022-01-18 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atendimento', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contato',
            options={},
        ),
        migrations.AlterField(
            model_name='contato',
            name='data',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contato',
            name='horário',
            field=models.CharField(blank=True, choices=[('08:00 as 09:00', '08:00 as 09:00'), ('09:00 as 10:00', '09:00 as 10:00'), ('11:00 as 12:00', '11:00 as 12:00'), ('12:00 as 13:00', '12:00 as 13:00'), ('13:00 as 14:00', '13:00 as 14:00'), ('14:00 as 15:00', '14:00 as 15:00'), ('15:00 as 16:00', '15:00 as 16:00'), ('16:00 as 17:00', '16:00 as 17:00'), ('17:00 as 16:00', '17:00 as 16:00'), ('17:00 as 18:00', '17:00 as 18:00'), ('18:00 as 19:00', '18:00 as 19:00'), ('ESPECIAL', 'ESPECIAL')], max_length=50, null=True),
        ),
    ]