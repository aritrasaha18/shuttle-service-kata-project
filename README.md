<h1 align="center">Trinity College Shuttle Service </h1>

## Project Information 👤
* Authors: B D S Aritra & Andrew Briden
* Date: 06/06/2023
* Course: [CPSC 415]

## Project Description

The Trinity College Shuttle Service is a cutting-edge web-based micro-service application that effectively addresses the transportation needs of the Trinity College community. This sophisticated service boasts an array of features, including the ability to search for routes to multiple stops on campus, access the shuttle schedule, request shuttle services with real-time tracking, and even connect with shuttle drivers for additional information.

Such a service is undoubtedly a game-changer for students, faculty, and staff alike, enabling them to navigate the sprawling Trinity College campus with ease and efficiency. By offering real-time tracking and arrival times, this micro-service application empowers users to plan their schedules with greater precision and optimize their time on campus.

In essence, the Trinity College Shuttle Service represents a shining example of how micro-service applications can enhance the user experience by providing valuable and innovative services to a specific community. Its impressive features and capabilities are sure to impress and delight anyone who is seeking an elegant and sophisticated solution to their transportation needs on campus.

## Primary UI Functions

Routes : The route search feature automatically identifies the nearest stops to the user's location and generates a route reach the closest stop.

Schedule : The Shuttle Service also provides a detailed schedule of the shuttle service running times, allowing users to plan their commutes efficiently and optimize their time on campus. 

Request Shuttle : The Shuttle Service also provides a detailed schedule of the shuttle service running times, allowing users to plan their commutes efficiently and optimize their time on campus. Moreover, the service offers a request shuttle function that enables users to request shuttle services based on the current time, providing real-time information about the shuttle's location on campus and anticipated arrival times.

Contacts: By storing the contact information of shuttle drivers, the Shuttle Service empowers users to connect with drivers directly, streamlining the communication process and making it easier to address any special needs or concerns that may arise during transportation. 

## Modules 
Number of modules : 6

## Languages and Frameworks : 

### Front-end : 

1. Python
2. Flask
3. HTML and CSS

### Back-end :

1. MongoDB - Database
2. Python

## Devops Technologies:

1. Kubernetes
2. Docker

## External Services

1. Google Maps API - retrieves the Google Maps with access to current location and destinations

## Microservices


| Microservice Name  | Purpose                                                |
|-----------------|--------------------------------------------------------|
| Contacts        | Creates and displays contact information of the shuttle drivers
| RealTime       | Generates a time between 9:00 pm and 1:00 am
| RequestShuttle | Generates the arrival time and location of the shuttle
| RealTimeTracking| Generates the real-time tracking of the shuttle service
| Database | Holds stops and times to access 

## Trinity College Shuttle Service Architecture Diagram

![Diagram](https://github.com/aritrasaha18/shuttle-service-kata-project/blob/main/cloudproject.png)

## Sequence Diagram
![Sequence Diagram](https://github.com/aritrasaha18/shuttle-service-kata-project/blob/main/cloudproject-Sequence.png)

## How to deploy the application on Kubernetes

To run the app in Kubernetes, install Docker for Desktop Mac or Windows or choose GCP Kubernetes cluster. The folder inside shuttle-service named yaml_files contains all the YAML files for the app. Below are the steps for running the app in platforms:

1. First clone the project to GCP kubernetes cluster or local machine
```
    git clone https://github.com/aritrasaha18/shuttle-service-kata-project.git
```
2. Change directory to yaml_files
```
    cd shuttle-service/yaml_files
```
3. Compile and run the shell script, run.sh
```
    bash run.sh
```

4. Check and watch if all the components are up and running
```
   kubectl get all
```

## Testing the App on GKE

1. Follow the same procedures after cloning the files to your Google Kubernetes cluster
2. Deploy the Application in the same way as you would in Kubernetes running on your local machine
3. Access the main page by putting in the address as External-IP:8089 in Kubernetes from the command kubect get all as stated before
