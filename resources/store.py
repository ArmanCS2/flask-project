from flask_restful import Resource
from models.store import StoreModel


class Store(Resource):
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {'message': 'store not found'}

    def post(self, name):
        if StoreModel.find_by_name(name):
            return {'message': 'store already exists'}

        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {'message': 'server error'}, 500

        return {'message': 'store created successfully'}

    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
        return {'message': 'store deleted'}


class Stores(Resource):
    def get(self):
        return {'stores': [store.json() for store in StoreModel.query.all()]}
