# JAK TECH HUB
--------------

Jak tech hub on face value is the the website of Jak Technologies, but in reality, it's the hub that will manange the soul of Jak technologies business activities and it's human resources.

### Features of the Jak Tech hub
--------------------------------
Jack tech hub will have the following features and more...


### The Console
---------------

We have integrated a command-line tool as a means of interacting with our applications models via the commandline using specific commands. 
This is serves a quick way tomake simple changes like create, view, delete, etc


- To run the command-line tool, type ```python console.py``` on your terminal, ensure you're in the same directory as the manage.py file

### Available Commands
----------------------

**Below are the different commands you can run on the tool and their details**

|**Command**    |       **Description**                                |
|---------------|-------------------------------------------------------|
|**quit or EOF**| Exits the program                                    |
|**help**       | Provides description of how to use a command         |
|**create**     | Creates a new instance of the ```Class``` and saves it in the database ```Usage: create <app_name> <class_name> <field_value_1> <field_value_2> ...``` e.g. *create users Skills 13 Data-Science* The instance ID follows after class|
|**show**       | Prints the string representation of an instance based on the class name and ```id``` ```Usage: show <app_name> <class_name> <object_id>``` e.g. *show blog BlogPost 1*|
|**destroy**    | Deletes an instance based on the class name and id ```Usage: destroy <app_name> <class_name> <object_id>``` e.g. *destroy users Specialization 1*|
|**all**        | Prints all string representation of all instances based on the class name & retrieves the number of instances of that class. ```Usage: all <app_name> <class_name>``` e.g. *all project_creation ProjectComment*|
|**update** (Yet to be implemented)     | Updates an instance based on the class name and ```id``` by adding or updating attribute (saves the changes into a JSON file).|

### Alternative commands for the console
---------------------------------------
We also implemented the default method in the console to allow developers user alternative commands for almost all exiting commands. Here are the list of alternative commands:

- To retrieve all instances of a class

```Usage: <app name>.<class name>.all()```

- To retrieve the number of instances of a class

```Usage: <app name>.<class name>.count()```

- To retrieve an instance based on its 

```Usage: <app name>.<class name>.show(<id>)```

- To create an instance 

```Usage: <app name>.<class name>.create(<field_id> <field_value>)```

- To destroy an instance based on its ID

```Usage: <app name>.<class name>.destroy(<id>)```

- To update an instance based on its ID #Not implemented 

```Usage: <app name>.<class name>.update(<id>, <attr name>, <attr value>)```

- To update an instance based on its ID with a dictionary #Not implemented yet

```Usage: <app name>.<class name>.update(<id>, <dictionary representation>)```




###### User Authentication and Authorization:
- Implement a secure user authentication system.
- Include roles and permissions for different user types (admin, regular user, etc.). All of us the pioneers can be admin/superusers while future employees will be regular users.

###### User Profile Management:
- Allow users to create and update their profiles.
- Include features such as profile pictures, personal information (bio), and preferences.

###### Content Creation and Management:
- Enable users to create, edit, and delete content (e.g., posts, articles, images).
- Implement rich text editing and media upload functionalities. Content creation in this regard may be a project idea you may wish the company to consider undertaking. So this will be where you create it, and when you do, we will all get notifications (email and in-app). The rest of us should also be able to comment on the post through different means.

###### Search Functionality:
- Integrate a search feature to allow users to find content or other users.
- Implement filters and sorting options for search results.

###### Notifications:
- Include a notification system to alert users of relevant activities (e.g., new messages, likes, mentions).

###### Admin Dashboard:
- Create a separate dashboard for administrators to manage users, content, and other platform aspects.
- Implement analytics and reporting features. 
- Develop an analytics dashboard to track user activity, popular content, and other key metrics.

###### Responsive Design: (Frontend guys)
- Ensure the project is mobile-friendly and works well on different screen sizes.

###### Security Measures:
- Implement best practices for web security, such as input validation, encryption, and protection against common web vulnerabilities (e.g., Cross-Site Scripting, Cross-Site Request Forgery).

###### Documentation:
- Create thorough documentation for code and usage to facilitate collaboration and future development. So this will be developers and other users

###### Internationalization and Localization:
- If applicable, consider making the platform accessible in multiple languages.

###### Accessibility:
- Ensure that the project is accessible to users with disabilities by following web accessibility standards (e.g., WCAG).

###### Gamification Elements:
- Add gamification elements to encourage user engagement (e.g., badges, points, leaderboards). We will determine activities that can earn you a badge later

###### Feedback Mechanism:
- Include a way for users to provide feedback or report issues.
- Consider implementing a feedback form or a community forum.

###### Testing:
- Develop a suite of automated tests to ensure the reliability and stability of the platform.
- Consider both unit tests and end-to-end tests.

###### Continuous Integration/Continuous Deployment (CI/CD):
- Implement a CI/CD pipeline to automate the testing and deployment process.
This is where we invoke the DevOps in us

###### Scalability Considerations:
- Design the system with scalability in mind. Consider how the platform would handle a growing user base and increased data.
- Since this is our playground and there's no way we can implement all of these features plus more that will be suggested at once, designing with scalability in mind is something that we will give a thorough consideration. This will enable us to integrate any new feature with ease.

###### Integration with External Services:
- Integrate with third-party APIs or services (e.g., social media login, payment gateways, mapping services, or as the case may be) to simulate real-world scenarios.

*NOTE*
---- 
``` We will rewrite this README to describe the project and how to use later. For now, this is just let us know a bit of what we want to achieve```
