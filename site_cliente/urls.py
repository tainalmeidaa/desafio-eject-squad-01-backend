from django.contrib import admin
from django.urls import path, include
# from django.conf import settings
# from django.conf.urls.static import static
from home import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home), #retirar esta linha inteira caso vá testar o site para aparecer que a instalação do django
                               #foi feita com sucesso (o que foi feito é pra implementar depois)
    path('api/', include('home.urls')),
]
