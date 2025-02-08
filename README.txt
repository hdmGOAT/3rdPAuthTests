Repository for Testing the processes / and how effectively different 3rd Party Authentication Providers integrate with Django. 

- Clerk
    - Pros
        - Has a lot of built-in features notably its Authentication based components 
            - E.g signed in /signed out
        - Built in manage users
        - Has built in OAUTH functions
        - Extremely well documented
        - Easy to use middlware, Easy protect routes
    - Neutral
        - App is associated with account for dashboard
        - Extremely abstracted
    - Cons
        - Not connected and not able to connect to ur own database for users
        - Data interaction is reliant or prebuilt clerk hooks, auth() etc

- NextAuth.js

- Lucia-Auth
