# Django App demonstrating Zappa deployment

![Python 3.7.3](https://img.shields.io/badge/Python-3.6-brightgreen.svg) ![Django 3.1.7](https://img.shields.io/badge/Django-3.1.7-skyblue.svg) ![zappa 0.52.0](https://img.shields.io/badge/zappa-0.52.0-skyblue.svg)

• A simple and basic Web application to upload files to **_AWS S3_** and access the files using **_S3 URL_**.

• It helps you in deploying Django Application to **_AWS Lambda_** using Library **_zappa_** library.

• You need to create an account in **_http://console.aws.amazon.com_** in order to access AWS.

• Create a **_IAM user_** through AWS Console and add _*IAM Full Access*_ permission and create a new policy with **_AWS text file_** and attach to the user.

• Configure AWS*ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY in AWS configuration file using \*\*\_AWS CLI*\*\*.

• Use the following commands

> pip install zappa
> zappa init
> zappa deploy <envt>

• IF you see the below error then  
Error: Warning! Status check on the deployed lambda failed. A GET request to '/' yielded a 500 response code.
(Sometime you can find SQLITE version issue. Use compatible Version or use AWS RDS service for DB)

> zappa tail

• The above command shows the error logs to analyze the issues. After solving the issue please update the deployment using below command.

> zappa update <envt>

• Please do ⭐ the repository, if it helped you in anyway.
