# Web 100: Space Force 
**Author**: neon_spandex

**Flag**: RITSEC{hey_there_h4v3_s0me_point$_3ny2Lx}

## Description
The Space Force has created a portal for the public to learn about and be in
awe of our most elite Space Force Fighters. Check it out at {{LINK}}!

## Deployment
Two docker containers must be deployed for this challenge. One is an Apache/PHP
webserver that listens on port 80, and the other is a MariaDB webserver. The
following files are required to deploy the containers:
- [`docker-compose.yml`](./docker-compose.yml): The docker compose file that
  will be used to spin up the containers
- [`schema.sql`](./schema.sql): The sql script used to initialize the database
- [`app/`](./app/): The PHP scripts that run the simple webapp

## Writeup
The writeup directory contains the following files:
- [`writeup.docx`](./writeup/writeup.md): A description of how the challenge
  would be solved
- [`*.png`](./writeup/): Images used in the writeup document