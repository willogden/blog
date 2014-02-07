Title: Django Forms Boolean Radio Button
Date: 2014-02-06 14:45
Category: Django
Tags: python, django
Slug: boolean-radio-button
Author: Will Ogden
Summary: Trying to get a boolean value from a radio button in Django forms

After much searching and trying out various different syntaxes, I finally found the following which allows a boolean field to be rendered as radio buttons. This has been tested in Dango 1.4. I think a few of the StackOverflow answers related to this are for older versions of Django:

	my_boolean_field = forms.BooleanField(widget=forms.RadioSelect(choices=((1, 'Yes'),(0, 'No'))), initial=0, required=False)
