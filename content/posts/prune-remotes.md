---
title: "Removing merged remote branches"
date: 2014-06-10T18:45:00Z
categories: ["Git"]
tags: ["git"]
slug: "prune-remotes-git"
summary: "Easily remove all those merged remote branches for your local repo..."
aliases: ["/prune-remotes-git.html"]
---

Again just another reminder for me; it's like the 4th time i've had to look this up on SO...if you need to prune your list of remote branches in your local repo do the following:

    git remote update --prune
