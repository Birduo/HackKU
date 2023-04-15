import weaviate
import json

client = weaviate.Client(
    url="http://localhost:8080",  # Replace with your endpoint
)

bm25 = {
    "query" : "Kansas with purple flowers",
    'properties' : ["states^10", "description"]
}
result = (
    client.query
    .get("Plant", ["name", "description", "states", "common_name"])
    .with_bm25(bm25['query'], bm25['properties'])
    .with_limit(10)
    .do()
)

results = result['data']['Get']['Plant']
for result in results:
    print(result)