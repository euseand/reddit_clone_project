from django.urls import path, include

from .views import PostsView, VotesView, VoteView


urlpatterns = [
    path('posts/', PostsView.as_view(), name='posts'),
    path('posts/<int:post_id>/votes/', VotesView.as_view(), name='votes'),
    path('posts/<int:post_id>/votes/<int:vote_id>', VoteView.as_view(), name='vote'),
    path('api/auth', include('rest_framework.urls')),
]
