# Generated by Django 5.0.1 on 2024-02-12 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dweetapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dweet',
            options={'ordering': ['-modified', '-created']},
        ),
        migrations.AddField(
            model_name='dweet',
            name='like',
            field=models.BooleanField(default=False),
        ),
    ]