# Generated by Django 2.2.9 on 2020-01-25 21:06

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0005_auto_20200111_1606'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='postpage',
            options={},
        ),
        migrations.AddField(
            model_name='postpage',
            name='blurb',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
    ]
