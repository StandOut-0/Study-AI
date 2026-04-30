import requests
def main():
 response = requests.get("https://api.github.com")
 print("상태 코드:", response.status_code)
#  print("응답 일부:", response.text[:100])
 print("응답 일부:", response.text)

if __name__ == "__main__":
 main()