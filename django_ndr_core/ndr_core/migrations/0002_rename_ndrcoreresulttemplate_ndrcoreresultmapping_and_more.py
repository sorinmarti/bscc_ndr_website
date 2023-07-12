# Generated by Django 4.1.4 on 2023-01-05 15:03

import colorfield.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ndr_core', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='NdrCoreResultTemplate',
            new_name='NdrCoreResultMapping',
        ),
        migrations.AddField(
            model_name='ndrcorecolorscheme',
            name='container_bg_color',
            field=colorfield.fields.ColorField(default='#FFFFFF', help_text='Basic container (cards, tables, etc.) color of the whole page.', image_field=None, max_length=18, samples=None),
        ),
        migrations.AddField(
            model_name='ndrcorecolorscheme',
            name='footer_bg',
            field=colorfield.fields.ColorField(default='#FFFFFF', image_field=None, max_length=18, samples=None),
        ),
        migrations.AddField(
            model_name='ndrcorecolorscheme',
            name='form_field_bg',
            field=colorfield.fields.ColorField(default='#FFFFFF', image_field=None, max_length=18, samples=None),
        ),
        migrations.AddField(
            model_name='ndrcorecolorscheme',
            name='form_field_fg',
            field=colorfield.fields.ColorField(default='#FFFFFF', image_field=None, max_length=18, samples=None),
        ),
        migrations.AddField(
            model_name='ndrcorecolorscheme',
            name='title_color',
            field=colorfield.fields.ColorField(default='#FFFFFF', help_text='Title text color for the whole page.', image_field=None, max_length=18, samples=None),
        ),
        migrations.AlterField(
            model_name='ndrcoreapiconfiguration',
            name='api_auth_key',
            field=models.CharField(blank=True, default='', help_text='If the API needs user authentication, you can provide an authentication key', max_length=512),
        ),
        migrations.AlterField(
            model_name='ndrcoreapiconfiguration',
            name='api_password',
            field=models.CharField(blank=True, default='', help_text='If the API needs user authentication, you can provide the password', max_length=50),
        ),
        migrations.AlterField(
            model_name='ndrcoreapiconfiguration',
            name='api_user_name',
            field=models.CharField(blank=True, default='', help_text='If the API needs user authentication, you can provide your username', max_length=50),
        ),
        migrations.AlterField(
            model_name='ndrcoreimage',
            name='image',
            field=models.ImageField(help_text='Upload an image file', upload_to='images'),
        ),
        migrations.AlterField(
            model_name='ndrcorepage',
            name='page_type',
            field=models.IntegerField(choices=[(1, 'Template Page'), (2, 'Simple Search'), (3, 'Custom Search'), (4, 'Simple/Custom Search'), (5, 'Contact Form'), (6, 'Filterable List'), (7, 'Flip Book'), (8, 'About Us Page')], default=1, help_text='Choose a type for your page.'),
        ),
        migrations.AlterField(
            model_name='ndrcorepage',
            name='parent_page',
            field=models.ForeignKey(blank=True, default=None, help_text='If you want this page to be a sub-page of another one, you canchoose the parent page here', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ndr_core.ndrcorepage'),
        ),
        migrations.AlterField(
            model_name='ndrcoreuielement',
            name='type',
            field=models.CharField(choices=[('card', 'Card'), ('slides', 'Slideshow'), ('carousel', 'Carousel'), ('jumbotron', 'Jumbotron'), ('iframe', 'IFrame')], max_length=100),
        ),
    ]
