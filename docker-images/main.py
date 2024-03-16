"""
Copyright (c) 2008-2022 synodriver <synodriver@gmail.com>
"""


async def app(scope, receive, send):
    assert scope['type'] == 'http'
    await send({"type": "http.response.start", "status": 200, "headers": [(b"Content-Type", b"text/html; charset=UTF-8")]})
    await send({"type": "http.response.body",
                "body": b"<h1>If you see this, the container is working and further configuration is needed</h1>"})
