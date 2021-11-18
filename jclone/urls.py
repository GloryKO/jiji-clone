"""jclone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.schemas import get_schema_view
#from rest_framework_swagger.views import get_swagger_view
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view( 
   openapi.Info(
      title="JiJiClone API",
      default_version='v1',
      description="A Web API for a JiJi-like App",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny,]
)

#API_TITLE = 'JiJiClone API'
#API_DESCRIPTION = 'A Web API for a JiJi-like App.'
#schema_view = get_swagger_view(title=API_TITLE) 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('jiji.urls')),
    path('api/v1/',include('api.urls')),
    path('api-auth/',include('rest_framework.urls')),
    path('api/v1/rest-auth/',include('rest_auth.urls')),
    #path('api/v1/rest-auth/registration/',include('rest_auth.registration.urls')),
    #path('swagger-docs/',schema_view),
    path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/',schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/',schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)