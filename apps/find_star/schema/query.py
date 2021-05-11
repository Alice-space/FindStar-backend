import graphene
from graphene_django import DjangoObjectType

from apps.find_star.models import Birth, Image


class BirthType(DjangoObjectType):
    class Meta:
        model = Birth
        fields = ["id", "birth", "image_set"]


class ImageType(DjangoObjectType):
    class Meta:
        model = Image
        fields = [
            "id",
            "birth",
            "url"
        ]


class Query(graphene.ObjectType):

    birth = graphene.Field(BirthType, date=graphene.Date(required=True))

    def resolve_birth(root, info, date):
        print(date)
        print(type(date))
        return Birth.objects.get(birth=date)

    birth_no_found = graphene.List(ImageType)

    def resolve_birth_no_found(self, info):
        return Image.objects.filter(birth__isnull=True)
