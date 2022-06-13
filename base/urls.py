from django.urls import path
from . import views


urlpatterns = [
    path("", views.homepage, name="home"),
    path('project/<str:pk>/', views.projectPage, name='project'),
    path('blog/<str:pk>/', views.blogPage, name='blog'),
    path('add-project/', views.addProject , name='add-project'),
    path('add-blog/', views.addBlog , name='add-blog'),
    path('edit-project/<str:pk>/', views.editProject , name='edit-project'),
    path('edit-blog/<str:pk>/', views.editBlog , name='edit-blog'),
    path('inbox/', views.inboxPage , name='inbox'),
    path('message//<str:pk>/', views.messagePage , name='message'),
    
]


