
<h2 align="center">Dash Cool Components</h2>

<p align="center">
  Cool React components, wrapped for Plotly Dash
</p>

[![PyPI version](https://badge.fury.io/py/dash-cool-components.svg)](https://badge.fury.io/py/dash-cool-components)

## Table of contents

- [Installation](#installation)
- [Quick Start](#quickstart)

## Installation

```sh
pip install dash-cool-components
```

## Components

<details>
  <summary>
    <strong>Datetime Picker</strong>
  </summary>

  A date-time-timezone picker input. Implemented with
  [Timezone Picker React component](https://www.npmjs.com/package/react-bootstrap-timezone-picker).
  
  ### Component Properties:  
    
  **The ID used to identify this component in Dash callbacks.**
  * id: string  
  
  **The input's current value, on ISO format with date, time and timezone.**  
  * value: string
  
  **Defines if the timezone input should be rendered. Defaults to true.**  
  * renderTimezone: boolean  

  **The component container's style. Can be a style object or a css string.**  
  * style: object | string

  **The date input's style. Can be a style object or a css string.**  
  * dateInputStyle: object | string

  **The timezone container's style. Must be a style object.**  
  * timezoneInputStyle: object  

  ```
  import dash
  import dash_html_components as html
  import dash_cool_components

  app = dash.Dash(__name__)

  app.layout = html.Div([
      dash_cool_components.DateTimePicker(
              id='timezone',
              renderTimezone=True,
          ), width={'size':4}
      html.Div(id='output')
  ])
  
  @app.callback(Output('output', 'children'), [Input('input', 'value')])
  def display_output(value):
      if value is not None:
          output_div = html.Div([
              html.H4('Datetime: {}'.format(value['datetime'])),
              html.H4('Timezone: {}'.format(value['timezone']))
          ])
          return output_div

  if __name__ == '__main__':
      app.run_server(debug=True)

  ```

  ![](images/gif_datetimetimezonepicker.gif)
</details>


<details>
  <summary>
    <strong>Keyed File Browser</strong>
  </summary>

  File and directory browser given a flat keyed list of objects.
  [Source React component](https://github.com/uptick/react-keyed-file-browser).
  
  ### Component Properties
    
  **The ID used to identify this component in Dash callbacks.**  
  * id: string

  **A selectedPath that will be printed when this component is rendered**  
  * selectedPath: string

  **Array with objects containing files paths and infos**  
  * value: array

  ```
  import dash
  import dash_html_components as html
  import dash_bootstrap_components as dbc
  import dash_cool_components


  external_stylesheets = [dbc.themes.BOOTSTRAP]
  app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

  dir_dict = [
      {'key': 'dir1/my_image.jpeg', 'size': 2782874},
      {'key': 'dir2/other_image.tif', 'size': 499240007}
  ]

  my_component = dash_cool_components.KeyedFileBrowser(
      id='file_explorer',
      value=dir_dict,
  )
  app.layout = html.Div(my_component, style={'width': '500px'})

  if __name__ == '__main__':
      app.run_server(debug=True)

  ```

  ![](images/gif_keyedfilebrowser.gif)
</details>

<details>
  <summary>
    <strong>Tag Input</strong>
  </summary>

  A tag input component.
  [Source React component](https://github.com/leekevinyg/react-tag-input).
  
  ### Components Properties
    
  **The ID used to identify this component in Dash callbacks.**  
  * id: string

  **Wrapper style css**  
  * wrapperStyle: object  
  
  **Tag style css**  
  * tagStyle: object

  **Input style css**  
  * inputStyle: object

  **Delete button style**  
  * tagDeleteStyle: object

  **Placeholder**  
  * placeholder: string

  **Tags Values**
  * value: array


  ```
  import dash
  import dash_html_components as html
  import dash_cool_components

  app = dash.Dash(__name__)

  my_component = dash_cool_components.Keywords(id='tag_input')
  app.layout = html.Div(my_component)

  if __name__ == '__main__':
      app.run_server(debug=True)

  ```

  ![](images/gif_taginput.gif)
</details>
