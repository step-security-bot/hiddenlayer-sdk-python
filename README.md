# HiddenLayer SDK Python (Beta)

Hiddenlayer is a Python SDK that provides a simple and efficient way to interact with the Hiddenlayer API, a platform for building and deploying machine learning models. The SDK allows developers to easily protect models using the Hiddenlayer API, without having to write complex code or manage the underlying infrastructure.

## Contents

- [Installation](#installation)
- [Getting started](#getting-started)
- [Code examples](#code-examples)
- [Interface stability](#interface-stability)


## Installation

Install from PyPi using [pip](https://pip.pypa.io/en/latest/), a package manager for Python.

`pip install git+https://github.com/hiddenlayerai/hiddenlayer-sdk-python.git`

## Getting Started

Once you've installed the hiddenlayer-python package, instantiate the `HiddenlayerServiceClient`:

```python
from hiddenlayer import HiddenlayerServiceClient

hl_client = HiddenlayerServiceClient(
  host="https://api.hiddenlayer.ai",
  api_id=..., # Your Hiddenlayer API Client ID
  api_key=... # Your Hiddenalyer API Secret Key
)

hl_client.model_scanner.scan_model_file(model_id="name_of_the_model", model_path="path/to/model/file.pkl")
```

## Code Examples

Code examples can be found in the repo [here](https://github.com/hiddenlayerai/hiddenlayer-sdk-python/tree/main/examples)

## Interface Stability

Hiddenlayer is actively working on stabilizing the Hiddenlayer SDK for Python's interfaces. You are highly encouraged to pin the exact dependency version.
