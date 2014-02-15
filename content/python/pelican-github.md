Title: Pelican, Github Pages and Grunt
Date: 2014-02-06 10:20
Category: Python
Tags: pelican, publishing
Slug: pelican-github
Author: Will Ogden
Summary: Static site generation using Pelican, Github Pages and Grunt

A bit of a meta post about the construction of this blog. Over the years I have got so much neat information and assistance from blogs, that I thought it time to finally do my own.

After spending sometime in the past working with Wordpress, I knew I wanted a static site generator - I have to manage a full web stack for my day job, so wanted something simple needing no love at all. I looked at [Jekyll](http://jekyllrb.com/) but because it's Ruby I kept looking. I then came accross [Pelican](http://blog.getpelican.com/). It uses Markdown and after installing it just seemed to work great.

Next up was hosting. I was going down the S3 route, but came accross [Github Pages](http://pages.github.com/). I've come quite late to Github, but now love it, so seemed like worth trying. Again this worked super well. After creating a new repo, creating the *gh-pages* branch, added a file named *CNAME* in the root that contained my custom domain, then in DNS pointed my custom domain at [willogden.github.io](willogden.github.io), everything just worked. I can (will) write a blog post, run the *pelican* generate command, and then *git add/commit/push* straight to Github and the site is published.

I then wanted to build a theme for Pelican and decided on using [purecss.io](http://purecss.io). I have since found this has already been done, but for me it was an exercise to try it out and see what was involved in writing a theme (answer is not a lot). Having to re-run the *pelican* command whenever I made a change to the theme began to become tedious...quickly. Step in Grunt. In my last role I had been on the frontend and using Grunt for the last 12 months, so was my go to tool for task running. Below is the Grunt file I came up with. This does the following:

*	Runs the Python simple HTTP server to serve up the site
*	Watches for changes to the content and theme folders and re-generates the site if it sees any changes
*	Live reloads the browser

It's pretty simple. Only thing to note is that I'm using a fork of the original *shell* Grunt contrib. This allows processes to be spawned asychronously so that the Python HTTP server can just sit in the background serving up the site whilst the *watch* task runs in the foreground. Here's the Gruntfile.

	module.exports = function(grunt) {

		grunt.initConfig({
		pkg: grunt.file.readJSON('package.json'),

		shell: {
		    pelican: {
		        command: 'pelican'
		    },
		    server: {
		      command: 'python -m SimpleHTTPServer 8888',
		      options: {
		        async: true
		      }
		    }
		},

		watch: {
		  files: ['content/**/*.md','themes/**/*.*'],
		  tasks: ['shell:pelican'],
		  options: {
		    // Start a live reload server on the default port 35729
		    livereload: true,
		  }
		}
		});

		grunt.loadNpmTasks('grunt-shell-spawn');
		grunt.loadNpmTasks('grunt-contrib-watch');


		grunt.registerTask('default', ['shell:server','watch']);

	};