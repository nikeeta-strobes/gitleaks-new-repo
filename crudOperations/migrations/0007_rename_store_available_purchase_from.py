# Generated by Django 3.2.5 on 2021-08-10 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crudOperations', '0006_customer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='available',
            old_name='store',
            new_name='purchase_from',
        ),
    ]