# Invoicing Application – Testing details

[Main README.md file](README.md)

[View website on Heroku](https://katjas-invoicing-app.herokuapp.com/)

## Testing
- [W3C CSS Validation](https://jigsaw.w3.org/css-validator/)
- [W3C Markup Validation](https://validator.w3.org/)
    - The developer used **W3C CSS Validation Service** and **W3C  Markup Validation Service** to check the validity of HTML and CSS code.

### Client stories testing:
Due to the very specific nature of the application, there are two kinds of users for this application: existing ones and new ones. Seamless access for both groups was tested during the testing process.

## Testing client stories from UX section of README.md
1. As a new visitor to the website, I want to have easy access to the music, so I can get a taste of the musical.
   1. A link in the shape of an easily recognizable Spotify logo on the homepage leads the visitor directly to the musical's Spotify presence.
   2. The logo at the top of each page lead the visitor back to homepage.
3. For those who become curious about the music after learning some more about the musical, there is a link to the musical's Spotify page embedded in the copy on the About page
    
2. As a new visitor to the website, I want find reader-friendly, well-organized information about the musical's content, background, and those involved in it.
   1. The navigation bar is structured based on the topics of most of interest to new visitors, moving from more general to more specific.
   2. While visiting the Cast + Team page, the visitor can determine about which individuals they would like to learn more by clicking on the profile picture or the name.
   3. The Cast + Team navigation bar button leads the visitor from the individual profile pages directly back to the overview page.
   4. The About page contains information about both the background and the content of the musical without being overwhelming.

3. As a new visitor to the website, I want to find out where I can find more information about the musical, especially on social media platforms I already use.
   1. Visitors can get to the Contact by selecting it in the navigation bar 
   2. Additionally, there is a direct link form the homepage to the Contact page
   3. On top of the Contact page, visitors find easily recongizable links to the musical's Facebook and Instagram presence
   4. Additionally, visitors have the option to either subscribe to the newsletter or send a message directly to the musical team

4. As someone already familiar with the musical, I want to have a way to stay updated about recent developments related to the musical, including its new premier date.
   1. Visitors already familiar with the musical, can use the direct link to the Contact page provided on the homepage to sign up for the newsletter.

5. As someone already familiar with the musical, I want to have a way to stay updated about recent developments related to the musical, including its new premier date.
   1. The navigation bar item "Sponsors" leads to a full ist of local businesses and organizations supporting the musical financially.
   (2. On request of the client, no direct links to the sponsors websites were included.)

6. As a journalist focusing on local news and/or LGBTQIA issues, I want to be have access to background information about the musical and ways of contacting those involved.
   1. The About page provides a summary of both the musical's background and content and links to its musicals for interested journalists to get a first impression of the musical.
   2. To let journalists know to whom to address their message on the contact page, the copy on the About page includes the name of the writer, composer, and producer of the musical.

### Manual (logical) testing of all elements and functionality on every page.

#### Home Page
1. Navigation bar & homepage background image
   1. Go to the "Home" page from a desktop.
   2. Using both Firefox Developer Tools and different devices: Look at the homepage on a desktop screen, a tablet screen, and a phone screen (both in portrait and landscape orientation) to verify that
      - The navigation bar turns into a burger menu when navigating to the homepage on a phone screen.
      - The background image gets resized and cropped in a way that its content remains recognizable and aesthetically pleasing.
   3. Make sure the burger menu pushes down the content when opened. _During testing, the menu would initially overlay the remaining website content. This turned out to be due to a typo in the linked script._
   4. Click on the logo in the navigation bar and verify that it links to the homepage. 
   5. Click on each navigation menu item and verify that it links to the correct page.
   6. Repeat steps 4 and 5 on phone and a tablet.

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