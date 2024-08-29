#!/bin/bash
#
# Generate the reports for the standards validator

echo "Running generate configuration schema script"
echo "Current working directory: $(pwd)"
echo "Contents of current working directory: $(ls -a)"
echo "Creating schemas folder in case it does not exist"
mkdir -p ./schemas
node ./ts-to-json-schema.js
echo "Contents of the schemas folder: $(ls ./schemas)"
echo "Finished running generate configuration schema script"