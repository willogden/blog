---
title: "apt-get won't connect following hardening via iptables"
date: 2014-07-25T08:05:00Z
categories: ["DevOps"]
tags: ["devops"]
slug: "iptables-apt-get-issue"
summary: "Hardening a VPS using iptables breaks apt-get..."
aliases: ["/iptables-apt-get-issue.html"]
---

Following locking down a Wordpress VPS hosted on DigitalOcean, I found apt-get no longer could connect (E: Unable to fetch some archives, maybe run apt-get update or try with --fix-missing?). After a bit of fiddling around, the following iptable entries sorted the issue:

    Chain INPUT (policy ACCEPT)
    target     prot opt source               destination
    ACCEPT     all  --  anywhere             anywhere
    ACCEPT     udp  --  anywhere             anywhere             udp spt:domain
    ACCEPT     tcp  --  anywhere             anywhere             tcp dpt:ssh
    ACCEPT     tcp  --  anywhere             anywhere             tcp dpt:http
    ACCEPT     all  --  anywhere             anywhere             state RELATED,ESTABLISHED
    DROP       all  --  anywhere             anywhere
