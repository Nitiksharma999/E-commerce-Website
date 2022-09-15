# Generated by Django 3.2.15 on 2022-08-31 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20220829_2200'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderUdate',
            fields=[
                ('update_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_id', models.IntegerField(default='')),
                ('update_desc', models.CharField(max_length=2000)),
                ('timestamp', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
