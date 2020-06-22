# Multi-Container Docker Template (Flask, Elasticsearch, Kibana)

Run `build.sh` to spin up the containers using `docker-compose.yml`.

```
./build.sh
```

Elasticsearch is accessed at `http://localhost:9200`.
Kibana is accessed at `http://localhost:5601`.
The Flask application is accessed at `http://localhost:5000`.

Within other containers, Elasticsearch is accessed at `http://elasticsearch:9200`.