from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser
from rest_framework import status, mixins, renderers, generics, permissions, viewsets
from rest_framework.views import APIView

from rest_framework.decorators import api_view, detail_route
from rest_framework.reverse import reverse

from rest_framework.response import Response
from snippets.models import Snippet
from django.contrib.auth.models import User
from snippets.serializers import SnippetSerializer
from snippets.serializers import UserSerializer
from django.http import Http404
from snippets.permissions import IsOwnerOrReadOnly


class SnippetViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.abs
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
