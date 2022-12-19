from django.contrib import admin
from .models import port
# Register your models here.

# admin.site.register(port);

@admin.register(port)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'is_public', 'message', 'message_length', 'created_at', 'updated_at']
    list_display_links = ['message']
    list_filter = ['created_at' , 'is_public']
    search_fields = ['message']

    def message_length(self, port):
        return f"{len(port.message)} 글자"
    message_length.short_description = "메세지 글자 수"