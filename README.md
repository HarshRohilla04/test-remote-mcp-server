1)Run the server locally

In terminal run command:
uv run fastmcp run main_local_server.py

-> To test the server, after running the server run the command:
   uv run fastmcp dev main_local_server.py
   It will give a link, open the link -> change the transport type to http -> in configuration, add the token key if not present

2)Run the server remotely using the proxy server

In terminal run command:
fastmcp run main_remote_server.py --transport http --host 0.0.0.0 --port 8000
OR
uv run main_remote_server.py

-> To test the server after running the server run the command:
   uv run fastmcp dev main_remote_server.py 
   It will give a link, open the link -> change the transport type to http -> in configuration, add the token key if not present

To connect to the proxy server, run the command:
uv run fastmcp run local_proxy_server.py

NOTE: this will only run if the server is deployed on cloud. here i used the fastmcp.cloud and deployed there.


3)Connect to CLaude Desktop

In terminal run command:
uv run fastmcp install claude-desktop <file_name.py>(this works both for the proxy server and local server)


NOTE: if claude shows an error saying cannot connect to your server , then in CMD type where uv and copy the path. set this path in the Settings->Developer->edit config file->open in vs code->add the uv path->kill claude from task manager
