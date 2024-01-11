import openai

# Устанавливаем ключ API
openai.api_key = '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'
# Текст, на основе которого будет генерироваться ответ
# Текст, на основе которого будет генерироваться ответ
input_text = "Задайте вопрос GPT-3:"

# Вызываем GPT-3 для генерации ответа
response = openai.completions.create(
    model="text-davinci-001",  # Выберите подходящую модель, например, "text-davinci-003"
    prompt=input_text,
    max_tokens=150  # Максимальное количество токенов в ответе
)

# Извлекаем сгенерированный текст из ответа
generated_text = response['choices'][0]['text'].strip()

# Выводим сгенерированный текст
print("Ответ GPT-3:", generated_text)