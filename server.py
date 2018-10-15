import asyncio
from aiohttp import web
import json


async def simple_response(request):
    response_obj = { 'status' : 'success' }
    return web.Response(text=json.dumps(response_obj))

async def new_user(request):
    try:
        user = request.query['name']
        print("Creating new user with name: " , user)
        response_obj = { 'status' : 'success' }
        return web.Response(text=json.dumps(response_obj), status=200)

    except Exception as e:
        response_obj = { 'status' : 'failed', 'reason': str(e) }
        return web.Response(text=json.dumps(response_obj), status=500)


async def build_server(loop, address, port):
    
    app = web.Application(loop=loop)
    app.router.add_route('GET', "/", simple_response)
    app.router.add_route('POST',"/user", new_user)
    # app.router.add_post('/user', new_user)   
    return await loop.create_server(app.make_handler(), address, port)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(build_server(loop, 'localhost', 9999))
    print("Server ready!")

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        print("Shutting Down!")
        loop.close()