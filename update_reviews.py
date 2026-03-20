import os
import re

service_pages = [
    ('achalasia-cardia-treatment.html', 'Achalasia Cardia Treatment', ['Best Surgeon for Achalasia Cardia Treatment in Delhi', 'Achalasia Cardia Treatment in Delhi']),
    ('adrenal-gland-removal.html', 'Adrenal Gland Removal', ['Best Surgeon for Adrenal Gland Removal in Delhi', 'Adrenal Gland Removal in Delhi']),
    ('appendix-surgery.html', 'Appendix Surgery', ['Best Appendix Surgeon in Delhi', 'Appendix Surgery in Delhi']),
    ('colorectal-surgery.html', 'Colorectal Surgery', ['Best Colorectal Surgeon in Delhi', 'Colorectal Surgery in Delhi']),
    ('bariatric-surgery.html', 'Bariatric Surgery', ['Best Bariatric Surgeon in Delhi', 'Bariatric Surgery in Delhi']),
    ('endoscopic-anorectal-surgery.html', 'Endoscopic Anorectal Surgery', ['Best Surgeon for Endoscopic Anorectal Surgery in Delhi', 'Endoscopic Anorectal Surgery in Delhi']),
    ('gallbladder-surgery.html', 'Gallbladder Surgery', ['Best Gallbladder Surgeon in Delhi', 'Gallbladder Surgery in Delhi']),
    ('gastric-bypass-surgery.html', 'Gastric Bypass Surgery', ['Best Surgeon for Gastric Bypass Surgery in Delhi', 'Gastric Bypass Surgery in Delhi']),
    ('hernia-surgery.html', 'Hernia Surgery', ['Best Hernia Surgeon in Delhi', 'Hernia Surgery in Delhi']),
    ('hiatus-hernia.html', 'Hiatus Hernia', ['Best Surgeon for Hiatus Hernia in Delhi', 'Hiatus Hernia in Delhi']),
    ('laser-piles-treatment.html', 'Laser Piles Treatment', ['Best Doctor for Laser Piles Treatment in Delhi', 'Laser Piles Treatment in Delhi']),
    ('myasthenia-gravis-surgery.html', 'Myasthenia Gravis Surgery', ['Best Surgeon for Myasthenia Gravis in Delhi', 'Myasthenia Gravis Surgery in Delhi']),
    ('pilonidal-sinus-treatment.html', 'Pilonidal Sinus Treatment', ['Best Doctor for Pilonidal Sinus in Delhi', 'Pilonidal Sinus Treatment in Delhi']),
    ('robotic-surgery.html', 'Robotic Surgery', ['Best Robotic Surgeon in Delhi', 'Robotic Surgery in Delhi']),
    ('test-hernia.html', 'Hernia Surgery', ['Best Hernia Surgeon in Delhi', 'Hernia Surgery in Delhi']),
    ('thyroid-surgery.html', 'Thyroid Surgery', ['Best Thyroid Surgeon in Delhi', 'Thyroid Surgery in Delhi']),
    ('varicocelectomy-surgery.html', 'Varicocelectomy Surgery', ['Best Varicocelectomy Surgeon in Delhi', 'Varicocelectomy Surgery in Delhi'])
]

# For non-bariatric standard reviews:
rev1_regex = re.compile(r'<p class="review-text">"He gave me one of the best medical experiences I\'ve had[^<]*</p>')
rev2_regex = re.compile(r'<p class="review-text">"The facility is clean and modern, with advanced tools[^<]*</p>')
rev3_regex = re.compile(r'<p class="review-text">"Doctor was very patient in explaining everything before the surgery[^<]*</p>')
rev4_regex = re.compile(r'<p class="review-text">"His 25 years of experience really show[^<]*</p>')

# Bariatric specific
bar1_regex = re.compile(r'<p class="review-text">"My weight has always been a struggle[^<]*</p>')
bar2_regex = re.compile(r'<p class="review-text">"The decision to get bariatric surgery was terrifying[^<]*</p>')
bar3_regex = re.compile(r'<p class="review-text">"After years of trying everything[^<]*</p>')

for filename, name, keywords in service_pages:
    filepath = os.path.join(os.getcwd(), filename)
    if not os.path.exists(filepath):
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    kw1, kw2 = keywords[0], keywords[1]
    
    # Non-bariatric strings
    rev1_repl = f'<p class="review-text">"He gave me one of the best medical experiences I\'ve had. For anyone looking for the {kw1}, Dr. Aloy is the one. The staff was supportive and he explained everything in detail."</p>'
    rev2_repl = f'<p class="review-text">"The facility is clean and modern, with advanced tools. I would strongly recommend Dr. Mukherjee for {kw2}. The recovery was very fast."</p>'
    rev3_repl = f'<p class="review-text">"Doctor was very patient in explaining everything before the surgery. The entire process here for {name.lower()} is seamless and the recovery is much faster than I expected."</p>'
    rev4_repl = f'<p class="review-text">"His 25 years of experience really show. Very professional and calming demeanor while discussing my operation. If you need a top specialist in Delhi, he is extremely helpful."</p>'

    content = rev1_regex.sub(rev1_repl, content)
    content = rev2_regex.sub(rev2_repl, content)
    content = rev3_regex.sub(rev3_repl, content)
    content = rev4_regex.sub(rev4_repl, content)

    # Bariatric strings
    if filename == 'bariatric-surgery.html':
        bar1_repl = f'<p class="review-text">"My weight has always been a struggle, but finding the {kw1} changed my life. Dr. Aloy is truly a lifesaver."</p>'
        bar2_repl = f'<p class="review-text">"The decision to undergo this was terrifying, but getting {kw2} with Dr. Mukherjee was my best decision ever."</p>'
        bar3_repl = f'<p class="review-text">"After years of trying everything, Dr. Mukherjee\'s expertise made all the difference. I wish I had done it sooner with the top specialist!"</p>'
        
        content = bar1_regex.sub(bar1_repl, content)
        content = bar2_regex.sub(bar2_repl, content)
        content = bar3_regex.sub(bar3_repl, content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("done")
