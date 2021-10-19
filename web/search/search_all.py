
def search_all(es):
    query = {
            "size" : 100,
            "query": {
                "match_all": {}
            },
            "aggs" : {
                    "Name filter" : {
                        "terms" : { 
                        "field" : "Name.keyword",
                        "size": 5
                        } 
                    },
                    "Status filter" : {
                        "terms" : { 
                        "field" : "Status.keyword",
                        "size": 5
                        
                        } 
                    },
                    "Nationality filter" : {
                        "terms" : { 
                        "field" : "Nationality.keyword",
                        "size": 5
                        
                        } 
                    },
                    "Occupation filter" : {
                        "terms" : { 
                        "field" : "Occupation.keyword",
                        "size": 5
                        } 
                    }
                }
        }
    res = es.search(index="astronauts", body=query)  
    with open('test.txt', 'w') as f:
        f.write(str(res))
        f.close()
    hits = res['hits']['hits']
    astronauts = []

    for astronaut in hits:
        astronauts.append(astronaut['_source'])

    facets = res['aggregations']
    
    response_body = {
        "results" : astronauts,
        "facets" : {
            "Name filter" : facets['Name filter']['buckets'],
            "Status filter" : facets['Status filter']['buckets'],
            "Nationality filter" : facets['Nationality filter']['buckets'],
            "Occupation filter" : facets['Occupation filter']['buckets'],
        }      
    }
    return response_body
