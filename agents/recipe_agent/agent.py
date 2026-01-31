from google.adk.agents.llm_agent import Agent
# import fetch_by_tag
# recipe_agent = Agent(
#     name="recipe_agent",
#     model="gemini-2.5-flash-lite",
#     description="Provides recipe recommendations and cooking instructions.",
#     instruction="""
# You are a recipe generation agent.

# Your task:
# Create a helpful cooking recipe based on the user's request.

# Guidelines:
# - Focus on food preparation and cooking
# - Use clear, simple steps
# - Include ingredients and basic instructions
# - Assume the user is a home cook
# - Be practical and concise

# Constraints:
# - Do not mention marketing, branding, or products
# - Do not ask unnecessary follow-up questions
# - If details are missing, make reasonable assumptions
# - Do not explain system behavior or routing

# Output format:
# - Recipe name
# - Ingredients list
# - Step-by-step instructions
# - Optional tips or variations

# """
# )
# from google.adk.tools import Tool
# from .fetch_by_tag import fetch_assets_by_tags

# fetch_assets_tool = Tool(
#     name="fetch_assets_by_tags",
#     description="Fetch reference media assets by tags",
#     func=fetch_assets_by_tags,
# )
# recipe_agent = Agent(
#     name="recipe_agent",
#     model="gemini-2.5-flash-lite",
#     description="Generates recipes and fetches reference assets.",
#     tools=[fetch_assets_tool],
#     instruction="""
# You are a recipe agent.

# Steps:
# 1. Extract 2-3 search tags from the user's request
# 2. Call the `fetch_assets_by_tags` tool with those tags
# 3. Use limit=5
# 4. Return ONLY the fetched assets as JSON

# Rules for tags:
# - lowercase
# - single words
# - food or cooking related

# Do not explain anything.
# Do not ask questions.

# Output MUST be valid JSON.
# """
# )
from google.adk.tools import FunctionTool
from google.adk import Agent
from .fetch_by_tag import fetch_assets_by_tags

# Create the tool using FunctionTool - it uses the function's name and docstring
fetch_assets_tool = FunctionTool(func=fetch_assets_by_tags)

recipe_agent = Agent(
    name="recipe_agent",
    model="gemini-2.5-flash-lite",
    description="Generates recipes and fetches reference assets.",
    tools=[fetch_assets_tool],
    instruction="""
You are a recipe agent.

Steps:
1. Extract 2-3 search tags from the user's request
2. Call the `fetch_assets_by_tags` tool with those tags
3. Use limit=5
4. Return ONLY the fetched assets as JSON

Rules for tags:
- lowercase
- single words
- food or cooking related

Do not explain anything. Do not ask questions.
Output MUST be valid JSON.
"""
)