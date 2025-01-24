from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt import views as jwt_views
from rest_framework.permissions import AllowAny
from .views import (
    BooksListView, BookDetailView, AuthorsListView, AuthorDetailView,
    BookshelfListView, FormatListView, LanguageListView, SubjectListView,
    AuthUserListView, AuthUserDetailView, AuthGroupListView, AuthPermissionListView
)

# Swagger schema view
schema_view = get_schema_view(
    openapi.Info(
        title="Books API",
        default_version='v1',
        description="API documentation for the Books project.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(AllowAny,),
)

urlpatterns = [
    # Books Endpoints
    path('books/', BooksListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),

    #  # Token endpoints
    # path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    
    # Authors Endpoints
    path('authors/', AuthorsListView.as_view(), name='author-list'),
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),

    # Bookshelf Endpoint
    path('bookshelves/', BookshelfListView.as_view(), name='bookshelf-list'),

    # Format Endpoint
    path('formats/', FormatListView.as_view(), name='format-list'),

    # Language Endpoint
    path('languages/', LanguageListView.as_view(), name='language-list'),

    # Subject Endpoint
    path('subjects/', SubjectListView.as_view(), name='subject-list'),

    # Auth Users Endpoints
    path('users/', AuthUserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', AuthUserDetailView.as_view(), name='user-detail'),

    # Auth Groups and Permissions
    path('groups/', AuthGroupListView.as_view(), name='group-list'),
    path('permissions/', AuthPermissionListView.as_view(), name='permission-list'),

    # Swagger Endpoints
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

