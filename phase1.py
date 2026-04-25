#  Vector-Based Persona Matching

from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings


embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")   #convert the text into number

vectorstore = Chroma(                     #for storing the bots personality in database
    collection_name="bot_personas",
    embedding_function=embedding
)

personas = [                                #every bot has their name and behavior
    ("BotA", "I believe AI and crypto will solve all human problems."),
    ("BotB", "I believe capitalism is destroying society."),
    ("BotC", "I care about markets and ROI.")
]

for bot_id, text in personas:                #using loop for adding bot and storing bot personalities in database
    vectorstore.add_texts(
        texts=[text],
        metadatas=[{"bot_id": bot_id}]
    )

print("Personas added sucessfully")