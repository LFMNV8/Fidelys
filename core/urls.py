from django.urls import path  # Importa a função path para definir as rotas de URL
from .views import * # Importa a função de view 'home' do módulo 'views' local
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    
    path('', home, name='home'),
    
    
    
    path('Planos-e-servicos/', planoseservico, name='planoseservico'),
    
    path('carregando...', carregamento1 ,name='carregamento1'),
    
    path('carregando........', carregamentologadoplanos ,name='carregamentologadoplanos'),
    
    path('Planos/', carregamentologadoplanospage),
    
    path('carregando....', carregamentohome , name='carregamentohome'),
    
    
    path('carregando...............', carregamentohomelogado , name='carregamentohomelogado'),
    
    path('carregando.....', carregamentocadastro , name='carregamentocadastro'),
    
    path('carregando......', carregamentologin , name='carregamentologin'),
    
    path('cadastro/', cadastro, name='cadastro'),
    
    path('login/', login_view, name='login'),
    
    path('home_logado/', home_logado, name='home_logado'),
    
    #api
    
    path('criando...', criar_usuario, name='criar_usuario'),
    path('logando...', login_usuario, name='login_usuario'),
    path('atualizar_imagem/', atualizar_imagem, name='atualizar_imagem'),
    path('alterar_senha', alterar_senha, name='alterar_senha'),
    path('reset-password/', reset_password, name='reset_password')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)