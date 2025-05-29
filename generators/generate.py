import yaml
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML, CSS  # ✅ Include CSS

def load_yaml(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def load_all_sections(section_files):
    data = {}
    for key, filepath in section_files.items():
        section_data = load_yaml(filepath)
        data[key] = section_data  # Keep section keys separate
        
    return data

def generate_pdf(data, template_dir='templates', template_file='base.html', output_pdf='output/resume.pdf'):
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template(template_file)   
    html_out = template.render(**data)

    # ✅ Explicitly load the CSS file (adjust path if needed)
    css = CSS('assets/styles/main.css')  # <- make sure this path matches your actual CSS location

    # ✅ Generate PDF with styles
    HTML(string=html_out).write_pdf(output_pdf, stylesheets=[css])
    print(f"PDF generated successfully: {output_pdf}")
    
    
def generate_html(data, template_dir='templates', template_file='base.html', output_html='output/resume.html'):
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template(template_file)
    html_out = template.render(**data)

    with open(output_html, 'w', encoding='utf-8') as f:
        f.write(html_out)

    print(f"HTML generated successfully: {output_html}")