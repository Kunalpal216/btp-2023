import pprint
import time
import google.generativeai as palm

palm.configure(api_key='AIzaSyBKAer3Wb0zixnOOEDIIpvaU1mNxUVLq4E')

model_id = "btp-news"
operation = palm.create_tuned_model(
  id = model_id,
  source_model="models/text-bison-001",
  training_data=[{'text_input': 'example input', 'output': 'example output'},...]
)
tuned_model=operation.result()      # Wait for tuning to finish

palm.generate_text(f"tunedModels/{model_id}", prompt="...")