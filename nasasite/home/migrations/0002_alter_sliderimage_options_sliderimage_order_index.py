# Generated by Django 5.0.6 on 2024-05-08 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sliderimage',
            options={'ordering': ['order_index'], 'verbose_name': 'Картинка слайдера', 'verbose_name_plural': 'Картинки слайдера'},
        ),
        migrations.AddField(
            model_name='sliderimage',
            name='order_index',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
