# Generated by Django 4.2.2 on 2024-09-28 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_remove_reportform_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportform',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
