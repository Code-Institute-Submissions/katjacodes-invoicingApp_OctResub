# Invoicing Application – Testing details

[Main README.md file](README.md)

[View website on Heroku](https://katjas-invoicing-app.herokuapp.com/)

## Testing
- [W3C CSS Validation](https://jigsaw.w3.org/css-validator/)
- [W3C Markup Validation](https://validator.w3.org/)
- [JSHint](https://jshint.com/)
- [PEP8](http://pep8online.com/)
The developer used **W3C CSS Validation Service**, **W3C  Markup Validation Service**, **JSHint**, and **PEP8 online** to check the validity of HTML and CSS code.

### Client stories testing:
Due to the very specific nature of the application, there are two kinds of users for this application: existing ones and new ones. Seamless access for both groups was tested during the testing process.

#### Testing client stories from UX section of README.md
1. As a new user of the application, I want to be able to easily register and start using the applilication.
    1. The Login page appears upon navigating to the URL of the application, with the link to the registration displayed both at the bottom of the page and in the navbar.
    2. Registration information is validated upon entry.
    3. Upon successful registration, the new user is directed to the profile page with information about the application functinality and where to find it.

2. As an existing user of the application, I want to be able to manage my client information and easily create ready-to-share invoices
    1. The Login page appears upon navigating to the URL of the application.
    2. Login information is validated upon entry.
    3. Upon successful registration, the new user is directed to the profile page with information about the application functinality and where to find it.
    4. In addition to the explanation on the profile page, all functionality is accessible through the navbar through appropriately labelled items.


### Manual (logical) testing of all elements and functionality on every page.

#### Login Page
1. Navigage to the "Login" page from a desktop computer.
2. Using both Firefox Developer Tools and different devices: Look at the login on a desktop screen, a tablet screen, and a phone screen to verify that the navigation bar turns into a burger menu when navigating to the login on a tablet or a phone screen.
3. Click on the logo in the navigation bar and verify that it links back to the Login page.
4. Verify that only the Registration and Login items are visible in the navbar to users who are not logged in.
5. Click on each navbar item and the registration link at the bottom of the screen and verify that it links to the correct page.
6. Repeat steps 4 and 5 on phone and a tablet.
7. Log in with an existing user account and test if the form rejects a non-existing username and a wrong password.

#### Registration Page
1. Navigage to the "Registration" page from a desktop computer by using either the link at the bottom of the login page or the navbar item.
2. Using both Firefox Developer Tools and different devices: Look at the registration on a desktop screen, a tablet screen, and a phone screen to verify that the navigation bar turns into a burger menu when navigating to the registration on a tablet or a phone screen.
3. Click on the logo in the navigation bar and verify that it links back to the Login page.
4. Verify that only the Registration and Login items are visible in the navbar to users who are not logged in.
5. Click on each navbar item and the login link at the bottom of the screen and verify that it links to the correct page.
6. Repeat steps 4 and 5 on phone and a tablet.
7. Register a new user account and test if the form rejects invaldi input.

#### Add Client Page
1. Enter new client information and test if the form provides an error message in response to trying to submit the an incomplete form.
2. Submit the form.

#### Manage Clients Page
1. Click the **Delete** button to test if the selected entry was deleted.
2. Click the **Edit** button to test if the user is directed to the edit client information page.






2. Jumbotron
   1. Click on link to Contact page to verify it links to the Contact page.
   2. Click on the  Spotify logo to verify it links to the musical's Spotify page.

### About page
1. Navigation bar:
   1. Repeat verification steps for the navigation bar on the home page.

2.  Page content
    1. Reduce and expand width of window to verify that the text behaves the way expected
    2. Using both Firefox Developer Tools and different devices: Look at the About on a desktop screen, a tablet screen, and a phone screen (both in portrait and landscape orientation) to verify that
       - The text arrangement looks good on all device widths.
       - The margins adjust depending on the device width for optimal use of space.
    3. Click on the link to the musical's Spotify profile embedded in the text to verify it links to the correct page.

### Cast + team page & individual profile pages
1. Navigation bar
   1. Repeat verification steps for the navigation bar on the home page.

2. Page content
   1. Click on each profile image to verify it links to the correct profile.
   2. Using both Firefox Developer Tools and different devices: Look at the About on a desktop screen, a tablet screen, and a phone screen (both in portrait and landscape orientation) to verify that the images rearrange with increasing/decreasing screen width. _During testing, the imgages did not rearrange. Researching the reason for this, I found out that all of them need to be wrapped into on single row to be fully responsive._

3. Individual profile pages
   1. Navigation bar:
      1. Repeat verification steps for the navigation bar on the home page.

   2. Using both Firefox Developer Tools and different devices: Look at the About on a desktop screen, a tablet screen, and a phone screen (both in portrait and landscape orientation) to verify that
      - The text arrangement looks good on all device widths.
      -  The size of the profile image increase on tables and desktop screens.
      -  The styling of the quotes changes with increasing/decreasing screen width.

### Contact page
1. Navigation bar:
   1. Repeat verification steps for the navigation bar on the home page.

2. Page content
   1. Click on the  Facebook and Instagram logos to verify it links to the musical's social media presences. 
   2. Using both Firefox Developer Tools and different devices: Look at the About on a desktop screen, a tablet screen, and a phone screen (both in portrait and landscape orientation) to verify that
      - The text arrangement looks good on all device widths.
      - The margins and width text input fields adjust depending on the device width for optimal use of space.
   3. NOTE: The form is not functional while the website it deployed on GitHub. It will be once the client deploys it using Squarespace hosting.

###  Footer 
1. Using both Firefox Developer Tools and different devices: Look at the About on a desktop screen, a tablet screen, and a phone screen (both in portrait and landscape orientation) to verify that the footer is sticky on all pages and across devices. 
2. Click on the Letters and Bytes link to verify it leads to the developer's website  on all pages.

## Further testing: 
1. Asked friends, family members, and other Code Institute students to look at the site on their devices and report any issues they find. 