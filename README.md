# Migrate from Multilogin to GoLogin

For migration you will need:
- installed application Multilogin;
- the user's app.properties file;
- user token from gologin and multilogin;

Action sequence:
1. install Multilogin if it has not been installed before;
2. in the ~/.multiloginapp.com directory we put the user's app.properties file;
3. in the settings file (app.properties) add the line `multiloginapp.port = port_number` so that multilogin works on a specific port;
4. launch the Multilogin application (in this case, we must immediately get into the user profile without authentication);
5. in the config.py file, assign a value to the variables **MULTILOGIN_TOKEN**, **MULTILOGIN_PORT**, **GOLOGIN_TOKEN**;
6. run the main.py script

 
To copy a specific profile, you must:
1. comment out lines 10-23
2. uncomment lines 25-33
3. in line 27, instead of '**NaMe Of PrOfiLe**', enter the name of the multilogin profile for migration