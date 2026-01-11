import json, pathlib
m = json.loads(pathlib.Path('manifest.webmanifest').read_text(encoding='utf-8'))
assert 'name' in m and 'icons' in m and m.get('start_url'), 'manifest missing required fields'
print('manifest ok:', m['name'])
