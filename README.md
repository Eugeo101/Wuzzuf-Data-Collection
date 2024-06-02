# **Data Science Jobs Scraper**

This project scrapes Data Science job listings from [wuzzuf.com](https://wuzzuf.net/search/jobs/?a=navbl&q=data%20science%20jobs) and extracts key information from each listing. The collected data includes various attributes of the job listings which are then stored in a CSV file.

## **Table of Contents**
- [Features](#features)
- [Example Data](#example-data)
- [Requirements](#requirements)
- [Usage](#usage)
- [Output](#output)
- [License](#license)

## **Features**
The scraper collects the following columns for each job listing:
- `job_title`: Title of the job
- `company_name`: Name of the company offering the job
- `company_location`: Location of the company
- `time`: Time since the job was posted
- `job_type`: Type of job (e.g., Full Time, Internship)
- `work_location`: Whether the job is remote, on-site, etc.
- `level`: Experience level required for the job
- `experience_years`: Required years of experience
- `job_skills`: Skills required for the job
- `url`: URL to the job listing

## **Example Data**
Below are the first five rows of the scraped data:

| **job_title**                             | **company_name**                          | **company_location**  | **time**       | **job_type** | **work_location** | **level**     | **experience_years** | **job_skills**                                                                                                 | **url**                                                                                                            |
|-------------------------------------------|-------------------------------------------|-----------------------|----------------|--------------|-------------------|---------------|----------------------|------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| AI & Data Science Python Developer Intern | Sequel Solutions                          | Cairo, Egypt          | 1 month ago    | Internship   | Remote            | Student       | 0 - 1 Yrs of Exp     | IT/Software Development, Engineering, Telecom/Technology, Computer Science, Algorithms, Python, Software Development, Software Engineering, Programming | [Link](https://wuzzuf.net/internship/1kma8fGoLuav-AI-Data-Science-Python-Developer-Intern-Sequel-Solutions-Cairo-Egypt) |
| Data Analyst                              | EGEC                                      | Haram, Giza, Egypt    | 4 days ago     | Full Time    | On-site           | Experienced   | 2 - 5 Yrs of Exp     | Accounting/Finance, Analyst/Research, Engineering, analytical, Analysis, Computer Science, Reporting, Data Analysis, Communication skills            | [Link](https://wuzzuf.net/jobs/p/F99QNVxDd8Yp-Data-Analyst-EGEC-Giza-Egypt)                                         |
| Data Engineer                             | Hands of Hope Physical Therapy & Wellness | Maadi, Cairo, Egypt   | 5 days ago     | Full Time    | On-site           | Experienced   | 2 - 7 Yrs of Exp     | IT/Software Development, Analyst/Research, Engineering, Telecom/Technology, Computer Engineering, Data Modeling, Database, Database Design, Design, Engineering, ETL | [Link](https://wuzzuf.net/jobs/p/0yNNI8gqx135-Data-Engineer-Hands-of-Hope-Physical-Therapy-Wellness-Cairo-Egypt)      |
| Data Analyst                              | Alarabia Group                            | Cairo, Egypt          | 10 days ago    | Full Time    | On-site           | Experienced   | 3 - 5 Yrs of Exp     | IT/Software Development, Analyst/Research, Sales/Retail, business, Computer Science, Analysis, Computer Skills, Data Analysis, Information Technology (IT), Sales | [Link](https://wuzzuf.net/jobs/p/g31LAuLyaUXD-Data-Analyst-Alarabia-Group-Cairo-Egypt) |
| Data Analyst                              | Tiba Egypt                                | Haram, Giza, Egypt    | 12 days ago    | Full Time    | On-site           | Experienced   | 1 - 5 Yrs of Exp     | Analyst/Research, Analysis, business, Commerce, Computer Science, Data, Data Analysis, excel, FMCG, analytical | [Link](https://wuzzuf.net/jobs/p/N9p4GXhkCKsK-Data-Analyst-Tiba-Egypt-Giza-Egypt)                                   |

## **Requirements**
To run this project, you will need the following Python libraries:
- `requests`
- `beautifulsoup4`
- `pandas`

You can install these libraries using pip:
```bash
pip install requests beautifulsoup4 pandas
```

## **Usage**
1- Clone the repository:
```bash
git clone https://github.com/Eugeo101/Wuzzuf-Data-Collection
cd Wuzzuf-Data-Collection
```

2- Run the scraper script:
```bash
python scraper.py
```

3- The script will send requests to wuzzuf.com, parse the HTML response using BeautifulSoup, and handle various edge cases to ensure accurate data extraction.

## **Output**
The output will be a CSV file named data_science_jobs.csv containing all the scraped job listings with the specified columns.

## **License**
This project is licensed under the MIT License. See the [LICENSE](https://github.com/Eugeo101/Wuzzuf-Data-Collection/blob/main/LICENSE) file for details.
