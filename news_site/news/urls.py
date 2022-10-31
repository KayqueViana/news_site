from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index, name="homepage"),
    path('notice/<int:id>', views.noticeInternal, name="notice-intenal"),
    path('send-email/', views.sendEmail, name="send-email"),
    path('comment/', views.commentPage, name="comment"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)