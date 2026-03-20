const fs = require('fs');
const path = require('path');

const servicePages = {
    'achalasia-cardia-treatment.html': { name: 'Achalasia Cardia Treatment', keywords: ['Best Surgeon for Achalasia Cardia Treatment in Delhi', 'Achalasia Cardia Treatment in Delhi'] },
    'adrenal-gland-removal.html': { name: 'Adrenal Gland Removal', keywords: ['Best Surgeon for Adrenal Gland Removal in Delhi', 'Adrenal Gland Removal in Delhi'] },
    'appendix-surgery.html': { name: 'Appendix Surgery', keywords: ['Best Appendix Surgeon in Delhi', 'Appendix Surgery in Delhi'] },
    'colorectal-surgery.html': { name: 'Colorectal Surgery', keywords: ['Best Colorectal Surgeon in Delhi', 'Colorectal Surgery in Delhi'] },
    'bariatric-surgery.html': { name: 'Bariatric Surgery', keywords: ['Best Bariatric Surgeon in Delhi', 'Bariatric Surgery in Delhi'] },
    'endoscopic-anorectal-surgery.html': { name: 'Endoscopic Anorectal Surgery', keywords: ['Best Surgeon for Endoscopic Anorectal Surgery in Delhi', 'Endoscopic Anorectal Surgery in Delhi'] },
    'gallbladder-surgery.html': { name: 'Gallbladder Surgery', keywords: ['Best Gallbladder Surgeon in Delhi', 'Gallbladder Surgery in Delhi'] },
    'gastric-bypass-surgery.html': { name: 'Gastric Bypass Surgery', keywords: ['Best Surgeon for Gastric Bypass Surgery in Delhi', 'Gastric Bypass Surgery in Delhi'] },
    'hernia-surgery.html': { name: 'Hernia Surgery', keywords: ['Best Hernia Surgeon in Delhi', 'Hernia Surgery in Delhi'] },
    'hiatus-hernia.html': { name: 'Hiatus Hernia', keywords: ['Best Surgeon for Hiatus Hernia in Delhi', 'Hiatus Hernia in Delhi'] },
    'laser-piles-treatment.html': { name: 'Laser Piles Treatment', keywords: ['Best Doctor for Laser Piles Treatment in Delhi', 'Laser Piles Treatment in Delhi'] },
    'myasthenia-gravis-surgery.html': { name: 'Myasthenia Gravis Surgery', keywords: ['Best Surgeon for Myasthenia Gravis in Delhi', 'Myasthenia Gravis Surgery in Delhi'] },
    'pilonidal-sinus-treatment.html': { name: 'Pilonidal Sinus Treatment', keywords: ['Best Doctor for Pilonidal Sinus in Delhi', 'Pilonidal Sinus Treatment in Delhi'] },
    'robotic-surgery.html': { name: 'Robotic Surgery', keywords: ['Best Robotic Surgeon in Delhi', 'Robotic Surgery in Delhi'] },
    'test-hernia.html': { name: 'Hernia Surgery', keywords: ['Best Hernia Surgeon in Delhi', 'Hernia Surgery in Delhi'] },
    'thyroid-surgery.html': { name: 'Thyroid Surgery', keywords: ['Best Thyroid Surgeon in Delhi', 'Thyroid Surgery in Delhi'] },
    'varicocelectomy-surgery.html': { name: 'Varicocelectomy Surgery', keywords: ['Best Varicocelectomy Surgeon in Delhi', 'Varicocelectomy Surgery in Delhi'] }
};

const reviewsTrackRegex = /<div class="reviews-track" id="reviews-track">[\s\S]*?(?=<div class="text-center mt-4 fade-in-up")/g;

for (const [filename, data] of Object.entries(servicePages)) {
    const filePath = path.join(__dirname, filename);
    if (!fs.existsSync(filePath)) {
        console.log(`Skipping ${filename}`);
        continue;
    }
    
    let content = fs.readFileSync(filePath, 'utf8');
    const kw1 = data.keywords[0];
    const kw2 = data.keywords[1];
    
    const singleReviewHtml = `<div class="reviews-track" id="reviews-track">
                      <div class="review-card">
                          <div class="review-stars"><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i></div>
                          <p class="review-text">"He gave me one of the best medical experiences I've had. For anyone looking for the ${kw1}, Dr. Aloy is the one. I strongly recommend him for ${kw2}. The entire process was seamless."</p>
                          <h5 class="review-patient-name">Rajesh Kumar</h5>
                      </div>
                  </div>
              </div>
              `;

    content = content.replace(reviewsTrackRegex, singleReviewHtml);

    fs.writeFileSync(filePath, content, 'utf8');
}

console.log('done');
