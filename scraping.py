#################3
import requests
from bs4 import BeautifulSoup as bs
user_name= "mathew19642" #ask for yhe input of the user input
url = "https://github.com/" + user_name
results = requests.get(url)
soup = bs(results.content, "html.parser")
profile_pic = soup.find(' img' , {'alt' : 'Avatar'})
print(profile_pic)