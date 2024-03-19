import os
import numpy as np

from hiddenlayer import HiddenlayerServiceClient

hl_client = HiddenlayerServiceClient(
    host="https://api.hiddenlayer.ai",
    api_id=os.environ.get("HL_CLIENT_ID"),
    api_key=os.environ.get("HL_CLIENT_SECRET"),
)

# Generate some mock data
X = np.random.rand(100, 5)
y = np.random.rand(100, 1)

# First you have to create a model
model = hl_client.model.create(model_name="example_model")

# If you already have a model you can get the model id from the HiddenLayer model object
model = hl_client.model.get(model_name="example_model")


# Submit vectors to MLDR
hl_client.mldr.submit_vectors(
    model_id=model.sensor_id,
    input_vectors=X,
    output=y,
)
