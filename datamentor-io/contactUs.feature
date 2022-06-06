Feature: contact us

    As a user
    I want to fill out the contact us form
    So that I can submit my ideas and suggestion

    Background: the user is on the contact us page

    Scenario: User clicks on "DM" logo of header section
        Given the user is in header of the contact us
        When the user clicks on "DM logo"
        Then the user is redirected to DataMentor homepage

    Scenario: User types "string/numbers/signs" and clicks on "search-area" button of header section
        Given the user is in header of the contact us
        And the user types any type of string, integers or signs
        When the user clicks on search button
        Then the user is shifted to DataMentor homepage

    Scenario: User clicks
        Given context
        When event
        Then the user is shown three options to choose
            | Suggestion |
            | Error Page |
            | Other      |