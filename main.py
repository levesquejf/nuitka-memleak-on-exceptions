import aiohttp
import asyncio
import gc
import objgraph

url="http://127.0.0.1"

async def http_call():
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as resp:
                pass
        except Exception:
            pass


async def run():
    await http_call()
    
    print("Objects before HTTP loop")
    gc.collect()
    obj_start = len(gc.get_objects())
    objgraph.show_growth(shortnames=False)

    for _ in range(0,10):
        await http_call()
    
    print("\n\nObjects after HTTP loop")
    gc.collect()
    obj_end = len(gc.get_objects())
    objgraph.show_growth(shortnames=False)

    print(f"\nObjects Count Diff: {obj_end - obj_start}")


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())


if __name__ == "__main__":
    main()
