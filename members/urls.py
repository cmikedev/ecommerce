from django.urls import path
from . import views


urlpatterns = [
    path('login_user', views.login_user, name='login'),
    path('logout_user', views.logout_user, name='logout'),
]

#urlpatterns += static(settings.MEDIA_URL, document_root=settings.STATICFILES_DIRS)