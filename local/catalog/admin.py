from django.contrib import admin

# Register your models here.

from .models import Book, Author, Genre, BookInstance, Language

admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Language)

class AuthorAdmin(admin.ModelAdmin):
	list_display = ('last_name', 'first_name', 'date_of_birth')
	fields = [('last_name', 'first_name'), ('date_of_birth', 'date_of_death')]

class BooksInstanceInline(admin.TabularInline):
	model = BookInstance
	# Extra exercise
	def get_extra(self, request, obj=None, **kwargs):
		extra = 0
		return extra

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'display_genre')
	inlines = [BooksInstanceInline]

# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance) 
class BookInstanceAdmin(admin.ModelAdmin):
	list_display = ('book', 'status', 'borrower', 'due_back', 'id')
	list_filter = ('status', 'due_back')

	fieldsets = (
		(None, {
			'fields': ('book','imprint', 'id')
		}),
		('Availability', {
			'fields': ('status', 'due_back','borrower')
		}),
	)
