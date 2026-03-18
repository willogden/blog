---
title: "Back After 11 Years"
date: 2026-03-18T12:00:00Z
categories: ["Meta"]
tags: ["blogging", "ai"]
slug: "back-after-11-years"
summary: "11 years of silence, broken with a little help from Claude."
---

So. It's been a while.

The last post on this blog was January 2015. I'd just started a new role, life got busy, and somehow eleven years slipped by without a single post. The blog sat there, frozen in time — a Pelican-generated static site committed whole into a GitHub Pages branch, festooned with Grunt configs and Fabric scripts and a Python 2 `u'unicode string'` or two.

I kept meaning to come back to it. I never did.

What finally got me here was a conversation with [Claude](https://claude.ai). I'd been meaning to modernise the blog for ages — move it off GitHub Pages, drop the ancient Python toolchain, do something about that `/en/` URL prefix that made no sense for a monolingual blog. Classic yak-shaving territory; the kind of task that sits on the list forever because the effort-to-reward ratio never quite tips far enough.

On a whim I opened Claude and said: *"modernise this project to work with Cloudflare Pages"*. Thirty minutes later the whole thing was done.

Hugo instead of Pelican. PaperMod theme. Git submodule. All eleven posts migrated with frontmatter converted from Pelican's `Key: Value` format to YAML. Old URLs preserved via Hugo aliases. A `_redirects` file for Cloudflare Pages so `/en/` routes still work. Disqus and the long-dead Universal Analytics tracking dropped. The entire `en/` directory of committed build output — gone from git history.

The thing that struck me wasn't just that it worked. It was *how* it worked. Claude read the existing files, understood the project, asked clarifying questions, proposed a plan, and then implemented it step by step — catching its own errors and fixing them mid-flight when the build failed. It felt less like using a tool and more like pairing with someone who'd done this migration a hundred times before.

I'm aware there's something slightly paradoxical about writing a blog post in 2026 about how remarkable AI coding assistants are. It's not exactly a hot take. But experiencing it firsthand — watching a decade of accumulated technical debt get swept away in half an hour — still felt worth writing down.

So: the blog is back. New infrastructure, same vintage content. Let's see if I can manage more than eleven posts over the next eleven years.
