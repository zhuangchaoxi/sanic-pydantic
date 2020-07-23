from sanic_pydantic import webargs

from sanic import Sanic
from sanic.response import json
from pydantic import BaseModel

app = Sanic("new app")


class PathModel(BaseModel):
    id: int


class QueryModel(BaseModel):
    name: str


class BodyModel(BaseModel):
    age: int


@app.route("/get-request", methods=["GET"])
@webargs(query=QueryModel)
def example_get_endpoint(request, **kwargs):
    response = json(kwargs)
    return response


@app.route("/get/<id>", methods=["GET"])
@webargs(path=PathModel)
def example_get_endpoint_params(request, **kwargs):
    response = json(kwargs)
    return response


@app.route("/post-request", methods=["POST"])
@webargs(query=QueryModel, body=BodyModel)
def example_post_endpoint(request, **kwargs):
    print(kwargs)
    response = json(kwargs)
    return response


@app.route("/async-get-request", methods=["GET"])
@webargs(query=QueryModel)
async def async_example_get_endpoint(request, **kwargs):
    print(kwargs)
    response = json(kwargs)
    return response


@app.route("/async-post-request", methods=["POST"])
@webargs(query=QueryModel, body=BodyModel)
async def async_example_post_endpoint(request, **kwargs):
    print(kwargs)
    response = json(kwargs)
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
