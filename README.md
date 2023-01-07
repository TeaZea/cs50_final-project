# TODO LIST WEB APPLICATION

#### Description:

Hello, my name is Stefano from Toronto, Canada. For me final project for CS50, I've decided to create a a simple to-do list application.

I decided to do a to-do app because I think it does a good job of combining all full stack skills of backend and frontend. It uses Python and SQL on the backend with simple HTML and CSS with Bootstrap for the frontend. It takes the name of the person and their task and places it in a table. There's also a delete button to remove items from the table. Unfortunatly, because of the lack of experience in setting up databases locally (as it's complicated and expensive) as well as my lack of knowledge of using cloud services to set up a database, I resorted to using the database from the 'birthdays' project and just created my own table within that database. I know it's not best practice but I plan on recreating this project again once I learn how to set up a database myself.

I decided at the last minute to add a fun little counter to the top of the page to see how many tasks you completed in a single session just to keep track of how productive you are. This is done with a simple JavaScript counter script and will refresh once the application is closed unfortunatly. This can be improved on by ensureing that the counter is also on it's own independent table and is called upon when a button is clicked and will persistantly show on the page.

The project contains just the basic files for frontend languages including Bootstrap CDN link. The style is similar to past projects as I decided to use Boostrap as I'm a bit tight on time. I've also used Boostrap for my own personal portfolio website so it was second nature to me.

---

#### Challenges

The delete button was the most dificult thing to impliment. I had a hard time finding what I was supposed to be passing through the request.form.get() function. Once I figured that out, it all clicked rather easily and I was able to impliment the delete button to kill a row of items on the page.

---

#### The Future of this Project

The second iteration of this project I'm planning for my portfolio will involve using React and Node.js to create an SPA of this list. However, it will only manipulate the DOM and not send any queries to a database as I'm seeking to better understand components and props better with this iteration.

The third iteration will build more so on the second and use (as of right now) Google's Firebase platform as a database as well as making sure that the counter is also included in the table. I am nervous of using Firebase as it involves manually converting the data from the form into JSON before it is sent to the database on Firebase.

---
