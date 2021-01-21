from app import MODULES, CONTEXT
from flask import render_template



def admin_render_template(template_name_or_list, module_name, scripts=None, modals=None,**context):
    vdata = {
        'sidebar': None,
        'module': None
        }

    module = None
    
    for _module in MODULES:
        if _module.module_name == module_name:
            module = _module
            vdata['module'] = _module
            break
    
    if module.sidebar is not None:
        vdata['sidebar'] = module.sidebar

    context['vdata'] = vdata
    context['scripts'] = scripts
    context['modals'] = modals
    context['context'] = CONTEXT
    
    return render_template(template_name_or_list, **context)
