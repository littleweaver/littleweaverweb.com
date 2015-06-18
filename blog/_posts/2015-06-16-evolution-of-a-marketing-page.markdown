---
layout: post
title:  Evolution of a Marketing Page
date:   2015-06-16 00:00:00
author: stephen
---

Little Weaver has a single internal product, [Dancerfly](https://dancerfly.com). It's our baby. We're all social dancers of one sort or another, and we've all been frustrated at one time or another by the lack of good event registration websites for social dance events.

Dancerfly's first commit was on February 20, 2014. It's been a learning experience in so many ways; in this post, I'm going to talk about the five stages that our marketing pages went through to get to their current state, and some of what we learned along the way.

#Stage 0: No "marketing" pages

When we started creating Dancerfly, the idea was that we would create an open-source application that could be used by dance events across the country. All they'd need would be a volunteer / staff member with some python coding experience (or the time & willingness to learn) and they'd be able to install the app, set up some new views and templates to handle their event's specific needs, and voilà! Amazing registration experience!

Looking back, this was... naïve. Social dance weekends often run on volunteer work, which means that *all* their work time is at a premium. Most events don't have a dedicated web developer. And those that do – if the developer has free time to spend on customizing the website, they've generally a) already done it and b) wouldn't want to start from scratch in a language / framework they aren't already familiar with.

{% include image.html src="/media/2015/2015-06-16-0-splash-0-69a25ce.png" caption="June 30, 2014. We pretty quickly switched to a better branding, which has basically stuck with us ever since." %}

{% include image.html src="/media/2015/2015-06-16-0-splash-1-399ba5a.png" caption="June 20, 2014. Our first splash page was 100% information-focused and had some GREAT font choices!" %}

Trying to create a reusable app also required a lot more development on our part – in particular, we found ourselves trying to support a lot of potential scenarios that we [were not realistically going to need](http://c2.com/cgi/wiki?YouArentGonnaNeedIt).

Around August 2014, we made a conscious move away from the reusable app model and focused on developing Dancerfly as a platform service that was not intended to be reused. This change was reflected on our splash page, which added a list of features that the platform provided – though you can see we were still pushing the line that folks should contribute to the app!

![October 1, 2014](/media/2015/2015-06-16-0-splash-2-be8dedd.png)

Shortly after that version was made, we launched our site live at [dancerfly.com](https://dancerfly.com) and got our first event!

#Stage 1: Simple text information

After launching Dancerfly, we started signing up beta events – not as easy as it sounds! Essentially, we wrote a few cold emails to event organizers every week, giving a brief explanation of what the service was and why they should use it. Those emails evolved over time – but that could be an entire separate blog post!

For now what matters is that eventually, we got to a point where a couple things happened:

1. We realized that we had more information that we wanted to communicate to people stumbling across our site than was currently on the homepage.
2. We decided that we wanted the homepage to be more focused on the upcoming events – i.e. have them above the fold.

So we set up marketing pages. Or more accurately – we set up basic documentation. These pages are very simple - just a centered column of text. Informative, but not eye-grabbing and not easily scanned.

{% include image.html src="/media/2015/2015-06-16-1-splash.png" caption="February 13, 2015. Slimmed down header directs folks to the information pages." %}
{% include image.html src="/media/2015/2015-06-16-1-about.png" %}
{% include image.html src="/media/2015/2015-06-16-1-faq.png" %}
{% include image.html src="/media/2015/2015-06-16-1-international-support.png" %}
{% include image.html src="/media/2015/2015-06-16-1-pricing.png" %}

The information on the FAQ, pricing, and international support pages is all new at this point. You can also see on the About page that we've completely stopped trying to get people to contribute code, and are focused on people actually using the platform.

#April 27-28, 2015: Real marketing pages

After a couple months of that as our marketing effort, I happened to show Dancerfly to a friend of mine who had actual marketing experience, who made the astute point that we still had a long ways to go. On her recommendation, we made two changes:

1. We removed the signup / login forms from the splash page. We don't require folks to have an account to register for events, but our call-to-action on the homepage was "Sign up" – which turned some folks off. This change had the added benefit of making the header slimmer, which let us put more focus on the events. We even gave users the option to hide the header, to put even more emphasis on the events.
2. We split the About page into easily-digestible chunks that could be written in large font sizes.

{% include image.html src="/media/2015/2015-06-16-2-splash.png" %}
{% include image.html src="/media/2015/2015-06-16-2-about.png" %}

This was an improvement, but it still didn't go far enough. Our next iteration moved the splash page header into a sidebar widget, effectively merging the user experience for authenticated and anonymous users. Meanwhile, the About page got an additional section on pricing and features, and standardized its call-to-actions on emailing us.

{% include image.html src="/media/2015/2015-06-16-3-splash.png" %}
{% include image.html src="/media/2015/2015-06-16-3-about.png" caption="Note how much clearer the elevator pitch is with higher contrast and one sentence per line – plus we added in a line suggesting some possible uses!" %}

May 8, 2015: Incorporating illustrations & polishing copy

In this stage, we incorporated a set of illustrations we'd commissioned from [Lucy Bellwood](lucybellwood.com). They added a great flair of personality to the previously text-only pages. We also put some extra work into making the pages responsive, and rewrote the copy to highlight the most important points.

{% include image.html src="/media/2015/2015-06-16-4-splash.png" caption="We love the way this person is so excited about the event list!" %}
{% include image.html src="/media/2015/2015-06-16-4-pricing.png" caption="The whitespace in the table makes the information easier to parse. We added the note re: Stripe/Dwolla account creation because of issues with a couple prospective events." %}
{% include image.html src="/media/2015/2015-06-16-4-international-support.png" caption="Added headers, even though the content is so short, because it makes the content easier to grasp quickly." %}
{% include image.html src="/media/2015/2015-06-16-4-faq.png" %}
{% include image.html src="/media/2015/2015-06-16-4-about.png" %}
{% include image.html src="/media/2015/2015-06-16-4-about-mobile.png" %}
