# Changelog - Service App Espacio Extract Banner 

## [0.0.10] - 2024-04-30

Eduardo Izquierdo Rojas

### Added:

Added request body list payment sheet
- OpenAPI/payment_openapi.py

Added endpoint for list payment sheet
- apps/payment.py

Added repository for list payment sheet
- repositories/payment_repository.py

Added schema for list payment sheet
- schemas/payment_schema.py

### Changed:

rename variable row by col in iteration for of result in call functions

- repositories/academic_repository.py
- repositories/account_repository.py
- repositories/payment_repository.py
- repositories/student_repository.py


## [0.0.9] - 2024-04-29

Eduardo Izquierdo Rojas

### Added:

Added endpoint for general data 
- apps/student.py

Added request body for general data 
- OpenAPI/student_openapi.py

Added repository for general data 
- repositories/student_repository.py

Added schema for general data 
- schemas/student_schema.py

### Changed:

Addition of exception when there was an error connecting to the Oracle database 
or VPN interconnection error, when querying the database

- database/oracle/connection.py
- database/oracle/connection2.py
- repositories/academic_repository.py
- repositories/account_repository.py
- repositories/payment_repository.py
- repositories/student_repository.py
- repositories/table_repository.py

Adding incoming data to responses where there is no data to display 
- apps/academic.py
- apps/account.py
- apps/payment.py
- apps/student.py

Change in version 
- CHANGELOG.md
- app.py



## [0.0.8] - 2024-04-26

Eduardo Izquierdo Rojas

### Changed:

Adeed request body for  Report Card Unam and Academic History
- OpenAPI/academic_openapi.py

Added endpoints for  Report Card Unam and Academic History
- apps/academic.py

Added repositories for  Report Card Unam and Academic History
- repositories/academic_repository.py

Added schemas for  Report Card Unam and Academic History
- schemas/academic_schema.py


## [0.0.7] - 2024-04-26

Eduardo Izquierdo Rojas


### Changed:
Added request body for  generate sheet
- OpenAPI/payment_openapi.py

Added endpoint for generate sheet and get bank references
- apps/payment.py

Added repositories for generate sheet and get bank references
- repositories/payment_repository.py

Added response for generate sheet
- schemas/payment_schema.py


## [0.0.6] - 2024-04-25

Eduardo Izquierdo Rojas

### Changed:
Added insert_bank and reference repositories
- repositories/payment_repository.py

Added request bodies for insert_bank and reference repositories
- OpenAPI/payment_openapi.py

Added endpoints for insert_bank and reference repositories
- apps/payment.py

Added responses for insert_bank and reference
- schemas/payment_schema.py


## [0.0.5] - 2024-04-24

Eduardo Izquierdo Rojas

Added error when no exist school option 
- apps/academic.py                  
- apps/account.py                   
- apps/payment.py

### Changed:
Added return sequence repository

- repositories/payment_repository.py
- schemas/payment_schema.py
- OpenAPI/payment_openapi.py 

## [0.0.4] - 2024-04-23

### Changed:
Added debts repository

Added variable "UTG" to constants 
- constants/constants.py

Added response and open api for debts repository
- OpenAPI/payment_openapi.py
- apps/payment.py
- schemas/payment_schema.py

Added debts repository
-  repositories/payment_repository.py

Change name routes
- apps/academic.py
- apps/account.py
- apps/formalities.py
- apps/invoicing.py
- apps/payment.py
- apps/student.py


### Added:
added conection database UTG
- database/oracle/connection2.py
- config.py




## [0.0.3] - 2024-04-22

Eduardo Izquierdo Rojas

### Changed:
Added apps
- apps/academic.py

Added constants 
- constants/constants.py

Added response and app report card
- OpenAPI/academic_openapi.py
- apps/academic.py
- schemas/

Added repository
- repositories/academic_repository.py


## [0.0.2] - 2024-04-18

Eduardo Izquierdo Rojas

### Changed:

added app account 
- app.py 
- constants/routes.py

added dependencies 
- requirements.txt

added configuration in logger
- services/logger_service.py

added response success
- services/set_responses_service.py

### Added:
Added apps
- apps/academic.py
- apps/formalities.py 
- apps/invoicing.py 
- apps/payment.py 
- apps/student.py

Added constants 
- constants/constants.py

Added response and app account 
- OpenAPI/account_openapi.py
- apps/account.py
- schemas/

Added repository
- repositories/account_repository.py
  

## [0.0.1] - 2022-10-18

Eduardo Izquierdo Rojas

### Added:
Addition and structure of project of flask

Configuration
- python 3.10.X
- Connection to data base of mongodb
- Swagger Api documentation 3.0
- Framework Flask
- Routes and controller
- Pytest to create test's
- Pipenv environment
- Init Git
- logs

Directory's
- apps
- constants
- databases
- OpenApi
- repositories
- tests
- utils
- services
- logs



### Changed:
