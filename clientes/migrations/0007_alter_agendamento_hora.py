# Generated by Django 4.0.1 on 2022-01-12 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0006_agendamento_hora'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agendamento',
            name='hora',
            field=models.CharField(choices=[('1º', '08:00 as 09:00'), ('2º', '09:00 as 10:00'), ('3º', '11:00 as 12:00'), ('4º', '12:00 as 13:00'), ('5º', '13:00 as 14:00'), ('6º', '14:00 as 15:00'), ('7º', '15:00 as 16:00'), ('8º', '16:00 as 17:00'), ('9º', '17:00 as 16:00'), ('10º', '17:00 as 18:00'), ('11º', '18:00 as 19:00'), ('12º', 'ESPECIAL')], default='', max_length=50),
            preserve_default=False,
        ),
    ]
