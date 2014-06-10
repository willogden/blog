Title: Removing merged remote branches
Date: 2014-06-10 18:45
Category: Git
Tags: Git
Slug: prune-remotes-git
Author: Will Ogden
Summary: Easily remove all those merged remote branches for your local repo...

Again just another reminder for me; it's like the 4th time i've had to look this up on SO...if you need to prune your list of remote branches in your local repo do the following:

    git remote update --prune
