# EZOPS-DevOps

## Challenge Instructions


### Challenge D1 and D2 - Note Python 3 is used so you might have to replace python with python3 

#### 1. If you want to run the Flask portion of Challenge D1 locally - 
        A. Activate the venv by navigating to the folder that contains venv/ folder in terminal/shell and run - 
        (Linux/Mac) source venv/bin/activate
        (Windows) venv\Scripts\activate
        
        B. Navigate to the Challenge D1 and D2 folder and install the dependencies from requirements.txt -
        pip install -r requirements.txt
        
        C. Again while still in the Challenge D1 and D2 folder run the development server - 
        python app.py
        
        D. Open your browser and go put in either address - 
        localhost:5000
        0.0.0.0:5000
        
#### 2. The Flask app on AWS EC2 server running CentOS 7 - 
        http://3.17.205.54/
        
        

### Challenge D3 - Java

#### Debugging instructions are listed inside "Challenge D3.docx" file.



### Challenge D4 - Shell Scripting

#### 1. every_other.sh and reverse.sh are the Bash script equivalents of their counterparts in Challenge D1.

#### 2. ezops.sh is the complete script that pulls the .csv files and reverses columns, grabs every other column, as well
        as the newest option - to reverse text in every third column. Run it on any Linux/Mac terminal. Note that on 
        Windows since you might not have acess to sh you might have to run it with cygwin on command-prompt or powershell.
        

### Challenge D5 - Basic SQL

#### 1. You can test the table creation/queries on a site like db-fiddle.com

#### 2. Test by grabbing the create and insert statements to create table.

#### 3. Use the select query for the average.



### Challenge D5A - Advanced SQL

#### 1. Answers/Instructions provided in "ezops query plan answer.docx" file.

#### 2. A "ezops query plan.png" image file is provided for better clarity.



### Challenge D6 - Basic Docker


#### 1. You can go into each folder (tomcat, mysql, and ibm-mq) individually and build the images with -
        docker build -t "name" .
        You can go into each folder with their respective dockerfile and replace "name" with what you want to name the image.
        For example - 
        docker build -t mysql .
        
#### 2. Navigate to the tomcat folder and run the docker image -
        docker run -p 8080:8080 tomcat
        Then go to your browser and open localhost:8080
        
#### 3. Navigate to the mysql-tomcat-mq folder. Within terminal/shell run -
        docker-compose up
        
        
#### 4. For debugging open file "Debugging Demonstration.docx" for instructions for the last task.



### Challenge D6A - Advanced Docker
##### Note - Unfortunately somewhat incomplete.

#### 1. Navigate to the "Challenge D6A" folder while in terminal/shell and run the below to start the docker services -
        docker-compose up
        
#### 2. Instructions for Docker Swarm are provided in the file "Instructions.docx" or below -
        A. docker swarm init
        B. docker stack deploy -c ./docker-compose.yml ezops-swarm
        You can rename ezops-swarm to whatever you like.
        
     
        
        
        
