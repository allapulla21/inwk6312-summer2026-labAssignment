from jinja2 import Environment, FileSystemLoader

# Interface variables
interface = {
    "description": "Configured by Jinja2",
    "vlan": 10
}

# Load the Jinja2 template
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('template-task4.j2')

# Render the template with variables
output = template.render(interface=interface)

# Print the generated configuration
print(output)
