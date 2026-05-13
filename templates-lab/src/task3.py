from jinja2 import Environment, FileSystemLoader

# Interface variables
interface = {
    "description": "Configured by Jinja2",
    "vlan": 10
}

# Load template
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('template-task3.j2')

# Render template
output = template.render(interface=interface)

# Print configuration
print(output:wq
        :)
