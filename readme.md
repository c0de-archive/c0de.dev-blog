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


## Making new posts

For seperation, I store the content in a private repo (can't read my drafts and encrypted blogs without the password). Also as a matter of choice, I'm using [Markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) as markup language.

Categories are defined per folder in the [c0de.dev-content](https://github.com/alopexc0de/c0de.dev-content) repository. To create a new category, simply create a new folder in that repo with at least one post within. For posts without a category, simply throw the new posts in the root of the repo.

When a new post has been created (with the appropiate [metadata](https://docs.getpelican.com/en/3.6.3/content.html#file-metadata)), the steps to generate the output is as follows:

1. SSH into your server
1. `cd c0de.dev-blog`
1. Update all submodules (installs new plugins too) - `make update`
1. `cd pelican`
1. Clear the output cache if themes or globals changed - `make clean`
1. Generate the new static HTML site - `make html`

## TODO

* Service/Unit to run this in a server on prod
* Git hooks to automatically fetch content 
* NginX config
