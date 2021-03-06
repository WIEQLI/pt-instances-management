# Packet Tracer instance management

Web application which handles local PacketTracer instances using Docker.


Prerequisites
------------

This application currently uses [psutil](https://pythonhosted.org/psutil/).
As a side effect, you need to consider its [installation requirements](https://github.com/giampaolo/psutil/blob/master/INSTALL.rst) (which change from one system to another).


Installation
------------

Why would you want to install it?

    pip install git+https://github.com/PTAnywhere/pt-instances-management.git


Requirements
------------

The required packages are automatically installed in the procedure described above.

However, if you are going to contribute to this project, you might want to install __only__ the project's dependencies in your [virtualenv](http://virtualenv.readthedocs.org).

You can install them using the _requirements.txt_ file in the following way:

    pip install -r requirements.txt

Usage
-----

Before running the web application for the first time, follow these steps:

1. Customize _config.ini_ if needed.

1. Create the database and populate it with the available ports. Generally you should __only do this once__.
   
    ```cd src/ptinstancemanager; python run.py -createdb```


Then, simply __run the web server__:

    cd src/ptinstancemanager; python run.py

The API will be then available in the [port 5000](http://localhost:5000).
If you go to the root of the application, you will be automatically redirected to a [user friendly description](http://swagger.io) of the API.

Advanced usage
--------------
For a production ready installation using which uses Nginx, Gunicorn and Supervisor, check [this project](https://github.com/PTAnywhere/ptAnywhere-installation).

Acknowledgements
----------------

This API is being developed as part of the [FORGE project](http://ict-forge.eu/).
