from elasticsearch import Elasticsearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth

host = 'search-hillcyber-elsearch-rm5e5x4fido7yjkh4heavmton4.us-east-1.es.amazonaws.com'
awsauth = AWS4Auth('elsearch', 'AKIAIRVJGCEFMDAIQ4XQ', 'us-east-1', 'es')
es = Elasticsearch(
    hosts=[{'host': host, 'port': 443}],
    http_auth=awsauth,
    use_ssl=True,
    verify_certs=True,
    connection_class=RequestsHttpConnection
)
print(es.info())
