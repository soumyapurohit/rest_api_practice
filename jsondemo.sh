#!/bin/sh

data=$(curl -X GET https://api.github.com/)
echo $data
