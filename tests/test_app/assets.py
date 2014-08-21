from __future__ import absolute_import, unicode_literals

from django_assets import register
from pyquip import assets as jquip

register('test_app_js',
    jquip.all,
    'js/pyquip/jquery_global_var.js',
    filters=['jsmin'],
    output='test_app.min.js')
