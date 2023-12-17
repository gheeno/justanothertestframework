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
    1. Run the test `~ pytest --alluredir=allure-results`
    2. Generate the results  `~ allure generate allure-results --clean -o allure-report`
    3. Move history from report to results `~ mkdir -p allure-results/history && cp -r allure-report/history/* allure-results/history/ || true`
    4. Run report : `~ allure serve`


### Notes : 
- PageFactory Extended Methods : 
    - https://pypi.org/project/selenium-page-factory/


### TODO : 
1. Implement BDD
2. Define proper steps in reporting ( Allure )
    - This is solved in robotframework.
3. Test Tagging ( None Robotframework. )