import yaml
from jinja2 import Environment, FileSystemLoader
import os

# Load YAML data
with open('data/portfolio.yaml', 'r', encoding='utf-8') as file:
    profile = yaml.safe_load(file)

# Load Jinja2 template
env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('portfolio_template.html')

# Render template with data
output = template.render(profile)

# Write output to file
os.makedirs('output', exist_ok=True)
with open('output/index.html', 'w', encoding='utf-8') as f:
    f.write(output)

print("Profile generated successfully: output/index.html")