from urllib import parse


def get_host(netloc):
    if '.' not in netloc:
        return None
    if ':' in netloc:
        return netloc.split(':')[0]
    return netloc


def get_port(netloc, scheme):
    scheme_to_port_map = {
        'http': 80,
        'https': 443,
    }
    if ':' in netloc:
        return int(netloc.split(':')[1])
    try:
        return scheme_to_port_map[scheme]
    except KeyError:
        return "None"


def get_path(path):
    if path == '':
        path += '/'
        return path
    return path


def validate(url):
    components = parse.urlparse(url)
    result = {
        'Protocol': components.scheme,
        'Host': get_host(components.netloc),
        'Port': get_port(components.netloc, components.scheme),
        'Path': get_path(components.path),
        'Query': components.query,
        'Fragment': components.fragment
    }

    required_component_names = {'Protocol',
                                'Host',
                                'Port',
                                'Path'
                                }

    required_component_existing = all(result[name] for name in required_component_names)
    if required_component_existing:
        return result
    else:
        return 'Invalid URL'
        # print(result)


valid_tests = ['http://mysite.com:80/demo/index.aspx',
               'https://my-site.bg',
               'https://mysite.bg/demo/search?id=22o#go',
               'http://softuni.bg/',
               'https://softuni.bg:447/search?Query=pesho&Users=true#go',
               'https://mysite:80/demo/index.aspx',
               'somesite.com:80/search?',
               'https/mysite.bg?id=2',
               ]


result = [validate(url) for url in valid_tests]

for line in result:
    if isinstance(line, dict):
        for k, v in line.items():
            if v:
                print(f'{k}: {v}')
        print('')
    else:
        print(f'{line}\n')
