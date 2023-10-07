# Generated by Django 4.2.3 on 2023-09-28 20:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0003_alter_customuser_user_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='birth_date',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='email',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='user_type',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
