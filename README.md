Linux Server
==================

## Summary
Deploy the web application (CatalogApp) on virtual server in Amazon's elastic compute cloud (EC2)

### Access server
IP: 52.37.70.24
PORT: 2200

ssh -i <path_to_grader_private_key> grader@52.37.70.24 -p 2200

### Access web app
http://ec2-52-37-70-24.us-west-2.compute.amazonaws.com/

### Packages Installed
Here is the list of packages installed on the linux server to host the web app
  * PostgreSQL
  * Apache2
  * Python
  * Flask, SQLAlchemy, SQLAlchemy-Utils
  * Virtualenv
  * GIT

### Extra packages installed
  * sqlalchemy_utils : Provides helpful apis in addition to SQLAlchemy. I have used the database_exists and create_database api's to create postgres sql database if its doesn't exist from the python code
  * unattended-upgrades : Automatically install security updates and get notified for normal updates
  * fail2ban : Improve server security by stopping failed login attempts by users or bots and inform the owner (subgutt@gmail.com)
  * Nagios : Web interface to monitor the server. Configured it to send alerts to the owner (subgutti@gmail.com).
        Access it here : http://ec2-52-37-70-24.us-west-2.compute.amazonaws.com/nagios
        username : nagiosadmin
        password : udacity

### Host Catalog App
In order to host the Catalog App I have made the below configuration changes
  * Added an apache configuration file to host the Catalog app `/etc/apache2/sites-available/CatalogApp.conf`
  * Enabled the Catalog app configuration file using `sudo a2ensite CatalogApp`
  * As Apache uses .wsgi file to server, added a new .wsgi file in CatalogApp
  * Modified CatalogApp to use postgresql database rather than sqlite database

### Resources
  * [Flask](https://www.digitalocean.com/community/tutorials/how-to-deploy-a-flask-application-on-an-ubuntu-vps)
  * [PostgreSQL](http://www.cyberciti.biz/faq/howto-add-postgresql-user-account/)
  * [SQLAlchemy-Utils](http://sqlalchemy-utils.readthedocs.org/en/latest/database_helpers.html)
  * [Automatic Updates](https://help.ubuntu.com/lts/serverguide/automatic-updates.html)
  * [Fail2Ban](https://www.digitalocean.com/community/tutorials/how-to-protect-ssh-with-fail2ban-on-ubuntu-14-04)
  * [Nagios](https://www.digitalocean.com/community/tutorials/how-to-install-nagios-4-and-monitor-your-servers-on-ubuntu-14-04)