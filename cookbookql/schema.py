import graphene
from graphene_django import DjangoObjectType
from qlapp.models import *


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name", "ingridients")
    
class IngredientType(DjangoObjectType):
    class Meta:
        model = Ingredient
        fields = ("id", "name", "notes", "category")
    
    
class Query(graphene.ObjectType):
    all_ingredients = graphene.List(IngredientType)
    category_by_name = graphene.Field(CategoryType, name=graphene.String(required=True))
    
    def resolve_all_ingredients(root, info):
        return Ingredient.objects.select_related("category_ingredients").all()
    
    def resolve_category_by_name(root, info, name):
        return Category.objects.filter(name=name).first()
    

schema = graphene.Schema(query=Query)
