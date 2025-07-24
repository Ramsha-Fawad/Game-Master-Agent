from agents import Agent, handoff
from setup_config import model
from expert.monster_agent import monster_agent
from expert.item_agent import item_agent
from util.make_on_handoff_message import make_on_handoff_message
from tools.generate_event import generate_event


narrator_agent = Agent(
   name="NarratorAgent",
instructions="""
You are the voice weaving a captivating fantasy tale.

Responsibilities:
- Begin each scene vividly (e.g., “Mist curls around your feet in the haunted forest...”).
- Present choice points to the player.
- If danger looms, pass control to MonsterAgent.
- If treasure glimmers, pass to ItemAgent.
- Continue narrative based on the player's previous actions.

Tone: Enchanting, immersive, and slightly suspenseful.
""",
    model=model,
    tools=[generate_event],
    handoffs=[
        handoff(agent=monster_agent, on_handoff=make_on_handoff_message(monster_agent)),
        handoff(agent=item_agent, on_handoff=make_on_handoff_message(item_agent)),
    ]
)