from agents import function_tool
import random

@function_tool
async def roll_dice(sides: int = 6) -> dict:
    result = random.randint(1, sides)
    return {"sides": sides, "result": result}