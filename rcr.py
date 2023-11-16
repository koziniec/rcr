"""
Router Config Retrieval (RCR) Script

Version: 1.0
Release Date: 2023-11-16

This Python script, named Router Config Retrieval (RCR), establishes Telnet sessions to multiple routers, 
executes commands specified in the 'commands.cfg' file, and saves the output in Markdown format. 
It also generates a 'toc.yml' file to create a table of contents.

Authors:
- OpenAI (https://www.openai.com/)
- Terry Koziniec, School of Information Technology, Murdoch University

GitHub Repository:
- Repository URL: https://github.com/koziniec/rcr
- Please refer to the repository for the latest updates and contributions.

License:
This script is provided under the MIT License.
You are free to use, modify, and distribute this script, as long as you provide appropriate attribution to the authors.

"""

import telnetlib
import time
import os

def telnet_session(router_info, commands_file):
    router_name, router_ip, router_port = router_info

    # Create a "_docs" folder if it doesn't exist
    os.makedirs("_docs", exist_ok=True)

    # Create or append to toc.yml in the current directory
    toc_filepath = "toc.yml"
    with open(toc_filepath, 'a') as toc_file:
        # Write router entry
        toc_file.write(f"    - title: \"{router_name}\"\n")
        toc_file.write(f"      url: \"docs/{router_name}\"\n")
        toc_file.write("      children:\n")

    # Create a folder for the router inside "_docs"
    router_folder = os.path.join("_docs", router_name)
    os.makedirs(router_folder, exist_ok=True)

    # Connect to the router
    try:
        tn = telnetlib.Telnet(router_ip, router_port, timeout=5)
    except Exception as e:
        print(f"Failed to connect to {router_ip}:{router_port}. Error: {e}")
        return

    # Wait for the router prompt
    tn.read_until(b">", timeout=5)

    # Send a carriage return
    tn.write(b"\r\n")
    time.sleep(1)

    # Send the enable command
    tn.write(b"enable\n")
    time.sleep(1)

    # Set the terminal length to 0
    tn.write(b"terminal length 0\n")
    time.sleep(1)

    # Clear the buffer as we don't want to log the setup commands
    dummy = tn.read_very_eager()

    # Read commands from the file and execute them
    with open(commands_file, 'r') as file:
        commands = file.readlines()

    for command in commands:
        command = command.strip()  # Remove leading/trailing whitespaces
        tn.write(b"\n")  # CR to display command prompt
        time.sleep(1)
        tn.write(command.encode('ascii') + b"\n")
        time.sleep(2)  # Adjust sleep time if needed

        # Read and save the Telnet response to a file
        telnet_output = tn.read_very_eager().decode('ascii')
        output_filename = command.replace(' ', '-').replace('/', '-').replace('\\', '-')
        output_filepath = os.path.join(router_folder, f"{output_filename}.md")

        # Write the output in Markdown format
        with open(output_filepath, 'w') as output_file:
            output_file.write("---\n")
            output_file.write(f"title: {router_name}\n")
            output_file.write("tags:\n")
            output_file.write(f"description: {command}\n")
            output_file.write("---\n\n")
            output_file.write(f"# {command}\n\n")
            output_file.write("<pre><code>\n")
            output_file.write(f"{telnet_output}\n")
            output_file.write("</code></pre>\n")

        # Append toc.yml entry for the command
        with open(toc_filepath, 'a') as toc_file:
            toc_file.write(f"        - title: \"{command}\"\n")
            toc_file.write(f"          url: \"docs/{router_name}/{output_filename}\"\n")

    # Add a blank line in toc.yml
    with open(toc_filepath, 'a') as toc_file:
        toc_file.write("\n")

    # Close the Telnet session
    tn.close()

if __name__ == "__main__":
    routers_file = "routers.cfg"  # File containing router information
    commands_file = "commands.cfg"  # File containing commands

    # Initialize toc.yml in the current directory
    toc_filepath = "toc.yml"
    with open(toc_filepath, 'w') as toc_file:
        toc_file.write("- title: Documentation\n")
        toc_file.write("  url: docs\n")
        toc_file.write("  links:\n")

    with open(routers_file, 'r') as file:
        routers = [line.strip().split(',') for line in file]

    for router_info in routers:
        telnet_session(router_info, commands_file)
