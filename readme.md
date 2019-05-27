# c0de.dev Blog


This is a [Pelican](https://getpelican.com) based blog that powers [c0de.dev](https://c0de.dev). 
There's not really a whole lot here, but it contains all the configuration files and plugins/themes.


## Installation

1. SSH into your server
1. Clone the repo - `git clone --recurse-submodules https://github.com/alopexc0de/c0de.dev-blog`
1. `cd c0de.dev-blog`
1. Install the config and plugins - `make install`

## Updating

1. SSH into your server
1. `cd c0de.dev-blog`
1. `make update`

## TODO

* Service/Unit to run this in a server on prod
* Git hooks to automatically fetch content 
* NginX config
