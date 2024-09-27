# pip install requests
import requests

print("\nImportação e uso de um módulo de terceiros")

url = "https://www.example.com"
response = requests.get(url)
print(f"O status de retorno é: {response.status_code}")