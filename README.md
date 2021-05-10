# job_ads_database
Creating a database with job ads in order to analyse job requirements.

This database will contain the following:
1. Source - Where the job ads could be found (link).
2. Header - Title of the job ad.
3. Content - Text of the job ad (details of the ad which includes the job requirement etc.
4. Language - English/German.
5. Type of Employment - full time, part-time, internship, student job, etc.

# Differences between SQL and NoSQL
Generally, SQL database are relational and NoSQL are nonrelational. 
SQL database uses structured query language whereas NoSQL uses dynamic schema for unstructured data. 

Data Storage Model: 
•	SQL Database are tables based with fixed rows and columns
•	No SQL Database are Document such as JSON documents, Key-value such as key-value pairs, Wide-column such as tables with rows and dynamic columns, Graph with nodes and edges

Examples
•	SQL Database: Oracle, MySQL, Microsoft SQL
•	NoSQL Database: Document: MongoDB and CouchDB, Key-value: Redis and DynamoDB, Wide-column: Cassandra and HBase, Graph: Neo4j and Amazon Neptune. Consider what your use cases will be and check if the general purpose NoSQL database like MongoDB would be a better option.

Primary Purpose
•	SQL: General purpose
•	NoSQL: Document: general purpose, Key-value: large amounts of data with simple lookup queries, Wide-column: large amounts of data with predictable query patterns, Graph: analyzing and traversing relationships between connected data

Schemas
•	SQL: rigid and predefined
•	NoSQL: flexible/dynamic. A flexible schema allows you to easily make changes to your database as requirements change. You can iterate quickly and continuously integrate new application features to provide value to your users faster.

Joins
•	SQL: Typically required. Data in SQL databases is typically normalized, so queries for a single object or entity require you to join data from multiple tables. As your tables grow in size, the joins can become expensive. 
•	NoSQL: Typically, not required. Data in NoSQL databases is typically stored in a way that is optimized for queries. The rule of thumb when you use MongoDB is - Data that is accessed together should be stored together. Queries typically do not require joins, so the queries are faster than SQL databases. 

Data to Object Mapping
•	SQL: Requires ORM (object-relational mapping)
•	NoSQL: Many do not require ORMs. MongoDB documents map directly to data structures in most popular programming languages. Mapping can allow developers to write less code, leading to faster development time and fewer bugs

Scaling
•	SQL: Most SQL databases require you to scale-up vertically (migrate to a larger, more expensive server) when you exceed the capacity requirements of your current server.
•	NoSQL most NoSQL databases allow you to scale-out horizontally, meaning you can add cheaper, commodity servers whenever you need to.

Source: https://www.mongodb.com/nosql-explained/nosql-vs-sql


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
