import weaviate

client = weaviate.Client("http://localhost:8080")  # Replace with your endpoint

# delete class "YourClassName" - THIS WILL DELETE ALL DATA IN THIS CLASS
client.schema.delete_class("Plant")