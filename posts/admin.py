from django.contrib import admin

from posts.models import Post, Vote


class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ('id', 'title', 'user', 'created')
    list_display_links = ('id', 'title',)
    readonly_fields = ('created', 'updated',)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('title', 'user',)}
         ),
    )
    search_fields = ('title',)
    list_filter = ('user',)


class VoteAdmin(admin.ModelAdmin):
    model = Vote
    list_display = ('id', 'user', 'post')
    list_filter = ('user', 'post')


admin.site.register(Post, PostAdmin)
admin.site.register(Vote, VoteAdmin)
