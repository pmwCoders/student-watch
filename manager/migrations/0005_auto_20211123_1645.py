# Generated by Django 3.2.7 on 2021-11-23 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('manager', '0004_alter_presenca_estudante'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor_curso',
            name='curso',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='manager.curso'),
        ),
        migrations.AlterField(
            model_name='professor_curso',
            name='professor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.professorprofile'),
        ),
    ]
