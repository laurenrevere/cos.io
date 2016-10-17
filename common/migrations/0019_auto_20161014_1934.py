# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-14 19:34
from __future__ import unicode_literals

import common.blocks.columns
import common.blocks.tabs
from django.db import migrations, models
import django.db.models.deletion
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailembeds.blocks
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0018_auto_20161014_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custompage',
            name='content',
            field=wagtail.wagtailcore.fields.StreamField((('appeal', wagtail.wagtailcore.blocks.StructBlock((('icon', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('none', 'none'), ('flask', 'flask'), ('group', 'group'), ('laptop', 'laptop'), ('sitemap', 'sitemap'), ('user', 'user'), ('book', 'book'), ('download', 'download')])), ('topic', wagtail.wagtailcore.blocks.CharBlock(max_length=35, required=True)), ('content', wagtail.wagtailcore.blocks.TextBlock(max_length=255, required=True))), classname='appeal', icon='tick', template='common/blocks/appeal.html')), ('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('statement', wagtail.wagtailcore.blocks.CharBlock()), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('imagechooser', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('column', common.blocks.columns.RowBlock()), ('tabbed_block', common.blocks.tabs.TabbedBlock()), ('image', wagtail.wagtailcore.blocks.StructBlock((('main_image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('style', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('max-width:225px;max-height:145px', 'Small'), ('max_width:250px;max-height:250px', 'Medium'), ('max_width:250px;max-height:250px;padding-top:20px', 'Medium Pushed Down 20px'), ('height:auto', 'Shrink to Fit')], default='height:auto')), ('url', wagtail.wagtailcore.blocks.CharBlock(max_length=250, required=False))))), ('rich_text', wagtail.wagtailcore.blocks.RichTextBlock()), ('raw_html', wagtail.wagtailcore.blocks.RawHTMLBlock(help_text='With great power comes great responsibility. This HTML is unescaped. Be careful!')), ('people_block', wagtail.wagtailcore.blocks.StructBlock((('displayStyle', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('concise-team', 'concise-team'), ('concise-ambassador', 'concise-ambassador'), ('detailed', 'detailed')], default='concise')), ('tag', wagtail.wagtailcore.blocks.CharBlock(max_length=20))))), ('centered_text', wagtail.wagtailcore.blocks.StructBlock((('text', wagtail.wagtailcore.blocks.RichTextBlock()),))), ('hero_block', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=True)), ('description', wagtail.wagtailcore.blocks.RichTextBlock(required=True))))), ('spotlight_block', wagtail.wagtailcore.blocks.StructBlock((('bubbles', wagtail.wagtailcore.blocks.StreamBlock((('bubble_block', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('title', wagtail.wagtailcore.blocks.CharBlock(max_length=35, required=True)), ('description', wagtail.wagtailcore.blocks.RichTextBlock(required=True))))),))),))), ('job_whole_block', wagtail.wagtailcore.blocks.StructBlock(())), ('embed_block', wagtail.wagtailembeds.blocks.EmbedBlock()), ('whitespaceblock', wagtail.wagtailcore.blocks.StructBlock((('height', wagtail.wagtailcore.blocks.IntegerBlock()),))), ('clear_fixblock', wagtail.wagtailcore.blocks.StructBlock(())), ('code_block', wagtail.wagtailcore.blocks.StructBlock((('language', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('python', 'python'), ('css', 'css'), ('sql', 'sql'), ('javascript', 'javascript'), ('clike', 'clike'), ('markup', 'markup'), ('java', 'java')], default='python')), ('codes', wagtail.wagtailcore.blocks.TextBlock())))), ('calender_blog', wagtail.wagtailcore.blocks.StructBlock((('source', wagtail.wagtailcore.blocks.CharBlock(help_text='Such as: calendar@cos.io', max_length=255, required=True)),)))), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='custompage',
            name='footer',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='common.Footer'),
        ),
        migrations.AlterField(
            model_name='newsarticle',
            name='footer',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='common.Footer'),
        ),
        migrations.AlterField(
            model_name='newsindexpage',
            name='footer',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='common.Footer'),
        ),
    ]
