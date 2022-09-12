# Generated by Django 4.1 on 2022-09-12 07:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_doctor_direction_alter_hospital_region_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='siniordoctor',
            name='doctor',
        ),
        migrations.AddField(
            model_name='hospital',
            name='sinior_doctor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='app.siniordoctor'),
            preserve_default=False,
        ),
    ]