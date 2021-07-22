# Computer-Specs-Software

## Contents
* [Introduction](#introduction)
    * [Objective](#objective)
    * [Proposal](#proposal)
* [Architecture](#architecture)
    * [Risk Assessment](#risk-assessment)
    * [Trello Board](#trello-board)
    * [Entity Relationship Diagram](#entity-relationship-diagram)
    * [Test Analysis](#analysis-of-testing)
    * [Continuous Integration](#continuous-integration)
* [Development](#development)
    * [Unit Testing](#unit-testing)
    * [Front-End Design](#front-end)
    * [Read Page](#read-page)
    * [Add Page](#add-page)
    * [Update Page](#update-page)
    * [Delete Page](#delete-page)
    * [Integration Testing](#integration-testing)
* [Footer](#footer)

## Introduction

### Objective
The brief set the following objective to be achieved during this project: To create a CRUD application with utilisation of supporting tools,
methodologies and technologies that encapsulate all core modules
covered during training.
In short my aim is to create an application that Create, Read, Update and Delete functions to demonstare my skills gained through the first five weeks.
### Proposal
I have decided to create Computer-Specification website. The users are able to  use the website to create a list of computer parts that fit together and share this list specification with other users. The relationships between parts will not allow the users to combine parts which are not compatible together. The original idea included all of the computer parts required. To keep the focus of the project more simple and allow time to fully implement the current components, I have reduced them to just a few.
The CRUD implementation is as follows:
#### Create
   * CPU:
      * Name
      * Make
      * Model 
   * Motherboard
      * CPU 
      * Case
      * Name
      * Make
      * Model
      * Type
      * Series
   * Case
      * Name
      * Type
      * Make
      * Model 
#### Read 
   * Specification list that contains all the chosen parts from the user.
   * Specification list sent by other users.
#### Update
   * CPU choice.
   * Motherboard choice.
   * Case choice.
#### Delete
   * CPU choice.
   * Motherboard choice.
   * Case choice.
## Architecture

### Risk Assessment
Risk Assement table analyses the possible risks I could encounter during the development and management of the project.
<img src="https://github.com/IIvanov21/Computer-Specs-Software/blob/main/images/RiskAssesment.png" alt="Risk Assesment" />
All the highlighted rows were added later on during the development process after they became clear. The yellow risks are potential threat depending on how the development of the project is handled.
### Trello Board
The progress of the project is documented using Trello as it is well suited for a small scale project. The initials setup of the board looks as follows:
<img src="https://github.com/IIvanov21/Computer-Specs-Software/blob/main/images/KanBanBoard.jpg" alt="KanBanBoard" />
The full access to the board is here:https://trello.com/b/2TDZNQXU/computer-specs-crud
The updated Trello Board:
<img src="https://github.com/IIvanov21/Computer-Specs-Software/blob/main/images/KanBanBoard2.jpg" alt="KanBanBoard2" />
### Entity Relationship Diagram
My first ERD with one to many relationship .
<img src="https://github.com/IIvanov21/Computer-Specs-Software/blob/main/images/Database.png" alt="First ERD"/>
<br/>
My original ERD was a one-to-many relationship-diagram which is makes it fairly good ERD to follow for this project but to develop it further I have added an
extra relationship. A computer originally consists of multiple parts and to showcase how further relationships will work in future I have adpoted a relationship for another part:
<div style="block;"> 
<img align="right" src="https://github.com/IIvanov21/Computer-Specs-Software/blob/main/images/Database2.png" alt="Second ERD"/>
Through the use of the Motherboard table I have decided to use a many-to-many relationship by braking it up in multiple many-to-one relationships. A computer system should be a many-to-many relationship but taking many-to-one relationship aproach will allow me to construct dependecies which in this case is introducing compatability relationships between components. This aproach will also make it easier for a users to find a component that is already in the database system and easily introduce further features such as Cooler component to cooldown the CPU. 
<div style="block;"> 
<img align="right" src="https://github.com/IIvanov21/Computer-Specs-Software/blob/main/images/Database3.png" alt="Third ERD"/>
When developing the application I found the relationship between Motherboard and other components doesnt work together well. Therefore I isolated Motherboard as a single component and created an extra diagram called Build which ties in all the components together and represents relationships better between componenets.

### Analysis of Testing
The project follows only unit and integration testing which cover the scope of the application and allows us me to fully test it's given CRUD functionality. There are other forms of testing which can be implemented but are outside the scope of the project. These forms of testing mentioned bellow dont have to be followed sequientially and allow full testing for a bigger project.
   * API testing - testers validate that API connections and responses function as intended.
   * UI testing - testing of UI controls like buttons, menus and text input to ensure that the experience flow and features chosen are optimal for the user experience.
   * System testing - validate the complete and integrated software package to make sure it meets requirements.
   * White-box testing - tests several aspects of the software, such as predefined inputs and expected outputs, as well as decision branches, loops and statements in the code.
   * Black-box testing - testing against a system where the internal code, paths and infrastructure are not visible.
   * Acceptance testing - ensure that the end user can achieve the goals set in the business requirements.
   * Alpha testing - uses internal team members to evaluate the product.
   * Beta testing - a soft launch, enabling you to get feedback from real users who have no prior knowledge of the app.
   * Production testing - attempts to discover and triage user-reported defects as quickly as possible.
The plan below follows test that will be perfomed when the full functionality for my CRUD application is implemented. As more functions were implemented I have gradually added multiple tests:
<img src="https://github.com/IIvanov21/Computer-Specs-Software/blob/main/images/TestAnalysis.png" alt="Test Analysis"/>
When designing the test cases it helped me outline problems in my code which I had to adjust or simply implement new check that will prevent the overwriting and duplication of data. Such a feature is especially the build name. Allowing the build name to be unique will prevent the user creating duplication and getting the wrong information stored into the database.
   
### Continuous Integration
Continuous intergration allows me to automatically integrate code into my CRUD application through the focus on automatic testing. In my aproach I develop the application using Python which then gets pushed and pulled from the Version Control System GitHub. Jenkins with the provided script will get the repository and build it. This allows Jenkins to run unit and integration testing using Pytest and provide a report with Pytest coverage that will let us understand what code needs refactoring.
  
<img src="https://github.com/IIvanov21/Computer-Specs-Software/blob/main/images/Pipeline.png" alt="CI Pipeline"/>
   
### Jenkins Script
* This script will allow Jenkins to run the test every time.
* Install dependecies that are needed for testing the script. The chrome driver is needed for integration testing.
   * sudo apt-get install python3 python3-pip python3-venv chromium-browser wget unzip -y
   * version=$(curl -s https://chromedriver.storage.googleapis.com/LATEST_RELEASE_$(chromium-browser --version | grep -oP 'Chromium \K\d+'))
   * wget https://chromedriver.storage.googleapis.com/${version}/chromedriver_linux64.zip
   * sudo unzip chromedriver_linux64.zip -d /usr/bin
   * rm chromedriver_linux64.zip

* Clone the appliation to ensure everything is stored correctly on Jenkins.
   * git clone https://github.com/IIvanov21/Computer-Specs-Software.git
   * cd Computer-Specs-Software

* Install pip requirements. Pip contains pytest and pytest-cov which allow you to get a report for the designed test cases and what they cover.
   * python3 -m venv venv
   * source venv/bin/activate
   * pip3 install -r requirements.txt

* Run the test
   * python3 -m pytest --cov=application --cov-report=term-missing
   
## Development

### Unit Testing
Unit testing allows me to separate the route functions for each component such as the add functions for the Create functionality, read functions for the Read functionality etc.. this ten allows me to test each function with given scenarious to ensure they work correctly. These tests are tied to a Jenkins Virtual Machine which runs them automatically after every push on a select version control system which in my case is Git. Jenkins will print out if the test cases are succeful and provide a coverage report to what lines of the code are being missed in the test cases.
To run the test cases yourself follow the listed Jenkins steps above.
<img src="https://github.com/IIvanov21/Computer-Specs-Software/blob/main/images/UnitTesting.png" alt="Unit Testing"/>
   
If one of the test cases fails the entire build is marked as a failure in the Jenkins report.
   
<img src="https://github.com/IIvanov21/Computer-Specs-Software/blob/main/images/FailUnitTesting.png" alt="Unit Testing Fail"/>
   
### Front-End
#### Read Page
The read page allows the user to list an existing build in the database. To list it they simply need to enter the name of the build. Once a build is entered below a list of each part in the build is shown. If the build doesn't exist or a certain part hasn't been added the use will be notified. There are links below the list to access other functionality of the application. The CRUD functionality covered by this is READ.
<br>
<img src="https://github.com/IIvanov21/Computer-Specs-Software/blob/main/images/ReadPage.png" alt="ReadPage"/>
#### Add Page
The Add page contains a guide which tells the user how to create a new build list. The Add page cotains extra links for each component such as CPU, Motherboard and Case. Once the use has created a build name they get notified with a message and propmted to continue to each add page for a component. In the individual page for each component there is a form which allows the user to create an entry to the database for that component and tie it to the build database. If the user tries to use a non-existant name the application will prompt them to create a name first with a notification. The CRUD functionality covered by the Add Page is Read and Create.
<br>
   
Add Page:
   <br>
<img src="https://github.com/IIvanov21/Computer-Specs-Software/blob/main/images/AddPage.png" alt="AddPage"/>
<br>
   
Add Motherboard Page:
   <br>
<img src="https://github.com/IIvanov21/Computer-Specs-Software/blob/main/images/AddMotherboard.png" alt="AddMotherboard"/>
<br>
   
Add CPU Page:
   <br>
<img src="https://github.com/IIvanov21/Computer-Specs-Software/blob/main/images/AddCPU.png" alt="AddCPU"/>
<br>
   
Add Case Page:
   <br>
<img src="https://github.com/IIvanov21/Computer-Specs-Software/blob/main/images/AddCase.png" alt="AddCase"/>
<br>
   
#### Update Page
The functionality for the Update Page for taking information is the same as the AddPage. It will let the use change the name of a build and parts associated with that build. The difference is when Updaitng the information in the database. Instead of creating a new entry the Update function will look in the database of each component with the associated build id and update the information. The CRUD functionality here is Read and Update.
<br>
   
Update Page:
   <br>
<img src="https://github.com/IIvanov21/Computer-Specs-Software/blob/main/images/UpdatePage.png" alt="UpdatePage"/>
<br>
   
Update Motherboard Page:
   <br>
<img src="https://github.com/IIvanov21/Computer-Specs-Software/blob/main/images/UpdateMotherboard.png" alt="UpdateMotherboard"/>
<br>
   
Update CPU Page:
   <br>
<img src="https://github.com/IIvanov21/Computer-Specs-Software/blob/main/images/UpdateCPU.png" alt="UpdateCPU"/>
<br>
   
Update Case Page:
   <br>
<img src="https://github.com/IIvanov21/Computer-Specs-Software/blob/main/images/UpdateCase.png" alt="UpdateCase"/>
<br>
   
#### Delete Page
The delete page simply takes in a build name and a desired choice. The all choice will delete every component associated with the build and the build itself. The other choices "CPU", "Case","Motherboard" will delete the relavent component associated with the build. The CRUD functionality covered by this page is Read and Delete.
 <br>
   
<img src="https://github.com/IIvanov21/Computer-Specs-Software/blob/main/images/DeletePage.png" alt="DeletePage"/>
   
### Integration Testing

## Footer

### Future Improvements
   * A really good feature improvement will be having user control. The user control will allow people to create their own accounts which will allow them to create builds which can be easily shared with other users. User and Pass functionality will also prevent other people accessing unauthorized builds and changing them.
   * Another feature will be like mentioned in the proposal introduce further relationships between components. At the moment people can add CPU part from AMD to a build list with a motherboard part for an Intel CPU. Introducing further constraints will make the application more robust and reliable.
   * Since the goal of the application is to be a computer specification list. A future imporvement will be adding functionality for all the components need by a Computer. Such as Power Supply, Cooler, Graphics card etc.. This feature will allow a user to build a fully speced computer parts list.
### Author
Ivaylo Ivanov
### Acknowledgements
Oliver Nichols
Ryan Wright
Victoria Sacre
