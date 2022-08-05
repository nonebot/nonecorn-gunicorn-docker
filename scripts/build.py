"""
Copyright (c) 2008-2022 synodriver <synodriver@gmail.com>
"""
import asyncio
import os

NAME = os.getenv("NAME")
if NAME == "latest":
    NAME = "python3.10"


async def build_one():
    p = await asyncio.create_subprocess_exec(
        "docker",
        "build",
        "-f",
        f"./docker-images/{NAME}.dockerfile",
        "-t",
        f"synodriver/nonecorn-gunicorn-docker:{NAME}",
        "./docker-images/",
    )
    await p.wait()
    p = await asyncio.create_subprocess_exec(
        "docker", "push", f"synodriver/nonecorn-gunicorn-docker:{NAME}"
    )
    await p.wait()


if __name__ == "__main__":
    asyncio.run(build_one())
