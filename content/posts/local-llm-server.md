---
title: "Building a Local LLM Server"
date: 2026-08-01T12:00:00Z
categories: ["AI"]
tags: ["llm", "hardware", "qwen", "benchmarking"]
slug: "local-llm-server"
summary: "Scouring eBay for GPUs, writing benchmarks, and being genuinely impressed by Qwen3.6."
---

I've been meaning to run a local LLM server for a while.

Not because I'm particularly worried about privacy or data leakage — though that's a factor — but because there's something satisfying about owning the whole stack. No rate limits, no API keys, no waiting for a provider to change their pricing or deprecate a model. Just a box in the corner doing its thing.

The obvious blocker was hardware.

I've got a decent enough machine for development, but nothing that'll chew through a modern LLM without grinding to a halt. So I did what any sensible person does in 2026: I spent an uncomfortable amount of time on eBay looking for GPUs.

The used GPU market is a peculiar beast. You've got the genuine bargains — people upgrading and selling their old cards at reasonable prices — and then you've got the mining rigs, the smoke-damaged units, and the listings that say "tested, works fine" in a font size that screams "it absolutely does not work fine." I ended up finding a couple of solid cards from sellers with good feedback and no mention of crypto, which felt like winning the lottery.

With the hardware sorted, it was time to get something running.

Before I got too deep into configuration, I wanted a proper first test — something that'd tell me immediately whether the setup was actually working or whether I was about to spend three hours debugging environment variables. So I wrote a quick benchmarking tool. Nothing fancy — a Python script that sends a prompt, measures time to first token, and counts tokens per second over the response.

I started with SGLang — it's fast, well-maintained, and doesn't require a PhD in distributed systems to configure. Docker Compose made it trivial to spin up, and I had a model serving locally in about twenty minutes. Ran the benchmark as the first real test, and the local model passed without any fuss. Tokens streaming back, numbers looking reasonable. It felt good enough to stick with.

Then I hit the quantisation problem.

The model I wanted to run was only available in a quant format that SGLang didn't support. I spent a while hoping I'd missed something — a flag, a new version — but no. So I tried Llama instead. Same Docker Compose setup, same basic workflow, and it handled the quant format without complaint. Sometimes you pick your tool, and sometimes your tool picks you.

With that sorted, it was back to the benchmark — this time to see how fast things really were.

Here's where things got interesting.

I loaded up Qwen3.6 and ran the benchmark. I was expecting something reasonable — maybe 20-30 tokens per second, enough to be usable but not exactly snappy. Instead I was getting around 70 tokens per second.

Seventy.

That's fast enough that it feels like you're talking to something rather than waiting for something. Fast enough that the latency doesn't interrupt your train of thought. Fast enough that I found myself running test prompts just to watch the numbers, because they didn't seem right.

I'm not going to pretend I'm an expert on LLM inference optimisation. But running a capable model locally at that speed, on hardware I bought second-hand from eBay, felt like a bit of a cheat code. The gap between "this is a neat experiment" and "this is genuinely useful" is smaller than I expected.

So there it is. A local LLM server, built from eBay GPUs and Docker Compose files, churning out tokens at a rate that still surprises me. Next up: actually finding a good use for it that doesn't involve running the same benchmark with slightly different prompts.
