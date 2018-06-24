#!/usr/bin/env bash
curl -X POST \
  http://localhost:8080/api/v1/shipping \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \
  -H 'postman-token: 543c451e-858a-e503-c05d-1863a0ad3078' \
  -d '{
	"origin": "Ukraine",
	"package_type": "letter",
	"destination": "Ukraine",
	"dimensions": [10, 11, 1.0],
	"weight": 11.1
}'