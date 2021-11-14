import requests
from bs4 import BeautifulSoup

domain = "https://www.bayt.com"
bayt_url = f"{domain}/en/jordan/jobs/software-developer-jobs/"
response = requests.get(bayt_url)


html_text = response.text
# print(response.text)
with open("file.html", "w") as file:
    file.write(html_text)
# print(html_text)
soup = BeautifulSoup(html_text, "html.parser")
result = soup.find("div", id="results_inner_card")
jobs = result.find_all("li", class_="has-pointer-d")
print(len(jobs))
print(jobs[0])

title = jobs[0].find("h2").text.strip()
company = jobs[0].find("b").text.strip()
desc = jobs[0].find("p").text.strip()
salary_container = jobs[1].find("i", class_="is-salary")
salary = salary_container.parent.text.strip() if salary_container else None
# .parent.text.strip()
link = f"{domain}{jobs[0].find('a').get('href')}"

print(title)
print(company)
print(desc)
print(link)
print(salary)
cleaned_jobs = []
for job in jobs:
    title = job.find("h2").text.strip()
    company = job.find("b").text.strip()
    desc = job.find("p").text.strip()
    link = f"{domain}{job.find('a').get('href')}"
    salary_container = job.find("i", class_="is-salary")
    salary = salary_container.parent.text.strip() if salary_container else None
    cleaned_job = {
        "title": title,
        "company": company,
        "desc": desc,
        "link": link,
        "salary": salary,
    }
    cleaned_jobs.append(cleaned_job)
print(cleaned_jobs)


def clean_job(dirty_job):
    title = dirty_job.find("h2").text.strip()
    company = dirty_job.find("b").text.strip()
    desc = dirty_job.find("p").text.strip()
    link = f"{domain}{dirty_job.find('a').get('href')}"
    salary_container = job.find("i", class_="is-salary")
    salary = salary_container.parent.text.strip() if salary_container else None
    return {
        "title": title,
        "company": company,
        "desc": desc,
        "link": link,
        "salary": salary,
    }


cleaned_jobs = [clean_job(job) for job in jobs]
print(cleaned_jobs)


import json

json_data = json.dumps(cleaned_jobs)
print(json_data)
with open("bayt_json_data.json", "w") as file:
    file.write(json_data)
quit()
