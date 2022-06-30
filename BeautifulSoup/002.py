from bs4 import BeautifulSoup
import requests

url = requests.get('https://realpython.github.io/fake-jobs/')
# print(url.text)
soup = BeautifulSoup(url.content, 'html.parser')
# print(soup.prettify())

job_elements = soup.find_all("div", class_='card-content')
# print(job_elements)

for job_element in job_elements:
	print(job_element, end="\n"*2)
