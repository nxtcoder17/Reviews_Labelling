# Generated by Django 2.2.3 on 2019-08-28 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_text', models.CharField(max_length=10000)),
                ('sentiment', models.IntegerField(default=100)),
            ],
        ),
    ]