from __future__ import unicode_literals

from django.utils.text import slugify
from django.db import migrations, models
import django.db.models.deletion
import wagtail.wagtailcore.fields


def migrate_data(apps, schema_editor):
    AboutPage = apps.get_model('core', 'AboutPage')
    AuthorPage = apps.get_model('core', 'AuthorPage')
    BlogPage = apps.get_model("core", "BlogPage")
    AuthorProfile = apps.get_model("core", "AuthorProfile")
    try:
        about_page = AboutPage.objects.get()
    except (AboutPage.DoesNotExist, AboutPage.MultipleObjectsReturned):
        # we can only programmatically migrate this data if there is
        # exactly one about page
        return

    for snippet in AuthorProfile.objects.all():
        page = AuthorPage(name=snippet.name,
                          title=snippet.name,
                          slug=slugify(snippet.name),
                          picture_id=snippet.picture.pk,
                          bio=snippet.bio,
                          is_member=snippet.is_member,
                          twitter_username=snippet.twitter_username,
                          github_username=snippet.github_username)
        about_page.add_child(instance=page)
        BlogPage.objects.filter(author_old=snippet).update(author=page)


class Migration(migrations.Migration):

    # Not sure what the dependency should be for this...
    # Probably fill in with the last most recent migration file?
    dependencies = [
        ('core', '0045_auto_20160519_2307'),
    ]

    operations = [
        # Creates the AuthorPage in the database
        migrations.CreateModel(
            name='AuthorPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('name', models.CharField(max_length=100)),
                ('bio', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('is_member', models.BooleanField(default=False)),
                ('twitter_username', models.CharField(blank=True, max_length=15)),
                ('github_username', models.CharField(blank=True, max_length=30)),
                ('picture', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ],
            options={
                'abstract': False,
                },
            bases=('wagtailcore.page',),
            ),

        # Rename BlogPage.author to BlogPage.author_old
        migrations.RenameField(
            model_name='BlogPage',
            old_name='author',
            new_name='author_old',
            ),

        # Create a new field in BlogPage called author, linked to AuthorPage
        migrations.AddField(
            model_name='BlogPage',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.AuthorPage'),
            ),

        # migrates AuthorProfileData to the AuthorPage
        migrations.RunPython(migrate_data),

        # Delete the BlogPage.author_old field
        migrations.RemoveField(
            model_name='BlogPage',
            name='author_old',
            ),

        # Delete AuthorProfile
        migrations.DeleteModel(
            name='AuthorProfile',
            ),
        ]
