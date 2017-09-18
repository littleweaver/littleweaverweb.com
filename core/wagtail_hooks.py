from django.contrib.staticfiles.storage import staticfiles_storage
from wagtail.wagtailadmin.rich_text import HalloPlugin
from wagtail.wagtailcore import hooks
from wagtail.wagtailcore.whitelist import allow_without_attributes


@hooks.register('register_rich_text_features')
def register_embed_feature(features):
    features.register_editor_plugin(
        'hallo', 'code',
        HalloPlugin(
            name='code',
            order=15,
            js=[staticfiles_storage.url('js/hallo-code.js')],
        )
    )


# Allow <code> tag in rich text areas
@hooks.register('construct_whitelister_element_rules')
def whitelister_element_rules():
    return {
        'code': allow_without_attributes,
    }
