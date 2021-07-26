import asyncio
import cleverbotfree

#implementation from https://github.com/plasticuproject/cleverbotfree

async def async_chat():
    """Example code using cleverbotfree async api."""
    async with cleverbotfree.async_playwright() as p_w:
        c_b = await cleverbotfree.CleverbotAsync(p_w)
        while True:
            user_input = input("User: ")
            if user_input == 'quit':
                break
            bot = await c_b.single_exchange(user_input)
            print('Cleverbot:', bot)
        await c_b.close()

asyncio.run(async_chat())