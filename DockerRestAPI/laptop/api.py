from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from pymongo import MongoClient
import csv, io

app = Flask(__name__)
api = Api(app)

client = MongoClient('mongodb://proj5-mongo-mongodb-1:27017/')
db = client['brevetsdb']
collection = db['controls']


def get_times(only=None, top=None):
    results = []

    for control in collection.find({}, {'_id': 0}):
        entry = {}
        if only == 'open' or only is None:
            entry['open'] = control.get('open', '')
        if only == 'close' or only is None:
            entry['close'] = control.get('close', '')
        results.append(entry)

    sort_key = 'close' if only == 'close' else 'open'
    results.sort(key=lambda x: x.get(sort_key, ''))

    if top is not None:
        results = results[:int(top)]

    return results


def to_csv(data):
    if not data:
        return ""
    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)
    return output.getvalue()


class ListAll(Resource):
    def get(self, fmt='json'):
        top = request.args.get('top', None)
        data = get_times(only=None, top=top)
        if fmt == 'csv':
            return app.response_class(to_csv(data), mimetype='text/csv')
        return jsonify(data)


class ListOpenOnly(Resource):
    def get(self, fmt='json'):
        top = request.args.get('top', None)
        data = get_times(only='open', top=top)
        if fmt == 'csv':
            return app.response_class(to_csv(data), mimetype='text/csv')
        return jsonify(data)


class ListCloseOnly(Resource):
    def get(self, fmt='json'):
        top = request.args.get('top', None)
        data = get_times(only='close', top=top)
        if fmt == 'csv':
            return app.response_class(to_csv(data), mimetype='text/csv')
        return jsonify(data)


api.add_resource(ListAll,       '/listAll', '/listAll/<string:fmt>')
api.add_resource(ListOpenOnly,  '/listOpenOnly', '/listOpenOnly/<string:fmt>')
api.add_resource(ListCloseOnly, '/listCloseOnly', '/listCloseOnly/<string:fmt>')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)