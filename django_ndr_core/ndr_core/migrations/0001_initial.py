# Generated by Django 4.1.4 on 2022-12-30 23:48

import ckeditor_uploader.fields
import colorfield.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NdrCoreApiConfiguration',
            fields=[
                ('api_name', models.CharField(help_text="The (form) name of the API. Can't contain special characters or spaces.", max_length=100, primary_key=True, serialize=False, verbose_name='API Name')),
                ('api_host', models.CharField(help_text='The API host (domain only, e.g. my-api-host.org)', max_length=100, verbose_name='API Host')),
                ('api_protocol', models.PositiveSmallIntegerField(choices=[(1, 'http'), (2, 'https')], default=2, help_text='The protocol used (http or https)', verbose_name='Protocol')),
                ('api_port', models.IntegerField(default=80, help_text='Port to connect to.', verbose_name='Port')),
                ('api_label', models.CharField(help_text="The API's label is the title of the queried repository. Choose a short descriptive title.", max_length=250, verbose_name='Displayable Label')),
                ('api_description', models.TextField(default='', help_text='Description of this configuration', verbose_name='Description')),
                ('api_page_size', models.IntegerField(default=10, help_text="Size of the result page (e.g. 'How many results at once')", verbose_name='Page Size')),
                ('api_url_stub', models.CharField(blank=True, default=None, help_text='Static URL part after host, before API parameters.', max_length=50, null=True, verbose_name='URL stub')),
                ('api_user_name', models.CharField(blank=True, default='', max_length=50)),
                ('api_password', models.CharField(blank=True, default='', max_length=50)),
                ('api_auth_key', models.CharField(blank=True, default='', max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='NdrCoreApiImplementation',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('label', models.CharField(max_length=100, unique=True)),
                ('url', models.URLField(blank='True', null=True)),
                ('description', models.TextField(default='blank')),
                ('supports_simple', models.BooleanField(default=True)),
                ('supports_simple_and_or', models.BooleanField(default=True)),
                ('supports_advanced', models.BooleanField(default=True)),
                ('supports_lists', models.BooleanField(default=True)),
                ('supports_facets', models.BooleanField(default=False)),
                ('supports_single_result', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='NdrCoreColorScheme',
            fields=[
                ('scheme_name', models.CharField(help_text='This name is used for export reference and as css file name. No spaces and no special characters but underscores.', max_length=50, primary_key=True, serialize=False)),
                ('scheme_label', models.CharField(help_text='Human readable label of the scheme. Make it descriptive.', max_length=100)),
                ('background_color', colorfield.fields.ColorField(default='#FFFFFF', help_text='Basic background color of the whole page.', image_field=None, max_length=18, samples=None)),
                ('text_color', colorfield.fields.ColorField(default='#FFFFFF', help_text='Basic text color for the whole page.', image_field=None, max_length=18, samples=None)),
                ('button_color', colorfield.fields.ColorField(default='#FFFFFF', help_text='Background color of primary buttons.', image_field=None, max_length=18, samples=None)),
                ('button_hover_color', colorfield.fields.ColorField(default='#FFFFFF', help_text='Hover color of primary buttons.', image_field=None, max_length=18, samples=None)),
                ('button_text_color', colorfield.fields.ColorField(default='#FFFFFF', help_text='Text color of primary buttons.', image_field=None, max_length=18, samples=None)),
                ('button_border_color', colorfield.fields.ColorField(default='#FFFFFF', help_text='Border color of primary buttons.', image_field=None, max_length=18, samples=None)),
                ('second_button_color', colorfield.fields.ColorField(default='#FFFFFF', help_text='Background color of secondary buttons.', image_field=None, max_length=18, samples=None)),
                ('second_button_hover_color', colorfield.fields.ColorField(default='#FFFFFF', help_text='Hover color of secondary buttons.', image_field=None, max_length=18, samples=None)),
                ('second_button_text_color', colorfield.fields.ColorField(default='#FFFFFF', help_text='Text color of secondary buttons.', image_field=None, max_length=18, samples=None)),
                ('second_button_border_color', colorfield.fields.ColorField(default='#FFFFFF', help_text='Border color of secondary buttons.', image_field=None, max_length=18, samples=None)),
                ('link_color', colorfield.fields.ColorField(default='#FFFFFF', help_text='Color for links.', image_field=None, max_length=18, samples=None)),
                ('accent_color_1', colorfield.fields.ColorField(default='#FFFFFF', help_text='Accent color 1. Used as navigation background and the like.', image_field=None, max_length=18, samples=None)),
                ('accent_color_2', colorfield.fields.ColorField(default='#FFFFFF', help_text='Accent color 2. Used as element background and the like.', image_field=None, max_length=18, samples=None)),
                ('info_color', colorfield.fields.ColorField(default='#FFFFFF', help_text='Info color for alerts.', image_field=None, max_length=18, samples=None)),
                ('success_color', colorfield.fields.ColorField(default='#FFFFFF', help_text='Success color for alerts.', image_field=None, max_length=18, samples=None)),
                ('error_color', colorfield.fields.ColorField(default='#FFFFFF', help_text='Error color for alerts.', image_field=None, max_length=18, samples=None)),
            ],
        ),
        migrations.CreateModel(
            name='NdrCoreDataSchema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schema_url', models.URLField()),
                ('schema_label', models.CharField(max_length=100)),
                ('schema_name', models.CharField(max_length=100)),
                ('fixture_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='NdrCoreFilterableListConfiguration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_name', models.CharField(max_length=100, unique=True)),
                ('api_configuration', models.ForeignKey(help_text='TODO', on_delete=django.db.models.deletion.CASCADE, to='ndr_core.ndrcoreapiconfiguration')),
            ],
        ),
        migrations.CreateModel(
            name='NdrCoreImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='', help_text='Title of the image.', max_length=200)),
                ('caption', models.CharField(blank=True, default='', help_text='Caption of the image.', max_length=200)),
                ('citation', models.CharField(blank=True, default='', help_text='Citation text of the image.', max_length=200)),
                ('url', models.URLField(blank=True, default=None, help_text='URL to image or source', null=True)),
                ('image', models.ImageField(help_text='TODO', upload_to='images')),
                ('image_group', models.CharField(choices=[('backgrounds', 'Background Images'), ('elements', 'Slideshow Images'), ('figures', 'Figures'), ('logos', 'Partner Images'), ('people', 'People')], max_length=100)),
                ('index_in_group', models.IntegerField(default=0)),
                ('image_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='NdrCoreResultTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='NdrCoreSearchField',
            fields=[
                ('field_name', models.CharField(help_text="Choose a name for the field. Can't contain spaces or special charactersand must be unique", max_length=100, primary_key=True, serialize=False)),
                ('field_label', models.CharField(help_text="This is the form field's label", max_length=100)),
                ('field_type', models.PositiveSmallIntegerField(choices=[(1, 'String'), (2, 'Number'), (3, 'Dictionary')], default=1, help_text='Type of the form field. String produces a text field, Number a number field and dictionary a dropdown.')),
                ('field_required', models.BooleanField(default=False, help_text='Does this field need to be filled out?')),
                ('help_text', models.CharField(blank=True, default='', help_text='The help text which will be displayed in the form', max_length=250)),
                ('api_parameter', models.CharField(blank=True, default='', help_text='The name of the API parameter which is used to generate a query', max_length=100)),
                ('schema_name', models.CharField(help_text='Name of the schema this search_field is created from', max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='NdrCoreUIElement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('card', 'Card'), ('slides', 'Slideshow'), ('carousel', 'Carousel'), ('jumbotron', 'Jumbotron')], max_length=100)),
                ('title', models.CharField(help_text='Title of the element for your reference.', max_length=100)),
                ('use_image_conf', models.BooleanField(default=True, help_text="Use the image's title, caption and URL?")),
                ('show_indicators', models.BooleanField(default=True, help_text='Show the indicators for slideshows and carousels?')),
                ('show_title', models.BooleanField(default=True, help_text='Show the title?')),
                ('show_text', models.BooleanField(default=True, help_text="Show the element's text?")),
                ('show_image', models.BooleanField(default=True, help_text='Show the images?')),
                ('link_element', models.BooleanField(default=True, help_text='Link the elements to the supplied url?')),
                ('autoplay', models.BooleanField(default=False, help_text='Autoplay carousels and slideshows?')),
            ],
        ),
        migrations.CreateModel(
            name='NdrCoreUiStyle',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('label', models.CharField(max_length=100)),
                ('filename', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='NdrCoreUserMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_subject', models.CharField(max_length=200)),
                ('message_text', models.TextField()),
                ('message_time', models.DateTimeField(auto_now_add=True)),
                ('message_ret_email', models.EmailField(max_length=254)),
                ('message_archived', models.BooleanField(default=False)),
                ('message_forwarded', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='NdrCoreValue',
            fields=[
                ('value_name', models.CharField(help_text="This is the identifier of a NdrCoreValue. Can't contain special characters.", max_length=100, primary_key=True, serialize=False)),
                ('value_type', models.CharField(choices=[('string', 'String'), ('integer', 'Integer'), ('boolean', 'Boolean'), ('list', 'List'), ('url', 'URL')], default='string', help_text='The type of your value', max_length=10)),
                ('value_label', models.CharField(help_text='This is a human readable label for the value. It is used in the admin view forms.', max_length=100)),
                ('value_help_text', models.CharField(help_text='This is the help text of the form field.', max_length=250)),
                ('value_value', models.CharField(help_text='This is the actual value which can be updated', max_length=100)),
                ('value_options', models.CharField(default='', help_text='Used for value_type LIST: comma-separated list', max_length=200)),
                ('is_user_value', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='NdrCoreUiElementItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_idx', models.IntegerField()),
                ('title', models.CharField(blank=True, max_length=100)),
                ('text', models.TextField(blank=True)),
                ('url', models.URLField(blank=True)),
                ('belongs_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ndr_core.ndrcoreuielement')),
                ('ndr_image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ndr_core.ndrcoreimage')),
            ],
        ),
        migrations.CreateModel(
            name='NdrCoreSearchStatisticEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search_term', models.CharField(max_length=100)),
                ('search_time', models.DateTimeField(auto_now_add=True)),
                ('search_location', models.CharField(max_length=20, null=True)),
                ('search_api', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ndr_core.ndrcoreapiconfiguration')),
            ],
        ),
        migrations.CreateModel(
            name='NdrCoreSearchFieldFormConfiguration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_row', models.IntegerField(help_text='The row in the form. Starts with 1.', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(20)])),
                ('field_column', models.IntegerField(help_text='The column in the form. Is a value between 1 and 12.', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)])),
                ('field_size', models.IntegerField(help_text='The size of the field. Is a value between 1 and 12.', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)])),
                ('search_field', models.ForeignKey(help_text='The search field to place in a form', on_delete=django.db.models.deletion.CASCADE, to='ndr_core.ndrcoresearchfield')),
            ],
        ),
        migrations.CreateModel(
            name='NdrCoreSearchConfiguration',
            fields=[
                ('conf_name', models.CharField(help_text="Name of this search configuration. Can't contain spaces or special characters.", max_length=100, primary_key=True, serialize=False)),
                ('conf_label', models.CharField(help_text='Label of this search configuration', max_length=100, unique=True)),
                ('api_configuration', models.ForeignKey(help_text='The API to query', on_delete=django.db.models.deletion.CASCADE, to='ndr_core.ndrcoreapiconfiguration')),
                ('search_form_fields', models.ManyToManyField(help_text='Fields associated with this configuration', to='ndr_core.ndrcoresearchfieldformconfiguration')),
            ],
        ),
        migrations.CreateModel(
            name='NdrCoreResultTemplateField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target_field_name', models.CharField(max_length=100)),
                ('source_field_name', models.CharField(max_length=100)),
                ('alternate_field_name', models.CharField(blank=True, max_length=100, null=True)),
                ('field_none_value', models.CharField(default='', max_length=100)),
                ('field_label', models.CharField(blank=True, max_length=100, null=True)),
                ('field_container', models.CharField(choices=[('options', 'Options'), ('values', 'Value List')], max_length=100)),
                ('field_renderer', models.IntegerField(blank=True, choices=[(1, 'url-link'), (2, 'geonames.org')], null=True)),
                ('belongs_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ndr_core.ndrcoresearchconfiguration')),
            ],
        ),
        migrations.CreateModel(
            name='NdrCorePage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('view_name', models.CharField(help_text='The url part of your page (e.g. https://yourdomain.org/p/view_name)', max_length=200, unique=True)),
                ('page_type', models.IntegerField(choices=[(1, 'Template Page'), (2, 'Simple Search'), (3, 'Custom Search'), (4, 'Simple/Custom Search'), (5, 'Contact Form'), (6, 'Filterable List'), (7, 'Flip Book'), (8, 'About Us Page')], default=1, help_text='Choose a type for your page. Template is a static page, search pagesdisplay search forms, a filtered list displays data resources with afilter, contact form displays a form to send a message.')),
                ('name', models.CharField(help_text="The name of the page, e.g. the page's title", max_length=200, verbose_name='Page Title')),
                ('label', models.CharField(help_text="The label of the page, e.g. the page's navigation label", max_length=200)),
                ('nav_icon', models.CharField(blank=True, help_text='The fontawesome nav icon (leave blank if none)', max_length=200)),
                ('index', models.IntegerField(default=0, help_text='Page order')),
                ('template_text', ckeditor_uploader.fields.RichTextUploadingField(blank=True, help_text='Text for your template page', null=True)),
                ('list_configs', models.ManyToManyField(to='ndr_core.ndrcorefilterablelistconfiguration')),
                ('parent_page', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ndr_core.ndrcorepage')),
                ('search_configs', models.ManyToManyField(to='ndr_core.ndrcoresearchconfiguration')),
                ('simple_api', models.ForeignKey(blank=True, help_text='Api for simple search', null=True, on_delete=django.db.models.deletion.SET_NULL, to='ndr_core.ndrcoreapiconfiguration')),
            ],
        ),
        migrations.CreateModel(
            name='NdrCoreCorrection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('corrected_record_id', models.CharField(max_length=255)),
                ('corrector_orcid', models.CharField(max_length=50)),
                ('corrected_dataset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ndr_core.ndrcoreapiconfiguration')),
            ],
        ),
        migrations.CreateModel(
            name='NdrCoreCorrectedField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_name', models.CharField(max_length=100)),
                ('old_value', models.TextField()),
                ('new_value', models.TextField()),
                ('ndr_correction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ndr_core.ndrcorecorrection')),
            ],
        ),
        migrations.AddField(
            model_name='ndrcoreapiconfiguration',
            name='api_type',
            field=models.ForeignKey(help_text='Choose the API implementation of your configuration.', on_delete=django.db.models.deletion.CASCADE, to='ndr_core.ndrcoreapiimplementation', verbose_name='API Type'),
        ),
    ]
