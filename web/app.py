from flask import Flask
from elasticsearch import Elasticsearch
import os
import search.search_all as search_all
import search.search_by_parameter as search_by_parameter
import search.search_by as search_by
from flask import jsonify
from flask import request

es_host = os.environ['ELASTICSEARCH_URL']
print('Elastic host is {}'.format(es_host))
es = Elasticsearch([es_host])

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return jsonify(search_all.search_all(es))
@app.route('/searchBy/param')
def searchby_param():
    parameter = request.args.get('searchby')
    term = request.args.get('term')
    return search_by_parameter.search_by_parameter(es,parameter, term)
@app.route('/searchBy/missions')
def searchby_mission():
    missions = request.args.get('missions')
    missions = missions.strip()
    missions = [x.strip() for x in missions.split(',')]
    return search_by.search_by_mission(es,missions)    
@app.route('/searchBy/bday')
def searchby_bday():
    to = request.args.get('to')
    from_d = request.args.get('from')
    return search_by.search_by_bdate(es,to,from_d)   
@app.route('/searchBy/time') 
def searchby_time():
    lt = request.args.get('lt')
    gt = request.args.get('gt')
    return search_by.search_by_time(es,lt,gt)      
@app.route('/facetedSearch', methods=['GET', 'POST'])
def faceted_search():                                                                                                                              
    data = request.get_json()
    return search_by.search_by_faceted(es,data)      
@app.route('/advanceSearch', methods=['GET', 'POST'])
def advance_search():                                                                                                                              
    data = request.get_json()
    return search_by.advanced_search(es,data)      
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')