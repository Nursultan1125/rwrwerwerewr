from django.contrib import admin

from footer_data.models import ListFooter, TitleFooter, Delivery


class FooterInline(admin.StackedInline):
    model = ListFooter
    extra = 3


class FooterAdmin(admin.ModelAdmin):
    fields = ['title_body']
    inlines = [FooterInline]


admin.site.register(TitleFooter, FooterAdmin,)
admin.site.register(Delivery)
