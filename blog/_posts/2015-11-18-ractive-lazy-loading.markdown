---
layout: post
title:  Ractive lazy loading
date:   2015-11-18
author: stephen
---

We at Little Weaver have been using [Ractive](http://www.ractivejs.org/) and loving it. Recently, though, we ran into a problem. We were working on a project that required us to load our ractive template asynchronously. Ordinarily, that’s not so hard. You make an AJAX call to a script that returns your template data, then do your initialization. Here’s an abbreviated example, using PHP:

{% highlight php %}
<!-- /ractive-json.php -->
<?php
$out = array('template' => "<div {{#if loaded}}class='loaded'{{/if}}>Super cool template!</div>");
echo sprintf("%s(%s)", $_GET['callback'], json_encode($out));
?>
{% endhighlight %}

{% highlight js %}
// init.js
$.ajax({
    dataType: 'jsonp',
    cache: false,
    url: "/ractive-json.php",
    success: function (data) {
        $('body').append('<div id="ractive"></div>')
        var ractive = window.ractive = new Ractive({
            el: '#ractive',
            template: data.template,
            data: {
                // ... init data & helper functions
            },
            // ... any additional methods
        });

        // ... any setup that requires the ractive object
        // i.e. calls to ractive.on() or ractive.observe()
    }
});
{% endhighlight %}

On a small project, this is all you need. You just wait until the ractive template is loaded, then you hook up all your listeners, run all your api calls, etc. But it doesn’t scale.

The project we were working on was big enough that we had to split it into a number of different files related to different pieces of functionality or risk not being able to find *anything*.

And here’s where we ran into two problems.

1. We wanted to use the ractive object as soon as our javascript was parsed – either to set up listeners or template helpers related to our modules, or in AJAX callbacks – but Ractive can’t be instantiated without template data, so we couldn’t rely on its presence.
2. We needed to keep our code as readable as possible, both for ourselves and for anyone coming to the project from the ractive tutorial.

The solution? Provide a global ractive variable right from the start that keeps track of listeners and data, and hands it all of off to the actual ractive instance when the time is right. That lets us consistently use `ractive.set()`, `ractive.on()`, etc. without needing to worry about our timing.

{% highlight js %}
var FakeRactive = window.FakeRactive = function () {
    this.pendingOn = [];
    this.pendingObserve = [];
    this.pendingSet = {};
    this.pendingFire = [];
};

FakeRactive.prototype.on = function() {
    this.pendingOn.push(Array.prototype.slice.call(arguments));
};

FakeRactive.prototype.observe = function() {
    this.pendingObserve.push(Array.prototype.slice.call(arguments));
};

FakeRactive.prototype.set = function(key, value) {
    if (typeof key == 'object') {
        $.extend(this.pendingSet, key);
    } else {
        this.pendingSet[key] = value;
    }
};

FakeRactive.prototype.fire = function() {
    this.pendingFire.push(Array.prototype.slice.call(arguments));
};

FakeRactive.prototype.release = function (ractive) {
    $.each(this.pendingOn, function (idx, args) {
        ractive.on.apply(ractive, args);
    });
    $.each(this.pendingObserve, function (idx, args) {
        ractive.observe.apply(ractive, args);
    });
    ractive.set(this.pendingSet);
    $.each(this.pendingFire, function (idx, args) {
        ractive.fire.apply(ractive, args);
    });
};

var ractive = window.ractive = new FakeRactive();

$.ajax({
    dataType: 'jsonp',
    cache: false,
    url: "/ractive-json.php",
    success: function (data) {
        var fakeRactive = ractive;
        $('body').append('<div id="ractive"></div>')
        ractive = window.ractive = new Ractive({
            el: '#ractive',
            template: data.template,
            data: {
                // ... init data & helper functions
            },
            // ... any additional methods
        });

        // no setup here!

        fakeRactive.release(ractive);
    }
});
{% endhighlight %}


The one thing this system (as written) would *not* handle well is an early API call with a callback that used `ractive.get()`; it’s just not something we needed. If someone *were* to need it, I would suggest they wrap their API calls something like this:

{% highlight js %}
var project = window.project = {
    apiEndpoint: '/api'
};

project.api = function(data, success) {
    $.ajax({
        dataType: 'jsonp',
        cache: false,
        url: project.apiEndpoint,
        data: data,
        success: function() {
            ractive.onRealRactive(success, Array.prototype.slice.call(arguments));
        }
    });
};
{% endhighlight %}

On the fake ractive instance, this would store the arguments for later release. On the real ractive instance, this would immediately call the success function with its arguments. I’ll leave actually writing the `onRealRactive()` methods to you, since it should be relatively simple and also since I don’t want to post *more* code I haven’t actually used. ;-)

I hope this was useful and/or interesting for you, dear reader! Ractive is so much fun to use, and asynchronous loading of data can be pretty great. And it turns out it’s not so hard to do both!
