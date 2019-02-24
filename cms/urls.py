
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from blog.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
	path('', home),
	path('create/', create_post),
	path('post/<int:post_id>/', post_page),
    path('login/', signIn),
    path('logout/', signOut),
    path('signup/', signUp),



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
