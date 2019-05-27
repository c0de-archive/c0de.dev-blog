# c0de.dev Blog


This is a [Pelican](https://getpelican.com) based blog that powers [c0de.dev](https://c0de.dev). 
There's not really a whole lot here, but it contains all the posts and content; as well as all configuration files.


## Installation

1. SSH into your server
1. Clone the repo - `git clone https://github.com/alopexc0de/c0de.dev-blog`
1. `cd c0de.dev-blog`
1. Setup a virtualenv - `virtualenv venv`
1. Activate it - `source venv/bin/activate`
1. Install dependencies into virtualenv - `pip install -r requirements.txt`
1. Install the service and plugins - `sudo make install`

## Updating

1. SSH into your server
1. `cd c0de.dev-blog`
1. `source venv/bin/activate`
1. `make update`

## TODO

* Service/Unit to run this in a server on prod
* Git hooks to automatically fetch content 
* NginX config
* Automatic plugin linking
