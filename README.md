# Lab: Class 32 - DRF API Permissions and Postgresql

## Open Git Pull Requests  


## Overview  

Let’s move our site closer to production grade by adding Permissions and Postgresql Database.

## Feature Tasks and Requirements  

### General
- You have been supplied with two demos, each presenting a key new feature.
  - `blogapi-permissions` demonstrates how to restrict access to portions of your APIs data.
  - `blogapi-postgres `demonstrates switching over to using postgres vs sqlite
- Your job is to merge the functionality of both demos.
- Customize your project to use different application features/models than `Blog` and `Post`

### Django REST Framework  
- [x] Make your site a DRF powered API as you did in previous lab.
- [x] Adjust project’s permissions so that only authenticated user’s have access to API.
- [x] Add a custom permission so that only author of blog post can update or delete it.
- [x] Add ability to switch user’s directly from browsable API.

### Docker  
- `NOTE` Refer to demo for built out `Dockerfile` and `docker-compose.yml` examples.
  - [x] create `Dockerfile` based off `python:3.8-slim`
- [x] create `docker-compose.yml` to run Django app as a `web` service.
- [x] enter `docker-compose up --build` to start your site.
- [] add `postgres 11` as a service
    - Note: It is not required to include a volume so that data can persist when container is shut down.
- [x] Go to browsable api and confirm site properly restricts users based on their permissions.

## Implementation Notes:  
- [] You should NOT be running Postgres directly on host machine.
  - [] This means that operations like createsuperuser and migrate will need to happen inside the container.

## User Acceptance Tests  
- [x] Adjust any tests provided in demo to work with your project.  

## Dependencies  
- Docker version 19.03.8, build afacb8b7f0
- python = "^3.8"
- django = "^3.0.7"
- djangorestframework = "^3.11.0"

## Authors  
- Software Developer: Joseph Zabaleta
  - [Official Github](https://github.com/joseph-zabaleta)  

## Collaborations  
- none  

## License  
This project is under the MIT License.

## Acknowledgements / Resources  
- none

## Version History  
- 1.0.0 20200623
    - Initial files created.  
