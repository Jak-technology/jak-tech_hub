Date: march 1st 2024
Bug report: server error 400 for project form
status: resolved 

* name fields for form imput fields and api serializer did not match
* page contained two forms with one submit button on the second form there by attempting to send only the form with a submit button
* form **action** fields not necessary, i removed them(even one was a get route).
**This is where i had to make a decision, i combined both forms to one which in turn had some repercussions on the styling, sorry frontend(not too bad though)**

author:
emma obinna
