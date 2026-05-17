from django.urls import path
from .views import home, comunidade, login, cadastro, criar_post, logout_view, detalhe_post, excluir_post

urlpatterns = [
    path('', home, name='home'),
    path('comunidade/', comunidade, name='comunidade'),
    path('usuario/login/', login, name='login'),
    path('usuario/cadastro/', cadastro, name='cadastro'),
    path('comunidade/criar-post/', criar_post, name='criar_post'),
    path('logout/', logout_view, name='logout'),
    path('comunidade/post/<int:id>/', detalhe_post, name='detalhe_post'),
    path('post/excluir/<int:id>/', excluir_post, name='excluir_post'),
]