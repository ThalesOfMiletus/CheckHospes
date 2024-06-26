from django.contrib import admin
from django.urls import path
from pricing import views as pricing_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', pricing_views.home, name='home'),  # Página inicial
    path('calendario/', pricing_views.visualizar_calendario, name='visualizar_calendario'),
    path('adicionar_quarto/', pricing_views.adicionar_quarto, name='adicionar_quarto'),
    path('quartos/', pricing_views.lista_quartos, name='quartos'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),  # URL de logout
    path('meu_hotel/', pricing_views.meu_hotel, name='meu_hotel'),  # URL para "Meu Hotel"
]