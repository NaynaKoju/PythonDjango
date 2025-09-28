from django.contrib import admin
from .models import Project, Bio, About, Skill, Contact, CV

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "link")
    search_fields = ("title",)

admin.site.register(Bio)
admin.site.register(About)
admin.site.register(Skill)
admin.site.register(Contact)
admin.site.register(CV)