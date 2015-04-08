littleweaverweb.com
===================

Little Weaver Web Collective's [Jekyll][]-powered website.

Updating the website requires the following Ruby Gems:

* [Jekyll][]
* [Compass](http://compass-style.org/)
* [Bootstrap-SASS](https://github.com/twbs/bootstrap-sass)

You can install them using Bundler:

```bash
gem install bundler # if not already installed
bundle install # from the root of the littleweaverweb.com repo
```

To generate and test the site locally, we recommend:

```bash
jekyll serve -w
```

To modify the styles, you must use Compass:

```bash
cd static
compass watch
```

or use [Compass.app](http://compass.kkbox.com/)

[Jekyll]: http://jekyllrb.com/
