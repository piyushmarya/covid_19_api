from flask_restful import Resource

from models.world_model import WorldModel

class WorldResource(Resource):
    def get(self):
        return WorldModel.get_world_data(),200

    def post(self):
        obj = WorldModel()
        obj.save_world_data()
        return 200
