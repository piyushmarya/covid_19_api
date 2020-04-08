from flask import request
from flask_restful import Resource, reqparse
from models.world_model import WorldModel


class WorldResource(Resource):
    parser = reqparse.RequestParser()
    def get(self):
        return WorldModel.get_world_data(),200

    def post(self):
        data = request.json
        obj = WorldModel(data)
        if obj.save_world_data():
            return 200
        return 404
