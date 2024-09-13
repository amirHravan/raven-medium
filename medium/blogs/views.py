from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db.models import Sum
from rest_framework.throttling import UserRateThrottle

from .permissions import IsOwner
from .models import Blog
from .serializers import BlogSerializer, BlogDetailSerializer


class BlogListView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated]


class BlogCreateView(generics.CreateAPIView):
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class BlogUpdateDeleteView(generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class BlogDetailView(generics.RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogDetailSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]

    def get(self, request, *args, **kwargs):
        blog = self.get_object()
        blog.views += 1
        blog.save()
        return super().get(request, *args, **kwargs)


class BlogLikeView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        blog = Blog.objects.get(pk=pk)
        blog.likes += 1
        blog.save()
        return Response(status=status.HTTP_200_OK)


class BlogAnalyticsView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        total_likes = Blog.objects.filter(author=request.user).aggregate(Sum('likes'))['likes__sum'] or 0
        total_views = Blog.objects.filter(author=request.user).aggregate(Sum('views'))['views__sum'] or 0
        return Response({'total_likes': total_likes, 'total_views': total_views})
