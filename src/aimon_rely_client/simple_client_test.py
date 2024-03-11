# Run python3 setup.py install --user

# Generated by CodiumAI

import pytest
from aimon_rely_client.simple_client import SimpleAimonRelyClient, RetryableError

API_KEY = "YOUR API KEY HERE"
class TestSimpleAimonRelyClient:

    #  Sends an HTTP POST request to the Aimon Rely Hallucination Detection API with valid data and receives a valid response
    def test_valid_data_valid_response(self):
        client = SimpleAimonRelyClient(api_key=API_KEY)
        data_to_send = [{"context": "This is the context", "generated_text": "This is the context"}]
        response = client.detect(data_to_send)
        assert "is_hallucinated" in response
        assert response["is_hallucinated"] == "False"
        assert "score" in response
        assert "sentences" in response
        assert len(response["sentences"]) == 1

    #  Sends an HTTP POST request to the Aimon Rely Hallucination Detection API with a single dict object containing a valid "context" and "generated_text" but with a very short text and receives a valid response
    def test_short_text_valid_response(self):
        client = SimpleAimonRelyClient(api_key=API_KEY)
        short_text = "a"
        data_to_send = [{"context": "This is the context", "generated_text": short_text}]
        response = client.detect(data_to_send)
        assert "is_hallucinated" in response
        assert response["is_hallucinated"] == "True"
        assert "score" in response
        assert "sentences" in response
        assert len(response["sentences"]) == 1

    #  Sends an HTTP POST request to the Aimon Rely Hallucination Detection API with a single dict object containing a valid "context" and "generated_text" but with a text containing special characters and receives a valid response
    def test_special_characters_valid_response(self):
        client = SimpleAimonRelyClient(api_key=API_KEY)
        special_text = "!@#$%^&*()_+"
        data_to_send = [{"context": "This is the context", "generated_text": special_text}]
        response = client.detect(data_to_send)
        assert "is_hallucinated" in response
        assert response["is_hallucinated"] == "True"
        assert "score" in response
        assert "sentences" in response
        assert len(response["sentences"]) == 12
