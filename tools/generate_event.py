from agents import function_tool
import random

@function_tool
async def generate_event(context: str) -> dict:
    # Mock dynamic events
    events = {
       "forest": [
    "Leaves crackle as something moves among the branches…",
    "From the shadows, a snarling goblin leaps forward!",
    "You spot a narrow, overgrown trail leading deeper into the woods."
],
"castle": [
    "A distant echo follows your footsteps as the heavy door swings shut.",
    "Suddenly, the floor gives way beneath you—spikes glint in the dim torchlight!",
    "A stern knight, sword drawn, blocks your path and demands your purpose."
],
"cave": [
    "Wings flutter all around as you step into the damp cavern.",
    "In a dusty alcove, a chest lies half-buried—its lid ajar.",
    "A deep growl shakes the cavern—something colossal has stirred."
],
    }
    possibilities = events.get(context.lower(), ["Nothing happens."])
    event = random.choice(possibilities)
    return {"context": context, "event": event}