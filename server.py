import asyncio
from aiohttp import web
import json


async def simple_response(request):
    response_obj = { 'status' : 'success' }
    return web.Response(text=json.dumps(response_obj))


async def build_server(loop, address, port):
    
    app = web.Application(loop=loop)
    app.router.add_route('GET', "/", simple_response)

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