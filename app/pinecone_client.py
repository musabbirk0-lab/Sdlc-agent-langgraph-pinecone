import os
import pinecone


API_KEY = os.environ.get('PINECONE_API_KEY')
ENV = os.environ.get('PINECONE_ENV')
INDEX_NAME = os.environ.get('PINECONE_INDEX','sdlc-index')


def init_pinecone():
if not API_KEY:
raise EnvironmentError('PINECONE_API_KEY missing')
pinecone.init(api_key=API_KEY, environment=ENV)
if INDEX_NAME not in pinecone.list_indexes():
pinecone.create_index(INDEX_NAME, dimension=1536)
return pinecone.Index(INDEX_NAME)
