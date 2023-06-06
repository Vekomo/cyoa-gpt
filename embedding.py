import openai
import pinecone
import os

from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
pinecone_api_key = os.getenv("PINECONE_API_KEY")
pinecone_environment = os.getenv("PINECONE_ENVIRONMENT")
pinecone.init(
    api_key = pinecone_api_key,
    environment = pinecone_environment
)

index_name = "cyoa"

embed_model = "text-embedding-ada-002"
'''
 try:
        res = openai.Embedding.create(input=texts, engine=embed_model)
    except:
        done = False
        while not done:
            sleep(5)
            try:
                res = openai.Embedding.create(input=texts, engine=embed_model)
                done = True
            except:
                pass

'''

res = openai.Embedding.create(
    input=[
        "In the Kingdom of Lorobo, there is a man named Janus the sly. He is a very weird guy.",
        "In the Kingdom of Lorobo, unicorns are real. There's no proof, but they just know."
    ], engine=embed_model
)

if index_name not in pinecone.list_indexes():
    pinecone.create_index(
        index_name,
        dimension=len(res['data'][0]['embedding']),
        metric='cosine',
        metadata_config={
            'indexed': ['channel_id', 'published'],
        }
    )
    
index = pinecone.Index(index_name)

embeds = [record['embedding'] for record in res['data']]

index.upsert(vectors=embeds)

def embed_text(text):
    embed_model = "text-embedding-ada-002"
    
    res = openai.Embedding.create(
        input =[
            text
        ], engine = embed_model
    )
    
    # query vector for pinecone
    xq = res['data'][0]['embedding']
    
    
    return res