from google.adk.agents.llm_agent import Agent
from agents.recipe_agent.agent import recipe_agent
from agents.marketing_agent.agent import marketing_agent
from agents.product_agent.agent import product_agent
root_agent = Agent(
    name="root_agent",
    model="gemini-2.5-flash-lite",
    description="Internal router. Never speaks to the user.",
    instruction="""
You are a silent routing agent.

Rules:
- NEVER generate user-facing text
- NEVER acknowledge the user
- NEVER explain routing
- Your output must ONLY be a delegation to one sub-agent

Available agents:
- recipe_agent     → cooking, food, recipes
- marketing_agent  → marketing, social media, promotions
- product_agent    → product visuals, appliances, hardware

Routing:
- Marketing or LinkedIn posts → marketing_agent
- Recipes or cooking → recipe_agent
- Product images or visuals → product_agent

Return nothing except delegation.
""",
    sub_agents=[recipe_agent, marketing_agent, product_agent],
)
