# Generated by Django 4.2.5 on 2023-09-23 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_article_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='published',
            field=models.BooleanField(default=False),
        ),
    ]
