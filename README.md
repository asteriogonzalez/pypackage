# pypackage

A custom cookiecutter template for python packages

Features:

- Sphinx live documentation
- Docker support
- run pytest in parallel
- continuos testing using pytest-watch plugin
- full code coverage, including tests suite.
- wingide remote debugging support.



## Usage

Create project folder using cookiecutter

```bash
cookiecutter pypackage
full_name [Asterio Gonzalez]: 
email [asterio.gonzalez@gmail.com]: 
github_username [asterio.gonzalez]: 
project_name [Dummy]: Incremental Storage
project_slug [incremental_storage]: incstorage
project_short_description [Python Dummy Package]: Incremental Storage
pypi_username [asterio.gonzalez]: 
version [0.1.0]: 
use_pytest [y]: 
use_black [y]: 
use_wingide_remote_debug [y]: 
use_pypi_deployment_with_travis [y]: 
add_pyup_badge [n]: 
Select command_line_interface:
1 - Click
2 - Argparse
3 - No command-line interface
Choose from 1, 2, 3 [1]: 
create_author_file [y]: 
Select open_source_license:
1 - MIT license
2 - BSD license
3 - ISC license
4 - Apache Software License 2.0
5 - GNU General Public License v3
6 - Not open source
Choose from 1, 2, 3, 4, 5, 6 [1]: 

 ```

Create a and activate virtual environment

```bash
make create-venv
source venv/bin/activate
make install-testing-requisites
```

## Testing

```bash
make test
```
or 
```bash
make ptw
```


