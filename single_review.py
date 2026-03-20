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

reviews_track_regex = re.compile(r'<div class="reviews-track" id="reviews-track">.*?(?=<div class="text-center mt-4 fade-in-up")', re.DOTALL)

for filename, name, keywords in service_pages:
    filepath = os.path.join(r'C:\Users\GC Venture\Downloads\_public_html (1)', filename)
    if not os.path.exists(filepath):
        print(f"Skipping {filename}")
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    kw1, kw2 = keywords[0], keywords[1]
    
    single_review_html = f"""<div class="reviews-track" id="reviews-track">
                      <div class="review-card">
                          <div class="review-stars"><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i></div>
                          <p class="review-text">"He gave me one of the best medical experiences I've had. For anyone looking for the {kw1}, Dr. Aloy is the one. I strongly recommend him for {kw2}. The entire process was seamless."</p>
                          <h5 class="review-patient-name">Rajesh Kumar</h5>
                      </div>
                  </div>
              </div>
              """

    new_content = reviews_track_regex.sub(single_review_html, content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

print("done")
