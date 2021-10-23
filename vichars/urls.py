from django.urls import path
import vichars.views as views

urlpatterns = [
    path('',views.vicharCreateAPIView.as_view()),
    path('<uuid:pk>',views.vicharAPIView.as_view()),
    path('<uuid:pk>/addComment',views.commentCreateAPIView.as_view()),
    path('comment/<uuid:pk>',views.commentAPIView.as_view()),
    path('<uuid:pk>/likepost',views.likePost),
    path('<uuid:pk>/removelike',views.removeLike)
]