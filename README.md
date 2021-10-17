# Interpreter Invoicing App

<div align="center">
    <img src="assets/images/mockup.png" alt="Mockup of how home page looks on diffferent screen sizes"/>
</div>
<br>

[View deployed site here](https://#/)

## Project Description
As a freelance interpreter, invoicing is the most tedious part of my job. However, it is also crucial because it is how I get paid. Existing invoicing apps do not really work for because of the specific rate structure I have as an interpreter working within the language justice framework, i.e., charging based on the client's overall budget. Building an application to autmoate invoicing has been a goal of mine ever since I embarked on my coding journey with the Code Institute.

The current version of the application is a prototype designed to be used only by myself. However, in the future I hope to tweak it further add additinal features based on my experience using the application and share it with other language justice practitioners. 

Currently, the general goals of the application are:
* Provide login, logout, and new user registration functionality
* Accept new client data and store it in the database
* Allow the user to edit and delete existing client data entries
* Provide an easy-to-use templae for interpreting invoice creation
* Convert the HTML invoice into a PDF document ready to be shared with clients


## UX

### Core Target Audience
#### The core target audience of this application is:
* Interpreters working within the language justice framework, like myself
* Interpreters living in the United States and using English as their language of communication with their clients
* Interpreters with recurring clients whose invoicing process can be facilitated by drawing on a client information database

#### Users of this application are searching for:
* A place to save, modify, and delete interpreting client information
* An easy way to created interpreting invoices based on existing client and rate information

#### Client Stories
1. As a new user of the application, I want to be able to easily register and start using the applilication.
2. As an existing user of the application, I want to be able to manage my client information and easily create ready-to-share invoices

### Wireframe Mockups: 
- [Registration Page](assets/img/wireframes/#)
- [Login age](assets/img/wireframes/#)
- [Add Client Page](assets/img/wireframes/#)
- [All Clients Page](assets/img/wireframes/#)
- [Edit Client Page](assets/img/wireframes/#)
- [New Invoice Page](assets/img/wireframes/#)
- [Profile Page](assets/img/wireframes/#)


## Features
#### Across Pages
Each page features a responsive **navigation bar** with conventional placing of **logo** (top left).

Every page features a background appropriate to the them of invoicing. 

#### Registration
The registration page allows new users to register. The **input fields** for username and password have input **validation** to ensure the new account is properly set up. Users who are already registered can get the login page by clicking either on the navbar item in the upper right corner or by the link proviced below the sign-up field.

#### Login
The login page allows existing users to log in to their account. The **input fields** for username and password have input **validation** to ensure the input matches the requirements for each field. New users can get the registration page by clicking either on the navbar item in the upper right corner or by the link proviced below the login field.

#### Add Client Page
The add client page allows users to add client information to the database. Each entry consists of **four text input fields**:
- Name of the organization
- Name of the contact 
- Position of the contact
- Email address of the contact
In addition, the **dropdown menu** at the bottom lets the user select the rate tier of the organization: Institution, Small Non-Profit, Large Non-Profit. All fields are required. Upon completing the form, the user will click the **Submit button** to add the new client to the database.

**NOTE I:** _Once I have tested the application out myself for a bit, I would like to make it available to other language justice practitioners. At that stage, I will add a page where users will be able add rates the same way they are now able to add client information. For this initial prototype, I'm using rates I have added dirctly to MongoDB._

#### Manage Clients Page
The manage client page contains a **list of all client organizations in the database**. Upon clicking on the caret, the user can view the full set of client details fore each user. Clicking the carot again, closes the details section. Additionally, the user can delete any entry by clikcing the **Delete button** or edit it by clicking the **Edit button**, which takes the user to the edit client page.

##### Edit Client Page
The edit client page allows users to edit existing client information. Each entry consists of **four text input fields**:
- Name of the organization
- Name of the contact 
- Position of the contact
- Email address of the contact
In addition, the **dropdown menu** at the bottom lets the user select the rate tier of the organization: Institution, Small Non-Profit, Large Non-Profit. Subsequently, the user can either click the **Submit button** to modify the client data in the database or the **Cancel button** to discard the changes. Upon clicking the Submit button, the user sees the confirmation message "Client Successfully Updated." Upon clicking either button, the user is eventually sent back to the manage clients page.

#### New Invoice Page
The new invoice page provides a templae for the user to create an invoice based on the client and rate data in the database. Upon selecting the **client organization** from the dropdown menu, the remaining fields (contact, position, and email address) populate automatically. In the next template section, the user manually adds ***event name, date, and time**. In the third and final template section, the user selects a **rate based on the job duration** and a **billable amount** from two dropdown menus. If **consulting** was part of the job, the user gets to select this and the corresponding **billable amount** in from the dropdown menus on the next line. At the bottome of the page, the total amount gets caculated automatically. Finally, the user can click the **Download PDF** button to download his invoice as a pdf document.

#### Profile Page
The profile page greets the user with his **username**. It is displayed upon login, and the user can get back to it anytime while they are logged in by clicking on the logo in the upper left corner. In addtion to the greeting, the profile page provides a quick overview of the application functionality with hyperlinks to the corresponding pages. 

**NOTE II:** _Before sharing the application with other langauge justice practitioners, I will expand the profile page. Users will be able to additional contact information here and submit it to the database, and the header on the invoice will be drawn directly from there. Additionally, there will be a contact form on this page and copyright information across all pages._

### Existing Features
- Header Navigation Bar - Exists on [every page](base.html) and allows all users to easily navigate all the website's pages and find what they are looking for quickly, including being led back to their profile page when cklicing on the **logo**. (When clicking on the logo while not logged in, the login page will reload.)
- [Registration Page](register.html) - Allows new users to open an account and leads existing users to the login page throughte embedded link or by clicking on the Log In item in the navbar.
- [Login Page](login.html) - Allows existing users to log in to their account and leads new users to the registration page throughte embedded link or by clicking on the Log In item in the navbar.
- [Add Client Page](addClient.html) - Displayed only to logged in users. Provides interface to enter and save new client information.
- [Manage Clients Page](clientInfo.html) - Displayed only to logged in users. Displays the organization name of all saved client information entries and allows uers to view the complete entries, delete them, and access the edit page. 
- [Edit Client Page](editClient.html) - Displayed only to logged in users. Allows users to modify every line of the selected client information entry and either save or discard the changes.
- [New Invoice Page](invoice.html) - Displayed only to logged in users. Allows users to create an invoice by using the dropdown menus and textfields that are part of the form and converting the completed form into ready-to-share pdf document at the end.
- [Profile Page](profile.html) - Displayed only to logged in users. Provides quick explanations of and direct links to the different functionalities of the application.
- [Events Page in English](events.html) and [Events Page in Spanish](events_es.html) - Provides information about the different volunteer roles available during the Fire and Earthquake Safety Expo at a glance followed by a **sign-up form**.
- [Gallery Page in English](gllery.html) and [Gallery Page in Spanish](gallery_es.html) - Will display images from the expo after the event with the **option for visitors to enlarge them on cklick**.

### Features to Implement in the Future
- POST request-based functionality for users to submit additional personal information on the profile page, which will then be added to the invoice header via GET request.
- Functionality to add rates to the database the same way it is currently possible to add client information.
- A modal confirming a user's intent to delete a client information entry.
- Forgot password functionality.


## Technologies Used

### Tools
- This project uses Python, HTML, CSS, and JavaScript programming languages.
- [Gitpod](https://gitpod.io) 
    - This project uses **Gitpod** for their IDE.
- [MongoDB](https://www.mongodb.com/)
    - This project uses **MongoDB** for data storage.
- [Heroku](https://heroku.com/)
    - This project uses **Heroku** as a cloud platform to deploy the project.
- [ColorSpace](https://mycolor.space)
    - This project uses **ColorSpace** to determine font colors that go well together.
- [WAVE](https://wave.webaim.org)
    - This project uses the **Web Accessibilty Evaluation Tool** to make sure the website if accessible to visitors of differing abilities. 
- [WebAIM](https://webaim.org/resources/contrastchecker/)
    - This project uses the **WebAIM contrast checker** to make sure the website is accessible to readers with impaired vision.
- [HTML to PDF Rocket](https://www.html2pdfrocket.com/)
    This project uses **HTML to PDF Rocket** to provide an API for HTML to PDF conversion.
    
### Libraries
- [Materialize](https://materializecss.com/)
    - This project uses **Materialize 1.0.0** to simplify the structure of the website and make the website responsive
- [FontAwesome](https://www.bootstrapcdn.com/fontawesome/)
    - This project uses **Font Awesome** for icons on the login, registration, add client, and edit client pages.
- [jQuery](https://jquery.com/)
    - This project uses **jQuery** to reference Javascript needed for the initialization of Materialize.
- [Flask](https://flask.palletsprojects.com/en/2.0.x/)
    - This project uses **Flask** to construct and render the pages.
- [PymMongo](https://pypi.org/project/pymongo/)
    - This project uses **PyMongo** to facilitate communication between Python and MongoDB.
- [Jinja](https://jinja.palletsprojects.com/en/3.0.x/)
    This project uses **Jinja** to facilitate the display of data from the back end.

## Testing 
Testing information can be found in a separate [TESTING.md file](TESTING.md).

## Deployment
This project was developed using the [Gitpod](https://gitpod.io), committed to git, and pushed to GitHub using the Gitpod terminal. 

To deploy this page to GitHub Pages from its [GitHub repository](https://github.com/katjacodes/northern-sonoma-CERT), the following process was completed: 
1. Log into GitHub. 
2. Klick on the account avatar in the top right corner and select "Your repositories" from the dropdown menu.
3. From the list of repositories, select **northern-sonoma-CERT**.
4. From the menu bar at the top of the page, select **Settings**.
5. In the menu bar on the left side of the screen, select the second menu item from the bottom, "Pages."
6. In the **Source** section, select **Master Branch** from the dropdown menu, then click on **Save**.
7. As a result, the page is refreshed and the website deployed. The **website URL** appears in a blue box above the **Source Section**.

At the moment of submitting this Milestone project the Development Branch and Master Branch are identical. 

### How to Run This Project Locally
To clone this project into Gitpod you will need a Github account, and API Spreadsheets account, and a Gmail account. You can [create a Github account here](https://github.com/), [create an API Spreadsheets account here.](https://www.apispreadsheets.com/), and [create a Gmail account here](https://mail.google.com/).

Then follow these steps:
1. Log into [Gitpod](https://gitpod.com) with your gitpod account.
2. Navigate to the [Project GitHub repository](https://github.com/katjacodes/gbrw)
3. Click the green "Gitpod" button in the top right corner of the respository
4. This will trigger a new gitpod workspace to be created based on the code in GitHub. There, you will be able to work locally.

To work on the project code within a local IDE such as VSCode, Sublime Text, etc.:
1. Navigate to the [Project GitHub repository](https://github.com/katjacodes/gbrw)
2. Click the "Code" download button next to the green "Gitpod" button.
3. In the Clone section, select HTTPs and copy the clone URL for the repository. 
4. Open your local terminal.
5. Change the current working directory to the location where you want the cloned directory to be located.
6. Type ```git clone```, and then paste the URL you copied in Step 4.
7. Press Enter for your local clon to be created.

You will need to create a Google spreadsheet and an API Spreadsheets acount to create your own sign-up form. To do so, follow theses steps:
1. Create a Google spreadsheet whose colum titles exactly match the ```name``` attribute of your form ```<input>``` tags.
2. If you want to create more than one spreadsheet within the same file, you can add additional sheets. Make sure to specify which sheet to link to in the drop-down menu that appears after you create the API url in **API Spreadsheets**.
3. Create an **API Spreadsheets** account or log into yours if you already have one.
4. On the dashboard, click on the **Google Sheets** button, sign in with your Gmail account, and select the spreadsheet you created to hold the form data.
5. Copy the API url for the spreadsheet and paste it into line 104 of the [form validation JavaScript file](form-validation.js), as demonstrated below:

```// submit to the server if the form is valid```\
```if(isFormValid) {```\
    &nbsp;&nbsp;&nbsp;&nbsp;``` var vals = $("#signup").serialize();```\
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```$.ajax({```\
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```url: "[INSERT API URL HERE]]",```  
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```method: "POST",```\
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```data: vals,```\
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```success: function(){```\
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```alert("Form data submitted");```\
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```},```\
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```error: function(){```\
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```alert("There was an error");```\
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```}```\
      ```});```\


## Credits
### Content
- The event flyers in English and Spanish and the English volunteer role titles and descriptions were provided by Geoff Peters. 

### Code
- HTML and JS code for the burger menu was originally taken from [W3 Schools](https://www.w3schools.com/bootstrap4/tryit.asp?filename=trybs_navbar_collapse) and then edited.
- HTML, CSS, and JS code for the sign-up form was originally taken from [JavaScript TUTORIAL](https://www.javascripttutorial.net/javascript-dom/javascript-form-validation/), [Love Spreadsheets](https://lovespreadsheets.medium.com/save-web-html-form-data-to-google-sheets-47e48f7517e6), and [CODEMAHAL](https://www.codemahal.com/video/checkboxes-and-form-validation/)  and substantially edited to fit project needs
- HTML, CSS, and JS code for the image gallery originally taken from [W3 Schools](http://www-db.deis.unibo.it/courses/TW/DOCS/w3schools/howto/howto_css_modal_images.asp.html) and edited to fit project needs.
- HTML, CSS, and JS code for the scroll-to-top button originally taken from [W3 Schools](https://www.w3schools.com/howto/tryit.asp?filename=tryhow_js_scroll_to_top) and edited slightly to fit project needs.

### Acknowledgements
- I got the opportunity to build a website for a real-world project from Geoff Peters.
- My Code Institute mentor, Sebastian Immel provided helpful feedback regarding the behavior when I got stuck with my sign-up form. Thanks to his guidance, I tried coding the form validation adn submission pieces separately, which eventually solved my issue. (See [TESTING.md file](Testing.md) for details.)
- Dominik Habersack helped me located a bug in my form submission code, which prevented the sign-up form from submitting. (See [TESTING.md file](Testing.md) for details.)