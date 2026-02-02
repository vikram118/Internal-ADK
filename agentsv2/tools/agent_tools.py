from google.adk.tools.agent_tool import AgentTool
from agentsv2.recipe_agent.agent import recipe_agent
from agentsv2.marketing_agent.agent import marketing_agent
from agentsv2.product_agent.agent import product_agent

recipe_tool = AgentTool(
    agent=recipe_agent
)

marketing_tool = AgentTool(
    agent=marketing_agent
)

product_tool = AgentTool(
    agent=product_agent
)

ALL_AGENT_TOOLS = [
    recipe_tool,
    marketing_tool,
    product_tool,
]
