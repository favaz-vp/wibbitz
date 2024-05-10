# Generated by Django 5.0.3 on 2024-04-04 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_feature'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoBlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='VideoBlog/image/')),
                ('title', models.CharField(max_length=128)),
                ('logo', models.FileField(upload_to='VideoBlog/logo/')),
            ],
        ),
    ]
