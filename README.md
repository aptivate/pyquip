# pyquip

Simple installation and django-assets for jQuip.

[![Build Status on Travis](https://travis-ci.org/aptivate/pyquip.svg?branch=master)](https://travis-ci.org/aptivate/pyquip)

## Purpose

[jQuip](https://github.com/mythz/jquip) is a lightweight alternative to
[jQuery](http://jquery.com/). It doesn't have all the features, but it's
95% smaller.

## FAQ

### Why do we need a JavaScript library at all?

Because:

* browsers are all different, requiring compatibility code and testing;
* many useful methods are missing from core JavaScript, such as manipulating
  DOM trees, listening to events, etc.

### Why do we need jQuip?

Because jQuery is too big and bloated, and slows down page loading times
on low bandwidth connections.

### Why not Zepto?

Zepto only works with the latest browsers, which is against our philosophy
that web pages should be accessible:

* Using old browsers (e.g. Internet Explorer 8) for those without bandwidth,
  skills or permission to upgrade their browsers.
* Using mobile devices (smart phones, feature phones, low cost tablets) as well
  as desktop PCs. So our designs should be responsive, compatible with
  older and simpler browsers such as Opera Mini, and not require Javascript.

### Why use pyquip?

jQuip wasn't packaged as an easy-to-install module for Django, so extra work
was required to install the Git submodule in an appropriate place, and make the
static files accessible. (Of course you could just copy and paste the files,
but then you lose track of where they came from).

And there's no integration with django-assets.

## Installation

### With DYE

If you don't yet have a Django project, the easiest way to get started is:

* [use DYE and cookiecutter](https://github.com/aptivate/dye/blob/develop/readme-cookiecutter.rst)
  to create one,
* enter `django` or `cms` for the *Project type*.

Whether this is a new or an existing DYE project, add `pyquip` to it:

* add this line to `deploy/pip_packages.txt`:
    -e git+https://github.com/aptivate/pyquip.git
* run `deploy/bootstrap.py`,
* run `deploy/tasks.py deploy:dev`.

### Manual Installation

If you're not using DYE, then install `cmsbootstrap` in your global Python
environment or virtualenv:

    pip install pyquip

Or if it's not available on PyPI, or you need a newer version:

    pip install -e git+https://github.com/aptivate/pyquip.git

Of course you need [Django](https://www.djangoproject.com/)
(1.5 or higher) for this to do anything useful. It will be installed
automatically by Pip if you don't have it already.  

### Add to `INSTALLED_APPS`

Add `pyquip` to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'pyquip',
    )

This allows Django to find the static files that we've provided.
It also allows `django-assets` to find the assets and compile them.

### Building the assets

If you want to use the assets, then you'll need to install `django-assets`
in your project and then build the assets at least once:

    django/website/manage.py assets build

Or you can run the following command, in a spare terminal, to watch the sources
for changes and rebuild them automatically when necessary:

    django/website/manage.py assets watch

## Usage

### Without django-assets

Add the following line to your template(s) to load all of jQuip in one go:

	<script src="{{ STATIC_URL }}js/jquip/dist/jquip.all.min.js" type="text/javascript"></script>

Or to load a non-minified version for debugging:

	<script src="{{ STATIC_URL }}js/jquip/dist/jquip.all.js" type="text/javascript"></script>

Or to load one or more modules, choose from the following lines, respecting
dependencies:

	<script src="{{ STATIC_URL }}js/jquip/dist/jquip.min.js" type="text/javascript"></script>
	<script src="{{ STATIC_URL }}js/jquip/dist/jquip.ajax.min.js" type="text/javascript"></script>
	<script src="{{ STATIC_URL }}js/jquip/dist/jquip.css.min.js" type="text/javascript"></script>
	<script src="{{ STATIC_URL }}js/jquip/dist/jquip.custom.min.js" type="text/javascript"></script>
	<script src="{{ STATIC_URL }}js/jquip/dist/jquip.docready.min.js" type="text/javascript"></script>
	<script src="{{ STATIC_URL }}js/jquip/dist/jquip.events.min.js" type="text/javascript"></script>
	<script src="{{ STATIC_URL }}js/jquip/dist/jquip.q-min.min.js" type="text/javascript"></script>

### With django-assets

The following assets are provided in the `pyquip.assets` module:

	all, core, ajax, css, custom, docready, events, q_min

All of the individual modules are prefixed with `jquip.` when registered with
`django-assets`, so to include them in your templates, add that prefix. For
example:

	{% load assets %}
	{% assets "jquip.all" %}
		<script type="text/javascript" src="{{ ASSET_URL }}"></script>
	{% endassets %}

Or to include an individual module:

	{% load assets %}
	{% assets "jquip.core" "jquip.css" %}
		<script type="text/javascript" src="{{ ASSET_URL }}"></script>
	{% endassets %}

### Combining with your bundles

You can include the modules that you want in your `django-assets` bundles, to
reduce the number of HTTP requests, and hence the page loading time, as well as
repetition in your templates:

	from django_assets import Bundle, register
	from pyquip import assets as jquip

	all_js = Bundle(jquip.core, jquip.css, 'js/mine.js',
		filters='jsmin',
		output='js/all.js')

	register('all_js', all_js)

> *Note:* if you want to use the `jsmin` filter as shown in the example above,
> you'll need to install the `jsmin` package in your Python environment or
> `virtualenv`, much as you did with `pyquip` itself.

Then you can include all your jQuip modules, and your own code, in one go,
by including a single file in your templates:

	{% load assets %}
	{% assets "all_js" %}
		<script type="text/javascript" src="{{ ASSET_URL }}"></script>
	{% endassets %}
