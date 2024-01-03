import chainlit as cl

@cl.on_message
async def main(message: cl.Message):

    # Send an intermediate response from Tool 1.
    await cl.Message(
        author='Tool',
        content=f"Response from tool",
        parent_id=message.id,
    ).send()

    # Send the final answer.
    await cl.Message(content=f'This is the final answer').send()
