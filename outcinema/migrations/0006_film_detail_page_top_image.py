# Generated by Django 4.2.5 on 2023-12-07 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outcinema', '0005_film_start_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='detail_page_top_image',
            field=models.ImageField(default=False, upload_to='films'),
            preserve_default=False,
        ),
    ]