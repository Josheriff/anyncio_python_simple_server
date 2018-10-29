from sanic import Sanic
from sanic import response
from sanic_cors import CORS

app = Sanic(__name__)
CORS(app)

# app.static("/static", "./static") <- in case we want to serve statics

@app.post('/post')
async def post_handler(request):

    return response.json({'message': 'Post method you end a jsonStringified post and your name is: {}'.format(request.body)})

@app.get('/get')
async def get_handler(request):
    return response.json({'message': 'Post method! {}'.format(request.args)})


if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
        port=8000
    )
    