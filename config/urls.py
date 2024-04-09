from django.contrib import admin
from django.urls import path
from app.views import home, project_detail,about, blog, portfolio, blog_detail
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('project-detail/<int:pk>/', project_detail, name="project_detail"),
    path('about', about),
    path('portfolio', portfolio),
    path('blog', blog, name='blog'),
    path('blog-detail/<int:pk>/', blog_detail, name="blog_detail"),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)