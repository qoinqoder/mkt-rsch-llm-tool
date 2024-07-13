from elasticsearch import Elasticsearch
import json

# Initialize Elasticsearch client
es = Elasticsearch(hosts = ['https://localhost:9200'],
                   verify_certs = False,
                   http_auth=('elastic', '7d2s+DGTc9MnWpunVqU6'))

# Index documents
def index_documents(documents):
    for i, doc in enumerate(documents):
        es.index(index="market_research", id=i, body=doc)

# Load and index documents
with open('market_data.json') as f:
    documents = json.load(f)
    index_documents(documents)