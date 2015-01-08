Title: Overriding template blocks in included templates
Date: 2015-01-08 12:45
Category: Django
Tags: python, django
Slug: override-block-in-include
Author: Will Ogden
Summary: Solution to overriding blocks in included templates

First post of 2015, doesn't time fly.

So a bit of background; I'm trying more and more to develop using pattern libraries in my projects. Developing independant and encapsulated components makes prototying quicker, and bugs fewer so a big win overall. However I ran into a bit of stumbling block when trying to get Django Templates to play ball with this approach. What I wanted to do was create a template for a component and include this in a base template whenever I wanted to use the component. In itself that's fine - Django has `{% include "blah.html" %}` which does this nicely; the issue is that for specific components I wanted to override a `{% block my_block %}` within the included template. Out the box (as far as I can tell) this is only possible when extending (`{% extend blah %}`) a template. What is possible is to use `with` e.g.

	{% include "my_component.html" with custom_var="hello world" %}

After a bit of playing around I came up with a custom tag that allows the capture of arbitrary html between the start and end tags to be saved to a named context variable. This can then be passed using `with` to the included template. It allows you to do the following:

##### base.html
	{% blockvar some_html %}
	<li>Item 1</li>
	<li>Item 2</li>
	{% endblockvar %}

	{% include "my_component.html" with list_html=some_html %}

##### my_component.html
	<ul class="my_component">
	{{ list_html }}
	</ul>

Grab the tag code [here]("https://gist.github.com/willogden/09574bbb526fd124c9d4"). Enjoy!
