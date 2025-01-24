from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import (
    AuthGroup, AuthPermission, AuthUser, BooksAuthor, BooksBook,
    BooksBookshelf, BooksFormat, BooksLanguage, BooksSubject
)
from .serializers import (
    AuthGroupSerializer, AuthPermissionSerializer, AuthUserSerializer,
    BooksAuthorSerializer, BooksBookSerializer, BooksBookshelfSerializer,
    BooksFormatSerializer, BooksLanguageSerializer, BooksSubjectSerializer
)

from rest_framework.permissions import IsAuthenticated

# List and Detail Views for Books
class BooksListView(generics.ListAPIView):
    queryset = BooksBook.objects.all()
    serializer_class = BooksBookSerializer
    permission_classes = [IsAuthenticated]

from rest_framework.filters import SearchFilter, OrderingFilter

class BooksListView(generics.ListAPIView):
    queryset = BooksBook.objects.all()
    serializer_class = BooksBookSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'authors__name']
    ordering_fields = ['download_count']


class BookDetailView(generics.RetrieveAPIView):
    queryset = BooksBook.objects.all()
    serializer_class = BooksBookSerializer


# List and Detail Views for Authors
class AuthorsListView(generics.ListAPIView):
    queryset = BooksAuthor.objects.all()
    serializer_class = BooksAuthorSerializer


class AuthorDetailView(generics.RetrieveAPIView):
    queryset = BooksAuthor.objects.all()
    serializer_class = BooksAuthorSerializer


# List Views for Other Entities
class BookshelfListView(generics.ListAPIView):
    queryset = BooksBookshelf.objects.all()
    serializer_class = BooksBookshelfSerializer


class FormatListView(generics.ListAPIView):
    queryset = BooksFormat.objects.all()
    serializer_class = BooksFormatSerializer


class LanguageListView(generics.ListAPIView):
    queryset = BooksLanguage.objects.all()
    serializer_class = BooksLanguageSerializer


class SubjectListView(generics.ListAPIView):
    queryset = BooksSubject.objects.all()
    serializer_class = BooksSubjectSerializer


# List and Detail Views for Auth Users and Groups
class AuthUserListView(generics.ListAPIView):
    queryset = AuthUser.objects.all()
    serializer_class = AuthUserSerializer


class AuthUserDetailView(generics.RetrieveAPIView):
    queryset = AuthUser.objects.all()
    serializer_class = AuthUserSerializer


class AuthGroupListView(generics.ListAPIView):
    queryset = AuthGroup.objects.all()
    serializer_class = AuthGroupSerializer


class AuthPermissionListView(generics.ListAPIView):
    queryset = AuthPermission.objects.all()
    serializer_class = AuthPermissionSerializer


