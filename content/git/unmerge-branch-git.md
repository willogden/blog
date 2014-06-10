Title: Unmerging a branch in git
Date: 2014-04-22 10:45
Category: Git
Tags: Git
Slug: unmerge-branch-git
Author: Will Ogden
Summary: When people change their mind, use git to rewind...

Mostly posting as a future reference for me, but surely useful for others who find themselves in the situation of signed off changes becoming unsigned off changes just before deployment. To unmerge a feature branch whilst preserving subsequent commits do the following:

    git revert -m 1 hash_of_merge_commit
