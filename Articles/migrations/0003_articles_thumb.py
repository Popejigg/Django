# Generated by Django 3.2.5 on 2021-12-01 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Articles', '0002_articles_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='thumb',
            field=models.ImageField(blank=True, default='default.png', upload_to=''),
        ),
    ]
