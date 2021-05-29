# Generated by Django 3.1.1 on 2021-05-29 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20210529_2139'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(default='No descrition', max_length=200),
        ),
        migrations.AddField(
            model_name='post',
            name='content',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='excerpt',
            field=models.TextField(default='No excert available', max_length=200),
        ),
    ]
