# Rock in Class

![responsive](docs/readme_images/responsive.jpg)


Rock in Class, an online music school, serves as a platform where individuals can discover skilled tutors and schedule online music classes with them.


You can view the live site at **[Rock in Class](https://rock-in-class-324f436b36b0.herokuapp.com/).**


## Table of contents

 1. [ UX ](#ux)
 2. [ User Story and Agile Development](#user-story-and-agile)
 3. [ Features ](#features)  
 4. [ Technology used ](#technology-used) 
 5. [ Testing ](#testing)  
 6. [ Bugs ](#bugs)  
 7. [ Deployment](#deployment)
 8. [ Credits](#credits)
 9. [ Content](#content)  
 10. [ Acknowledgements](#acknowledgements)  

 # Ux

 Rock in Class is a conceptual online music school that I conceived and developed a website for. The primary objective of the website is to provide users with the ability to explore available tutors, assess their offerings, and, if satisfied, create an account to schedule music classes.

 ## Design

 Upon discovering the name,  I opted for a modern and minimalistic design approach for the website—something straightforward yet easily navigable.
 ### Colors
 The selected primary colors for the website.
 ![color-pallete](docs/readme_images/color-palette.jpg)

 ### Wireframes

 I have created wireframes for the key pages of the site, utilizing Paint3D for the design. The following wireframes for the main pages:

- Home Page

 My objective with this project was to create a minimalist website, designed to showcase the tutors of the school's music department. I purposefully kept the page count to a minimum to prioritize and highlight the essential functionality.
 ![home-page](docs/readme_images/home-page.jpg)

- Tutors

 The tutors' wireframe is designed to display their pictures, provide a brief introduction, and detail the type of instrument and genre of music they specialize in.
 ![tutors](docs/readme_images/tutors.jpg)

- About

The wireframe for the "About" page includes our contact information and provides a brief overview of who we are.
![about](docs/readme_images/about.jpg)

- Sign up

The signup wireframe is straightforward, requiring only your username, email, password, and password confirmation.
![Sign-up](docs/readme_images/signup.jpg)

- Sign in

The sign-in wireframe is uncomplicated, requesting only your username and password for authentication.
![Sign-in](docs/readme_images/sigin.jpg)

- Profile

Within the profile wireframe, you can view your bookings, as well as edit (reschedule) or delete them as needed.
![profile](docs/readme_images/profile.jpg)


# User story and Agile

## User Story

I have established Epics for every essential feature outlined in my scope. Here are the projected user stories associated with each of them:

### Admin management

 - As an **admin** I can **log in to the admin panel** so that **I can manage/see the panel**.

- As an **admin** I can **manage the booking that was made by a student** so that I can **delete or reschedule the appointment**.
- As an **admin** I can **manage the tutor profile in the admin panel** so that I can **delete, update, or add a new tutor**.

### Student account

- As a **student** I can **create an account** so that I can **save my preferences**.

- As a **student** I can **receive a message in the website** so that I am **aware that the registration process is correct**.
- As a **student** I can **log out** so that I **keep my account information secure**.

### Manage booking

- As a **student** I can **log in** so that I can **view my profile or edit it**.

- As a **student** I can **select the date, time and tutor** so that I can **book a class**.

- As a **student** I can **manage my booking** so I can **reschedule or delete the booking**.

#### The user story that is label as Won't have is:
 - As a **student** I can **reset my password** so that I can **change my password if I forget**.

 This might be implemented in the future. Currently, if a student forgets their password, they should reach out to the school for assistance, as indicated on the website.

## Agile development


I initiated this project in a GitHub Projects Page to monitor and organize the anticipated workload. The goal was to outline the expected tasks, categorize them into epics, and further break them down into user stories or manageable tasks. This structured approach aimed to facilitate progress and ensure timely completion of the website.

To see Kanban please click [here](https://github.com/users/Bruna-Andelieri/projects/2/views/1).



# Features

### Home Page
It involves a banner featuring the music school's slogan, creating a straightforward website.
![home-page](docs/readme_images/feat-home.jpg)

### Navegation bar
It's straightforward – the **logo**(directs to home page), **Tutors** section for class bookings, **Sign In** for existing accounts, and **Sign Up** for new students.
![nav-bar](docs/readme_images/feat-navbar.jpg)

### About
In this section, you'll find a brief description of the school, along with the contact email and links to our social media profiles.
![about](docs/readme_images/feat-about.jpg)

### Tutors
- This section you can find out more about the Tutors.
Each tutor has a brief description highlighting the genre of music they specialize in and the instruments they play.
![tutors](docs/readme_images/feat-tutors.jpg)

- For tutors who haven't a profile picture yet, a default image is provided.
![tutors-default](docs/readme_images/feat-tutors-default.jpg)

- Upon selecting the tutors for your class, a message will be displayed to sign in beforehand.
![tutors-signin](docs/readme_images/feat-tutors-book.jpg)

- When logged into the website, you can book a class directly from the tutors' page.
![tutors-booking](docs/readme_images/feat-booking.jpg)

### Sign up
- This section is for sign up to the website. There is a validation of the password.
![sigup](docs/readme_images/feat-signup.jpg)

- Once you've successfully signed up on the website, feedback will appear at the top of the page.
![signup-logon](docs/readme_images/feat-sucessfuly-signed.jpg)

### Sign in
Once you have your account you can sign in if your username and password.
![signin](docs/readme_images/feat-signin.jpg)

### Profile
This section the student could reschedule or delete a booking.
![profile](docs/readme_images/feat-profile.jpg)


# Testing
In my project, I utilize a manual testing. I employ a range of tools to validate HTML  and Python code.I have integrated performance checks from Google Lighthouse as well.

### Manual testing:

|   Test  |                    Expected                    | Result |
|:-------:|:----------------------------------------------:|:------:|
| Sign Up | user able to type an username                  | pass   |
|         | user able to type an email                     | pass   |
|         | user able to type a password                   | pass   |
|         | user able to type a password confirmation      | pass   |
|         |                                                |        |
| Sign In | user able to type an username                  | pass   |
|         | user able to type a password                   | pass   |
|         | user able to log out                           | pass   |
|         |                                                |        |
| User    | user able to click about page                  | pass   |
|         | user able to click tutors page                 | pass   |
|         | user able to click sign in page                | pass   |
|         | user able to click sign up page                | pass   |
|         | user able to click links to social media       | pass   |
|         | user able to navigate trhough the website      | pass   |
|         |                                                |        |
| Booking | student able to booking a class                | pass   |
|         | student able to select the date                | pass   |
|         | student able to select the time of the class   | pass   |
|         | student able to edit booking                   | pass   |
|         | student able to delete booking                 | pass   |
|         | student able to save booking in profile        | pass   |
|         |                                                |        |
| Admin   |                                                |        |
|         | admin able to log in django panel              | pass   |
|         | admin able to add, edit and delete tutors      | pass   |
|         | admin able to edit and delete bookings         | pass   |
|         | admin able to add, edit and delete instruments | pass   |
|         | admin able to add, edit and delete music style | pass   |
|         |                                                |        |
|         |                                                |        |


### HTML validator

![HTML](docs/readme_images/html-validator.jpg)

### Python and Django

Because of the numerous Python files in my projec I have install [Flake8](https://pypi.org/project/flake8-django/) in my terminal for testing Python and Django. 

![Flake](docs/readme_images/flake-validator.jpg)

I have used [CI Python](https://pep8ci.herokuapp.com/) for some files.
![Python](docs/readme_images/python-linter.jpg)

### Accessibility 

![Lighthouse](docs/readme_images/lighthouse.jpg)

# Technology used

[HTML](https://html.spec.whatwg.org/) is the standard markup language for documents designed to be displayed in a web browser.

[CSS](https://www.w3.org/Style/CSS/Overview.en.html) Cascading Style Sheets (CSS) is a stylesheet language used to describe the presentation of a document written in HTML or XML.

[JavaScript](https://www.javascript.com/) is a programming language that adds interactivity to your website.

[Bootstrap 5](https://getbootstrap.com/) is a free and open-source CSS framework directed at responsive, mobile-first front-end web development. It contains HTML, CSS and (optionally) Javascript.

[Python](https://www.python.org/) is an interpreted, high-level, and general-purpose programming language.

[Django](https://www.djangoproject.com/) is a high-level Python Web framework that encourages rapid development and clean, pragmatic design.

[ElephantSQL](https://www.elephantsql.com/) is a well-tuned and optimized PostgreSQL databases system.

[Cloudinary](https://cloudinary.com/) is a cloud service that offers a solution to a web application's entire image management pipeline.

[Heroku](https://www.heroku.com/) is a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

# Deployment

<details>
<summary>Heroku Deployment</summary>

- sLog in to Heroku or sign up if you don't have an account.
- On the main Heroku Dashboard page, click 'New' and then 'Create New App.'
- Provide a unique name for your project, and then choose a region closest to you (EU or USA).
- Click on "Create App" to proceed.
- Heroku will create the app and take you to the deploy tab.
- From the new app Settings, click Reveal Config Vars, and set your environment variables:

>`CLOUDINARY_URL`        | insert your own Cloudinary API key here                      
>`DATABASE_URL`          | insert your own ElephantSQL database URL here         
>`DISABLE_COLLECTSTATIC` | 1 (_this is temporary, and can be removed for the final deployment_)
>
>`SECRET_KEY`            | this can be any random secret key   
- Heroku needs two additional files in order to deploy properly(add in your code).

  - requirements.txt
  - Procfile
- Select **Automatic Deployment** from the Heroku app to conect to your Github repository.     
</details>                     
<details>
<summary>Cloudinary</summary>

- Log in to Cloudinary or sign up if you don't have an account.
- Under Primary interest, select Programmable Media for image and video API.
- Optionally, customize your assigned cloud name to something more memorable.
- On your Cloudinary Dashboard, copy your API Environment Variable.
- Ensure to exclude CLOUDINARY_URL= from the API **value**; this part is the **key**.

</details>

<details>
<summary>ElephantSQL Database</summary>

- To set up your personal Postgres Database, register with your GitHub account, and then proceed with the following steps:
  - Initiate the process by clicking on Create New Instance to establish a new database.
  - Give a name for the database, typically aligned with the project's name.
  - Opt for the Tiny Turtle (Free) plan.
  - The Tags field can be left empty.
  - Choose the nearest Region and Data Center for your location.
  - Once the database is created, click on its name to access details such as the database URL and Password.
</details>

<details>
<summary>Local Deployment</summary>

Feel free to clone or fork this project to establish a local copy on your system.
#### Cloning 
To clone the project please follow the steps bellow:

- Visit the GitHub repository
- Find the Code button above the file list, and click it. 
- Choose your preferred cloning method (HTTPS, SSH, or GitHub CLI) and click the copy button to copy the URL. 
- Open the Terminal, navigate to the desired directory, and in your IDE Terminal, enter the command:
  - git clone https://github.com/Bruna-Andelieri/rock-in-class.git
- Press Enter to create your local clone.

#### Forking
Forking the GitHub repository allows you to create a duplicate of the original repository, enabling you to view or make changes without impacting the original. This can be done by:

- Sign in to GitHub or sign up for an account.
- Find the repository.
- On the repository page, at the upper right corner, choose "Fork" from the available buttons.
- A duplicate of the repository will be generated in your personal repository.

</details>


# Credits

[Unplash](https://unsplash.com/) is a go-to platform for high-quality, freely usable images contributed by photographers, serving diverse creative needs.
All images I used in this website are sourced from Unsplash, and due credit goes to the generous photographers who have shared their work for free use.

- Tutor "Bob" - Photo by <a href="https://unsplash.com/@jerec_?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Jeremias Ybañez</a> on <a href="https://unsplash.com/photos/a-man-holding-a-guitar-while-standing-next-to-a-microphone-Q0NOkBPGtU8?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>

- Tutor "Michael" - Photo by <a href="https://unsplash.com/@adrianlinaresfoto?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Adrian Linares</a> on <a href="https://unsplash.com/photos/man-in-black-jacket-playing-electric-keyboard-dWVRLLhmyL0?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>

- Tutor "Alice" - Photo by <a href="https://unsplash.com/@xan868?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Ruslan Mingazhov</a> on <a href="https://unsplash.com/photos/a-woman-sitting-at-a-piano-on-a-beach-ijOz6pNmUew?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>

- Tutor "Emma" - Photo by <a href="https://unsplash.com/@imjustintime?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Justin Clark</a> on <a href="https://unsplash.com/photos/a-woman-holding-a-guitar-in-a-field-mK8bHYCtLrg?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>
  
  
  

# Content

[W3 Schools](https://www.w3schools.com/) was employed for various research and tutorials related to HTML and CSS. 

[Stack Overflow](https://stackoverflow.com/) was utilized to seek answers and clarification for questions. 

[PEP8 ORG](https://pep8.org/) provided solutions for flags concerning diagrams in the PEP8 Validator.

# Acknowledgements

In conclusion, I want to convey my sincere gratitude to the individuals and communities mentioned below:

- Code Institute provided me with essential support and guidance during the project's development, thanks to my mentor Rohit Sharma, the helpful Slack community, and the invaluable support from my Cohort and colleagues in our class.

- My partner, Ivan, who not only assisted me with coding but also believed in me. His unwavering support has enabled my transition into the field of software development, and I am genuinely thankful for his contributions, which played a crucial role in the success and completion of this project.
