Feature: Programiz Homepage

    As a user
    I want to view homepage
    so that i can view all the contents available on the homepage

    Background: The user is on the homepage


    Scenario: A user clicks on the Programiz logo

    Given the user is visible to the programiz logo on the header section
    When the user clicks on the programiz logo
    Then the homepage should reload


    Scenario: A user clicks on the tutorials dropdown

    Given the user is visible to the tutorials dropdown on the header section
    When the user clicks on the tutorials dropdown
    Then the user should see the list of courses available 



    Scenario: A user clicks on the exmaples dropdown

    Given the user is visible to the exmaples dropdown on the header section
    When the user clicks on the examples dropdown
    Then the user should see the list of examples available
 

    Scenario: A user searches a course

    Given the user is visible to the search at the navBar
    When the user enters a course name
    Then the user should see the details of that course available on the website



    # Scenario: A user sees the correct heading and pagragraph of the webpage

    Given the user is on the homepage
    When 
    Then the user should see the correct heading with text
            """Learn to Code for Free"""
    And paragraph
        """Learn to code with our beginner-friendly tutorials and examples. Read tutorials and examples, write programs, run code and learn to code."""



    Scenario: A user subscribe for the latest tutorials and updates

    Given the user is visible to the "Enter your email address" placeholder on the homepage
    When the user enters an email id
    And clicks Subscribe button
    Then the user should see "Thank you for subscribing!" message on the Homepage screen




    Scenario: A user clicks on "Learn Python" button

    Given the user is visible to the programming languages list on the homepage
    When the user clicks on Learn python
    Then the user should be redirected to the learn python programming page



    Scenario: A user clicks on "View all tutorials" link

    Given the user is visible to the programming languages list on the homepage
    When the user clicks on the view all tutorials 
    Then the user should see all the list of programming languages with their respective buttons on the homepage



    
    # Scenario: A user clicks on "View fewer tutorials button"

    # Given when the user is visible to the programming languages list on the homepage
    # When the user clicks on the view fewer tutorials button
    # Then the user should see all the list of programming languages with their respective buttons


    Scenario: A user clicks on "Join for FREE" button 

    Given the user is visible to the "Join for FREE" button on the homescreen
    When the user clicks on the button
    Then the user should be redirected to the "programiz.pro" website




    Scenario: A user clicks on "Python Programming Course" course card on Enroll Now for FREE Section

    Given the user is on the Enroll Now for FREE Section
    When the user clicks on the 
        """
        Python Programming Course
        """ 
    Then the user should be redirected to the "programiz.pro" website




    Scenario: A user clicks on "Python Compiler" button on "Practice with our online compilers" Section

    Given the user is on the Practice with our online compilers Section
    When the user clicks on 
        """
        Python Compiler
        """
    Then the user is redirected to "programiz.com/python-programming/online-compiler" website


    # Scenario: A user sees 


    Scenario: A user clicks on "Learn C Programming App" mobile app card on "Learn on the Go: Programiz for iOS & Android" Section

    Given the user is on the "Learn on the Go: Programiz for iOS & Android" Section
    When the user clicks on 
            """
            Learn C Programming App
            """
    Then the user should be redirected to "programiz.com/learn-python" website


    #footer
    Scenario: A user clicks on the google play button on the footer section

    Given the user is on the footer section 
    When the user click on the google play button
    Then the user should be redirected to the google play store



    Scenario: A user clicks on the "About" button on the footer section

    Given the user is on the footer section
    And is visible to the About button
    When the user clicks on the about button
    Then the user should be redirected to the About page
    And the user should also see the contents available on the About page



    Scenario: A user clicks on the social media icons which are available at the bottom right corner of the footer section

    Given the user is on the footer section 
    And the user is visible to the social media icons
    When the user clicks on one of the icon
    Then the user should be redirected to the respective social media pages
    




    















