import chainlit as cl
from agents import Runner
from agents.run import RunConfig
from setup_config import model, external_client
from expert.narrator_agent import narrator_agent
from expert.monster_agent import monster_agent
from expert.item_agent import item_agent

@cl.on_chat_start
async def start():
    cl.user_session.set("history", [])
    await cl.Message(
    "Welcome, brave explorer! Type anything to begin your journey... or type 'end' to finish the adventure.").send()

@cl.on_message
async def handle(message: cl.Message):
    user_input = message.content.strip().lower()

    if user_input.lower() in ["end", "exit", "quit"]:
        await cl.Message( "Your quest concludes—for now. Until next time, brave traveler!").send()
        cl.user_session.set("history", [])

        return

    history = cl.user_session.get("history") or []
    history.append({"role": "user", "content": message.content})

    thinking = await cl.Message("Loading…").send()

    try:
        result = await Runner.run(
            narrator_agent,  # Starting agent
            history,
            run_config=RunConfig(
                model=model,
                model_provider=external_client,
                tracing_disabled=True
            )
        )

        thinking.content = result.final_output
        await thinking.update()
        cl.user_session.set("history", result.to_input_list())

    except Exception as e:
        thinking.content = f"❌ Error: {e}"
        await thinking.update()