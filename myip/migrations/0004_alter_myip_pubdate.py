# Generated by Django 4.1.7 on 2023-05-13 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myip', '0003_alter_myip_pubdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myip',
            name='pubdate',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]