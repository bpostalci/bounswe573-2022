Before running up the system you need to ensure your system has the Docker tool. You can install Docker to your system by following instructions on the link: https://docs.docker.com/engine/install/ 

After installing Docker to your system you must add the “edume.env” file that contains environment variables to run the system to the “backend/edume/” path of the project. You need to define following environment variables:

DJANGO_SECRET

DB_NAME

DB_USER

DB_PASS

DB_HOST

DB_PORT

EDUME_DOMAIN

After creating the “edume.env” file. You need to run following commands in “backend” path of the project to run the system:

`docker build -t edume .`

`docker run -p 8000:8000 -dit edume`


Then you can reach the running system by visiting ‘localhost:8000’ in your preferred browser. 
