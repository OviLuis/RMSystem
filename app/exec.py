import asyncio

from os import environ

from producer import Producer
from connection import Connection

if __name__ == "__main__":
    try:
        hostname = environ.get("REDIS_HOSTNAME", "localhost")
        port = environ.get("REDIS_PORT", 6379)
        print(hostname)
        print(port)
        connection = Connection(hostname, port)
        r = connection.connect_to_redis()

        p = Producer(r)
        loop = asyncio.get_event_loop()

        asyncio.ensure_future(p.send_data())
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        print("Closing Loop")
        loop.close()
        
