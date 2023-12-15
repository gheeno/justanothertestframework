# justanothertestframework
Python Test Framework

A simple Selenium Automation Test Framework.

### How to use

Perform commands from root folder ```/justanothertestframework```
1. Install pip requirements : 
    ```commandline
    ~ pip install -r requirements.txt 
    ```
    ```commandline
    ~ pip install -e .
    ```

2. Install Allure for reporting : 
    ```commandline
    brew install allure
    ```

2. To run sample test and generate allure results :
    ```commandline
    ~ pytest --alluredir=allure-results
    ```

### Reporting
1. Robotframework : `./results`
2. Allure : 
- Generate : 
    ```commandline
    ~ allure generate allure-results -o allure-report --clean
    ```
- Serve : 
    ```commandline
    ~ allure serve allure-results
    ```


### Notes : 
- PageFactory Extended Methods : 
    - https://pypi.org/project/selenium-page-factory/


### TODO : 
1. Implement BDD
2. Add screenshot to reporting
3. Define proper steps in reporting ( Allure )
    - This is solved in robotframework.
4. Test Tagging ( None Robotframework. )