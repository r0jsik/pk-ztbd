curl localhost:9200/index \
  -X PUT \
  -H 'Content-Type: application/json' \
  -d '{ "settings" : { "index" : { } }}'
