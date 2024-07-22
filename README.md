# Send data from Back-end to Front-end in django using Jinja tags

--Explanation of this project
1. Data Preparation in Views:
 * Django views ( views.py) handle incoming requests, process data, and generate the context dictionary.
 * This context dictionary holds the data you want to send to the template.
   
2. Passing Context to Templates:
 * In your view function use the render function from django shortcuts to return an HTTP response with the template and context.

3. Accessing Data in Templates:
 * Using Jinja template tags provide access to the data you passed in the context dictionary.
 * You can use double curly braces {{ }} to display variables.
