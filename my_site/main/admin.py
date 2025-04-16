from django.contrib import admin
from .models import Article, Slide, Counter, CompanyInfo, HomeSection, Logo

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title', 'content')
    list_filter = ('created_at',)
    # prepopulated_fields = {'slug': ('title',)}  # اگر فیلد slug دارید

class SlideAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active')
    list_editable = ('is_active',)

admin.site.register(Article, ArticleAdmin)
admin.site.register(Slide, SlideAdmin)
admin.site.register(Counter)
admin.site.register(CompanyInfo)

# from django.contrib import admin
# from .models import HomeSection
#
# @admin.register(HomeSection)
# class HomeSectionAdmin(admin.ModelAdmin):
#     list_display = ('section_type', 'title', 'is_active', 'order')
#     list_editable = ('is_active', 'order')
#     list_filter = ('section_type', 'is_active')
#     search_fields = ('title', 'content')
# from django.contrib import admin
# from .models import HomeSection

@admin.register(HomeSection)
class HomeSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'section_type', 'is_active')
    list_filter = ('section_type', 'is_active')

@admin.register(Logo)
class SiteSettingAdmin(admin.ModelAdmin):
    list_display = ('image', 'is_active')