import openai

# Замените "ваш_ключ_здесь" на ваш фактический ключ API
api_key = "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"
# Создайте экземпляр класса OpenAI с использованием ключа API
openai.api_key = api_key

# Ваш остальной код здесь
# ...

# Например:
response = openai.Completion.create(
  engine="text-davinci-002",
  prompt="Translate the following English text to French: '{}'",
  max_tokens=60
)

print(response['choices'][0]['text'])
