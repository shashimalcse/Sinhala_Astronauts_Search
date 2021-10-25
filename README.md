# Sinhala-Astronauts-Search-Engine
Astronauts details search engine for Sinhalese language using Elasticsearch python and docker. 

The corpus contains Astronauts details with the following parameters. The corpus is created by using a wikipedia astronauts details page.
1. 'Name'
2. 'Birth day'
3. 'Status'
4. 'Nationality'
5. 'Space Time'
6. 'Mission names'
7. 'Selection'
8. 'Occupation'
9. 'Summary'

### Quick start
#### Pre requesists : 
- Docker and Docker compose

#### Steps : 
1. Clone the repository.
2. Run build.sh (```bash build.sh``` or ```./build.sh```).
3. Run ```docker exec -it web bash -c "python3 utils/wiki_scrap.py; bash"``` to put the corpus to the Elasticsearch.
4. Now you can create requests to below-mentioned endpoints.

#### Endpoints and techniques used in designing indexing and querying

| Endpoint  | Request Type | Functionality | Example |
| ------------- | ------------- | ---------- | -----------|
| /searchBy/param  | GET  | Search by specific filed with a term  |  /searchBy/param?searchby=Nationality&term=ඇමෙරිකානු |
| /searchBy/bday  | GET  | Range search by birth day  |  /searchBy/bday?to=2000-08-05&from=1920-08-07 |
| /searchBy/time  | GET  | Range search by space time  |  /searchBy/time?gt=0&lt=12000 |
| /searchBy/missions  | GET  | Search by mission names  |  /searchBy/missions?missions=STS-119,Soyuz TM-12 |
| /facetedSearch  | POST  | After selecting filters from received facets request to this with the term and selected filters  |  /facetedSearch { "term": "1960-08-26", "filter" : [ {"Nationality" : "ඇමෙරිකානු"}, {"Occupation": "නියමු"}]}  | 
| /advanceSearch  | POST  | Search with given set of fields including range of birthday and space time  |  /advanceSearch { "filter" : [ {"keyword" : "Nationality", "value": "ඇමෙරිකානු" },{"keyword" : "Status", "value": "විශ්රාමික" } ], "ranges": [ {"keyword" : "Time", "range": {"gte" : 0, "lte": 12000} }, {"keyword" : "BDay", "range": {"gte" : "1920-08-05", "lte": "1970-08-05"} }]} |

Also you can find those endpoints in postman collection
