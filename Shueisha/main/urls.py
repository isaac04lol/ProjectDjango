from django.urls import path
from . import views 

app_name = "main"

urlpatterns = [

    path('',views.IndexView.as_view(),name="home"), #Pagina principal
    path('review/',views.ReviewView.as_view(),name="reviews"), #Comentarios
    path('tublog/',views.CrearBlog,name="tublog"), #Creacionde Blog
    path('reviews/',views.reviews), #Zona de creacion de comentarios
    path('login/',views.loginPage,name="login"), #Login
    path('register/',views.registerPage,name="register"), #Registro
    path('logout/',views.logoutUser,name="logout") #cerrar sesión

]