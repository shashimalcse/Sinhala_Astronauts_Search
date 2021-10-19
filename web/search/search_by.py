def search_by_mission(es,missions):
    query = {
        "query": {
            "bool": {
            "filter": {
                "term": {
                "Status": missions[0],
                }
            }
            }
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

def search_by_bdate(es,to,from_d):
    query = {
        "query": {
                "range": {
                    "BDay": {
                    "lt": to,
                    "gt": from_d,
                    "format": "yyyy-MM-dd"
                    }
                }
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
def search_by_time(es,lt,gt):
    query = {
        "query": {
                "range": {
                    "Time": {
                    "lt": lt,
                    "gt": gt,
                    }
                }
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
