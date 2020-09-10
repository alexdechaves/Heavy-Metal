#!flask/bin/python
from flask import Flask, jsonify, request, abort
from heavy_metal.data import *
from heavy_metal.structs import *

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/site.db'


@app.route('/all_shows', methods=['GET'])
def get_shows():
    query = map_show_data(TVShowDB.query.all())
    return jsonify({'shows': query}), 200


@app.route('/shows/<id>', methods=['GET'])
def get_show(id):
    query = map_show_data(TVShowDB.query.get(id))
    return jsonify({'show': query}), 200


@app.route('/create_show', methods=['POST'])
def create_show():
    if not request.json:
        abort(400)

    dbjob = TVShowDB(show=request.json['show'])
    db.session.add(dbjob)
    db.session.commit()

    return jsonify({'Success!': request.json}), 201


@app.route('/assets', methods=['GET'])
def get_assets():
    query = map_asset_data(AssetDB.query.all())
    return jsonify({'data': query}), 200


@app.route('/create_asset', methods=['POST'])
def create_asset():
    if not request.json or not 'filename' in request.json or not 'title' in request.json or not 'path' in request.json:
        abort(400)

    dbjob = AssetDB(title=request.json['title'], filename=request.json['filename'], path=request.json['path'], status=request.json['status'])
    db.session.add(dbjob)
    db.session.commit()

    return jsonify({'Success!': request.json}), 201


if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True, port=8080)
