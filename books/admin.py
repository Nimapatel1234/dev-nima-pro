# from django.contrib import admin

from django.contrib import admin
from .models import (
    AuthGroup, AuthGroupPermissions, AuthPermission, AuthUser, AuthUserGroups,
    AuthUserUserPermissions, BooksAuthor, BooksBook, BooksBookAuthors,
    BooksBookBookshelves, BooksBookLanguages, BooksBookSubjects,
    BooksBookshelf, BooksFormat, BooksLanguage, BooksSubject,
    DjangoAdminLog, DjangoContentType, DjangoMigrations
)

# Inline configuration for relationships
class AuthGroupPermissionsInline(admin.TabularInline):
    model = AuthGroupPermissions
    extra = 1

class AuthUserGroupsInline(admin.TabularInline):
    model = AuthUserGroups
    extra = 1

class AuthUserPermissionsInline(admin.TabularInline):
    model = AuthUserUserPermissions
    extra = 1

class BooksBookAuthorsInline(admin.TabularInline):
    model = BooksBookAuthors
    extra = 1

class BooksBookBookshelvesInline(admin.TabularInline):
    model = BooksBookBookshelves
    extra = 1

class BooksBookLanguagesInline(admin.TabularInline):
    model = BooksBookLanguages
    extra = 1

class BooksBookSubjectsInline(admin.TabularInline):
    model = BooksBookSubjects
    extra = 1

class BooksFormatInline(admin.TabularInline):
    model = BooksFormat
    extra = 1

# Admin Models
@admin.register(AuthGroup)
class AuthGroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    inlines = [AuthGroupPermissionsInline]

@admin.register(AuthUser)
class AuthUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'is_active', 'is_staff', 'date_joined')
    search_fields = ('username', 'email')
    list_filter = ('is_active', 'is_staff')
    inlines = [AuthUserGroupsInline, AuthUserPermissionsInline]

@admin.register(BooksAuthor)
class BooksAuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'birth_year', 'death_year')
    search_fields = ('name',)

@admin.register(BooksBook)
class BooksBookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'media_type', 'download_count', 'gutenberg_id')
    search_fields = ('title',)
    list_filter = ('media_type',)
    inlines = [
        BooksBookAuthorsInline,
        BooksBookBookshelvesInline,
        BooksBookLanguagesInline,
        BooksBookSubjectsInline,
        BooksFormatInline
    ]

@admin.register(BooksBookshelf)
class BooksBookshelfAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(BooksLanguage)
class BooksLanguageAdmin(admin.ModelAdmin):
    list_display = ('id', 'code')
    search_fields = ('code',)

@admin.register(BooksSubject)
class BooksSubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(DjangoAdminLog)
class DjangoAdminLogAdmin(admin.ModelAdmin):
    list_display = ('id', 'action_time', 'user', 'action_flag', 'object_repr')
    search_fields = ('object_repr', 'change_message')
    list_filter = ('action_flag', 'action_time')

@admin.register(DjangoContentType)
class DjangoContentTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'app_label', 'model')
    search_fields = ('app_label', 'model')

@admin.register(DjangoMigrations)
class DjangoMigrationsAdmin(admin.ModelAdmin):
    list_display = ('id', 'app', 'name', 'applied')
    search_fields = ('app', 'name')
