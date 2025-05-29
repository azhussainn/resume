from generators.generate import generate_pdf, load_all_sections, generate_html

def main():
    section_files = {
        'personal': 'data/sections/personal.yaml',
        'summary': 'data/sections/summary.yaml',
        'experience': 'data/sections/experience.yaml',
        'projects': 'data/sections/projects.yaml',
        'skills': 'data/sections/skills.yaml',
        'education': 'data/sections/education.yaml',
    }

    # Load all sections
    data = load_all_sections(section_files)

    # Generate PDF
    generate_pdf(data)
    generate_html(data)

if __name__ == '__main__':
    main()
    