from json import dumps
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin
import twitter as t
import bayes as b

app = Flask(__name__)
api = Api(app)
CORS(app)
        
class TweetScore(Resource):
  def get(self, keywords_id):
    data = t.ReadTweets(keywords_id)
    return {'score':b.setKeyword(data), 'text':data}

api.add_resource(TweetScore, '/api/score/<keywords_id>') # Route_1

if __name__ == '__main__':
  app.run(port='5002')