from django.contrib import admin
from django.urls import path
from products import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('products', views.products),
    path('show', views.show),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.destory),
    path('', views.show)
]
