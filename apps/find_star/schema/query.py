import graphene
from graphene import Scalar
from graphene_django import DjangoObjectType

from apps.find_star.models import Birth, Image, Post


class BirthType(DjangoObjectType):
    class Meta:
        model = Birth
        fields = ["id", "birth", "word", "image_set", "post"]


class ImageType(DjangoObjectType):
    class Meta:
        model = Image
        fields = [
            "id",
            "url"
        ]


class FileField(Scalar):
    @staticmethod
    def serialize(value):
        if not value:
            return ""
        return value.url

    @staticmethod
    def parse_literal(node):
        return node

    @staticmethod
    def parse_value(value):
        return value


class PostType(DjangoObjectType):
    post = FileField()

    class Meta:
        model = Post
        fields = ["id", "post"]


class Query(graphene.ObjectType):

    birth = graphene.Field(BirthType, date=graphene.Date(required=True))

    def resolve_birth(root, info, date):
        return Birth.objects.get(birth=date)

    birth_no_found = graphene.List(ImageType)

    def resolve_birth_no_found(self, info):
        return Image.objects.filter(birth__isnull=True)
