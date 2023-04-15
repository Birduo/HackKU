#localhost:8080
import weaviate

client = weaviate.Client(
    url = "http://localhost:8080",  # Replace with your endpoint
)

client.schema.get()
'''
plant_obj = {
    'class' : "Plant",
    'vectorizer' : "text2vec-contextionary"
}


client.schema.create_class(plant_obj)'''


'''
in file
--------
sci_name url states  common_name

data
----
[
    {
        sci_name : value,
        url : value,
        states : [value],
        common_name : value
    },
    {
        sci_name : value,
        url : value,
        states : [value],
        common_name : value
    }, ...
]
'''

filename = "flower_info.txt"
data_file = open(filename, 'r', encoding='UTF8')
data = []
flag = 0
for line in data_file:
    print(flag)
    flag+=1
    linelist = line.strip().split('\t')
    data.append({
        'name' : linelist[0],
        'description' : linelist[3].replace('â€“', '-').replace("Ã—", '*'),
        'states' : linelist[2],
        'common_name' : linelist[1]
    })
data_file.close()

with client.batch as batch:
    batch.batch_size=20
    # Batch import all Questions
    for datapoint in data:
    
        properties = {
            "name": datapoint["name"],
            "description": datapoint["description"],
            "states": datapoint["states"],
            'common_name' : datapoint['common_name']
        }

        client.batch.add_data_object(properties, "Plant")
print(client.query.aggregate("Plant").with_meta_count().do())
