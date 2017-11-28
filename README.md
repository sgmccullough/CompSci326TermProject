# // TODO: Team Name
Nugget

# Team Overview
Arwa Farrag (arwaGypt), Scott McCullough (mcculloughsco), Pinak Kapoor (pinakkapoor), Malachai Purgahn (mpurgahn), Emily Goroza (egoroza), Sangmin Yun (joeyun)

# Sources/Frameworks Used:
~ Materialize CSS (materializecss.com)
~ CSS Creatures (bennettfeely.com/csscreatures)
~ FreePik (freepik.com)
~ Django


# Innovative Idea
Nugget is a virtual pet website in which individual users can login, create and customize their own pet, and interact with others. Users of Nugget have the ability to create their own ‘Nugget’ and customize them to their hearts content. They can access the Store and purchase items to customize their Nugget, and interact with other users through the Chat feature. The site largely functions as an interactive social network of these Nuggets.
Nugget takes inspiration from 2000s based pet websites such as Neopets, Webkinz or Club Penguin in that users login and interact with each other. Where our application differs is that it focuses less on the ‘game’ part of these sites and focuses on the customization/social aspect. Granted, our site still features a ‘battle arena’ in which users compete and wager their Coins.

# Implementation Updates (Project 2)
Our application is a virtual pet site in which users can create a Nugget and interact with other Nuggets through battles. Two aspects of our project that have changed slightly comes down to battles and chat features. The issues we foresee with these two aspects of our project is dynamic updating of a given user’s view. For example, implementing chat so that when one user posts a message, the receiver sees the message without refreshing the page might be difficult to implement. These are things that might be implemented in the final submission, but might not due to complexity.

# Implementation Updates (Project 3)
Our application now supports user signup and login and dynamic data display by session. Much of the functionality of our application is broken due to forms not working properly, but we aim to have that completed by the due date of the project. The login/logout largely is based around the default Django authentication system. Where things were a little tricky was with our index page and our User model. The index page contains both the login and signup form, so configuring those two forms to work simultaneously was a challenge, but works. Secondly, we had created a User model that contains data that extends and exists separately from Django’s User. We made Django’s user push data into our User (now named Profile) and everything works fine. We aim to on top of finishing the forms, implement some form of chat functionality through an API. 

# Important Data
Since our application functions as a sort of social network, the amount of data our application deals with is as limitless as we want. However, the main data that our application uses is the following:
1. Firstly, user data (email, username, password, name, etc) will be stored to differentiate every user and ensure account security.
2. Besides user login/personal information, Nugget customization is probably the most important data that we store. The current configuration of a user’s Nugget, as well as the contents of their inventory is important since our entire website functions around these Nuggets.
3. Birthday (not birthdate) of each user to give them some sort of event/reward for logging in on their birthday. For example, if you log in on your birthday, you may get a special hat to customize your Nugget with.
4. The number of Coins a user has. Coins form the backbone of the economy of Nugget, and users gain and lose Coins through various activities such as purchasing items from the Store to customize their Nugget. Maintaining a record of their Coin balance and also a certain amount of previous balances will allow for the maintenance of said economy.
5. Chat history is another form of data that we store so that users can see what they have said to other players if they so want to. We might also maintain a record of what users say should any issues arise about the content of said messages.

# User Interface
1. (index.html) First is the landing page. This is the page people see when they first get to our webiste and aren’t logged in. This is different from the login page in that it gives users information about what the website is without needing to login or sign up.
2. (create-a-nugget.html) This page is the first page that users see after they sign up. Users will be redirected to this page until they create their nugget, and then are placed into the actual content of Nugget. This page will allow user to customize their Nugget, and change features about them such as the look, some of their attributes, and set up their Nugget to then interact with other users.
3. (home.html) This is the page that users see when they log in (after they have created their Nugget). This is essentially the main dashboard of the site, sort of like a user’s main feed on Facebook. From here, users can see quick information about their Nugget, as well as news about what is happening around the site (for example, there might be a special event for Halloween that will be advertised here). Most likely more information will be added to this page as development continues.
4. (nugget.html) The My Nugget page is where users can interact with their Nugget, and find out information about their Nugget, and use items to either customize the look of their Nugget or alter their Nugget’s stats.
5. (shop.html) The Shop is the place where users can purchase items using their accumulated Coins. From here they can buy items like hats that will be added to their inventory to customize their Nugget. Users can also buy items that may boost certain stats to give them an advantage in battle.
6. (chat.html) This is simply a page where users can chat with other users and interact with each other. Functionality may be added so that users can directly battle each other, or perhaps trade items with each other. Communities can be created so that users can interact with others about similar interests or topics.
7. (battle.html) Finally, the Battle page is the page where users use their Nugget for battle. The battle system will be relatively simplistic as to avoid making it feel too much like a game.

# Team Notes
1. Please use css/style.css for custom CSS.
2. Please use js/custom.js for custom JS.
