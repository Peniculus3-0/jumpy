import asyncio

# Define an asynchronous function
async def my_coroutine():
    # Sleep for 2 seconds to simulate an asynchronous task
    await asyncio.sleep(2)
    return "Hello, world!"

# Create an event loop
loop = asyncio.get_event_loop()

# Create a coroutine object
coro = my_coroutine()

# Define a callback function to handle the result when the Future is resolved
def callback(future):
    print("Future resolved:", future.result())

# Create a Task object from the coroutine
my_task = asyncio.ensure_future(coro)

# Attach the callback to the Task
my_task.add_done_callback(callback)

# Run the event loop using loop.run_until_complete() with the Task as argument
loop.run_until_complete(my_task)

# Close the event loop
loop.close()
