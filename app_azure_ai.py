from langchain_openai import AzureChatOpenAI
from browser_use import Agent
from pydantic import SecretStr
import os
import asyncio

# Initialize the model
llm = AzureChatOpenAI(
    model="gpt-4o",
    api_version='2024-10-21',
    azure_endpoint=os.getenv('AZURE_OPENAI_ENDPOINT', ''),
    api_key=SecretStr(os.getenv('AZURE_OPENAI_KEY', '')),
)
async def main():
# Create agent with the model
    agent = Agent(
        task="Search for Deepseek, Click into Models & Pricing, get me the pricing details of deepsek-chat",
        llm=llm
    )

    result = await agent.run()
    print(result)
asyncio.run(main())
