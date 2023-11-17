# Router Config Retrieval (RCR) Script

## Version: 1.0
**Release Date:** 2023-11-16

This Python script, named Router Config Retrieval (RCR), establishes Telnet sessions to multiple routers, executes commands specified in the 'commands.cfg' file, and saves the output in Markdown format. It also generates a 'toc.yml' file to create a table of contents.

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

- router_name: A user-defined name for the router.
- router_ip: The IP address of the router.
- router_port: The TCP port number for the Telnet connection.

## Example:

```plaintext
R1,192.168.1.1,23
R2,192.168.1.2,23
