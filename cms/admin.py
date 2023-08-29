from django.contrib import admin
from django.utils.safestring import mark_safe

from cms.models import CmsSlider


# Register your models here.
class CmsAdmin(admin.ModelAdmin):
    list_display = ('cms_title', 'cms_text', 'cms_css', 'get_image')
    list_display_links = ('cms_title',)
    list_editable = ('cms_css',)
    fields = ('cms_title', 'cms_text', 'cms_css', 'get_image')
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        if obj.cms_image:
            return mark_safe(f'<img src="{obj.cms_image.url}" width=80px>')
        else:
            return 'No picture'

    get_image.short_description = 'Minipic'


admin.site.register(CmsSlider, CmsAdmin)
