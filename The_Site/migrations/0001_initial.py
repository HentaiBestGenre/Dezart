# Generated by Django 4.0.4 on 2022-06-18 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlackList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=45)),
                ('time_for', models.DateTimeField(verbose_name='data published')),
            ],
        ),
    ]
