Title: AngularJS Seed App Using Browserify and Gulp
Date: 2014-04-04 10:45
Category: Javascript
Tags: javascript
Slug: angular-acorn
Author: Will Ogden
Summary: A an AngularJS seed app using Browserify and Gulp...

As my first look into using AngularJS for a major project, I really wanted to get the app structured correctly from the go get. So many times I've built an application only to have to massively refactor after the inevitable feature requests and spec creep.

As a starting point I looked into the various popular seed projects. The first was [angular-seed](https://github.com/angular/angular-seed); this seemed the most popular, but doesn't have a modular structure - controllers, directives, etc are all lumped in together. Not great as the application grows. The next was [ngBoilerplate](https://github.com/ngbp/ngbp); this is an awesome project. Grunt has been my goto task runner for a while, so the high level of automation ticked a lot of boxes. It did however have a few downsides:

* Used LESS (I wanted to use SASS)
* Used Bootstap (A bit heavy for my needs)
* The Grunt build process (although awesome) was complicated and had build steps for Coffeescript source and the like. I didn't need this.

I actually ended up forking it and adding in SASS support and removing bootstrap and coffeescript support, however at the same time I was playing around with Gulp. Seemed like a good opportunity to try it out on a real world project, hence the creation of [angular-acorn](https://github.com/willogden/angular-acorn).

Here are some of the features:

* Uses Gulp for build automation (gulp build, gulp release, gulp test, gulp watch are the main tasks you would want to use...but take a look at the Gulpfile)
* Browserify for dependency management. I've used RequireJS a lot in previous projects, but with the rise of NPM I think Browserify is the future!
* SASS/Bourbon/Bitters for CSS and base style and typography.
* Susy/Breakpoint for killer semantic grids and media query management
* Jasmine/Karma for testing
* Angular-UI Router (which is amazing)
* (Basic) mobile first responsive design with off canvas navbar
* IE8 Support...at the moment.

Here's a [demo](/en/demos/angular-acorn/index.html) of the release version.

Still some work to be done (notably around responsive image support), but a good first step. Hope it's useful to someone. All feedback welcome.
