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
### Entity Relationship Diagram
My first ERD with one to many relationship .
<img src="https://github.com/IIvanov21/Computer-Specs-Software/blob/main/images/Database.png" alt="First ERD"/>
<br/>
My original ERD was a one-to-many relationship-diagram which is makes it fairly good ERD to follow for this project but to develop it further I have added an
extra relationship. A computer originally consists of multiple parts and to showcase how further relationships will work in future I have adpoted a relationship for another part:
<div style="block;"> 
<img align="right" src="https://github.com/IIvanov21/Computer-Specs-Software/blob/main/images/Database2.png" alt="Second ERD"/>
Through the use of the Motherboard table I have decided to use a many-to-many relationship by braking it up in multiple many-to-one relationships. A computer system should be a many-to-many relationship but taking many-to-one relationship aproach will allow me to construct dependecies which in this case is introducing compatability relationships between components. This aproach will also make it easier for a users to find a component that is already in the database system and easily introduce further features such as Cooler component to cooldown the CPU. 


### Analysis of Testing
### Continuous Integration
### Jenkins Script

## Development

### Unit Testing
### Front-End
### Integration Testing

## Footer

### Future Improvements
### Author
Ivaylo Ivanov
### Acknowledgements
