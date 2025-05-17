v1 : Bare minimum basic version of code
v2 : Option to switch between the SQLite and Local MySQL database
v3 : Added Some features (need to check)
v4 : Full fledged version with all the features and options w cognito and all


Curr changes:
- add support for s3 image fetching

* In the readme, add logos of AWS services used (maybe in a table)

Create readme now for this basic version, with aws steps as well
- s3
- ec2
- how to update code on ec2 using nano
- instead of entering into complexities, tell them to:
    - fork the repo
    - clone the repo locally
    - make changes
    - push the changes
    - Clone on EC2
    - run the code

    - mention that VSC Remote extension can be used to edit the code on EC2 directly
    - But, follow below steps for easiest possible setup

    - To make changes: 
        + edit whatever u want
        + git add .
        (dont worry about secrets here as they are not added in this version at all)
        + git commit -m "type what u changed"
        + git push origin main
        + git pull origin main on EC2

    - Do not enable any feature/service which you do not know about
    - U will get charged for the services you enable

In v2 actually, i removed the support for SQLite
Either RDS can be added in intermediate version
But, it wont add any value as one dedicated version just for RDS is not needed
So, in advanced version directly, i will add support for RDS 

Try to make code as customizable as possible to enable or disable features


- -------------------------------------------------------------------------------------------
[nitpick] Consider implementing a runtime toggle or using configuration logic to switch between Flask and S3 image paths instead of relying on manually commented blocks in the HTML template.

Suggested change
            <!-- From flask server
            -->
            <img src="/get_img/{{ place.image }}" alt="{{ place.name }}" class="main-image">
            <!-- From S3 bucket
            <img src="{{ place.s3_base_url }}/{{ place.image }}" alt="{{ place.name }}" class="main-image">
            -->
            {% if use_s3 %}
            <img src="{{ place.s3_base_url }}/{{ place.image }}" alt="{{ place.name }}" class="main-image">
            {% else %}
            <img src="/get_img/{{ place.image }}" alt="{{ place.name }}" class="main-image">
            {% endif %}
