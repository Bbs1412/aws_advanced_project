<img src="https://cdn.jsdelivr.net/gh/Bbs1412/aws_advanced_project/Docs/amazonwebservices-original-wordmark.svg" alt="AWS" width="60" align="left">

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
            <td><image src="https://cdn.jsdelivr.net/gh/Bbs1412/aws_advanced_project/Docs/IAM%20Identity%20Center.svg" alt="IAM-icon" height=45></td>
            <td>AWS IAM</td>
            <td>For managing access to AWS services with roles and policies.</td>
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
            <td><image src="https://cdn.jsdelivr.net/gh/Bbs1412/aws_advanced_project/Docs/bedrock-color.svg" alt="Bedrock-icon" width=45></td>
            <td>AWS Bedrock</td>
            <td>For future AI features (not implemented yet).</td>
        </tr>
        <tr>
            <th colspan="3">(Optional) You can add these services easily</th>
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


# 🚀 Steps to run:
To run the project locally on your device first, follow these steps:

1. Create fork of the repository:
    - Click on the `Fork` button at the top right corner of this page to create a copy of the repository in your GitHub account.
    - This will also help to easily deploy the project on AWS later.
    - Now, you have your own copy of the project repository in your GitHub account.

1. Clone the repository from your GitHub account:
    ```bash
    # Replace the <your-username> with your GitHub username
    git clone https://github.com/<your-username>/aws_advanced_project.git
    cd aws_advanced_project
    ```

1. Create a virtual environment and install the required packages:
    ```bash
    # Create virtual environment
    python -m venv venv

    # Activate virtual environment (Windows):
    ./venv/Scripts/activate
    # Linux:
    source venv/bin/activate  

    # Install required packages
    pip install -r requirements.txt
    ```

