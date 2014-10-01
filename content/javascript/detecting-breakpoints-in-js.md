Title: Detecting active breakpoints in JavaScript
Date: 2014-10-01 21:45
Category: Javascript
Tags: javascript
Slug: detecting-breakpoints-in-js
Author: Will Ogden
Summary: Detecting the active media query breakpoints in JavaScript...

During the recent responsive redesign of [TrustedHousesitters.com](http://www.trustedhousesitters.com) we had the requirement to execute different JavaScript dependant on the active media query breakpoint. Our use case was specific to the smartphone experience of Google Maps, but similar requirements for more basic navigation interactions probably exist.

The easy solution is to simply check something like `window.innerWidth` e.g.

    if(window.innerWidth <= 480) {
        // Do something for small screens
    } else if (window.innerWidth <= 1024) {
        // Do something for medium screens
    }

However this requires breakpoint dimensions being defined in 2 places, both in SASS/CSS and also JS. Not great separation of concerns and definitely increasing the risk of bugs. Another solution was needed...

Since we're using the excellent [Breakpoint SASS library](http://breakpoint-sass.com/) to create our breakpoints, they are already given a **name** e.g.

    $small: 600px;
    .content {
        @include breakpoint($small) {
            content: 'Phone stuff';
        }
    }

What we really want is to be able to test if **$small-screen** is active by name not by dimensions. If we decided to tweak the breakpoint width's in SASS, the JS code will just continue to work. The solution (all be it hacky), is to encode the name of the breakpoint within the `font-family` style of a class that is then queried from JS e.g.

    .media-query-info {
        display: none;
        font-family: '{"enabled" : "0"}';

        @media all and (max-width: 600px) and (min-width: 0px) {
            font-family: '{"enabled" : "1", "breakpoint" : "small"}';
        }

        @media all and (max-width: 800px) and (min-width: 600px) {
            font-family: '{"enabled" : "1", "breakpoint" : "medium"}';
        }

        @media all and (min-width: 800px) {
            font-family: '{"enabled" : "1", "breakpoint" : "large"}';
        }
    }

The above goes a step further and encodes the breakpoint as JSON. Using the following, it's now possible to write conditional JS based on the active media query. Job done!

    // Get MQ info stored in font-family
    var infoJSON = $(".media-query-info").css("font-family");

    // Remove the leading/trailing quote and remove backslashes
    infoJSON = infoJSON.substring(1, infoJSON.length-1).replace(/\134/g,"");

    // Parse
    var info = JSON.parse(infoJSON);

    // Output active breakpoint
    console.log(info.breakpoint);

Check out this [pen](http://codepen.io/willogden/pen/mqDaB) for a full example.
