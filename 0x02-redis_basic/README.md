# Project Title: Redis Basic

## Description

This project focuses on learning how to use Redis for basic operations and as a simple cache. The tasks include implementing Redis commands, interacting with Redis using Python, and setting up Redis as a cache for an application.

## Resources

- [Redis commands](#)
- [Redis python client](#)
- [How to Use Redis With Python](#)
- [Redis Crash Course Tutorial](#)

## Learning Objectives

- Learn how to use Redis for basic operations
- Learn how to use Redis as a simple cache

## Requirements

- All files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
- All files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- Code should use the pycodestyle style (version 2.5)
- All modules, classes, functions, and methods should have documentation
- Documentation should be real sentences explaining the purpose (length will be verified)
- Functions and coroutines must be type-annotated

## Setup

### Install Redis on Ubuntu 18.04

```bash
$ sudo apt-get -y install redis-server
$ pip3 install redis
$ sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf
