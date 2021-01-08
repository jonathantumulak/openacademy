Odoo Tutorial https://www.odoo.com/documentation/14.0/howtos/backend.html

# Progress

##Building a module   
- Implemented openacademy module based from "Building a module" tutorial
- Docker image uses python2. Haven't checked if there's an available one with python3.
- Development/debugging takes quite some time, from restarting server to upgrading the module in the UI.
Not sure if there's a more streamlined way to do it.
- Method decorator "onchange" is not called when changing data from a wizard.
- Will need to investigate if it is possible to define model methods when we can pass extra params.
    eg. `session.user_is_attendee(user_id)`
    Also not sure if this kind of use case is possible.
- Has two types of model inheritance
- Can create default groups via security.xml or on the fly using the UI
- When creating a record via a form field with a domain, the created record will not have the restrictions defined in the domain. Probably needs a bit more customization

###UI   
- Can support view inheritance
- UI elements are prepackaged, dont have to worry about displaying data/forms.
- Defined in views as xml files.
- Possible to create Dashboards to have a view of all data at a glance
- Possible to create custom Reports

##Multi-Company Guidelines
- haven't started on this yet.

##Theme tutorial
- haven't started on this yet