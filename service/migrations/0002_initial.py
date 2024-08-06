# Generated by Django 5.0.2 on 2024-03-19 19:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('service', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='providerservice',
            name='address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.address'),
        ),
        migrations.AddField(
            model_name='providerservice',
            name='provider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user'),
        ),
        migrations.AddField(
            model_name='provideravailability',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.providerservice'),
        ),
        migrations.AddField(
            model_name='servicebooking',
            name='address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.address'),
        ),
        migrations.AddField(
            model_name='servicebooking',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.providerservice'),
        ),
        migrations.AddField(
            model_name='servicebooking',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user'),
        ),
        migrations.AddField(
            model_name='providerservice',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.servicecategory'),
        ),
        migrations.AddField(
            model_name='servicerating',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.servicebooking'),
        ),
    ]