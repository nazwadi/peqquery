import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField


from models import NPCTypes
from models import Items


class NPC(SQLAlchemyObjectType):
    class Meta:
        model = NPCTypes
        interfaces = (relay.Node, )


class Items(SQLAlchemyObjectType):
    class Meta:
        model = Items
        interfaces = (relay.Node, )


class Query(graphene.ObjectType):
    node = relay.Node.Field()

    all_npcs = SQLAlchemyConnectionField(NPC.connection)
    all_items = SQLAlchemyConnectionField(Items.connection)


schema = graphene.Schema(query=Query)
