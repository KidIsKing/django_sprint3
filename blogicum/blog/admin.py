# from django.contrib import admin

# from .models import Post
# from .models import Category
# from .models import Location


# admin.site.register(Post)
# admin.site.register(Category)
# admin.site.register(Location)


from django.contrib import admin
from django.contrib.admin import DateFieldListFilter
from .models import Category, Location, Post, Comment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "is_published", "created_at", "post_count")
    list_filter = (
        "is_published",
        ("created_at", DateFieldListFilter),
    )
    search_fields = ("title", "description")
    list_editable = ("is_published",)
    prepopulated_fields = {"slug": ("title",)}
    list_per_page = 20

    def post_count(self, obj):
        return obj.posts.count()

    post_count.short_description = "Количество постов"


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ("name", "is_published", "created_at", "post_count")
    list_filter = (
        "is_published",
        ("created_at", DateFieldListFilter),
    )
    search_fields = ("name",)
    list_editable = ("is_published",)
    list_per_page = 20

    def post_count(self, obj):
        return obj.posts.count()

    post_count.short_description = "Количество постов"


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "category",
        "location",
        "is_published",
        "pub_date",
        "comment_count",
    )
    list_filter = (
        "is_published",
        "category",
        "location",
        "author",
        ("pub_date", DateFieldListFilter),
        ("created_at", DateFieldListFilter),
    )
    search_fields = (
        "title",
        "text",
        "author__username",
        "category__title",
        "location__name",
    )
    list_editable = ("is_published",)
    filter_horizontal = ()
    date_hierarchy = "pub_date"
    raw_id_fields = ("author",)  # Для быстрого выбора пользователя
    list_select_related = ("category", "location", "author")
    list_per_page = 25

    fieldsets = (
        ("Основное", {"fields": ("title", "text", "image", "author")}),
        ("Категоризация", {"fields": ("category", "location")}),
        (
            "Публикация",
            {"fields": ("is_published", "pub_date"), "classes": ("collapse",)},
        ),
    )

    def comment_count(self, obj):
        return obj.comments.count()

    comment_count.short_description = "Комментарии"


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("text_preview", "post", "author", "created_at")
    list_filter = (
        "post",
        "author",
        ("created_at", DateFieldListFilter),
    )
    search_fields = ("text", "post__title", "author__username")
    list_per_page = 30
    raw_id_fields = ("post", "author")

    def text_preview(self, obj):
        if len(obj.text) > 50:
            return f"{obj.text[:50]}..."
        return obj.text

    text_preview.short_description = "Текст комментария"
