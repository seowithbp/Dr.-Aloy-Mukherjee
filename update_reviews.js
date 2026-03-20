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
    'hiatus-hernia.html': { name: 'Hiatus Hernia', keywords: ['Best Surgeon for Hiatus Hernia in Delhi', 'Hiatus Hernia Treatment in Delhi'] },
    'laser-piles-treatment.html': { name: 'Laser Piles Treatment', keywords: ['Best Doctor for Laser Piles Treatment in Delhi', 'Laser Piles Treatment in Delhi'] },
    'myasthenia-gravis-surgery.html': { name: 'Myasthenia Gravis Surgery', keywords: ['Best Surgeon for Myasthenia Gravis in Delhi', 'Myasthenia Gravis Surgery in Delhi'] },
    'pilonidal-sinus-treatment.html': { name: 'Pilonidal Sinus Treatment', keywords: ['Best Doctor for Pilonidal Sinus in Delhi', 'Pilonidal Sinus Treatment in Delhi'] },
    'robotic-surgery.html': { name: 'Robotic Surgery', keywords: ['Best Robotic Surgeon in Delhi', 'Robotic Surgery in Delhi'] },
    'test-hernia.html': { name: 'Hernia Surgery', keywords: ['Best Hernia Surgeon in Delhi', 'Hernia Surgery in Delhi'] },
    'thyroid-surgery.html': { name: 'Thyroid Surgery', keywords: ['Best Thyroid Surgeon in Delhi', 'Thyroid Surgery in Delhi'] },
    'varicocelectomy-surgery.html': { name: 'Varicocelectomy Surgery', keywords: ['Best Varicocelectomy Surgeon in Delhi', 'Varicocelectomy Surgery in Delhi'] }
};

for (const [filename, data] of Object.entries(servicePages)) {
    const filePath = path.join(__dirname, filename);
    if (!fs.existsSync(filePath)) continue;
    
    let content = fs.readFileSync(filePath, 'utf8');
    
    // We will find the reviews block by regex
    // The reviews block usually looks like:
    // <div class="review-card"> ... <p class="review-text">"He gave me one of the best medical experiences I've had..."</p>
    
    const kw1 = data.keywords[0];
    const kw2 = data.keywords[1];
    
    // We assume there are exactly 4 reviews on most pages. For bariatrics it might be 3 or 4.
    // Let's replace the review-text globally
    
    // Original Review 1
    const rev1Regex = /<p class="review-text">"He gave me one of the best medical experiences I've had[^<]*<\/p>/;
    const rev1Replacement = `<p class="review-text">"He gave me one of the best medical experiences I've had. For anyone looking for the ${kw1}, Dr. Aloy is the one. The staff was supportive and he explained everything in detail."</p>`;
    
    // Original Review 2
    const rev2Regex = /<p class="review-text">"The facility is clean and modern, with advanced tools[^<]*<\/p>/;
    const rev2Replacement = `<p class="review-text">"The facility is clean and modern, with advanced tools. I would strongly recommend Dr. Mukherjee for ${kw2}. The recovery was very fast."</p>`;
    
    // Original Review 3
    const rev3Regex = /<p class="review-text">"Doctor was very patient in explaining everything before the surgery[^<]*<\/p>/;
    const rev3Replacement = `<p class="review-text">"Doctor was very patient in explaining everything before the surgery. The entire process here for ${data.name.toLowerCase()} is seamless and the recovery is much faster than I expected."</p>`;
    
    // Original Review 4
    const rev4Regex = /<p class="review-text">"His 25 years of experience really show[^<]*<\/p>/;
    const rev4Replacement = `<p class="review-text">"His 25 years of experience really show. Very professional and calming demeanor while discussing my operation. If you need a ${"top specialist in Delhi"}, he is extremely helpful."</p>`;

    // For bariatric-surgery, the reviews are different:
    // "My weight has always been a struggle... Dr. Aloy is truly a lifesaver."
    // "The decision to get bariatric surgery was terrifying... best decision."
    // "After years of trying everything... I wish I had done it sooner!"
    const bariatricRev1Regex = /<p class="review-text">"My weight has always been a struggle[^<]*<\/p>/;
    const bariatricRev1Replacement = `<p class="review-text">"My weight has always been a struggle, but finding the ${kw1} changed my life. Dr. Aloy is truly a lifesaver."</p>`;
    
    const bariatricRev2Regex = /<p class="review-text">"The decision to get bariatric surgery was terrifying[^<]*<\/p>/;
    const bariatricRev2Replacement = `<p class="review-text">"The decision to undergo this was terrifying, but getting ${kw2} with Dr. Mukherjee was my best decision ever."</p>`;
    
    const bariatricRev3Regex = /<p class="review-text">"After years of trying everything[^<]*<\/p>/;
    const bariatricRev3Replacement = `<p class="review-text">"After years of trying everything, Dr. Mukherjee's expertise made all the difference. I wish I had done it sooner with the top specialist!"</p>`;

    content = content.replace(rev1Regex, rev1Replacement);
    content = content.replace(rev2Regex, rev2Replacement);
    content = content.replace(rev3Regex, rev3Replacement);
    content = content.replace(rev4Regex, rev4Replacement);

    content = content.replace(bariatricRev1Regex, bariatricRev1Replacement);
    content = content.replace(bariatricRev2Regex, bariatricRev2Replacement);
    content = content.replace(bariatricRev3Regex, bariatricRev3Replacement);

    fs.writeFileSync(filePath, content, 'utf8');
}

console.log('Reviews updated successfully.');
