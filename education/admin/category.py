from django.contrib import admin


class CategoryAdmin(admin.ModelAdmin):
    search_fields = (
        'name',
    )


class LevelAdmin(admin.ModelAdmin):
    search_fields = (
        'name',
    )