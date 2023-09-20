# MASSA PROTO PYTHON

Generated Python class from protobuf files for Massa blockchain.

# Quickstart

* Create a fresh venv
  * python3 -m venv venv
  * venv/bin/python -m pip install -e __PATH_TO_MASSA_PROTO_PYTHON_REPO__
* run python from this venv:
  * venv/bin/python

```python

import asyncio
import betterproto
from grpclib.client import Channel

from massa_proto_python.massa.api.v1 import (
    PublicServiceStub,
    PrivateServiceStub,
    GetStatusRequest,
    GetStatusResponse
)

async def public_grpc_call(
    self, host: str, port: int, function_name: str, request: betterproto.Message
) -> betterproto.Message:
    # Note: asyncio.run will create a new event loop - channel must be created in this event loop
    #       that's why we need to have everything in this 'generic' function
    channel = Channel(host=host, port=port)
    service = PublicServiceStub(channel)
    f = getattr(service, function_name)
    result = await f(request)
    # Avoid warning message
    channel.close()
    return result

def get_status(host: str, pub_grpc_port: int):
    request = GetStatusRequest()
    get_status_response: GetStatusResponse = asyncio.run(
        public_grpc_call(host, pub_grpc_port, "get_status", request)
    )

if __name__ == "__main__":
    get_status("127.0.0.1", 33037)
```

# Regen 

* clone massa-proto
* python3 -m venv venv
* venv/bin/python -m pip install betterproto==2.0.0b6
* PATH=$PATH:venv/bin/ protoc -I$HOME/dev/massa-proto/proto/commons/ -I$HOME/dev/massa-proto/proto/apis/massa/api/v1/ -I$HOME/dev/massa-proto/proto/third_party/ --python_betterproto_out=massa_proto_python $HOME/dev/massa-proto/proto/apis/massa/api/v1/public.proto $HOME/dev/massa-proto/proto/apis/massa/api/v1/private.proto
