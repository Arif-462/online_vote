# Generated by Django 4.2.3 on 2023-10-06 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0006_alter_candidate_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='bio',
            field=models.TextField(max_length=50),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='fullname',
            field=models.CharField(max_length=20),
        ),
    ]
