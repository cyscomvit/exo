from exo.exocore import ExoCore

API_KEY = "" #Enzoic API Key here
SECRET_KEY = "" #Enzoic Secret Key here
exo = ExoCore(API_KEY, SECRET_KEY)

result = exo.results("abc123@12")

print(result)
