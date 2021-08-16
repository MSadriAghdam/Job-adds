# job_ads_database
Creating a database with job ads in order to analyse job requirements.

This database will contain the following:
1. Source - Where the job ads could be found (link).
2. Header - Title of the job ad.
3. Content - Text of the job ad (details of the ad which includes the job requirement etc.
4. Language - English/German.
5. Type of Employment - full time, part-time, internship, student job, etc.

Using Google API to connect google form with Jupyter notebook:
To do this we need to do these 3 steps:
step 1: create a google service account.
step 2: Share the Google form with generated email.
step 3: Load the data on jupyter notebook.
Here is the link: https://www.analyticsvidhya.com/blog/2020/07/read-and-update-google-spreadsheets-with-python/


# Data Analysis

During the data analytics process we engaged in the data preprocessing, analysis, and data visualization.
First, useful libraries such as pandas, seaborn, matplotlib, re, and many others were imported to be used in the analysis. All the functions used during analysis were created in a python file and also imported. Each column has a python file with several function performing different tasks.

With regards to the language requirements, the functions extracted languages such as english, german, or english and german. Indicating some job expects applicants to be fluent on either english or german or both.

With the employment, we extracted internships, part-time, student jobs, and full-time. Most of the ads were for full- time bases. In terms of employment levels, internship, entry level, junior, and senior levels were also extracted and analysed

The locations of the jobs were also analysed, with cities such as Berlin, Hambury, Stuttgart and many others was extracted from the job ads.

The software skill expected of applicants was extracted and analysed. Skill such as Python, SQL, R, Matlab, Java, Javascript, Swift, Julia, Scala, Octave, and SAS were checked. Python and SQL dominated the job ads.

Also, with reference to the experience of applicants, most jobs did not specify how many years of experience is expected of the applicants. However, we extracted 1 to 3 years of experience, 3 to 5 years, and 5 years plus of working experience expected of applicants.

Finally, further analysis was done on the correlation of these columns to get an insight of the data using seaborn and matplotlib for visualization.
We also created a dashborad on data studio which is avalable here :https://datastudio.google.com/s/rADvuIXI694
