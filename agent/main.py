import asyncio
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from mcp_use import MCPAgent, MCPClient

async def main():
    load_dotenv()

    
    config = {
      "mcpServers": {
        "playwright": {
          "command": "npx",
          "args": ["@playwright/mcp@latest"],
          "env": {
            "DISPLAY": ":1"
          }
        }
      }
    }

    client = MCPClient.from_dict(config)
    

    llm = ChatGroq(model="qwen-qwq-32b", api_key=os.getenv("GROQ_API_KEY"))

    agent = MCPAgent(llm=llm, client=client, max_steps=30)

    result = await agent.run(
        "what is the weather now in tunis",
    )
    print(f"\nResult: {result}")

if __name__ == "__main__":
    asyncio.run(main())