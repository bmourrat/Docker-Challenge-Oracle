Instructions on how to build then run the container:

In the Docker terminal:
- Change directories into the 'Docker Challenge Oracle' directory

- Build the app:
	
	$ docker build -t server .

	Do not forget the '.' at the end of the command line

- Run the app:
	
	$ docker run -p 192.168.99.100:80:80 server
	
	The server should now be running : 'Running on http://0.0.0.0:80/ (Press CTRL+C to quit)' 
	The '-p 192.168.99.100:80:80' option is to tell Docker to link the port 80 of our container to the port 192.168.99.100:80 of the machine
	We use 192.168.99.100 because Docker is configured to use it.

- To call the server, in the browser of your choice:

	http://192.168.99.100:80/fibonacci/<number> will return the fibonacci sequence and the sorted sequence of <number> terms.

- To close the container properly, in the Docker terminal:
	
	CTRL + C
	
	$ docker container ls : display all the active containers. Copy the ID of the server container
	
	$ docker container stop <ID>
	
	





