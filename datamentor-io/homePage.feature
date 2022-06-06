Feature: homepage exploration

    As a user
    I want to click all the present buttons
    So that I can explore more about the website

    Background:
        Given the user is on the homepage

    Scenario: User clicks on the DM logo
        When the user clicks on the "DM logo" on the header section
        Then the homepage is refreshed
        And the homepage is seen again with heading text
            """"
            Beginner's guide to Data Science with R
            """

    Scenario: User clicks on "Learn more on this book" link on the hero section
        Given the user is on the hero section
        When the user clicks on the link
            """
            Learn more on this book
            """
        Then the user is redirected to "r for beginners" page
        And the user should see these texts
            """
            R Programming for the Beginners eBook
            """
        And the page is linked to "R eCode" link of header section


    Scenario: User clicks on "About" link on the navigation tab bar
        Given the user is on the nav-tab section
        And the user sees different links with following texts
            | About | Course Index | Bonuses | FAQS |
        When the user clicks on the "About" link
        Then the user is scrolled directly to the about contents of the about-content section
        And the user should see the content with these texts
            """
            About this course
            """
    (with video)

    Scenario: User clicks the play button in the video of about-content__video section
        Given the user is now on the video section
        When the user clicks on the "play button"
        Then the user should see the video playing about Data Science
        And the user also sees other text in the sides

    Scenario: User clicks on "Read our beginner's guide to data science" of the convince-box section
        Given the user is on the convince section
        And the user scrolls and sees the texts Wondering if Data Science is for you?
        And the user also see read guide link with these texts
            """
            Read our beginner's guide to data science link
            """
        When the user clicks on the read guide link
        Then the user should switched to "What is Data Science Page?"

    Scenario: User clicks on "Course Index" link on the navigation tab bar
        Given the user is on the nav-tab bar
        When the user clicks on the "Course Index" link
        Then the user is scrolled down to the main course index of course section
        And the user should see the course index content with these texts of course accordian class
            | Getting Started      | 5 lectures |
            | Introduction         | Preview    |
            | Onboarding           | Preview    |
            | Get Data             | 8 lectures |
            | Explore Data: Part I | 6 lectures |

    Scenario: User clicks on "Expand All" link on the course section
        Given the user is now on the course section
        When the user clicks "+Expand All" link
        Then the whole course index content is displayed in the window
        And the user should see the course index content with these texts
            | Getting Started | 5 lectures |
            | Introduction    | Preview    |
            | Onboarding      | Preview    |


    Scenario: User clicks on "Expand All" link again
        Given the user is now on the course section
        When the user clicks "+Expand All" link again
        Then the whole course index content is collapsed from the window
        And the user sees these texts
            | Getting Started      | 5 lectures |
            | Get Data             | 8 lectures |
            | Explore Data: Part I | 6 lectures |

    Scenario: User clicks on the "Preview" link of course index
        Given the user is on the "Expand All" link
        When the user clicks on "Preview" link of the course accordian class
        Then the user should see the playing video of respective preview

    Scenario: User clicks on "Bonuses" link on the navigation tab bar
        Given the user is on the nav-tab section
        When the user clicks on the "Bonuses" link
        Then the user is scrolled down to the contents of bonus section
        And the user should see the texts
            """
            Bonus resoures included in the course
            """

    Scenario: User clicks on "Try our Code Playground" link of bonus section
        Given the user is on the bonus section
        When the user clicks the "Try our Code Playground" link of bonus content
        Then the user is redirected to "Playground" page
        And the user sees these texts
            """
            502 Bad Gateway
            """

    Scenario: User clicks on "Learn more about the book" link of bonus section
        Given the user is on the bonus section
        When the user clicks the "Learn more about the book" link of bonus content
        Then the user is redirected to "R eBook" page
        And the user sees these texts
            """
            R Programming for Beginners eBook
            A comprehensive book to getting started with R Programming.
            """

    Scenario: User clicks on "Try our Quiz" link of bonus section
        Given the user is on the bonus section
        When the user clicks the "Try our Code Playground" link of bonus content
        Then the user is redirected to "Quiz" page
        And the user sees these texts
            """
            502 Bad Gateway
            """

    Scenario: User clicks on "FAQs" link on the navigation tab bar
        Given the user is on the nav-tab section
        When the user clicks on the "FAQs" link
        Then the user is scrolled down to the contents of faq section
        And the user should see the texts
            """
            Frequently asked questions
            """

    Scenario: User clicks on "expand button"
        Given the user is on faq-accordion__nodes of the faq section
        When the user clicks on expand button (>) of faq accordion node second
        Then the user is displayed hidden texts of answer to the question with the answers
            """
            You are only charged a one-time fee for the course, and you can access all the materials of the course anytime you want. There are no additional or recurring charges.
            """

    Scenario: User clicks on "expand button" again
        Given the user is on faq-accordion__nodes of the faq section
        When the user clicks on expand button (>) of  any faq accordion nodes
        Then the user is displayed answers of that specific node while other stay hidden

    Scenario: User clicks on "DM logo" of footer section
        Given the user is in the footer section
        When the user clicks on DM logo
        Then the page is refreshed
        And the user goes to the top of the page

    Scenario: User clicks on "Data Science with R" link of footer section
        Given the user is in footer list item of Courses in the footer section
        When the user clicks on Data science with R link
        Then the page is redirected to top of the homepage

    Scenario: User clicks on "R Examples" link of footer section
        Given the user is in footer list item of Free Resources in the footer section
        When the user clicks on R Examples link
        Then the page is shifted to "R Programming Examples- DataMentor" page
        And the user sees the heading which says
            | R Programming Examples |
        And the heading is followed by the texts
            """
            This page contains examples on basic concepts of R programming.
            """

    Scenario: User clicks on "Contact Us" link of footer
        Given the user is in footer list item of Company in the footer section
        When the user clicks on contact us link
        Then the user is redirected to Contact Us page
        And the user sees this text
            """
            Contact Us
            """

    Scenario: User clicks on "Privacy Policy" link of footer
        Given the user is in footer list item of Legal in the footer section
        When the user clicks on privacy policy link
        Then the user is redirected to privacy policy page
        And the user sees this heading
            | Privacy Policy |
        And the heading is followed by these texts
            """
            This privacy policy sets out how Parewa Labs Pvt. Ltd. (“we/Parewa Labs”) treats the privacy of customers and others with whom we interact.
            """































