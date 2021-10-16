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
In addition, the **dropdown menu** at the bottom lets the user select the rate tier of the organization: Institution, Small Non-Profit, Large Non-Profit. All fields are required. Upon completing the form, the user will click on the **Submit button** to add the new client to the database.

#### Manage Clients Page
The manage client page contains a list of all client entries. 




#### Home
The landing page features the offical CERT logo as the **hero image**. The percentage of the screen the hero image covers increases for screens 768px and above in potrait mode and decreases for screens 768px and above in landscape mode to make the page visually appealing and the content below the hero image easy to locate. Below the hero image, visitors can find direct links to **the event flyer** in pdf format and the volunteer sign-up form. Depending on the language in which the visitor is accesing the landing page, they will be directed to the flyer and the sign-up form in either English or Spanish. In the future, the links to the current event-related information will be replaced with more general information about the program and updated links to event information. Due to the evolving business needs of the client, the homepage is designed in a way that its content can easily be updated and adapted. 

#### Events

**NOTE I:** _The API urls and Google Sheets file used in this code are for testing purposes only. The Google Sheets file can be accessed here as part of project review: [Google spreadsheet for form data](https://docs.google.com/spreadsheets/d/1Va0UQl8pYm_fklu2lM1uxFyFnnlQG6ktYPXwd_D1SuM/edit?usp=sharing)_

**NOTE II:** _The real-life website will use a paid API Spreadsheets account, which includes the option to make the API url private to avoid spamming and other forms of unwanted use._

Currently, the events pages features **information about volunteer roles** at the upcoming Fire and Earthquake Safety Expo and **sign-up form** that transmits the information directly to a Google spreadsheet using the _API Spreadsheets_ API. The form is optimized to usable on mobile screens and adapts to tablet and computer screens (768px and above). Depending on the language in which the form is displayed to the user, the form data will either be submitted to a spreasheet indicating that the user's preferred language is English or to a spreadshet indicating that the user's preferred language is Spanish. This information will help the event organizers plan any follow-up communication.

#### Gallery
The gallery page currently features sample images demonstrating what the gallyery layout will look like once the event pictures get added to it. The standard setting of the **image grid** is one image per row. Above that, the grid features two images per row on screens 768px and above and three images per row on screens 1400px and above. The purpose of this structure is to allow users to clearly see the details of the images at first glance. In addition, the image gallery provides a **JavaScript-supported modal** that enlarge an image to full-screen size on click. After looking at the image, the visitor can return to the gallery by clicking ont the "x" in the upper right corner. Additionally, as soon as the menu bar is no longer visible on the screen, a **scroll-to-the-top button** appears in the lower right corner of the screen. On clicking it, the visitor is taken directly back to the top of the gallery.

### Existing Features
- Language Selection Menu - Exists on [every page](index.html) and allows all users to selct their preferred language on any page. Clicking a language option sends the user to the current page in the selected language and displays the navigatio bar in the selected language.
- Header Navigation Bar - Exists on [every page](index.html) and allows all users to easily navigate all the website's pages and find what they are looking for quickly, including the CERT program's **social media presence on Facebook**.
- Footer Copyright Info - Exists on [every page](index.html) and protects business copyright.
- [Landing Page in English](index.html) and [Landing Page in Spanish](index_es.html) - Allows interested community members to see right away whose page they have landed on and where to find information about the upcoming expo.
- [Events Page in English](events.html) and [Events Page in Spanish](events_es.html) - Provides information about the different volunteer roles available during the Fire and Earthquake Safety Expo at a glance followed by a **sign-up form**.
- [Gallery Page in English](gllery.html) and [Gallery Page in Spanish](gallery_es.html) - Will display images from the expo after the event with the **option for visitors to enlarge them on cklick**.

### Features to Implement in the Future
- Contact form. - Client is currently using his personal email address and will set up business email address to liink the form to in the future.
- Event evaluation form. - Content will be provided by the client after the expo.
- Program description and overview. - Still being developed.


## Technologies Used
- This project uses HTML, CSS, and JavaScript programming languages.
- [Gitpod](https://gitpod.io) 
    - This project uses **Gitpod** for their IDE.
- [BootstrapCDN](https://www.bootstrapcdn.com/)
    - This project uses **Bootstrap4** to simplify the structure of the website and make the website responsive
    - This project also uses BootstrapCDN to provide icons from [FontAwesome](https://www.bootstrapcdn.com/fontawesome/)
- [Google Fonts](https://fonts.google.com/)
    - This project uses **Google fonts** to style the website fonts.
- [jQuery](https://jquery.com/)
    - This project uses **jQuery** to reference Javascript needed for the responsive navbar and sign-up form submission functionality.
- [Popper.js](https://popper.js.org/)
    - This project uses **Popper.js** to reference Javascript needed for the responsive navbar.
- [API Spreadsheets](https://www.apispreadsheets.com)
    - This project uses **API Spreadsheets** to connect the sign-up form to Google spreadsheets via an API.
- [ColorSpace](https://mycolor.space)
    - This project uses **ColorSpace** to determine font colors that go well together.
- [WAVE](https://wave.webaim.org)
    - This project uses the **Web Accessibilty Evaluation Tool** to make sure the website if accessible to visitors of differing abilities. 
- [WebAIM](https://webaim.org/resources/contrastchecker/)
    - This project uses the **WebAIM contrast checker** to make sure the website is accessible to readers with impaired vision.
- [Google PageSpeed Insights](https://developers.google.com/speed/pagespeed/insights/)
    - This project uses **Google PageSpeed Insights** to optimize loading time.

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