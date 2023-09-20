# MASSA PROTO PYTHON

Generated Python class from protobuf files for Massa blockchain.

# Regen 

* clone massa-proto
* python3 -m venv venv
* venv/bin/python -m pip install betterproto==2.0.0b6
* PATH=$PATH:venv/bin/ protoc -I$HOME/dev/massa-proto/proto/commons/ -I$HOME/dev/massa-proto/proto/apis/massa/api/v1/ -I$HOME/dev/massa-proto/proto/third_party/ --python_betterproto_out=massa_proto_python $HOME/dev/massa-proto/proto/apis/massa/api/v1/public.proto $HOME/dev/massa-proto/proto/apis/massa/api/v1/private.proto