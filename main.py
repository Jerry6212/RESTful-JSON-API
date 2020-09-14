from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)
video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", help("Name of the video"), type=str, required=True)
video_put_args.add_argument("views", help("Views of the video"), type=str, required=True)
video_put_args.add_argument("likes", help("Likes of the video"), type=str, required=True)

videos = {}


# keeps server from crashing when asking for movie that doesnt exist
def abort_if_vid_doesnt_exist(video_id):
    if video_id not in videos:
        abort(404, message="Video ID not valid")
#keeps server from crashing if posing video id that already exist
def abort_if_vid_exist(video_id):
    if video_id in videos:
        abort(409, message="video already exists")

class Video(Resource):
    def get(self, video_id):
        abort_if_vid_doesnt_exist(video_id)
        return videos[video_id]

    def put(self, video_id):
        abort_if_vid_exist(video_id)
        args = video_put_args.parse_args()
        videos[video_id] = args
        return videos[video_id], 201


def delete(self, video_id):
    abort_if_vid_doesnt_exist(video_id)
    del videos[video_id]
    return "", 204

api.add_resource(Video, "/video/<int:video_id>")

# only for testing
if __name__ == "__main__":
    app.run(debug=True)
