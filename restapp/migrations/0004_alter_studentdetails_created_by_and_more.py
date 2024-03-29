# Generated by Django 4.2.5 on 2023-12-19 14:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('restapp', '0003_alter_studentdetails_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdetails',
            name='created_by',
            field=models.ForeignKey(db_column='created_by', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='studentdetails',
            name='reference_id',
            field=models.CharField(default='30cd1d0b7d6443e68935498e4e377926', max_length=32, primary_key=True, serialize=False, unique=True),
        ),
    ]
