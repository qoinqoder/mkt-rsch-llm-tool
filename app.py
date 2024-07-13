import streamlit as st
from elasticsearch import Elasticsearch
from openai import OpenAI

client = OpenAI(api_key='')
import requests

# Initialize Elasticsearch client
es = Elasticsearch(hosts = ['https://localhost:9200'],
                   verify_certs = False,
                   http_auth=('elastic', '7d2s+DGTc9MnWpunVqU6'))

# OpenAI API Key

# Streamlit App
st.title("Market Evaluation Tool")
st.write("Enter your market research query below:")

query = st.text_input("Query")

if st.button("Search"):
    if query:
        # Retrieve documents from Elasticsearch
        res = es.search(index="market_research", body={"query": {"match": {"content": query}}})
        documents = [hit['_source']['content'] for hit in res['hits']['hits']]

        if documents:
            # Generate response using OpenAI GPT-4
            gpt_response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": f"Summarize the following information based on the query: {query}\n\nDocuments:\n" + "\n".join(documents)}])
            # ,
            #     prompt=f"Summarize the following information based on the query: {query}\n\nDocuments:\n" + "\n".join(documents),
            #     max_tokens=10)

            st.write("### Response:")
            st.write(gpt_response.choices[0].message.content.strip())
        else:
            st.write("No relevant documents found.")
    else:
        st.write("Please enter a query.")
