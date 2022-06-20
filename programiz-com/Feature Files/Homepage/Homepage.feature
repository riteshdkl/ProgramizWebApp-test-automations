Feature: programiz.com Homepage

    As a user
    I want to view homepage
    so that i can view all the contents available on the homepage

    Background: The user is on the homepage


    Scenario: A user clicks on the Programiz logo

        Given the user is visible to the programiz logo on the navbar section
        When the user clicks on the programiz logo
        Then the homepage should reload
        And the user should see the title text
            """
            Programiz: Learn to Code for Free
            """


    Scenario: A user clicks on the tutorials dropdown

        Given the user is visible to the tutorials dropdown on the navbar section
        When the user clicks on the tutorials dropdown
        Then the user should see the list of courses available
            | Python |
        And inside the python course the user should see buttons with the text
            | ENROLL FOR FREE!     |
            | All Python Tutorials |
            | View all             |
            | SQl                  |
            | JavaScript           |
            | C                    |
            | C++                  |
            | Java                 |
            | Kotlin               |
            | Swift                |
            | C#                   |
            | DSA                  |


    Scenario: A user clicks on the exmaples dropdown

        Given the user is visible to the exmaples dropdown on the header section
        When the user clicks on the examples dropdown
        Then the user should see the list of examples available
            | Python     |
            | JavaScript |
            | C          |
        And inside the C examples the user should see buttons with the text
            | ENROLL FOR FREE! |
            | All C Examples   |
            | C++              |
            | Java             |
            | Kotlin           |



    Scenario: A user searches a course

        Given the user is visible to the search on the navbar section
        When the user enters a course name """Python"""
        Then the user should see all the details of the python courses available
            | Learn Python With 100+ Challenges — Enroll for Free |
            | Python Programming                                  |
            | Python 3 Tutorial                                   |
            | Python JSON                                         |
            | Python Modules                                      |


    Scenario: A user is visible to the heading and pagragraph of the heading section

        Given the user is on to the heading section
        When the user is visible to the texts
        Then the user should see the heading with text
            """Learn to Code for Free"""
        And the user should see the paragraph with text
            """
            Learn to code with our beginner-friendly tutorials and examples. Read tutorials and examples, write programs, run code and learn to code.
            """


    Scenario: A user subscribe for the latest tutorials and updates

        Given the user is visible to the """Enter your email address""" placeholder on the heading section
        When the user enters an email id
        And the user clicks on the Subscribe button
        Then the user should see a message on the screen with the text
            """
            Thank you for subscribing!
            """


    Scenario: A user visible to the """Choose what to learn""" heading of the heading section

        Given the user is on the heading section
        When the user is visible to the text
        Then the user should see the heading with the text
            """
            Choose what to learn
            """


    Scenario: A user clicks on """Learn Python""" button

        Given the user is visible to the programming languages list on the heading section
        When the user clicks on """Learn python""" button
        Then the user should be redirected to the """Learn Python Programming""" page
        And the user should heading with the text
            """
            Learn Python Programming
            """


    Scenario: A user clicks on """View all tutorials""" button

        Given the user is visible to the programming languages list on the heading section
        When the user clicks on the view all tutorials button
        Then the user should see """View fewer tutorials""" button
        And the user should see the list of programming languages being expanded with their respective buttons
            | Learn Swift  |
            | Learn C#     |
            | Learn Kotlin |


    Scenario: A user clicks on """View fewer tutorials""" button

        Given when the user is visible to the programming languages list on the heading section
        When the user clicks on the view fewer tutorials button
        Then the user should see """View all tutorials""" button
        And the user should see the list of programming languages that were added when pressing the """View all tutorials""" being collapsed



    Scenario: A user is visible to the """Programiz PRO Prepare for Your Career""" heading of the programizpro section

        Given the user is on the programizpro section
        When the user is visible to the texts
        Then the user should see the heading with text
            """
            Programiz Pro\nPrepare for Your Career
            """


    Scenario: A user clicks on """Join for FREE""" button

        Given the user is visible to the "Join for FREE" button on the programizpro section
        When the user clicks on the """Join for FREE""" button
        Then the user should be redirected to the "programiz.pro" website
        And the user should see the |ProgramizPRO| logo on the navbar section


    Scenario: A user clicks on "Interative Python Course" course card on Enroll Now for FREE Section

        Given the user is on the programizpro Section
        When the user clicks on the
            """
            Interative Python Course
            """
        Then the user should be redirected to the "programiz.pro" website
        And the user should see the heding text
            """Become a Python Master"""


    Scenario: A user clicks on """View all courses""" button on Enroll Now for FREE Section

        Given the user is on the programizpro Section
        When the user click on "View all courses" button
        Then the user should be redirected to the "https://programiz.pro/catalog" page
        And the user should see the course catalog-card
            | Become a Python Master          |
            | Become a C Master               |
            | Learn Python Basics             |
            | Python Beyond Basics            |
            | Learn C Programming             |
            | Python Basics Challenges        |
            | Python Beyond Basics Challenges |
            | C Programming Challenges        |
            | Become a Java Maste             |
            | Java Basics                     |
            | Java Basics Challenges          |
            | Java OOP                        |
            | Java OOP Challenges             |
            | Java Beyond Basics              |
            | Java Beyond Basics Challenges   |


    Scenario: A user is visible to the """Practice with our Online Compilers""" heading of the onlineCompilers section

        Given the user is on the onlineCompilers section
        When the user is visible to the texts
        Then the user should see the heading with the text
            """
            Practice with our Online Compilers
            """



    Scenario: A user clicks on "Python Compiler" button on onlineCompilers Section

        Given the user is on the onlineCompilers Section
        When the user clicks on
            """
            Python Compiler
            """
        Then the user is redirected to "programiz.com/python-programming/online-compiler" website
        And the user should see the heading with the text
            """
            Python Online Compiler
            """



    Scenario: A user is visible to "why programiz?" heading of the whyProgramiz Section

        Given the user is on the whyProgramiz section
        When the user is visible to the texts
        Then the user should see the contents with these texts
            """
            (tick icon)Programming made easy
            (star icon)Content You Can Trust
            (sad)Learn by Doing
            """

    Scenario: A user is visible to "Learn on the Go: Programiz for iOS & Android" heading of the mobileApplication section

        Given the user is on the mobileApp section
        When the user is visible to the texts
        Then the user should see the heading with the text
            """
            Learn on the Go: Programiz for iOS & Android
            """


    Scenario: A user clicks on "Learn C App" mobile app card on mobileApp Section

        Given the user is on the "Learn on the Go: Programiz for iOS & Android" Section
        When the user clicks on
            """
            Learn C App
            """
        Then the user should be redirected to "programiz.com/learn-python" website
        And the user should see the heading with the text
            """
            Learn C Programming on the Go
            """

    Scenario: A user clicks on "View all mobile apps" card on the mobileApp section

        Given the user is on the mobileApp section
        When the user clicks on the "View all mobile apps" button
        Then the user should see the "Learn java app" card being added on the screen


    #footer
    Scenario: A user clicks on the google play button on the footer section

        Given the user is on the footer section
        When the user click on the google play button
        Then the user should be redirected to the google play store
        And the user should see "Learn Python: Programiz" App on the play store


    Scenario: A user clicks on the "About" button on the footer section

        Given the user is on the footer section
        And is visible to the About button
        When the user clicks on the about button
        Then the user should be redirected to the About page
        And the user should see the contents heading with the text
            """
            4.9 Million monthly users rely on Programiz to learn programming
            """



    Scenario: A user clicks on the "Facebook" social media icon at the bottom right corner of the footer section

        Given the user is on the footer section
        And the user is visible to the Facebook icon
        When the user clicks on the icon
        Then the user should be redirected to the Programiz facebook page
        And the user should see the programiz logo on the screen





















