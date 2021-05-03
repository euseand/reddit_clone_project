from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import PostSerializer, VoteSerializer
from .models import Post, Vote


class PostsView(APIView):
    permission_classes = [IsAuthenticated, ]

    @staticmethod
    def get(request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response({'posts': serializer.data, 'total': len(serializer.data)}, status.HTTP_200_OK)

    @staticmethod
    def post(request):
        data = {
            'title': request.data.get('title'),
            'content': request.data.get('content'),
            'url': request.data.get('url'),
            'user': request.user.id,
        }
        print(data)
        serializer = PostSerializer(data=data, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response({'post': serializer.data}, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class VotesView(APIView):

    @staticmethod
    def post(request, post_id):
        data = {
            'user': request.user.id,
            'post': post_id,
        }
        if Vote.objects.filter(user_id=data.get('user'), post_id=post_id).exists():
            return Response('You have already voted on this post', status.HTTP_400_BAD_REQUEST)
        serializer = VoteSerializer(data=data, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response({'vote': serializer.data}, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class VoteView(APIView):

    @staticmethod
    def get(request, post_id, vote_id):
        try:
            vote = Vote.objects.get(pk=vote_id)
            if vote.post_id == post_id:
                return Response({'vote': vote_id, 'post': post_id}, status.HTTP_200_OK)
            else:
                return Response({'detail': 'Vote not found'}, status.HTTP_404_NOT_FOUND)
        except ObjectDoesNotExist:
            return Response({'detail': 'There is no such vote'}, status.HTTP_404_NOT_FOUND)

    @staticmethod
    def delete(request, post_id, vote_id):
        try:
            vote = Vote.objects.get(pk=vote_id)
            if vote.post_id == post_id:
                vote.delete()
                return Response({'detail': 'You have unvoted on this post'}, status.HTTP_200_OK)
            else:
                return Response({'detail': 'Vote not found'}, status.HTTP_404_NOT_FOUND)
        except ObjectDoesNotExist:
            return Response({'detail': 'You have never voted on this post'}, status.HTTP_404_NOT_FOUND)
