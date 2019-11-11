# Jekyll Post API

Lightweight API for posting new content to the _posts directory

## Getting Started

You'll need to run this script under whatever user/group has rights to your jekyll _posts directory

### Prerequisites

py version: 3+
pip3 install: magic, flask

```
pip3 install flask
pip3 install magic
```

### Installing

Begin by replacing the default parameters inside the jekyll_api.py script
```
japi.config['DEBUG'] = True
japi.config['POSTDIR'] = '/var/www/default/_posts' # Location of your posts directory
japi.config['SAFEEXT'] = {'md', 'markdown'} # Acceptable file formats (WIP, nonfunctional)
japi.config['SECUREID'] = 'asdf12345' # Token id. This will get passed as a header to authorize you
japi.config['HOSTIP'] = '127.0.0.1' # Listening IP
japi.config['PORT'] = '10000' # Listening port
``

## Contributing

TODO


## Authors

* **Skippy** - *Initial functionality* - [skippyj](https://github.com/skippyj)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* The amazing people at jekyllrb
* The flask framework developers
