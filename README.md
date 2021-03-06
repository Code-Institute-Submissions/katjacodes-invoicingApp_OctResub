# Interpreter Invoicing App

<div align="center">
    <img src="static/img/mockup.png" alt="Mockup of how home page looks on diffferent screen sizes"/>
</div>
<br>

[View deployed site here](https://katjas-invoicing-app.herokuapp.com/)

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
- [Registration Page](static/img/wireframes/registration.png)
- [Login Page](static/img/wireframes/login.png)
- [Add Client Page](static/img/wireframes/addClinet.png)
- [All Clients Page](static/img/wireframes/clientInfo.png)
- [Edit Client Page](staticimg/wireframes/editClient.png)
- [New Invoice Page](static/img/wireframes/invoice.png)
- [Profile Page](static/img/wireframes/profile.png)


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
- [Manage Clients Page](clientInfo.html) - Displayed only to logged in users. Displays the organization names of all saved client information entries *in alphabetical order* and allows uers to view the complete entries, delete them, and access the edit page. 
- [Edit Client Page](editClient.html) - Displayed only to logged in users. Allows users to modify every line of the selected client information entry and either save or discard the changes. Automatically displays the current date in standard U.S. format at the top of the page.
- [New Invoice Page](invoice.html) - Displayed only to logged in users. Allows users to create an invoice by using the dropdown menus and textfields that are part of the form and converting the completed form into ready-to-share pdf document at the end.
- [Profile Page](profile.html) - Displayed only to logged in users. Provides quick explanations of and direct links to the different functionalities of the application.

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
- [HTML to PDF Rocket](https://www.html2pdfrocket.com/)
    This project uses **HTML 2 PDF Rocket** to provide an API for HTML to PDF conversion.
    
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
This project was developed using the [Gitpod](https://gitpod.io) deveopment environment, committed to git, and pushed to GitHub using the Gitpod terminal. 

To deploy this page to [Heroku](https://heroku.com/) from its [GitHub repository](https://github.com/katjacodes/invoicingApp), the following process was completed: 
1. Log in to Heroku
2. Click **"]New** and select **Create New App** from the drop-down menu in the upper right half of the window. 
3. Enter a **Name** for your application. The name needs to be unique. Next, select the **Region** closest to your geographical location. When you're finished, click **Create App**.
4. In the navbar at the top of the page, click on **Settings**, scroll down to the **Reveal Config Vars** button, and click it.
5. Enter the following information:
    IP: 0.0.0.0
    MONGODB_NAME: [name of the MongoDB cluster you are using for your application]
    MONGO_URI: [the URI you created after setting up your collection in MongoDB found by logging in to MongoDB > navigating to the cluster that holds the collection you are using for your application > clicking on "Connect" > selecting "Connect your application" > selecting the correct driver & version > copying the generated string & replacing the placeholders in it with your own information]
    PORT: 5000
    SECRET_KEY: [copy from the [env.py](env.py) file
    Click **Add** after entering each variable.
6. Scroll down and click **Buildpacks** and select **Python**, then click **Save changes**.
7. In the navbar at the top of the page, click on **Deploy**, scroll down to **Deployment method**, and select **GitHub**.
8. **Authorize** the connection to GitHub.
9. Search for your **GitHub repository name** and select the repository holding the code for you application.
10. Make sure the **Main Branch** is selected for deployment and select **Enable Automatic Deploys** for Heroku to automatically re-build your application every time you push your code to GitHub.
11. Click the **Deploy Branch** button. Once Heroku has built the application, a pop-up message will confirm deployment
12. You can click the **View** button to be taken directly to the site.

At the moment of submitting this Milestone project the Development Branch and Main Branch are identical. 

### How to Clone the Repository
To clone this project into Gitpod you will need a Github account and an HTML 2 PDF Rocket account. You can [create a Github account here](https://github.com/), and you can [create an HTML 2 PDF Rocket account here.](https://www.html2pdfrocket.com/).

Then follow these steps:
1. Log into [Gitpod](https://gitpod.com) with your gitpod account.
2. Navigate to the [Project GitHub repository](https://github.com/katjacodes/invoicingApp)
3. Click the green "Gitpod" button in the top right corner of the respository
4. This will trigger a new gitpod workspace to be created based on the code in GitHub. There, you will be able to work locally.

To work on the project code within a local IDE such as VSCode, Sublime Text, etc.:
1. Navigate to the [Project GitHub repository](https://github.com/katjacodes/invoicingApp)
2. Click the "Code" download button next to the green "Gitpod" button.
3. In the Clone section, select HTTPs and copy the clone URL for the repository. 
4. Open your local terminal.
5. Change the current working directory to the location where you want the cloned directory to be located.
6. Type ```git clone```, and then paste the URL you copied in Step 4.
7. Press Enter for your local clon to be created.

You will need to create an HTML to PDF Rocket account to obtain an API key for the API that will allow you to create PDF a PDF version of your invoice. To do so, follow these steps.
1. Ater you [create your HTML 2 PDF Rocket account](https://www.html2pdfrocket.com/), you will be sent your API key to the email you registered with. At that time, you can also update your password.
2. Navigate to to the [Code Examples page](https://www.html2pdfrocket.com/Examples/javascript) and copy the HTML and JavaScript code to create a button that will allow you to create PDF documents.
3. Make sure to update the following information in the code:
    - Your API key
    - The URL of the page you want turn into a PDF document, i.e., the URL of your invoice page.


## Credits
### Content
- The background image was created by [Ramiro Menes for Unsplash](https://unsplash.com/photos/sMCBEI5zkqc) and made available under the [Do Whatever You Want License](https://unsplash.com/license).

### Code
- The [Code Institute Walk-Through project](https://github.com/Code-Institute-Solutions/TaskManagerAuth/tree/main/08-SearchingWithinTheDatabase/01-text_index_searching) for Milestone 3 was taken as a starting point for the set-up of the base, addClient, clientInfo, editClient, login, register, and logout templates and edited heavily.
- The [Code Institute Walk-Through project](https://github.com/Code-Institute-Solutions/TaskManagerAuth/tree/main/08-SearchingWithinTheDatabase/01-text_index_searching) for Milestone 3 was taken as a starting point for parts of the [app.py](app.py) file.
- HTML, CSS, and JS code for the scroll-to-top button originally taken from [W3 Schools](https://www.w3schools.com/howto/tryit.asp?filename=tryhow_js_scroll_to_top) and edited slightly to fit project needs.
- The JavaScript code for the automatic date set function on the invoice page was taken from [W3 Schools](https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_tolocaledatestrin) and edited to display the date in U.S. format.
- The JavaScript code for the addition of charges on the invoice page was taken from [Codegrepper](https://www.codegrepper.com/code-examples/javascript/calculate+two+number+and+diplay+next+field+without+reload+the+page+javascript) and edited to fit project needs.
- The HTML and JavaScript code for the integration of the PDF conversion API was taken from [HTML 2 PDF Rocket](https://www.html2pdfrocket.com/Examples/javascript) and edited to fit project needs.
- Joshua Ugba helped me understand how to connect Python and Javascript for the automatic address field population section of the invoice page.


### Acknowledgements
- The Code Institute Slack Community and my session with a tutor was really really helped me out by providing pointers when I got stuck and unable to see the forest for the trees.
- Joshua Ugba took the time to explain to me in depth how to integrate JavaScript and Python. I owe a better understanding of JSON files to him. 