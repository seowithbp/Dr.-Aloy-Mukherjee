import os
import re

template_file = 'gallbladder-surgery.html'
with open(template_file, 'r', encoding='utf-8') as f:
    content = f.read()

services = [
    ("Hernia Surgery", "hernia-surgery.html", "Hernia"),
    ("Bariatric Surgery", "bariatric-surgery.html", "Bariatric"),
    ("Hiatus Hernia", "hiatus-hernia.html", "Hiatus Hernia"),
    ("Adrenal Gland Removal", "adrenal-gland-removal.html", "Adrenal Gland"),
    ("Myasthenia Gravis Surgery", "myasthenia-gravis-surgery.html", "Myasthenia Gravis"),
    ("Colorectal Surgery", "colorectal-surgery.html", "Colorectal"),
    ("Gastric Bypass Surgery", "gastric-bypass-surgery.html", "Gastric Bypass"),
    ("Pilonidal Sinus Treatment", "pilonidal-sinus-treatment.html", "Pilonidal Sinus"),
    ("Achalasia Cardia Treatment", "achalasia-cardia-treatment.html", "Achalasia Cardia"),
    ("Varicocelectomy Surgery", "varicocelectomy-surgery.html", "Varicocelectomy"),
    ("Laser Piles Treatment", "laser-piles-treatment.html", "Piles"),
    ("Endoscopic Anorectal Surgery", "endoscopic-anorectal-surgery.html", "Anorectal")
]

for service_name, target_file, short_name in services:
    new_content = content
    # Replace URLs and names
    new_content = new_content.replace('gallbladder-surgery.html', target_file)
    new_content = new_content.replace('Gallbladder Stone Surgery', service_name)
    new_content = new_content.replace('Gallbladder Surgery', service_name)
    new_content = new_content.replace('Gallbladder Stone', short_name)
    new_content = new_content.replace('Gallstone', short_name)
    new_content = new_content.replace('Gallbladder', short_name)
    new_content = new_content.replace('gallbladder', short_name.lower())
    new_content = new_content.replace('gallstone', short_name.lower())
    
    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
print("Service pages generated.")

# Extract sections for About and Contact pages from index.html
with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

# Very basic page generation for about and contact to get them started
header_part = index_content.split('<!-- Section 1: Hero Banner -->')[0]
footer_part = '<!-- Footer -->' + index_content.split('<!-- Footer -->')[1]

# about.html
about_section_match = re.search(r'(<!-- Section 2: About Doctor -->.*?)</section>', index_content, re.DOTALL)
about_section = about_section_match.group(1) + '</section>' if about_section_match else "<h2>About Doctor section missing</h2>"

about_html = header_part.replace('<title>Dr. Aloy Mukherjee - Senior Laparoscopic, Bariatric & General Surgeon</title>', '<title>About Dr. Aloy Mukherjee</title>')
about_html += '<main style="padding-top: 100px;">' + about_section + '</main>'
about_html += footer_part
# fix hero active link
about_html = about_html.replace('href="#about" class="nav-link"', 'href="index.html#about" class="nav-link"')

with open('about.html', 'w', encoding='utf-8') as f:
    f.write(about_html)

# contact.html
contact_section_match = re.search(r'(<!-- Section 6: Contact Section -->.*?)<!-- Footer -->', index_content, re.DOTALL)
contact_section = contact_section_match.group(1) if contact_section_match else "<h2>Contact section missing</h2>"

contact_html = header_part.replace('<title>Dr. Aloy Mukherjee - Senior Laparoscopic, Bariatric & General Surgeon</title>', '<title>Contact Dr. Aloy Mukherjee</title>')
contact_html += '<main style="padding-top: 100px;">' + contact_section + '</main>'
contact_html += footer_part

with open('contact.html', 'w', encoding='utf-8') as f:
    f.write(contact_html)

print("About and Contact pages generated.")
