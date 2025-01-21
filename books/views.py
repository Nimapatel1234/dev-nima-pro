# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.pagination import PageNumberPagination
# from django.db.models import Q
# from .models import Book
# from .serializers import BookSerializer

# class BookListView(APIView):
#     def get(self, request):
#         filters = Q()
#         if 'language' in request.query_params:
#             filters &= Q(language__icontains=request.query_params['language'])
#         if 'title' in request.query_params:
#             filters &= Q(title__icontains=request.query_params['title'])
#         if 'author' in request.query_params:
#             filters &= Q(author_name__icontains=request.query_params['author'])
#         if 'topic' in request.query_params:
#             topic = request.query_params['topic']
#             filters &= Q(subject__icontains=topic) | Q(bookshelf__icontains=topic)

#         books = Book.objects.filter(filters).order_by('-download_count')
#         paginator = PageNumberPagination()
#         paginator.page_size = 25
#         paginated_books = paginator.paginate_queryset(books, request)
#         serializer = BookSerializer(paginated_books, many=True)
#         return paginator.get_paginated_response(serializer.data)


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


