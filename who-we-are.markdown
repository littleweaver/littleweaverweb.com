---
layout: default
nav: Who We Are
title: Who We Are
---

{% for member in site.data.members %}
<div class="margin-leader">
	<div class="media">
		<img class="media-object pull-left col-xs-4 col-sm-3 img-circle img-responsive" src="/static/images/{{ member.shortname }}.jpg" alt="{{ member.name }}">
		<div class="media-body">
			<h3>{{ member.name }}</h3>
			<p><a href="https://twitter.com/{{ member.twitter }}" class="unstyled"><i class="fa fa-lg fa-twitter"></i> &#64;{{ member.twitter }}</a></p>
			<p><a href="https://github.com/{{ member.github }}" class="unstyled"><i class="fa fa-lg fa-github"></i> {{ member.github }}</a></p>
		</div>
	</div>
</div>
{% endfor %}
