def search_by_parameter(es,parameter, term):
    query = {
        "query": {
            "match": {
            parameter: term}
            }
        }
    res = es.search(index="astronauts", body=query)  
    hits = res['hits']['hits']
    astronauts = []    
    for astronaut in hits:
        astronauts.append(astronaut['_source'])


    response_body = {
        "hits" : len(astronauts),
        "results" : astronauts
    }
    return response_body