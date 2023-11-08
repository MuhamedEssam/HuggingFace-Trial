
from transformers import pipeline

captioner = pipeline("image-to-text",model="Salesforce/blip-image-captioning-base")
generator = pipeline('text-generation', model = 'gpt2')


caption=captioner(img_url)
story_generated=generator(caption[0]['generated_text'], max_length = 100, num_return_sequences=1)
story_generated[0]['generated_text']

st.text("Story Generated",story_generated[0]['generated_text'] )