1. Set up environment variables:
    - Copy the `.env.example` file to `.env` file and fill in the required values in the `.env` file.
    - For the env variables, you first need to setup various AWS services, that part is covered in [deployment](#-steps-to-deploy) section.

1. Run the Flask application:
    ```bash
    python app.py
    ```

1. Now, server is live and project can be accessed at [`http://localhost:5000/`](http://localhost:5000/) in your browser.

1. You can make any changes in the code files and push them to your GitHub repository.


---


# 🌐 Steps to deploy:

> [!CAUTION]
> Avoid doing anything un-necessary in the AWS console, unless you know what you are doing.  
> It can lead to unexpected charges on your AWS account.  
> Don't forget to stop or terminate the resources after you are done with the project.  
> More details are here in [Important Instructions](#-important-instructions) and [Cleanup](#-cleanup) sections.

## Update the project files:
1. Assuming that you have already created a fork of the repository and cloned it to your local machine.
1. If you have made any changes to the code, make sure to commit and push those changes to GitHub (to your own version of the project).
1. Some files like `.env` are git-ignored and hence, need to be updated manually on the EC2 instance later. See this [section](#...) for more details.

> [!TIP]
> AWS resources can be used across various regions.
> Make sure that you always select the same region for all the resources you create, to avoid any issues later. (Regions are visible in the top right corner of the AWS console.)
> Default region is `us-east-1`, so you can use that for all the resources.


## Security rules:
- To serve our application, we need a compute instance that can run the Flask application.
- But, before setting up the EC2 instance, we need to create a security group that allows incoming traffic on port 5000 (or any other port you want to use).
- Follow these steps to create a security group:
    1. Go to the [AWS Console](https://console.aws.amazon.com/) and log in to your AWS account.
    1. Navigate to the EC2 service. (You can search for "EC2" in the search bar.)
    1. In the left sidebar, click on **Security Groups** under **Network & Security**.
    1. Click on the **Create security group** button.
    1. Name your security group something like `travel-guide-sg` and a description like `Security group for travel guide application`.
    1. Under **Inbound rules**, click on **Add rule**. Add the following rules:
        | Sr | Type | Protocol | Port Range | Source | Explanation |
        |----|------|----------|------------|--------|-------------|
        | 1  | Custom TCP Rule | TCP | 5000 | Anywhere-IPv4 | Allow incoming traffic on port 5000 for the Flask application |
        | 2  | MySQL/Aurora | TCP | 3306 | Anywhere-IPv4 | Allow incoming traffic on port 3306 for RDS MySQL database |
        | 3  | SSH | TCP | 22 | My IP (or Anywhere-IPv4) | Allow incoming traffic on port 22 for SSH access |
    1. Under **Outbound rules**, by default all traffic protocols and destinations are allowed. You can leave it as it is.
- Now, you have a security group that allows incoming traffic on port 5000 from anywhere (IPv4).
- And, allowing SSH on port 22 also allows you to use SFTP if needed. Instead of My IP, you can also select Anywhere-IPv4 for SSH rule if facing issues.
- You can also add rules for IPv6 if you want to allow traffic from IPv6 addresses as well.


## Set Up S3 Bucket:
- In the project code files, static assets are served from the EC2 instance itself.
- Optionally, you can use S3 to serve the static assets.
- Make the below mentioned changes first:
    - Uncomment the S3 bucket code in the [`static/script.js`](static/script.js#L168) and [`templates/place_detail.html`](templates/place_detail.html#L65).
    - Comment out the flask serve static code at same places.
    - Fill in the S3 URL in the env variable file.
- From AWS Console, navigate to the S3 service, and create a new S3 bucket:
    1. Name you bucket something like `travel-guide-project` (or any unique name) 
    1. Other settings can be left as default.
    1. ***Block Public Access settings for this bucket*** section and uncheck the **Block all public access** option. Acknowledge the warning and click on **Create bucket** button.
    1. Add `Bucket Policy` to allow public access to the bucket, [Your bucket > **Permissions** tab > **Bucket policy** > **Edit**]:
        ```json
        {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Sid": "PublicReadGetObject",
                    "Effect": "Allow",
                    "Principal": "*",
                    "Action": "s3:GetObject",
                    "Resource": "arn:aws:s3:::travel-guide-project/*"
                }
            ]
        }
        ```
    1. Make sure you replace `travel-guide-project` with your actual bucket name in the above policy. 
    1. Click on **Save changes**.
- Now, you can add all the assets from [static/images](static/images) directory to the S3 bucket using same file upload method.


## Set Up EC2 Instance:
- Now, we can set up an EC2 instance to run our Flask application.
- Go to AWS Console > EC2 service > **Instances** (left sidebar) > **Launch Instances** button.
- These are some recommended settings, but you can change them as per your requirements:
    1. Names and tags: Enter some name for the instance, like `travel-guide-server`.
    1. Application and OS Images: **Amazon Linux**.
    1. Instance Type:
        - Select **t2.micro** or any free tier eligible instance type.
        - Our project is lightweight and can run on any minimum configuration instance.
    1. Key Pair (login):
        - Create a new key pair, with any name like `travel-guide-key`.
        - Rest can be left as default. Create key and save downloaded `.pem` file securely. 
        - We need it in order to access the instance via SSH.
    1. Network Settings:
        - Under firewall settings, you will see the security group section.
        - Click on **Select an existing security group** and select the security group you created earlier (`travel-guide-sg`).
    1. Configure Storage: You can leave the default settings as they are.
    1. Click on **Launch Instances** button to launch the instance.
- After the instance is launched, you can see the success message with the instance ID (i-xxxxxx).
- Now the instance can be checked in the **Instances** section in the left sidebar of the EC2 service page.


## Set Up RDS Instance:
- Our project uses a MySQL database to store the destination data.
- Go to AWS Console > Aurora and RDS > **Databases** (left sidebar) > **Create database** button.
- These are some recommended settings, but you can change them as per your requirements:
    1. Database creation method: **Standard Create**.
    1. Engine type: **MySQL**.
    1. Templates: **Free tier**.
    1. Availability & durability: **Single AZ deployment** (1 instance).
    1. DB instance identifier: `travel-guide-db` (or any name you want).
    1. Master username: `admin` (or any username you want).
    1. Master password: Set a strong password and remember it, we will need it later.
    1. DB instance size: **db.t2.micro** (any free tier eligible).
    1. Storage: Leave default settings as they are.
    1. Connectivity:
        - Virtual Private Cloud (VPC): Default VPC.
        - Public access: **Yes**.
        - VPC security groups: **Choose existing** and select the security group you created earlier (`travel-guide-sg`).
    1. Click on **Create database** button to create the RDS instance.
- After the database is created, it will take some time to be available.
- Once the status changes to `Available`, click on the database name to see the details.
- Note down the **Endpoint** value, we will need it to connect to the database from our Flask application.
- It will be something like `<name>.<id>.<zone>.rds.amazonaws.com`.


## Set Up Translate, Cognito and SNS:
- Will add this soon...


## Deploy the Application:
Finally, we can deploy the Flask application on the EC2 instance.

1. Connect to the EC2 instance:
    - AWS Console > EC2 service > **Instances** > Your instance > **Connect**.
    - Or use ssh to connect from your terminal:
        ```powershell
        ssh -i /path/to/your-key.pem ec2-user@<your-ec2-public-ip>
        ```
    - Run the following commands:
        ```bash
        # Update the package manager
        sudo yum update -y
        # Install Python 3 and git
        sudo yum install python3 git -y
        ```

1. Clone the project repository:
    - Run the following command to clone the project repository:
        ```bash
        git clone https://github.com/<your-username>/aws_advanced_project.git
        cd aws_beginner_project
        ```
    - If you want to use S3, make sure that updated code files are already pushed to your GitHub repository.
    
1. Install the required packages in virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

1. Set up environment variables:
    - We need to create a `.env` file on the EC2 instance with all the required environment variables.
    - First make copy of the `.env.example` file:
        ```bash
        cp .env.example .env
        ```
    - Now, using `nano` or `vim`, open the `.env` file and fill in the required values:
        ```bash
        sudo nano .env
        # Save and exit (in nano: Ctrl+O, Enter, Ctrl+X)
        ```

1. Run the Flask application:
    ```bash
    python app.py &
    ```


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
