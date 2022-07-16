from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = "shop"

urlpatterns = [
	path('', views.home, name="home"),
	path('detail/<int:item_id>/', views.item_detail, name="detail"),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
