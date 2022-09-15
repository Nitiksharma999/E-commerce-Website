# Generated by Django 3.2.15 on 2022-08-28 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20220826_2257'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('inputzip', models.CharField(max_length=10)),
            ],
        ),
    ]
