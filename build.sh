#!/bin/bash

# shellcheck disable=SC2164
if [ ! -d "stubs" ]; then
  mkdir -p "stubs"
else
  rm -rf ./stubs/*pb2*.py
fi
touch stubs/__init__.py
echo "*************************"
echo $(pwd)

cd ./protos
echo "*************************"
echo $(pwd)

python -m grpc_tools.protoc \
        -I ./ \
        --python_out=../ \
        --grpc_python_out=../ \
        stubs/*.proto

cd ..
echo "*************************"
echo $(pwd)
echo "*************************"
mkdir -p ./shop/stubs
mkdir -p ./retailer/stubs


rm -rf ./shop/stubs/*_pb2*.py
rm -rf ./retailer/stubs/*_pb2*.py

touch ./shop/stubs/__init__.py
touch ./retailer/stubs/__init__.py

cp -r ./stubs/*.py ./shop/stubs
cp -r ./stubs/*.py ./retailer/stubs
