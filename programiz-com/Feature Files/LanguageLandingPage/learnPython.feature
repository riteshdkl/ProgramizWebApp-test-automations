Feature: Language landing page

    As a user
    I want to view language landing page
    so that i can view all the details about the language that are available on the website

    Background: The user is on the python-programming page

    Scenario: A user sees "Learn Python Programming" heading

        When the user is visible to the texts on the website
        Then the user should see the heading with the text
            """
            Learn Python Programming
            """

    Scenario: A user clicks on the "Try PRO for FREE" button

        When the user clicks on the "Try PRO for FREE" on the navbar
        Then the user should be redirected to the "https://programiz.pro/learn/master-python" link
        And the user should the heading with the text
            """
            Become a Python Master
            """

    Scenario: A user clicks on the "Tutorials" button

        When the user clicks on the "Tutorials" button
        Then the homepage should be refreshed
        And the user should see the heading with the text
            """
            Learn Python Programming
            """

    Scenario: A user clicks on the "Course" button

        When the user clicks on the "Course" button
        Then the user should be redirected to the "https://programiz.pro/learn/master-python" link
        And the user should see the heading with the text
            """
            Become a Python Master
            """

    Scenario: A user clicks on the "Examples" button

        When the user clicks on the "Examples" button
        Then the user should see the heading changed with the text
            """
            Python Examples
            """
        And the user should see the "Popular Examples" section
        And the user should see the python examples cards displayed with the text
            | Python Program to Check Prime Number             |
            | Python Program to Add Two Numbers                |
            | Python Program to Find the Factorial of a Number |
            | Python Program to Make a Simple Calculator       |
        And also the user should see the list of all examples


    Scenario: A user clicks on "REFERENCES" button


        When the user clicks on the "REFERENCES" button
        Then the user should see the heading changed with the text
            """Python References"""
        And the user should see a search bar for searching python methods
        And also the user should see the list of python built-in functions with text
            | Python Built-in functions |
            | Python Dictionary Methods |
            | Python List Methods       |
            | Python Set Methods        |
            | Python String Methods     |
            | Python Tuple Methods      |

    Scenario: A user clicks on "COMPILER" button


        When the user clicks on "COMPILER" button
        Then the user should be redirected to the compiler page
        And the user should see a heading with the text
            """
            Python Online Compiler
            """


    Scenario: A user clicks on the "Interactive Python Course" Link

        When the user clicks on the "Interactive Python Course" Link
        Then the user should be redirected to the "https://programiz.pro/learn/master-python" link
        And the user should see the heading with the text
            """
            Become a Python Master
            """

    Scenario: A user sees list of contents inside "Page Index" card

        When the user is visible to the texts
        Then the user should see the list of contents with the text
            | Introduction             |
            | Flow Control             |
            | Function                 |
            | Data Types               |
            | File Handling            |
            | Object & Class           |
            | Advanced Tutorials       |
            | Date and Time            |
            | About Python Programming |
            | Why Learn Python         |
            | How to learn Python      |
            | Python Resources         |

    Scenario: A user sees list of contents inside "Introduction" card


        When the user is visible to the texts
        Then the user should see the list of contents with the text
            | Getting Started          |
            | Keywords and Identifiers |
            | Statements & Comments    |
            | Python Variables         |
            | Python Datatypes         |
            | Python Type Conversion   |
            | Python I/O and import    |
            | Python Operators         |
            | Python Namespace         |

    Scenario: A user sees list of contents inside "Python Flow Control" card


        When the user is visible to the texts
        Then the user should see the list of contents with the text
            | Python if...else          |
            | Python for Loop           |
            | Python while Loop         |
            | Python break and continue |
            | Python Pass               |

    Scenario: A user sees list of contents inside "Python Functions" card


        When the user is visible to the texts
        Then the user should see the list of contents with the text
            | Python Functions           |
            | Function Argument          |
            | Python Recursion           |
            | Anonymous Function         |
            | Global, Local and Nonlocal |
            | Python Global Keyword      |
            | Python Modules             |
            | Python Package             |

    Scenario: A user sees list of contents inside "Python Datatypes" card


        When the user is visible to the texts
        Then the user should see the list of contents with the text
            | Python Numbers    |
            | Python List       |
            | Python Tuple      |
            | Python String     |
            | Python Set        |
            | Python Dictionary |

    Scenario: A user sees list of contents inside "Python Files" card

        When the user is visible to the texts
        Then the user should see the list of contents with the text
            | Python File Operation         |
            | Python Directory              |
            | Python Exception              |
            | Python Exception Handling     |
            | Python User-defined Exception |


    Scenario: A user sees list of contents inside "Python Object & Class" card


        When the user is visible to the texts
        Then the user should see the list of contents with the text
            | Python OOP           |
            | Python Class         |
            | Python Inheritance   |
            | Multiple Inheritance |
            | Operator Overloading |

    Scenario: A user sees the list of contents inside "Python Advanced Topics" card

        When the user is visible to the texts
        Then the user should see the list of contents with the text
            | Python Iterator   |
            | Python Generator  |
            | Python Closure    |
            | Python Decorators |
            | Python Property   |
            | Python RegEx      |
            | Python Examples   |

    Scenario: A user sees the list of contents inside "Python Date & Time" card

        When the user is visible to the texts
        Then the user should see the list of contents with the text
            | Python datetime Module     |
            | Python datetime.strftime() |
            | Python datetime.strptime() |
            | Current date & time        |
            | Get current time           |
            | Timestamp to datetime      |
            | Python time Module         |
            | Python time.sleep()        |


    Scenario: A user sees the "About Python Programming" section

        When the user is visible to the texts
        Then the user should see the heading with the text
            """
            About Python Programming
            """
        And the user should also see the bullet points with the text
            | Free and open-source - You can freely use and distribute Python, even for commercial use.                                                                        |
            | Easy to learn  - Python has a very simple and elegant syntax. It's much easier to read and write Python programs compared to other languages like C++, Java, C#. |
            | Portable - You can move Python programs from one platform to another, and run it without any changes                                                             |


    Scenario: A user sees the "Why Learn Python" Section


        When the user is visible to the texts
        Then the user should see the heading with the text
            """
            Why Learn Python?
            """
        And the user shoud also see the bullet points with the text
            | Python is easy to learn. Its syntax is easy and code is very readable.                                                               |
            | Python has a lot of applications. It's used for developing web applications, data science, rapid application development, and so on. |
            | Python allows you to write programs in fewer lines of code than most of the programming languages.                                   |
            | The popularity of Python is growing rapidly. Now it's one of the most popular programming languages.                                 |


    Scenario: A user sees the "How to learn Python?" section


        When the user is visible to the texts
        Then the user should see the heading with the text
            """
            How to learn Python?
            """
        And the user shoud also see the bullet points
        And also the user should see the links
            | Python Interactive Course |
            | Get started with Python.  |
            | Python tutorial.          |
            | Learn Python app          |




