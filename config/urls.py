from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title='JunPypack',
        default_version='v1',
        description='JunPypack swagger',
        terms_of_service='https://www.google.com/policies/terms/',
        contact=openapi.Contact(email='contack@snippets.local'),
        license=openapi.License(name='BSD License')
    ),
    public=True,
    permission_classes=[permissions.AllowAny]
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/docs/', schema_view.with_ui()),
    path('api/v1/', include('post.urls')),
    path('api/v1/reviews/', include('review.urls')),
    path('api/v1/account/', include('account.urls')),
]
