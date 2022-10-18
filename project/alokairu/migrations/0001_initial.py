# Generated by Django 4.1.1 on 2022-10-18 07:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pertsona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Kotxe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hasieradata', models.CharField(max_length=255)),
                ('bukaeradata', models.CharField(max_length=255)),
                ('pertsona', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='alokairu.pertsona')),
            ],
        ),
    ]