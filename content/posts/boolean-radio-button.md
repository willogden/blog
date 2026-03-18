---
title: "Django Forms Boolean Radio Button"
date: 2014-02-06T14:45:00Z
categories: ["Django"]
tags: ["python", "django"]
slug: "boolean-radio-button"
summary: "Trying to get a boolean value from a radio button in Django forms"
aliases: ["/boolean-radio-button.html"]
---

After much searching and trying out various different syntaxes, I finally found the following which allows a boolean field to be rendered as radio buttons. This has been tested in Dango 1.4. I think a few of the StackOverflow answers related to this are for older versions of Django:
	
	class MyForm(forms.Form):
		my_boolean_field = forms.BooleanField(widget=forms.RadioSelect(choices=((1, "Yes"),(0, "No"))), initial=0, required=False)
