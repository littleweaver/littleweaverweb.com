---
layout: post
title:  Evolution of a Marketing Page
date:   2015-06-24 01:00:00
author: stephen
---

Little Weaver has a single internal product, [Dancerfly](https://dancerfly.com). It's our baby. We were inspired to create this website because we're all of us social dancers of one sort or another – I do mostly blues, and Harris and Naomi do more contra – and over the years we've been frustrated, both as organizers and as attendees, by the lack of a really solid, easy-to-use event registration website specifically geared to the needs of social dance events.

But it turns out that there's a lot more to setting up a platform than just writing the code. And most of it we didn't know when we made the first commit on February 20, 2014, despite having worked professionally in web design & development for over five years!

So we learned a lot. I can't get into it all in this post, so I'm going to focus on the evolution of our marketing strategy and materials. I hope this'll be helpful to other non-sales folks who are looking to create and market their own product!

#Stage 0: No "marketing" pages

When we started creating Dancerfly, the idea was that we would create an open-source application that could be used by dance events across the country. All they'd need would be a volunteer / staff member with some python coding experience (or the time & willingness to learn) and they'd be able to install the app, set up some new views and templates to handle their event's specific needs, and voilà! Amazing registration experience!

Looking back, this was... naïve. Social dance weekends often run on volunteer work, which means that *all* their work time is at a premium. Most events don't have a dedicated web developer at all. And those that do – if the developer has free time to spend on customizing the website, they've generally a) already done it and b) wouldn't want to start from scratch in a language / framework they aren't already familiar with.

{% include image.html src="/media/2015/2015-06-23-0-splash-0-69a25ce.png" caption="June 20, 2014. Our first splash page was 100% information-focused and had some GREAT font choices!" %}

{% include image.html src="/media/2015/2015-06-23-0-splash-1-399ba5a.png" caption="June 30, 2014. We pretty quickly switched to a better branding, which has basically stuck with us ever since." %}

