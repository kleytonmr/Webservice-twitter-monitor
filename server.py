from json import dumps
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin
import twitter as t
import bayes as b

app = Flask(__name__)
api = Api(app)
CORS(app)
        
class TweetText(Resource):
  def get(self, keywords_id):
    return jsonify(t.ReadTweets(keywords_id))

class TweetScore(Resource):
  def get(self, keywords_id):
    return jsonify(b.setKeyword(keywords_id))

api.add_resource(TweetText,  '/api/text/<keywords_id>') # Route_1
api.add_resource(TweetScore, '/api/score/<keywords_id>') # Route_2

if __name__ == '__main__':
  app.run(port='5002')