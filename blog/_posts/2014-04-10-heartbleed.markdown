---
layout: post
title:  Heartbleed
date:   2014-04-10 15:38:00
author: Harris
---

I've seen a lot on Facebook recently about the Heartbleed bug with a lot of different information. I imagine some people are having trouble sorting the signal from the noise in this matter. I'm not a security expert, but I am a devoted security amateur, so with that in mind, here is my analysis and recommendations.

Heartbleed is a SERIOUS SECURITY FLAW. Security expert [Bruce Schneier says][1], "'Catastrophic' is the right word. On the scale of 1 to 10, this is an 11."

The short version is this: any information you've entered into certain secure websites over the past two years is potentially accessible to someone else and it's more or less impossible to know what information has been compromised.

For a slightly longer but legible explanations, both [NPR][2] and [Vox][3] have pretty good summaries, with Vox providing somewhat more technical detail.

Part of what makes this so devastating is there there's not much we as users can do about it. We have to rely on websites to update their own security before our connections are safe. That should happen pretty quickly. Security folks are pretty freaked out.

Obviously, as with any security flaw, someone would have to know about this flaw and want to exploit your information for something bad to happen to you. Chances are good nothing will happen to you. Still. The level of information that is potentially accessible from this is pretty bad.

My recommendations for what you can do are the following:

1. When a service updates and closes the security flaw (either wait for an announcement from them or use a [service](http://filippo.io/Heartbleed/) or [list][4] to check) change your password. If you change your password before they fix the bug, then your new password could still be compromised.
2. Be vigilant about your credit/debit card statements. The good news is that credit card holders in the US bear almost no liability for fraud ($50) provided you report it within 60 days. (N.b., Debit cards are a different story. Cardholders bear *extreme* liability for debit card fraud.)
3. Wherever possible, use Two Factor Authentication to ensure that even if your password is compromised, an attacker cannot access your accounts. http://twofactorauth.org/ TWO FACTOR AUTH IS AMAZING; USE IT. I recommend using it for everything, but having your Facebook, Gmail, or Apple ID accounts compromised could be particularly financially or socially devastating.

I personally think we've basically got to assume that intelligence agencies like the NSA have already been using Heartbleed and [other recent major security flaws][5]. There's certainly some [circumstantial evidence][6] for this.

If all of this was too long for you to read, [Wednesday's xkcd](http://xkcd.com/1353/) summarizes the whole saga pretty succinctly.

[1]: https://www.schneier.com/blog/archives/2014/04/heartbleed.html
[2]: http://www.npr.org/blogs/alltechconsidered/2014/04/08/300602785/the-security-bug-that-affects-most-of-the-internet-explained
[3]: http://www.vox.com/2014/4/8/5593654/heartbleed-explainer-big-new-web-security-flaw-compromise-privacy
[4]: http://mashable.com/2014/04/09/heartbleed-bug-websites-affected/
[5]: http://www.wired.com/2014/02/gotofail/
[6]: https://www.eff.org/deeplinks/2014/04/wild-heart-were-intelligence-agencies-using-heartbleed-november-2013
