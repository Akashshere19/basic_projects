from django.shortcuts import render
import requests
def output(requests):
    data=requests.get("https://regres.in/api/users")
    print(data.text)
    data=data.text
    return render(requests,'home.html',{'data':data})
    