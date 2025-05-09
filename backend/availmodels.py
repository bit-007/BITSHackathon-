import openai

client = openai.OpenAI(
    api_key="[Enter API KEY]"
    base_url="https://aiproxy.sanand.workers.dev/openai/v1"
)

try:
    models = client.models.list()
    print("Available Models:", [model.id for model in models.data])
except Exception as e:
    print("Error:", e)
