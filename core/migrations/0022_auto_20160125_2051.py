# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0023_alter_page_revision_on_delete_behaviour'),
        ('wagtailimages', '0010_change_on_delete_behaviour'),
        ('core', '0021_auto_20160118_2144'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailFormField',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sort_order', models.IntegerField(null=True, editable=False, blank=True)),
                ('label', models.CharField(help_text='The label of the form field', max_length=255, verbose_name='label')),
                ('field_type', models.CharField(max_length=16, verbose_name='field type', choices=[('singleline', 'Single line text'), ('multiline', 'Multi-line text'), ('email', 'Email'), ('number', 'Number'), ('url', 'URL'), ('checkbox', 'Checkbox'), ('checkboxes', 'Checkboxes'), ('dropdown', 'Drop down'), ('radio', 'Radio buttons'), ('date', 'Date'), ('datetime', 'Date/time')])),
                ('required', models.BooleanField(default=True, verbose_name='required')),
                ('choices', models.CharField(help_text='Comma separated list of choices. Only applicable in checkboxes, radio and dropdown.', max_length=512, verbose_name='choices', blank=True)),
                ('default_value', models.CharField(help_text='Default value. Comma separated values supported for checkboxes.', max_length=255, verbose_name='default value', blank=True)),
                ('help_text', models.CharField(max_length=255, verbose_name='help text', blank=True)),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EmailFormPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('to_address', models.CharField(help_text='Optional - form submissions will be emailed to this address', max_length=255, verbose_name='to address', blank=True)),
                ('from_address', models.CharField(max_length=255, verbose_name='from address', blank=True)),
                ('subject', models.CharField(max_length=255, verbose_name='subject', blank=True)),
                ('intro', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('thank_you_text', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('banner_image', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtailimages.Image', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AlterField(
            model_name='aboutpage',
            name='banner_image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtailimages.Image', null=True),
        ),
        migrations.AlterField(
            model_name='blogindexpage',
            name='banner_image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtailimages.Image', null=True),
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='banner_image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtailimages.Image', null=True),
        ),
        migrations.AlterField(
            model_name='simplepage',
            name='banner_image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtailimages.Image', null=True),
        ),
        migrations.AlterField(
            model_name='workpage',
            name='screenshot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtailimages.Image', null=True),
        ),
        migrations.AddField(
            model_name='emailformfield',
            name='page',
            field=modelcluster.fields.ParentalKey(related_name='form_fields', to='core.EmailFormPage'),
        ),
    ]