Trying to create a reusable app also required a lot more development work on our part – for example, every template we developed had to be 100% generic. If we wanted a branded version, or a version that had language specific to our platform, we had to create a separate app and override there. We also put a lot of work into adding features we *thought* someone might want (see also [YAGNI](http://c2.com/cgi/wiki?YouArentGonnaNeedIt)). We've done a lot of work to reduce this cruft, but some of it hangs around to this day.

Around August 2014, we made a conscious move away from the reusable app model and focused on shipping Dancerfly as a platform service that was not intended to be reused. This change was reflected on our splash page, which added a list of features that the platform provided – though you can see we were still pushing the line that folks should contribute to the app!

![October 1, 2014](/media/2015/2015-06-23-0-splash-2-be8dedd.png)

Shortly after that version was made, we launched our site live at [dancerfly.com](https://dancerfly.com) and signed on our first event!

#Stage 1: Simple text information

After launching Dancerfly, we started signing up beta events – not as easy as it sounds! Essentially, we wrote a few cold emails to event organizers every week, giving a brief explanation of what the service was and why they should use it.

Covering the evolution of those emails could be another entire blog post! For now what matters is that eventually, we got to a point where a couple things happened:

1. We realized that we had a *lot* of information that we wanted to communicate to people, and that most of it wasn't available on the Dancerfly website.
2. We realized that it didn't make sense for a website dedicated to events would require people to scroll below the fold to see any.

So we set up marketing pages. Or more accurately – we set up basic documentation. These pages are very simple - just a centered column of text. Informative, but not eye-grabbing and not easily scanned.

{% include image.html src="/media/2015/2015-06-23-1-splash.png" caption="February 13, 2015. Slimmed down header directs folks to the information pages." %}
{% include image.html src="/media/2015/2015-06-23-1-about.png" %}
{% include image.html src="/media/2015/2015-06-23-1-faq.png" %}
{% include image.html src="/media/2015/2015-06-23-1-international-support.png" %}
{% include image.html src="/media/2015/2015-06-23-1-pricing.png" %}

The information on the FAQ, pricing, and international support pages is all new to the website. You can also see on the About page that we've completely stopped trying to get people to contribute code, and are focused on people actually using the platform.

#April 27-28, 2015: Real marketing pages

After a couple months of that as our marketing effort, I happened to show Dancerfly to a friend of mine who had actual marketing experience, who made the astute point that we still had a long ways to go. On her recommendation, we made two changes:

1. We removed the signup / login forms from the splash page. We don't require folks to have an account to register for events, but our call-to-action on the homepage was "Sign up" – which turned some folks off. This change had the added benefit of making the header slimmer, which let us put more focus on the events. We even gave users the option to hide the header, to put even more emphasis on the events.
2. We split the About page into easily-digestible chunks that could be written in large font sizes.

{% include image.html src="/media/2015/2015-06-23-2-splash.png" %}
{% include image.html src="/media/2015/2015-06-23-2-about.png" %}

This was an improvement, but it still didn't go far enough. Our next iteration moved the splash page header into a sidebar widget, effectively merging the user experience for authenticated and anonymous users.

{% include image.html src="/media/2015/2015-06-23-3-splash.png" %}

Meanwhile, the About page got an additional section on pricing and features, which meant that folks could get all the basic information without clicking away. We also simplified the quick description of Dancerfly to the point where it could fit one sentence to a line and switched to high-contrast lettering that's easier to scanned. And we standardized the call-to-action while clarifying what it was that folks would actually end up doing.

{% include image.html src="/media/2015/2015-06-23-3-about.png" caption="We even added in a line suggesting some possible uses!" %}

#May 8, 2015: Incorporating illustrations & polishing copy

In this stage, we incorporated a set of illustrations we'd commissioned from [Lucy Bellwood](lucybellwood.com). They added a great flair of personality to the previously text-only pages. We also put some extra work into making the pages responsive, and rewrote the copy to highlight the most important points.

{% include image.html src="/media/2015/2015-06-23-4-splash.png" caption="We love the way this person is so excited about the event list!" %}
{% include image.html src="/media/2015/2015-06-23-4-pricing.png" caption="The whitespace in the table makes the information easier to parse. We added the note re: Stripe/Dwolla account creation because of issues with a couple prospective events." %}
{% include image.html src="/media/2015/2015-06-23-4-international-support.png" caption="Added headers, even though the content is so short, because it makes the content easier to grasp quickly." %}
{% include image.html src="/media/2015/2015-06-23-4-faq.png" %}
{% include image.html src="/media/2015/2015-06-23-4-about.png" caption="<a href='/media/2015/2015-06-23-4-about-mobile.png'>View mobile version</a>" %}

#Conclusions

So what do I think is the takeaway from all of this? Well, a few things.

First, basically no matter the circumstances, I would recommend building what you need to build *first*, before trying to make it a reusable, open-source app. Focus on making a product that *works* before trying to account for all future possibilities.

Second, think about your prospective audience and what they want / what you want them to know. In our case, we have two audiences, dance attendees and dance organizers. Luckily, the primary thing we want dance organizers to glean from the homepage is that a) other events use us already, and b) people coming to the site will be able to find their event.

Third, think about what you want people coming to your site to *do*. It's generally safe to be consistent! In our case, we made the mistake of asking people to "Sign up" even though account creation wasn't actually required. "Email us" is much clearer and has proven more effective.

Fourth, split important information into digestible chunks – big, lots of whitespace, and high contrast. Hire an illustrator or photographer to add some life to the words on the page!

And finally – maybe this one is obvious – don't try to get it perfect the first time. Getting to where we are took over a year, and having the more primitive versions didn't stop us from getting off the ground. And as far as we've come, I'm sure this won't be the last version of our marketing pages.


*If you'd like to use Dancerfly for a dance event **you** organize, send us an email at <hello@littleweaverweb.com>.*

*Oh, and by the way – Dancerfly is still an open-source project. If you'd like to contribute code or bug reports, or if you're curious to poke around under the hood, check out the repository on [Github](http://github.com/littleweaver/django-brambling).* ;-)
