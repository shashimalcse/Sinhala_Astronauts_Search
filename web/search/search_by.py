def search_by_mission(es,missions):
    query = {
        "query": {
            "terms": {
            "Mission_names": missions
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

def search_by_faceted(es,data):
    filters = []

    for filterobj in data['filter']:
        matchObj = {
            "match" : filterobj
        }
        filters.append(matchObj)

    query = {
            "query": {
                "bool": {
                "must": [
                    {
                    "query_string": {
                        "query": data['term']
                    }
                    }
                ],
                "filter": filters
                }
            },
            "aggs" : {
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
                },
                "Summary filter" : {
                    "terms" : { 
                    "field" : "Summary.keyword",
                    "size": 5
                    
                    } 
                },
                "Mission_names filter" : {
                    "terms" : { 
                    "field" : "Mission_names.keyword",
                    "size": 5
                    } 
                },
                "Name filter" : {
                    "terms" : { 
                    "field" : "Name.keyword",
                    "size": 5
                    
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


def advanced_search(es,data):
    mustobj = []

    for filterobj in data['filter']:
        matchObj = {"term" : {filterobj['keyword'] : filterobj['value']}}
        mustobj.append(matchObj)
    ranges = []
    for rangeObj in data['ranges']:
        obj = {rangeObj['keyword'] : rangeObj['range']}
        ranges.append(obj)

    query = {
            "size" : 10,
            "query" : {
                "bool" : {
                "must" : [
                    {
                    "bool" : {
                        "must" : mustobj
                    }
                    },
                    {
                    "bool":{
                    "must" : [{
                    "range" : range
                    } for range in ranges]
                    }
                    }
                
                ]
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



