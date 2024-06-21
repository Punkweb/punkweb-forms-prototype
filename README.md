# Punkweb Forms

Prototype application for creating dynamic forms from the Django admin interface, and rendering them in a Django template.

## Prototype

- You create Form and Field objects in the Django admin interface.
- Form class is dynamically generated from the Form and Field objects.
- Form view takes a form id and handles rendering and submitting the form.
- Submissions are stored as JSON.

Currently this has no validation, and is just a prototype to demonstrate the concept. You could generate JSON schema from the form objects and use that to validate submissions.
