from rest_framework import serializers
from django.contrib.auth.models import User
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


# class SnippetSerializer(serializers.ModelSerializer):
#     # or .CharField(read_only=True)
#     owner = serializers.ReadOnlyField(source='owner.username')

#     class Meta:
#         model = Snippet
#         fields = ('id', 'title', 'code', 'linenos',
#                   'language', 'style', 'owner')


# class UserSerializer(serializers.ModelSerializer):
#     snippets = serializers.PrimaryKeyRelatedField(
#         many=True, queryset=Snippet.objects.all())

#     class Meta:
#         model = User
#         fields = ('id', 'username', 'snippets')

class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(
        view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ('url', 'id', 'highlight', 'owner',
                  'title', 'code', 'linenos', 'language', 'style')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(
        many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'snippets')
