from django.urls import path
from . import views
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('', views.home, name='index'),
    # path('home/', views.home, name='home'),
    # path('todos/', views.todos, name='todos'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('contact-us/', views.contact_us, name='contact'),
    # path('dashboard/', views.dashboard, name='dashboard'),


    
   
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
