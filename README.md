<img src="https://cdn.jsdelivr.net/gh/Bbs1412/aws_beginner_project/Docs/amazonwebservices-original-wordmark.svg" alt="AWS" width="60" align="left">

# `Advanced Project`

- This is the project developed as part of the AWS course. The project is a simple Travel Guide application that gives information about various travel destinations.
- It utilizes various AWS services under free-tier limits, making it beginner-friendly.
- We faced a lot of challenges during development and deployment, so we've documented everything in detail to help others who might run into similar issues.
- It is second version of the project: [![AWS Beginner Project](https://img.shields.io/badge/Bbs1412/-AWS_Beginner_Project-ff8800.svg?logo=github)](https://github.com/Bbs1412/aws_beginner_project)
- This version is more advanced and includes additional features and services than previous beginner version.


# Index:
- [Project Details](#-project-details)
    - [Aim](#aim)
    - [Features](#features)
    - [Warning](#warning)
    - [Tech Stack](#-tech-stack)
- [Steps to run](#-steps-to-run)
- [To make changes](#%EF%B8%8F-to-make-changes)
- [Steps to deploy](#-steps-to-deploy)
- [Important Instructions](#%EF%B8%8F-important-instructions)
- [Cleanup](#-cleanup)
- [Contributions](#-contributions)
- [License](#%EF%B8%8F-license)
- [Contact](#-contact)


# 🎯 Project Details:
## Aim:
- Build a simple Travel Guide app that provides destination info using AWS services.
- Demonstrate how to easily deploy a project using common AWS components.
- Add some dynamic content than simple application.
- Integrate multiple free tier AWS services in a single project.

## Features:
- Responsive web UI that works well on different screen sizes.
- Utilization of AWS services for compute, authentication, storage, translation, and email notifications.

## Warning:
- The project is not meant for real-world use or as an impactful solution. Its main purpose is to demonstrate how different AWS services can be used together in a beginner-friendly setup.
- So, following strict best practices or writing production-ready code wasn't the main focus.

## 🧑‍💻 Tech Stack:

<!-- 
https://aws-icons.com/?
https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/html5/html5-plain.svg
-->

<table>
    <thead>
        <tr>
            <th>🖼️</th>
            <th>Tech </th>
            <th>Purpose</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><image src="https://cdn.jsdelivr.net/gh/Bbs1412/aws_advanced_project/Docs/html5-plain.svg" alt="HTML-icon" height=45></td>
            <td>HTML/CSS/JS</td>
            <td>Pretty obvious beginner-friendly web technologies for building the frontend.</td>
        </tr>
        <tr>
            <td><image src="https://cdn.jsdelivr.net/gh/Bbs1412/aws_advanced_project/Docs/flask-original-wordmark.svg" alt="Flask-icon" height=50></td>
            <td>Flask</td>
            <td>A lightweight Python web framework to serve the web application.</td>
        </tr>
        <tr>
            <th colspan="3">AWS Services</th>
        <tr>
            <td><image src="https://cdn.jsdelivr.net/gh/Bbs1412/aws_advanced_project/Docs/EC2.svg" alt="AWS-icon" height=45></td>
            <td>AWS EC2</td>
            <td>For hosting the web application.</td>
        </tr>
        <tr>
            <td><image src="https://cdn.jsdelivr.net/gh/Bbs1412/aws_advanced_project/Docs/Elastic%20Block%20Store.svg" alt="EBS-icon" height=45></td>
            <td>AWS EBS</td>
            <td>For persistent instance storage.</td>
        </tr>
        <tr>
            <td><image src="https://cdn.jsdelivr.net/gh/Bbs1412/aws_advanced_project/Docs/RDS.svg" alt="RDS-icon" height=45></td>
            <td>AWS RDS</td>
            <td>For getting stored data from a managed database service.</td>
        </tr>
        <tr>
            <td><image src="https://cdn.jsdelivr.net/gh/Bbs1412/aws_advanced_project/Docs/Simple%20Storage%20Service.svg" alt="S3-icon" height=45></td>
            <td>AWS S3</td>
            <td>For hosting the static website assets.</td>
        </tr>
        <tr>
            <td><image src="https://cdn.jsdelivr.net/gh/Bbs1412/aws_advanced_project/Docs/Translate.svg" alt="Translate-icon" height=45></td>
            <td>AWS Translate</td>
            <td>For translating destination descriptions to multiple languages.</td>
        </tr>
        <tr>
            <td><image src="https://cdn.jsdelivr.net/gh/Bbs1412/aws_advanced_project/Docs/Cognito.svg" alt="Cognito-icon" height=45></td>
            <td>AWS Cognito</td>
            <td>For user authentication (register/login).</td>
        </tr>
        <tr>
            <td><image src="https://cdn.jsdelivr.net/gh/Bbs1412/aws_advanced_project/Docs/Simple%20Notification%20Service.svg" alt="SNS-icon" height=45></td>
            <td>AWS SNS</td>
            <td>For sending OTPs and notifications to users.</td>
        </tr>
        <tr>
            <td><image src="https://cdn.jsdelivr.net/gh/Bbs1412/aws_advanced_project/Docs/bedrock-color.svg" alt="Bedrock-icon" height=45></td>
            <td>AWS Bedrock</td>
            <td>For future AI features (not implemented yet).</td>
        </tr>
        <tr>
            <th colspan="3">(Optional) You can add these services easily</th>
        </tr>
        <tr>
            <td><image src="https://cdn.jsdelivr.net/gh/Bbs1412/aws_advanced_project/Docs/IAM%20Identity%20Center.svg" alt="IAM-icon" height=45></td>
            <td>AWS IAM</td>
            <td>For managing access to AWS services with roles and policies.</td>
        </tr>
        <tr>
            <td><image src="https://cdn.jsdelivr.net/gh/Bbs1412/aws_advanced_project/Docs/CloudWatch.svg" alt="CloudWatch-icon" height=45></td>
            <td>AWS CloudWatch</td>
            <td>For monitoring instance performance and logs.</td>
        </tr>
        <tr>
            <td><image src="https://cdn.jsdelivr.net/gh/Bbs1412/aws_advanced_project/Docs/Budgets.svg" alt="Budgets-icon" height=45></td>
            <td>AWS Budgets</td>
            <td>For setting up cost and usage budgets to avoid unexpected charges.</td>
        </tr>
        <tr>
            <td><image src="https://cdn.jsdelivr.net/gh/Bbs1412/aws_advanced_project/Docs/CloudTrail.svg" alt="CloudTrail-icon" height=45></td>
            <td>AWS CloudTrail</td>
            <td>For tracking user activity and API usage.</td>
        </tr>
</table>



---

# ⚠️ Important Instructions:
- **Free-tier limits:** Make sure to stay within the free-tier limits of AWS services to avoid unexpected charges.

- **Instance type:** Use only `free-tier eligible` instance types like `t2.micro` to avoid charges.

- **Stop vs Terminate EC2:** 
    - **Stop:** Stopping the instance will not delete it, and you will still be charged for the EBS volume attached to it.
    - **Terminate:** Terminating the instance will delete it and you will not be charged for the instance or the EBS volume.

- **Region:** 
    - Make sure to select the same region for all AWS services to avoid any billing surprises.
    - It is visible in the top right corner of the AWS console.

- **Billing alerts:** 
    - Set up billing alerts in the AWS console to get notified if your usage exceeds the free-tier limits.
    - You can do this by going to the **Billing and Cost Management** section in the AWS console and setting up a budget.
    
- **RDS**
    - Avoid turning on RDS Backups, or make sure to delete the backups after you are done with the project.
    - Also delete the **RDS Subnet Group** created for the RDS instance, if you created one.

---

# 🤝 Contributions:

<table>
    <tbody>
    <tr>
        <td> 
            <img src="https://avatars.githubusercontent.com/Bbs1412" alt="Bhushan Songire" width="100" height="100">
        </td>
        <td> 
            <img src="https://avatars.githubusercontent.com/primegen-git" alt="Ujjawal Kumar" width="100" height="100">
        </td>
    </tr>
    <tr>
        <td> 
            <a href="https://github.com/Bbs1412">Bhushan Songire</a>
        </td>
        <td> 
            <a href="https://github.com/primegen-git">Ujjawal Kumar</a>
        </td>
    </tr>
</table>

- If you want to contribute to this project, please feel free to fork the repository and create a pull request.


# ⚖️ License:
- Project is licensed under the GNU General Public License v3.0 (GPL-3.0).
- See the [LICENSE](LICENSE) file for details.
- You are allowed to use code with **same license** and **proper attribution to the original author(s)**.


# 📧 Contact:
- **Email :** [bhushanbsongire@gmail.com](mailto:bhushanbsongire@gmail.com)
- **Email :** Ujjawal