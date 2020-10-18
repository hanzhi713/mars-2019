#!/bin/bash

mkdir -p protos
cd protos
rm jetsonrpc.proto
wget https://raw.githubusercontent.com/hanzhi713/mars-ros/master/src/rpc-server/jetsonrpc.proto
cd ..
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. protos/jetsonrpc.proto
