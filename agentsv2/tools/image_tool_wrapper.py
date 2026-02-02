from google.adk.tools.function_tool import FunctionTool
from agentsv2.tools.image_gen_tool import generate_image

image_gen_tool = FunctionTool(
    func=generate_image
)
