# Generated by Django 4.1 on 2022-09-10 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nurse',
            name='doctor',
        ),
        migrations.AddField(
            model_name='doctor',
            name='nurse',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='app.nurse'),
            preserve_default=False,
        ),
    ]
