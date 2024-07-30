import google.generativeai as genai
from google.generativeai import GenerationConfig
from eli.settings.main import settings

genai.configure(api_key=settings.API_GENAI)

generation_config = GenerationConfig(
    temperature=1,
    top_p=0.95,
    top_k=64,
    max_output_tokens=8192,
    response_mime_type="text/plain",
)

model = genai.GenerativeModel(model_name=settings.MODEL_NAME, generation_config=generation_config)
