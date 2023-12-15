*** Settings ***
Library           ../test/test_python_page.py

*** Variables ***
${MESSAGE}        Hello, world!

*** Test Cases ***
My Test
    [Documentation]    Example test.
    Run Test

Another Test
    Should Be Equal    ${MESSAGE}    Hello, world!

*** Keywords ***
Run Test
    test_python_page.robot_sampletest