# Generated by Django 4.1.1 on 2022-10-18 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alokairu', '0002_kotxe_alokatua_alter_kotxe_bukaeradata_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kotxe',
            name='bukaeradata',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='kotxe',
            name='hasieradata',
            field=models.CharField(default='', max_length=255),
        ),
    ]
