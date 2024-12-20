import fastapi, strawberry
import strawberry.fastapi
from .core import DSBType, SiteType
from designbuilder_schema.utils import load_model


@strawberry.type
class Query:

    @strawberry.field
    def dsb(self, filepath: str) -> DSBType:
        model = load_model(filepath)
        return DSBType.from_pydantic(model)

    @strawberry.field
    def site(self, filepath: str) -> SiteType:
        site = load_model(filepath).Site
        return SiteType.from_pydantic(site)


schema = strawberry.Schema(query=Query)
graphql_app = strawberry.fastapi.GraphQLRouter(schema)

app = fastapi.FastAPI()
app.include_router(graphql_app, prefix="/graphql")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)
