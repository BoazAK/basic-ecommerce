# Generated by Django 3.2 on 2021-04-18 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(max_length=100)),
                ('contact_email', models.EmailField(max_length=254)),
                ('contact_num', models.CharField(max_length=25, verbose_name='contact number')),
                ('contact_body', models.TextField()),
                ('contact_pub_date', models.DateTimeField(auto_now_add=True, verbose_name='publication date')),
                ('contact_readed', models.BooleanField(default=False, verbose_name='read statut')),
                ('contact_answered', models.BooleanField(default=False, verbose_name='answer statut')),
            ],
        ),
    ]
