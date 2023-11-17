# Router Config Retrieval (RCR) Script

## Version: 1.0
**Release Date:** 2023-11-16

This Python script, named Router Config Retrieval (RCR), establishes Telnet sessions to multiple routers, executes commands specified in the 'commands.cfg' file, and saves the output in Markdown format. It also generates a 'toc.yml' file to create a table of contents.
I intend this script to be used with an EVE-NG lab for extracting device information in an automated way.  You could use it with physical devices, but I have not included support for Telnet authentication.  It is trivial to add this, but in a production environment rcr is a really poor starting point for so many reasons. Please use this for lab and simulation support only.

## Authors:
- [OpenAI](https://www.openai.com/)
- Terry Koziniec, School of Information Technology, Murdoch University

## GitHub Repository:
- **Repository URL:** [https://github.com/koziniec/rcr](https://github.com/koziniec/rcr)
- Please refer to the repository for the latest updates and contributions.

## License:
This script is provided under the [MIT License](https://opensource.org/licenses/MIT). You are free to use, modify, and distribute this script, as long as you provide appropriate attribution to the authors.

---

## `routers.cfg` File

The `routers.cfg` file is used to specify information about routers. It follows a comma-separated values (CSV) format, where each line represents a router entry with the following structure:

```plaintext
router_name,router_ip,router_port
```
- router_name: A user-defined name for the router.
- router_ip: The IP address of the router.
- router_port: The TCP port number for the Telnet connection.

## Example:

```plaintext
R1,192.168.1.1,32769
R2,192.168.1.1,32770
```

## `commands.cfg` File
The commands.cfg file contains a list of commands to be executed on each router. Each line in the file represents a command to be executed, following this format:

```plaintext
command_1
command_2
command_3
```
- One IOS command per line

## Example:

```plaintext
show ip interface brief
show ip ospf neighbors
```

## Running crc

- Make sure you have a valid (`commands.cfg`) and (`routers.cfg`) in your current directory
  
```plaintext
python crc.py
```
- crc will create a directory (`_docs`) with a subdirectory for each device in the (`routers.cfg`) file.  Within each router directory a seperate markdown encoded file will be created with the output of each command specified in the (`commands.cfg`) file.
- crc will create a toc.yml (Table of Contentes in YAML) file in the current directory describing the location of each file. I use this to form an indexed list for use with gitpages.


## Important Notes:

- Ensure there are no leading or trailing whitespaces in the entries.
- Commands in the commands.cfg file should be valid commands for the routers.

When using these files with the provided Python script, make sure the file paths in the script match the actual file locations on your system. The script assumes that the files are in the same directory.

