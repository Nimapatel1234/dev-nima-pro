# from rest_framework import serializers
# from .models import Book, BookDownloadLink

# class BookDownloadLinkSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = BookDownloadLink
#         fields = ['mime_type', 'url']

# class BookSerializer(serializers.ModelSerializer):
#     download_links = BookDownloadLinkSerializer(many=True, required=False)

#     class Meta:
#         model = Book
#         fields = [
#             'id', 'title', 'author_name', 'genre', 'language', 'subject',
#             'bookshelf', 'download_count', 'download_links'
#         ]

from rest_framework import serializers
from .models import (
    AuthGroup, AuthPermission, AuthUser, BooksAuthor, BooksBook,
    BooksBookAuthors, BooksBookshelf, BooksFormat, BooksLanguage, BooksSubject
)


class AuthGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthGroup
        fields = ['id', 'name']


class AuthPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthPermission
        fields = ['id', 'name', 'codename', 'content_type']


class AuthUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        fields = [
            'id', 'username', 'email', 'first_name', 'last_name',
            'is_active', 'is_staff', 'date_joined'
        ]


class BooksAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksAuthor
        fields = ['id', 'name', 'birth_year', 'death_year']


class BooksBookSerializer(serializers.ModelSerializer):
    authors = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = BooksBook
        fields = ['id', 'title', 'gutenberg_id', 'media_type', 'download_count', 'authors']


class BooksBookshelfSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksBookshelf
        fields = ['id', 'name']


class BooksFormatSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksFormat
        fields = ['id', 'mime_type', 'url', 'book']


class BooksLanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksLanguage
        fields = ['id', 'code']


class BooksSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksSubject
        fields = ['id', 'name']

from rest_framework.test import APITestCase
from .models import BooksBook

class BooksBookSerializerTest(APITestCase):
    def test_serializer_fields(self):
        book = BooksBook.objects.create(title="Test Book", gutenberg_id=123)
        serializer = BooksBookSerializer(book)
        self.assertIn('title', serializer.data)
