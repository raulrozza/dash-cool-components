# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Keywords(Component):
    """A Keywords component.
ExampleComponent is an example component.
It takes a property, `label`, and
displays it.
It renders an input with the property `value`
which is editable by the user.

Keyword arguments:
- id (string; optional): The ID used to identify this component in Dash callbacks.
- wrapperStyle (dict; optional)
- tagStyle (dict; optional)
- inputStyle (dict; optional)
- tagDeleteStyle (dict; optional)
- placeholder (string; optional)"""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, wrapperStyle=Component.UNDEFINED, tagStyle=Component.UNDEFINED, inputStyle=Component.UNDEFINED, tagDeleteStyle=Component.UNDEFINED, placeholder=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'wrapperStyle', 'tagStyle', 'inputStyle', 'tagDeleteStyle', 'placeholder']
        self._type = 'Keywords'
        self._namespace = 'dash_cool_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'wrapperStyle', 'tagStyle', 'inputStyle', 'tagDeleteStyle', 'placeholder']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(Keywords, self).__init__(**args)
