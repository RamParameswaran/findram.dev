# Generated by Django 2.2.9 on 2022-02-21 03:36

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0008_auto_20220221_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postpage',
            name='body',
            field=wagtail.core.fields.StreamField([('rich_text', wagtail.core.blocks.RichTextBlock(features=['h4', 'bold', 'italic', 'underline', 'ol', 'ul', 'hr', 'link', 'document-link', 'image', 'embed', 'code', 'blockquote'])), ('code', wagtail.core.blocks.StructBlock([('language', wagtail.core.blocks.ChoiceBlock(choices=[('python', 'python'), ('javascript', 'javascript'), ('css', 'css'), ('markup', 'markup'), ('html', 'html'), ('go', 'go'), ('bash', 'bash')])), ('text', wagtail.core.blocks.TextBlock())], label='Code'))]),
        ),
    ]
