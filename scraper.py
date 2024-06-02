import requests
from bs4 import BeautifulSoup

link = "https://wuzzuf.net/search/jobs/?a=navbl&q=data%20science%20jobs&start=0"
res = requests.get(link)
soup = BeautifulSoup(res.text, "html.parser")
pages = soup.find("li", attrs={"class":"css-8neukt"}).text.split(" ")
jobs_in_one_page = int(pages[-3])
total_jobs = int(pages[-1])
result = total_jobs // jobs_in_one_page #
if result == total_jobs / jobs_in_one_page:
    pages = result
else:
    pages = result + 1
    
with open("data_science_jobs.csv", mode='w', encoding="utf-8") as fd:
    fd.write("job_title,company_name,company_location,time,job_type,work_location,level,experince_years,job_skills,url\n") # header
    for page in range(0, pages):
        print(f"scraping data from page {page}")
        res = requests.get(f"https://wuzzuf.net/search/jobs/?a=navbl&q=data%20science%20jobs&start={page}")
        soup = BeautifulSoup(res.text, "html.parser")
        job_tags = soup.find_all("div", attrs={"class":"css-1gatmva e1v1l3u10"})
        for i in range(len(job_tags)):
            
            # job_title, url
            job_title_tag = job_tags[i].find("a", attrs={'class':"css-o171kl"})
            job_title = job_title_tag.text.replace('"', "")
            url = job_title_tag.attrs['href']

            # company
            company_name = job_tags[i].find("a", attrs={"class":"css-17s97q8"}).text.strip(" -")

            # location
            company_location = job_tags[i].find("span", attrs={"class":"css-5wys0k"}).text.strip()

            # time
            time = job_tags[i].find("div", attrs={"class":"css-d7j1kk"}).find("div").text # brown and green styles

            # job_type, work_location
            job_type_tag = job_tags[i].find("div", attrs={"class":"css-1lh32fc"}).find_all("a")
            job_type = ""
            work_location = ""
            for j in range(len(job_type_tag)):
                result = job_type_tag[j].text
                if result.lower() in ["internship", "part time", "full time", "freelance / project"]:
                    job_type = job_type + " / " + result
                else:
                    work_location = work_location + " / " + result 

            job_type = job_type.strip(" /")
            work_location = work_location.strip(" /")

            # level, experince_years, skills
            skills = job_tags[i].find("div", attrs={"class":"css-y4udm8"}).find_all("div")[-1]
            level = skills.find("a", attrs={"class":"css-o171kl"}).text
            try:
                experince_years = skills.find("span").text
                experince_years = experince_years.strip("· ")
            except:
                experince_years = "None"
            job_skills = skills.find_all("a")
            job_skills.pop(0)
            # print(len(job_skills)) # correct for job 0
            skills = ""
            for i in range(len(job_skills)):
                skills = skills + job_skills[i].text
            skills = skills.strip(" · ")
            skills = skills.replace("·", "-")
            fd.write(f"\"{job_title}\",\"{company_name}\",\"{company_location}\",\"{time}\",\"{job_type}\",\"{work_location}\",\"{level}\",\"{experince_years}\",\"{skills}\",\"{url}\"\n")