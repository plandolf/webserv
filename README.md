# Webserv

## Introduction

Webserv is a custom HTTP server project designed to deepen understanding of network programming, HTTP protocols, and server mechanics. This project mimics the functionalities of an actual web server and can interact with real web browsers.

## Features

- **HTTP Server Implementation**: Handles HTTP requests and serves responses following the HTTP/1.1 standards.
- **CGI Support**: Implements CGI to run external scripts written in Python, C++, and C, enhancing the server's functionality to execute dynamic content.
- **Connection Handling**: Uses `epoll()` for efficient I/O event notification, suitable for high-load environments.
- **Docker Integration**: Includes a Makefile for easy Dockerization of the server environment, ensuring consistency across different setups.
- **Debug Mode**: Features a debug mode for detailed logging of server operations, helping in development and troubleshooting.
- **Full HTTP Compliance**: Supports methods GET, POST, and DELETE, and adheres to HTTP response status codes accurately.
- **Multiple Ports and Virtual Server Configurations**: Capable of listening on multiple ports and handling different virtual server configurations via a single instance.

## Getting Started

## Prerequisites

- Docker installed on your machine (for Dockerization)
- C++ compiler compliant with the C++98 standard (g++, clang++)
- Linux environment (due to the use of `epoll()`)
- **Firefox Web Browser**: Specific configuration steps are necessary for proper interaction with the web server due to its use of proxies and HTTPS settings.

## Browser Configuration

To ensure that Firefox interacts correctly with the web server, especially when proxies are used, follow these configuration steps:

### Configuring Firefox for Proxy Use

1. **Open Firefox** and access the preferences panel.
2. Navigate to **General** and scroll down to **Network Settings**.
3. Click on **Settings...** to configure how Firefox connects to the Internet.
4. Check **Automatic proxy configuration URL**.
5. Set the URL to `http://127.0.0.1:8080/set_proxy/`. This will configure Firefox to use the proxy settings served by the web server at the specified endpoint.

### Configuring HTTPS-Only Mode

1. In the **Network Settings** dialog, scroll to find the **HTTPS-Only Mode**.
2. Check **Enable HTTPS-Only Mode in all windows**.
3. Click on **Manage Exceptions...** to add exceptions for the server's domains.
4. Add the following addresses to the exceptions list:
   - `marvinx.42.fr`
   - `putchar.mc`
   - `ping.js`
   - `pong.js`

These steps ensure that Firefox can securely connect to and interact with the web server while respecting the server's security and proxy configurations. These settings are crucial for the proper functioning of the web server in development and testing environments.

### Installation

1) git clone [repository-url] webserv
2) cd webserv
3) make OR make debug

### Running the Server

Execute the server with a configuration file:

./webserv config_file

If no configuration file is provided, the server will look for a default configuration file in the working directory.
A simple default.conf is provided

## Configuration File Example

The `local.conf` file provided as part of the demo setup illustrates a complex server configuration with multiple virtual hosts listening on the same IP but different ports, handling a wide array of functionalities. Below are the key aspects of this configuration:

### Highlights of `local.conf`

- **Multiple Servers**: Configures several server blocks, each listening on `127.0.0.1` but on common and unique ports, demonstrating the server's ability to handle different domains and subdomains on the same machine.

- **CGI Support**: Specifies paths and extensions for CGI scripts, enabling dynamic content generation through Python and C++ scripts. This is highlighted in sections that allow `.py` and `.cgi` extensions within certain locations.

- **Advanced Request Handling**:
  - Restrictive methods management where certain paths only allow specific HTTP methods like GET, POST, DELETE, HEAD, PUT.
  - Custom error pages are specified for different servers, enhancing user experience when errors occur.
  - File upload capabilities and client body size limitations are demonstrated, important for content management and security.

- **Redirection and Aliasing**: Includes examples of URL redirection and aliasing, allowing the server to redirect requests or present content from different paths as if from the requested path.

- **Security and Access Control**:
  - Demonstrates the use of `autoindex` to control directory listing.
  - Shows how to secure specific directories by restricting allowed methods and using aliases to map URLs to filesystem paths differently.

## Acknowledgments
- project made in collaboration with [mc-putchar](https://github.com/mc-putchar) and [lbaron42](https://github.com/lbaron42),
