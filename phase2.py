# PHASE 2:Autonomous Content Engine (LangGraph)

from langgraph.graph import StateGraph
from typing import TypedDict



def mock_search(query: str):            ## fake search function (it behave as a internet search) as weare given predifined result

    """Return fake news based on query keyword."""
    
    if "AI" in query:
        return "OpenAI releases powerful new model"
    elif "crypto" in query:
        return "Bitcoin hits all-time high"
    else:
        return "Latest global news update"


class GraphState(TypedDict):            #graph state (flowing data inside)
    topic: str
    context: str
    bot_id: str
    post_content: str


def decides(state):                #it decide which topic is posted
    return {
        "topic": "Latest AI news",
        "bot_id": "BotA"
    }


def searchs(state):                    #here we doing fake search function call
    result = mock_search(state["topic"])
    return {
        "context": result
    }

def generates(state):                 # generating actual social media post
    return {
        "bot_id": state["bot_id"],
        "topic": state["topic"],
        "post_content": f" {state['context']} - Tech is the future!"[:280]
    }


builder = StateGraph(GraphState)       #build graph (flow create)

builder.add_node("decide", decides)
builder.add_node("search", searchs)
builder.add_node("generate", generates)

builder.set_entry_point("decide")
builder.add_edge("decide", "search")
builder.add_edge("search", "generate")

graph = builder.compile()

result = graph.invoke({})           #run graph

final_output = {                    # Clean final output (assignment format)
    "bot_id": result["bot_id"],
    "topic": result["topic"],
    "post_content": result["post_content"]
}

print("\n Final Output:\n")
print(final_output)