from django.urls import path
import users.views as views

urlpatterns = [
    path('<uuid:pk>',views.userAPIView.as_view()),
    path('',views.usersList.as_view()),
]