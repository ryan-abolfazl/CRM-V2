# Generated by Django 5.0.7 on 2024-07-23 19:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0002_agent_lead_userprofile_delete_leads_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='leads.userprofile'),
        ),
    ]
