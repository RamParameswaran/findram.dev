# Generated by Django 2.2.9 on 2020-01-11 04:27

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('frontend', '0002_homepage_banner_blurb'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('banner_title', wagtail.core.fields.RichTextField(blank=True)),
                ('banner_blurb', wagtail.core.fields.RichTextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='PostPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('body', wagtail.core.fields.RichTextField(blank=True)),
                ('created', models.DateTimeField(blank=True, editable=False, null=True)),
                ('modified', models.DateTimeField(blank=True, null=True)),
                ('author', models.CharField(blank=True, default='Ram Parameswaran', max_length=200, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='banner_avatar',
        ),
        migrations.AddField(
            model_name='portfolioitem',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='portfolioitem',
            name='in_progress',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='portfolioitem',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='portfolioitem',
            name='item_blogpost_link',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='portfolioitem',
            name='item_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AlterField(
            model_name='portfolioitem',
            name='item_link',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='portfolioitem',
            name='item_sourcecode_link',
            field=models.URLField(blank=True),
        ),
    ]
