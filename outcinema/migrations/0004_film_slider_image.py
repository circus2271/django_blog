# Generated by Django 4.2.5 on 2023-12-07 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outcinema', '0003_homepageslider_slide_delete_filmphoto'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='slider_image',
            field=models.ImageField(default=False, upload_to='films'),
            preserve_default=False,
        ),
    ]
