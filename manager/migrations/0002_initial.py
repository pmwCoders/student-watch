# Generated by Django 3.2.7 on 2021-11-20 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('manager', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='professor_curso',
            name='professor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='users.professorprofile'),
        ),
        migrations.AddField(
            model_name='presenca',
            name='aula',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='manager.aula'),
        ),
        migrations.AddField(
            model_name='presenca',
            name='estudante',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='users.estudanteprofile'),
        ),
        migrations.AddField(
            model_name='disciplina',
            name='curso',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='manager.curso'),
        ),
        migrations.AddField(
            model_name='disciplina',
            name='professor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='users.professorprofile'),
        ),
        migrations.AddField(
            model_name='curso',
            name='coordenador',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='users.coordenadorprofile'),
        ),
        migrations.AddField(
            model_name='coordenador_curso',
            name='coordenador',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='users.coordenadorprofile'),
        ),
        migrations.AddField(
            model_name='coordenador_curso',
            name='curso',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='manager.curso'),
        ),
        migrations.AddField(
            model_name='aula',
            name='dia_semana',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='manager.dia_semana'),
        ),
        migrations.AddField(
            model_name='aula',
            name='disciplina',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='manager.disciplina'),
        ),
        migrations.AddField(
            model_name='aula',
            name='turno',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='manager.turno'),
        ),
    ]
