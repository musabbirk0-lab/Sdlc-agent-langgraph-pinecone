from fastapi import FastAPI
from .langgraph_agent import SDLCSpecAgent


app = FastAPI()
agent = SDLCSpecAgent()


@app.get("/health")
def health():
return {"status": "ok"}


@app.post("/run")
async def run_agent(query: dict):
# query: {"task": "create_test_cases", "context": "..."}
result = await agent.run(query)
return {"result": result}
