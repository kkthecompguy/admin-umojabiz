# Generated by Django 3.0.6 on 2020-06-03 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adverts', '0002_advert_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='advert',
            name='status',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
