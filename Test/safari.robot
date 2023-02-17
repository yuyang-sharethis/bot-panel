*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}
${browser}

*** Test Cases ***
Safari Scraping
    Open Browser  ${url}  ${browser}
    Maximize Browser Window
    Close Browser