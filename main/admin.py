from django.contrib import admin
from .models import *

# Register your models here.
    
@admin.register(FashionCategoryModel)
class FashionCategoryAdmin(admin.ModelAdmin):
    readonly_fields = ("user_created", "created_date", "modified_date")
    search_fields = ('title',)
    list_display = ["pk", "title"]
    
    def save_model(self, request, obj, form, change):
        if change:
            obj.user_modified = request.user
        else:
            obj.user_modified = request.user
            obj.user_created = request.user
        return super().save_model(request, obj, form, change)


@admin.register(TextileCategoryModel)
class TextileCategoryAdmin(admin.ModelAdmin):
    readonly_fields = ("user_created", "created_date", "modified_date")
    search_fields = ('title',)
    list_display = ["pk", "title"]
    
    def save_model(self, request, obj, form, change):
        if change:
            obj.user_modified = request.user
        else:
            obj.user_modified = request.user
            obj.user_created = request.user
        return super().save_model(request, obj, form, change)


class FashionImageInlineAdmin(admin.TabularInline):
    model = FashionImageModel
    fields = ("product", "image")
    readonly_fields = ("user_created", "user_modified", "created_date", "modified_date")
    
    def save_model(self, request, obj, form, change):
        if change:
            obj.user_modified = request.user
        else:
            obj.user_created = request.user
            obj.user_modified = request.user
        return super().save_model(request, obj, form, change)

    
@admin.register(FashionModel)
class FashionAdmin(admin.ModelAdmin):
    readonly_fields = ("user_created", "created_date", "modified_date")
    search_fields = ('product_name',)
    list_display = ["pk", "product_category", "product_name", "product_date"]
    inlines = [FashionImageInlineAdmin]
    
    def save_model(self, request, obj, form, change):
        if change:
            obj.user_modified = request.user
        else:
            obj.user_modified = request.user
            obj.user_created = request.user
        return super().save_model(request, obj, form, change)
    

@admin.register(FashionImageModel)
class FashionImageAdmin(admin.ModelAdmin):
    readonly_fields = ("user_created", "user_modified", "created_date", "modified_date")
    search_fields = ("product__product_name",)
    
    def save_model(self, request, obj, form, change):
        if change:
            obj.user_modified = request.user
        else:
            obj.user_created = request.user
            obj.user_modified = request.user
        return super().save_model(request, obj, form, change)


class TextileImageInlineAdmin(admin.TabularInline):
    model = TextileImageModel
    fields = ("product", "image")
    readonly_fields = ("user_created", "user_modified", "created_date", "modified_date")
    
    def save_model(self, request, obj, form, change):
        if change:
            obj.user_modified = request.user
        else:
            obj.user_created = request.user
            obj.user_modified = request.user
        return super().save_model(request, obj, form, change)


@admin.register(TextileModel)
class TextileAdmin(admin.ModelAdmin):
    readonly_fields = ("user_created", "created_date", "modified_date")
    search_fields = ('product_name',)
    list_display = ["pk", "product_category", "product_name", "product_date"]
    inlines = [TextileImageInlineAdmin]
    
    def save_model(self, request, obj, form, change):
        if change:
            obj.user_modified = request.user
        else:
            obj.user_modified = request.user
            obj.user_created = request.user
        return super().save_model(request, obj, form, change)
    

@admin.register(TextileImageModel)
class TextileImageAdmin(admin.ModelAdmin):
    readonly_fields = ("user_created", "user_modified", "created_date", "modified_date")
    search_fields = ("product__product_name",)
    
    def save_model(self, request, obj, form, change):
        if change:
            obj.user_modified = request.user
        else:
            obj.user_created = request.user
            obj.user_modified = request.user
        return super().save_model(request, obj, form, change)


@admin.register(ContactModel)
class ContactAdmin(admin.ModelAdmin):
    readonly_fields = ("created_date",)
    search_fields = ("name", "email", "subject", "created_date")
    list_display = ["name", "subject", "email", "created_date"]
    
    def save_model(self, request, obj, form, change):
        if change:
            obj.user_modified = request.user
        else:
            obj.user_modified = request.user
            obj.user_created = request.user
        return super().save_model(request, obj, form, change)