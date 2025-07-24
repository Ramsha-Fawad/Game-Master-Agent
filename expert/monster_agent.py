from agents import Agent, handoff
from setup_config import model
from util.make_on_handoff_message import make_on_handoff_message
from expert.item_agent import item_agent
from tools.roll_dice import roll_dice

monster_agent = Agent(
   name="MonsterAgent",
instructions="""
You orchestrate thrilling combat encounters.

Responsibilities:
- Describe the clash of combat using dice roll results.
- Prompt the player when it’s time to roll.
- Determine outcomes—enemy defeat, injury, or retreat.
- If victory yields spoils, hand off to ItemAgent to handle loot.
- Encourage next steps after battle ends.

Tone: Intense, gritty, but fair.
""",
    tools=[roll_dice],
    model=model,
    handoffs=[
        handoff(agent=item_agent, on_handoff=make_on_handoff_message(item_agent))
    ]
)