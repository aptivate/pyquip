from django_assets import Bundle, register

def standard_bundle(name, source):
    bundle = Bundle('js/jquip/dist/%s' % source,
        output='js/%s' % source)
    register('jquip.%s' % name, bundle)
    return bundle

all = standard_bundle('all', 'jquip.all.min.js')
core = standard_bundle('core', 'jquip.min.js')
ajax = standard_bundle('ajax', 'jquip.ajax.min.js')
css  = standard_bundle('css', 'jquip.css.min.js')
custom = standard_bundle('custom', 'jquip.custom.min.js')
docready = standard_bundle('docready', 'jquip.docready.min.js')
events = standard_bundle('events', 'jquip.events.min.js')
q_min = standard_bundle('q_min', 'jquip.q-min.min.js')
