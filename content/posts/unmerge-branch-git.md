---
title: "Unmerging a branch in git"
date: 2014-04-22T10:45:00Z
categories: ["Git"]
tags: ["git"]
slug: "unmerge-branch-git"
summary: "When people change their mind, use git to rewind..."
aliases: ["/unmerge-branch-git.html"]
---

Mostly posting as a future reference for me, but surely useful for others who find themselves in the situation of signed off changes becoming unsigned off changes just before deployment. To unmerge a feature branch whilst preserving subsequent commits do the following:

    git revert -m 1 hash_of_merge_commit
