#!/bin/bash

for i in {1..20}
do
	
	response=$(
	  curl -s POST 'https://whp998h5y8.execute-api.eu-west-1.amazonaws.com/Prod/hello/'\
		  --data-raw '{"name":"Joker"}')
	echo $response
done
