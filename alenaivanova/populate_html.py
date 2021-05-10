import os
import glob
from jinja2 import Environment, FileSystemLoader
import requests as req
import json

# Create the jinja2 environment.
current_directory = os.path.dirname(os.path.abspath(__file__))
env = Environment(loader=FileSystemLoader(current_directory))

# Find all files with the j2 extension in the current directory
templates = glob.glob('file.html')

response = req.get("https://eddbapi.kodeblox.com/api/v4/systems?name=sirius")
loaded_json = json.loads(response.text)
info = loaded_json['docs'][0]

id = str(info['id'])
name = info['name']
faction_id = str(info['controlling_minor_faction_id'])
power_state = info['power_state']
ed_system_address = info['ed_system_address']
security = info['security']
allegiance = info['allegiance']
government = info['government']
primary_economy = info['primary_economy']
is_populated = info['is_populated']
population = info['population']


def render_template(filename):
    return env.get_template(filename).render(
        id=id,
        name=name,
        faction_id=faction_id,
        power_state=power_state,
        ed_system_address=ed_system_address,
        security=security,
        allegiance=allegiance,
        government=government,
        primary_economy=primary_economy,
        is_populated=is_populated,
        population=population
    )

for f in templates:
    rendered_string = render_template(f)
    print(rendered_string)
    open("output.html", "w").write(rendered_string)