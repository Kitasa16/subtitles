

import deepl
import wave
import whisper


# Set up the DeepL API client with your API key
translator = deepl.Translator(your_api_key_here)

# Translate a text using DeepL
text = '我今天去了公园'
result = translator.translate_text(text,target_lang="JA")

# Print the translated text
print(result)






