from django.contrib import admin

from price.models import PriceTable, PriceCard

# Register your models here.
admin.site.register(PriceTable)
admin.site.register(PriceCard)
