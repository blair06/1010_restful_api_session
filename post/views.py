from .serializer import PostSerializer
from .models import Post
from rest_framework import viewsets


#10:54 영상
# Create your views here.


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all() 
    serializer_class = PostSerializer 