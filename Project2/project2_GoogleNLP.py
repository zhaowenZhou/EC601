# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 18:05:38 2021

@author: 16418
"""
from google.cloud import automl

project_id = "project_id"
model_id = "model_id"
content = "your .txt content path"

prediction_client = automl.PredictionServiceClient()
model_full_id = automl.AutoMlClient.model_path(project_id, "us-central1", model_id)

file_path = content
with open(file_path, 'rb') as ff:
    content = ff.read()


payload = content

analysis = prediction_client.predict(name = model_full_id, payload = payload)

for annotation_payload in analysis.payload:
    print(
        'Predicted sentiment score:{}'.format(
            annotation_payload.text_sentiment.sentiment
            )
        )
    
