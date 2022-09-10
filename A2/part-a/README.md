A.0
===

Answer
------

`7567000`

Request
-------

```json
{
  "jsonrpc": "2.0",
  "method": "eth_blockNumber",
  "params": [],
  "id": 1
}
```

Response
--------

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": "0x737698"
}
```

A.1
===

Answer
------

`99999998`

Request
-------

```json
{
  "jsonrpc": "2.0",
  "method": "eth_gasPrice",
  "params": [],
  "id": 1
}
```

Response
--------

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": "0x5f5e0fe"
}
```


A.2
===

Answer
------

`63`

Request
-------

```json
{
  "jsonrpc": "2.0",
  "method": "eth_getBlockTransactionCountByHash",
  "params": [
    "0x78f20591bc53a4a06d28cc3a841608dc8637e669999f9cc854addd0a66024e78"
  ],
  "id": 1
}
```

Response
--------

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": "0x3f"
}
```


A.3
===

Answer
------

```
blockNumber: 5426162
blockHash: 0xe0018a6ff3a66fd5cb0f448c2048c4456eb238f1a4592412a92e49a1b9122817
cumulativeGasUsed: 200000
transactionIndex: 212
```

Request
-------

```json
{
  "jsonrpc": "2.0",
  "method": "eth_getTransactionByHash",
  "params": [
    "0x4210f581dda42ea2a2676fefa9edf784095a30ae2b49920e0965588d8fa78bf9"
  ],
  "id": 1
}
```

Response
--------

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "blockHash": "0xe0018a6ff3a66fd5cb0f448c2048c4456eb238f1a4592412a92e49a1b9122817",
    "blockNumber": "0x52cbf2",
    "chainId": "0x5",
    "from": "0x5217f29a4d1f96b5bc7951d95a13458cc34910df",
    "gas": "0x30d40",
    "gasPrice": "0x3b9aca00",
    "hash": "0x4210f581dda42ea2a2676fefa9edf784095a30ae2b49920e0965588d8fa78bf9",
    "input": "0x5feeed8d",
    "nonce": "0x1",
    "r": "0xdc3508887268d5aa9d8ba97192f27a240e30825dc38a9adaa5bd363732d86d84",
    "s": "0x177a797c0383c92062fe476d5361f3c22d787210718e061a11e190eea5dd9e07",
    "to": "0x07aaec0b237ccf56b03a7c43c1c7a783da560642",
    "transactionIndex": "0xd4",
    "type": "0x0",
    "v": "0x2e",
    "value": "0x0"
  }
}
```

A.4
===

Answer
------

`17`

Request
-------

```json
{
  "jsonrpc": "2.0",
  "method": "net_peerCount",
  "params": [],
  "id": 1
}
```

Response
--------

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": "0x11"
}
```

A.5
===

Answer
------

`1949960055592287000`

Request
-------

```json
{
  "jsonrpc": "2.0",
  "method": "eth_getBalance",
  "params": [
    "0x35F18427567108F800BDC2784277B9246eED37fA",
    "latest"
  ],
  "id": 1
}
```

Response
--------

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": "0x1b0fa656d7c77b18"
}
```


A.6
===

Answer
------

`0x4d44e869d323cc93ed935280337cc07e3a7194810525e12b30f39cea4063562b`

Request
-------

```json
{
  "jsonrpc": "2.0",
  "method": "eth_getTransactionByBlockNumberAndIndex",
  "params": [
    "0x52a96a",
    "0x1"
  ],
  "id": 1
}
```

Response
--------

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "blockHash": "0x6218c39ea8f67e291c706438a2a7698419426c7de840723e82e0733d10247fc4",
    "blockNumber": "0x52a96a",
    "chainId": "0x5",
    "from": "0x5c3f649ffdbc91a247ac45fc2c4c63f9319e5135",
    "gas": "0x186a0",
    "gasPrice": "0x12a05f200",
    "hash": "0x4d44e869d323cc93ed935280337cc07e3a7194810525e12b30f39cea4063562b",
    "input": "0xa9059cbb00000000000000000000000065d3aece81f66a579dcb2040f63bdfbd85177faf0000000000000000000000000000000000000000000000000e0a3cc5314d1a52",
    "nonce": "0x5d9fe",
    "r": "0x1f30e95087fdaffe23582d06a8fae040e0da43d03d5ab2c783ab99a67f4e61a4",
    "s": "0x1f4a014194f68129dd41cbd795d66ff81d6c72ff004fcd5893129eb786e6caf",
    "to": "0xf74a5ca65e4552cff0f13b116113ccb493c580c5",
    "transactionIndex": "0x1",
    "type": "0x0",
    "v": "0x2d",
    "value": "0x0"
  }
}
```
