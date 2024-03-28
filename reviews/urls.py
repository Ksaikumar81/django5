from charset_normalizer import cd
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    path('', views.review_list, name='review_list'),
    path('add/', views.add_review, name='add_review'),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)