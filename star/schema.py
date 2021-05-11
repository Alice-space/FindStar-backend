import graphene
from django.conf import settings
from graphene_django.debug import DjangoDebug

from apps.find_star.schema import Query as FindStarQuery


class Query(FindStarQuery, graphene.ObjectType):
    if settings.DEBUG:
        debug = graphene.Field(DjangoDebug, name="_debug")


schema = graphene.Schema(query=Query)
