import os
import re

directories_and_files = [f for f in os.listdir('.') if f.endswith('.html')]

faq_data = {
    'hernia-surgery.html': [
        {"q": "What happens if I delay Hernia treatment?", "a": "An untreated hernia can become strangulated, cutting off blood supply to the trapped tissue, which is a life-threatening medical emergency. Timely surgery is essential."},
        {"q": "How long does recovery take after laparoscopic hernia repair?", "a": "With laparoscopic repair, most patients return to light activities in a few days and fully recover within 2-3 weeks, compared to open surgery which takes much longer."},
        {"q": "Is the use of surgical mesh necessary?", "a": "In most modern hernia repairs, surgical mesh is highly recommended. It reinforces the weakened abdominal wall, significantly reducing the chances of the hernia recurring."},
        {"q": "Can a hernia return after surgery?", "a": "While recurrence is possible, the use of mesh and advanced laparoscopic techniques has reduced the recurrence rate to less than 2% in experienced hands like Dr. Aloy's."},
        {"q": "Will I have a large scar after the procedure?", "a": "No, laparoscopic and robotic hernia surgeries involve only 3-4 tiny keyhole incisions, resulting in minimal scarring that usually fades over time."},
        {"q": "When can I resume heavy lifting or gym workouts?", "a": "Patients are generally advised to wait at least 4 to 6 weeks before engaging in heavy lifting or strenuous athletic activities to allow the muscle wall to heal completely."}
    ],
    'gallbladder-surgery.html': [
        {"q": "Are gallbladder stones dangerous if left untreated?", "a": "Yes, they can slip into the bile duct, causing severe jaundice, pancreatitis, or acute infection. Prompt removal of the gallbladder (cholecystectomy) is the safest approach."},
        {"q": "Will my digestion be affected without a gallbladder?", "a": "The gallbladder stores bile, but your liver will continuously drip bile into the intestines. Most patients experience perfectly normal digestion within a few weeks of surgery."},
        {"q": "What diet should I follow after gallbladder removal?", "a": "In the initial weeks, a low-fat diet is recommended to prevent bloating or diarrhea. Gradually, you can reintroduce normal healthy fats into your diet as your body adapts."},
        {"q": "Why is Laparoscopic Cholecystectomy the standard?", "a": "It offers significantly less pain, a shorter 24-hour hospital stay, minimal scarring, and much faster return to normal activities compared to traditional open surgery."},
        {"q": "Can gallstones be removed without removing the gallbladder?", "a": "No, the medical standard is to remove the diseased gallbladder entirely. Simply removing stones guarantees they will reform because the gallbladder itself is functionally impaired."},
        {"q": "How soon can I return to work?", "a": "Most patients recovering from a laparoscopic gallbladder surgery can comfortably return to office or desk jobs within 5 to 7 days."}
    ],
    'bariatric-surgery.html': [
        {"q": "Who is considered a candidate for Bariatric Surgery?", "a": "Generally, individuals with a BMI over 35 with obesity-related conditions (like diabetes), or a BMI over 40. Dr. Aloy performs a thorough evaluation to determine the optimal approach."},
        {"q": "How much weight will I lose?", "a": "Weight loss varies by the specific procedure (Gastric Bypass vs Sleeve), but patients typically lose 60% to 80% of their excess body weight within the first 12-18 months."},
        {"q": "Does Bariatric Surgery cure Type 2 Diabetes?", "a": "It can lead to long-term remission of Type 2 Diabetes in up to 80% of patients. Many patients are able to stop insulin and oral medications shortly after surgery."},
        {"q": "Is Bariatric Surgery reversible?", "a": "Procedures like Gastric Bypass and Sleeve Gastrectomy are generally considered permanent. They involve restructuring the digestive system to enact lasting metabolic changes."},
        {"q": "Will I need to take vitamins forever?", "a": "Yes, bariatric surgery alters nutrient absorption. You will need to take designated daily bariatric multivitamins and possibly calcium, iron, and B12 for the rest of your life."},
        {"q": "What is the recovery timeline?", "a": "Patients typically spend 2-3 days in the hospital. Most can return to desk jobs in two weeks and resume more vigorous activities within 4-6 weeks."}
    ],
    'appendix-surgery.html': [
        {"q": "What are the early signs of appendicitis?", "a": "Symptoms typically start with dull pain near the navel that shifts to the lower right abdomen, accompanied by fever, nausea, vomiting, and loss of appetite."},
        {"q": "Is a burst appendix dangerous?", "a": "Yes, it is a medical emergency. A ruptured appendix spills infectious materials into the abdominal cavity, causing peritonitis, which can be fatal if not treated immediately."},
        {"q": "Why is Laparoscopic Appendectomy preferred?", "a": "It allows the surgeon to operate through tiny incisions, leading to drastically reduced post-operative pain, lowered infection risk, and faster recovery times."},
        {"q": "Do I need my appendix for anything?", "a": "The appendix has no essential function in adults. Living without it requires no lifestyle or dietary changes, and you will not notice its absence."},
        {"q": "How long will I be in the hospital?", "a": "For a standard, unruptured laparoscopic appendectomy, patients are often discharged within 24 hours of the surgery."},
        {"q": "When can I eat normally again?", "a": "You will start with clear liquids and progress to a normal diet within a couple of days as your bowel function returns to normal."}
    ],
    'thyroid-surgery.html': [
        {"q": "When is thyroid surgery recommended?", "a": "It is typically recommended for thyroid cancer, large goiters causing swallowing or breathing difficulties, or overactive thyroids (hyperthyroidism) that don't respond to medication."},
        {"q": "Will I need to take thyroid medication forever?", "a": "If the entire thyroid is removed (total thyroidectomy), you will need daily thyroid hormone replacement pills for life. If only a portion is removed, you may still produce enough naturally."},
        {"q": "Is there a risk to my vocal cords?", "a": "The nerves controlling your vocal cords run very close to the thyroid. In expert hands like Dr. Aloy's, nerve monitors are often used to minimize this risk to less than 1%."},
        {"q": "Can you do Robotic Thyroid Surgery?", "a": "Yes, select patients are eligible for Robotic/Endoscopic approaches, completely avoiding a visible neck scar by making hidden incisions under the arm or inside the mouth."},
        {"q": "How visible will the scar be if done openly?", "a": "Incisions are made in the natural skin creases of the neck and meticulously closed. They typically fade to a barely noticeable thin line over several months."},
        {"q": "What is the recovery like?", "a": "Patients usually stay overnight. Neck stiffness and a mild sore throat are common for a few days, but most return to normal activities within 1-2 weeks."}
    ],
    'robotic-surgery.html': [
        {"q": "Is the robot doing the surgery on its own?", "a": "No, the surgical robot is never autonomous. Dr. Aloy is in complete control 100% of the time, using the robotic system to translate his hand movements into ultra-precise surgical actions."},
        {"q": "What are the benefits of Robotic Surgery vs Laparoscopic?", "a": "Robotic surgery offers 3D high-definition vision and fully articulated instruments that bend like human wrists. This unparalleled precision is ideal for complex, tight-space operations."},
        {"q": "Is robotic surgery safe?", "a": "Yes, it is extremely safe and FDA-approved. It enhances surgeon precision while maintaining all the benefits of minimally invasive surgery like reduced blood loss and lowered infection rates."},
        {"q": "Which procedures are best suited for the robot?", "a": "It is excellent for complex gastrointestinal surgeries, difficult hernia repairs, colorectal procedures, and intricate solid organ removals like adrenalectomies or thymectomies."},
        {"q": "Will my recovery be faster?", "a": "Robotic surgery often causes even less tissue trauma than standard laparoscopy, which can lead to reduced pain medication requirements and an even swifter discharge from the hospital."},
        {"q": "Is robotic surgery covered by insurance?", "a": "Most major health insurance plans cover robotic-assisted surgery just as they would cover traditional laparoscopic surgery for the same medical indication."}
    ],
    'colorectal-surgery.html': [
        {"q": "What conditions require colorectal surgery?", "a": "It is often necessary for colorectal cancer, severe diverticulitis, inflammatory bowel disease (Crohn's or Ulcerative Colitis), and complex rectal prolapse."},
        {"q": "Will I need a permanent stoma bag?", "a": "The goal is always sphincter-preserving surgery. A stoma is often temporary to allow the bowel to heal. Permanent stomas are rarely necessary, saved only for very low rectal cancers."},
        {"q": "Is bowel prep required before surgery?", "a": "Yes, most colorectal surgeries require a thorough bowel cleansing the day before surgery, similar to a colonoscopy prep, to prevent infection."},
        {"q": "What is the benefit of a laparoscopic approach here?", "a": "Traditional open colon surgery requires a large incision and weeks of recovery. Laparoscopic surgery allows for smaller incisions, significantly faster return of bowel function, and less pain."},
        {"q": "What dietary changes are needed post-surgery?", "a": "You will initially be on a low-residue (low fiber) diet to give your colon time to heal. Gradually, fiber is reintroduced under the guidance of our nutritional team."},
        {"q": "How long is the hospital stay?", "a": "Depending on the complexity of the resection, patients generally stay in the hospital for 3 to 7 days until they can eat solid food and bowel function normalizes."}
    ],
    'endoscopic-anorectal-surgery.html': [
        {"q": "What are the advantages of endoscopic anorectal procedures?", "a": "Techniques like VAAFT or EPSiT view the interior of fistulas or sinus tracts with a tiny camera, allowing the surgeon to destroy the tract from the inside with minimal external cutting."},
        {"q": "Is it less painful than traditional surgery?", "a": "Yes. Because these procedures avoid large, open surgical wounds in sensitive areas, postoperative pain is drastically reduced compared to traditional open excision."},
        {"q": "How soon can I sit comfortably after the procedure?", "a": "Unlike traditional surgery that can make sitting painful for weeks, most patients undergoing endoscopic procedures experience minimal discomfort and can sit and walk normally within days."},
        {"q": "Is there a risk of incontinence?", "a": "Traditional fistula surgeries carry a risk of sphincter muscle damage. Endoscopic sphincter-saving techniques preserve the muscle perfectly, virtually eliminating the risk of incontinence."},
        {"q": "Will the fistula or pilonidal sinus recur?", "a": "Recurrence is a known risk for these diseases, but advanced endoscopic and laser cleanings offer excellent success rates that match or exceed those of traditional, more painful methods."},
        {"q": "Do I need to stay in the hospital?", "a": "These procedures are almost always performed as day-care or overnight stay cases, allowing you to recover comfortably in your own home the very next day."}
    ],
    'gastric-bypass-surgery.html': [
        {"q": "How is Gastric Bypass different from the Sleeve?", "a": "While the Sleeve only restricts stomach size, Bypass restricts size AND reroutes the intestines to reduce calorie absorption, making it highly effective for severe diabetes and reflux."},
        {"q": "What is Dumping Syndrome?", "a": "It occurs when high-sugar or high-fat foods move too quickly into the small intestine, causing nausea and sweating. It effectively acts as a deterrent against unhealthy eating habits."},
        {"q": "How much weight can I expect to lose?", "a": "Patients typically lose 70-80% of their excess body weight within the first 18-24 months after Gastric Bypass, provided they stick to the post-op dietary guidelines."},
        {"q": "Will I need to take supplements?", "a": "Yes, because the intestine is rerouted, you absorb vitamins differently. You will require lifelong supplementation of B12, iron, calcium, and multivitamins to prevent deficiencies."},
        {"q": "Is it a safe procedure?", "a": "When performed laparoscopically by a highly experienced bariatric surgical team, the risk profile is remarkably low, often comparable to routine gallbladder surgery."},
        {"q": "Can I get pregnant after Gastric Bypass?", "a": "Yes, many women experience improved fertility post-surgery. However, it is strongly recommended to wait 18 to 24 months after the procedure before attempting pregnancy."}
    ],
    'myasthenia-gravis-surgery.html': [
        {"q": "Why is the thymus gland removed for Myasthenia Gravis?", "a": "The thymus gland often plays a role in producing the antibodies that disrupt nerve-muscle communication in MG. Removing it can significantly improve or even cure the symptoms."},
        {"q": "What is VATS or Robotic Thymectomy?", "a": "It is a minimally invasive approach using small incisions between the ribs (Video-Assisted Thoracoscopic Surgery) or a surgical robot, completely avoiding the need to split the breastbone (sternotomy)."},
        {"q": "Will surgery cure my Myasthenia Gravis?", "a": "While not a guaranteed cure, over 70% of patients experience significant improvement in symptoms, and a large percentage achieve complete drug-free remission over time."},
        {"q": "How long does it take to see improvements?", "a": "Improvement is not always immediate. It can take several months to a few years for the circulating antibodies to decrease and for the full benefits of the thymectomy to be realized."},
        {"q": "What is the recovery like after a minimally invasive thymectomy?", "a": "Patients usually stay in the hospital for 2 to 3 days and return to light activities in 2 weeks, avoiding the painful sternotomy recovery that takes months."},
        {"q": "Will my regular medications change right away?", "a": "Your neurologist will tightly manage your medications before and after surgery. You will likely continue them initially, tapering off slowly as your symptoms improve."}
    ],
    'varicocelectomy-surgery.html': [
        {"q": "How does a varicocele affect fertility?", "a": "Varicoceles cause blood to pool in the scrotum, raising testicular temperature and damaging sperm production, quality, and motility. Repairing it often restores fertility."},
        {"q": "What is Laparoscopic Varicocelectomy?", "a": "It is a minimally invasive procedure where swollen veins are tied off inside the abdomen using small incisions, restoring proper blood flow and relieving pain smoothly."},
        {"q": "Is it painful?", "a": "Post-operative discomfort is generally very mild. The laparoscopic approach avoids trauma to the groin structures. Most patients only need over-the-counter pain medication for a day or two."},
        {"q": "How long until I can resume sexual activity?", "a": "Most surgeons advise patients to abstain from sexual intercourse and strenuous physical exertion for 2 to 3 weeks following the surgery to allow optimized healing."},
        {"q": "When will my sperm count improve?", "a": "The spermatogenesis cycle takes about 72 days. Therefore, improvements in semen analysis are typically evaluated 3 to 6 months after the surgical procedure."},
        {"q": "Can a varicocele come back?", "a": "Recurrence rates are very low (around 2-5%) when performed by an expert utilizing advanced microscopic or laparoscopic techniques to identify all affected veins."}
    ],
    'achalasia-cardia-treatment.html': [
        {"q": "What is Heller Myotomy?", "a": "It is the gold standard surgical treatment for Achalasia. The surgeon cuts the tight muscle fibers at the lower esophageal sphincter, allowing food and liquids to pass into the stomach easily."},
        {"q": "How is it performed?", "a": "Dr. Aloy performs this laparoscopically or robotically, requiring only small keyhole incisions. A partial fundoplication is often added to prevent post-surgery acid reflux."},
        {"q": "What is the success rate?", "a": "Laparoscopic Heller Myotomy has an extraordinarily high success rate, providing long-term relief from swallowing difficulties in over 90% of patients."},
        {"q": "What is the recovery time?", "a": "Patients typically spend one to two nights in the hospital. You will be on a liquid or soft diet initially, but most can return to work within 1 to 2 weeks."},
        {"q": "Is there an alternative to surgery?", "a": "Botox injections or pneumatic dilation are options, but they are temporary fixes with higher recurrence rates. Surgery offers the best definitive, durable chemical-free cure."},
        {"q": "Will I experience acid reflux afterwards?", "a": "By combining the Heller myotomy with a partial wrap of the stomach (Dor or Toupet fundoplication), the risk of developing severe postoperative acid reflux is minimized."}
    ],
    'adrenal-gland-removal.html': [
        {"q": "Why would I need an adrenal gland removed?", "a": "Adrenalectomy is required for tumors (benign or cancerous) that are either growing too large or overproducing hormones, causing conditions like Cushing's or Conn's syndrome."},
        {"q": "Can it be done laparoscopically?", "a": "Yes, the vast majority of adrenalectomies are now performed via laparoscopy or robotics, offering small incisions, less pain, and significantly quicker recoveries than open surgery."},
        {"q": "Will I need to take hormones after surgery?", "a": "You have two adrenal glands. If only one is removed, the other usually compensates perfectly. If both are removed, you will require lifelong hormone replacement therapy."},
        {"q": "How long is the hospital stay?", "a": "A minimally invasive adrenalectomy typically requires a short hospital stay of 1 to 2 days, depending on your hormone levels and post-operative blood pressure stability."},
        {"q": "What are the risks of the surgery?", "a": "While safe in expert hands, risks include bleeding, changes in blood pressure during the operation, and adjacent organ injury, making an experienced minimally invasive surgeon essential."},
        {"q": "When can I return to normal activities?", "a": "Most patients feel quite well within a week and can safely return to work and light daily activities within 2 weeks of the laparoscopic procedure."}
    ],
    'hiatus-hernia.html': [
        {"q": "How is a hiatus hernia related to GERD?", "a": "A hiatus hernia allows the upper part of the stomach to push through the diaphragm into the chest, weakening the valve and allowing stomach acid to easily reflux into the esophagus."},
        {"q": "When does a hiatus hernia require surgery?", "a": "Surgery is recommended for massive hernias, when parts of the stomach are twisting, or for patients with severe acid reflux that cannot be managed effectively with medications."},
        {"q": "What is a Laparoscopic Fundoplication?", "a": "It is the standard surgical repair where the hernia is pulled back into the abdomen, the diaphragm is tightened, and the top of the stomach is wrapped around the esophagus to recreate a strong valve."},
        {"q": "What is the recovery like?", "a": "It involves a 1-day hospital stay. The most crucial part of recovery is adhering to a strict, gradual diet (liquids to purees to soft foods) for 3-4 weeks to allow swelling to reside."},
        {"q": "Will I be able to burp or vomit after surgery?", "a": "Initially, the wrap may be tight, making belching or vomiting difficult. This typically relaxes over a few months, allowing for normal function while preventing acid reflux."},
        {"q": "How successful is the surgery?", "a": "Laparoscopic repair provides excellent, permanent relief from heart-burn and regurgitation in over 90% of patients, completely eliminating their need for daily antacid medications."}
    ],
    'laser-piles-treatment.html': [
        {"q": "What is Laser Hemorrhoidoplasty (LHP)?", "a": "LHP is an advanced, minimally invasive technique where a laser fiber is used to shrink and seal the hemorrhoidal tissue from the inside, naturally reducing the piles without cutting."},
        {"q": "Is laser treatment painful?", "a": "Compared to traditional open piles surgery, laser treatment causes dramatically less pain because there are no large surgical wounds, cuts, or stitches in the highly sensitive anal area."},
        {"q": "How fast is the recovery?", "a": "It is typically a day-care procedure. Patients are discharged the same day and can generally resume their normal office routines within 2 to 3 days."},
        {"q": "Is there a risk of incontinence?", "a": "Laser treatment is remarkably safe. Because it does not involve cutting the sphincter muscle tissue, the risk of fecal incontinence is virtually zero."},
        {"q": "Can the piles come back?", "a": "The laser effectively destroys the problematic blood vessels, keeping recurrence rates very low. Maintaining a high-fiber diet and hydration ensures they do not return."},
        {"q": "What dietary changes do I need to make?", "a": "A high-fiber diet with plenty of water intake is essential post-surgery to ensure soft bowel movements, which prevents straining and aids in a smooth healing process."}
    ],
    'pilonidal-sinus-treatment.html': [
        {"q": "What causes a Pilonidal Sinus?", "a": "It is typically caused by a combination of loose hair puncturing the skin in the cleft of the buttocks, friction, and pressure, leading to chronic infection and sinus tract formation."},
        {"q": "How is the laser treatment (EPSiT/Laser) different?", "a": "Traditional surgery cuts out a large chunk of tissue, leaving a huge wound that takes months to heal. Laser therapy cleans the sinus and seals it with heat via tiny pinholes."},
        {"q": "How long does it take to heal after laser surgery?", "a": "Healing is substantially faster. Most patients can return to work and sit comfortably within just a few days, compared to weeks of painful dressing changes with open surgery."},
        {"q": "Will it recur?", "a": "Recurrence is a challenge with this disease. However, advanced laser cleaning offers high success rates. Maintaining strict local hygiene and permanent hair removal prevents it from coming back."},
        {"q": "Do I need complex wound dressings every day?", "a": "No, this is the primary benefit of the minimally invasive approach. There is typically no large open wound, thus avoiding the painful, daily, messy gauze packings altogether."},
        {"q": "Is the laser procedure painful?", "a": "It is performed under anesthesia, and the post-operative discomfort is exceptionally mild, requiring only basic oral painkillers for a day or two."}
    ]
}

# Generic FAQ for location pages or other generic laparoscopic surgery pages
generic_lap_faqs = [
    {"q": "What is Laparoscopic Surgery?", "a": "Laparoscopic surgery, or minimally invasive surgery, utilizes a specialized camera and tiny instruments inserted through small (0.5 - 1 cm) incisions to perform operations, avoiding large traditional cuts."},
    {"q": "What are the benefits over open surgery?", "a": "The benefits are profound: significantly less post-operative pain, microscopic scarring, lower risk of wound infections, and a dramatically faster return to work and daily activities."},
    {"q": "Is laparoscopic surgery safe?", "a": "Yes, it is the worldwide gold standard for abdominal surgeries. In the hands of a highly experienced surgeon like Dr. Aloy, it is actually safer and involves less blood loss than open surgery."},
    {"q": "How long will I be in the hospital?", "a": "Most laparoscopic procedures, including gallbladder, hernia, and appendix surgeries, are performed as day-care or overnight procedures, meaning you go home within 24 hours."},
    {"q": "Will I have prominent scars?", "a": "No. The tiny keyhole incisions typically heal very cleanly. With proper care, they fade into faint, barely noticeable lines within a few months."},
    {"q": "Are there limitations to physical activity post-surgery?", "a": "While you will be walking the very same day, strenuous exercise and heavy lifting are usually restricted for 3 to 6 weeks to ensure the internal muscle layers heal correctly."}
    ]

# Populate the location pages with the generic faqs
directories = os.listdir('.')
for file in directories:
    if file.startswith('laparoscopic-surgeon') and file.endswith('.html'):
        faq_data[file] = generic_lap_faqs

updated_count = 0

for filename, faqs in faq_data.items():
    if not os.path.exists(filename):
        continue
    
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # We need to find the <section id="faq" class="faq section"> block and replace it.
    # We will use regex to find it.
    pattern = r'<section id="faq" class="faq section">.*?</section>'
    
    faq_html_items = ""
    for faq in faqs:
        faq_html_items += f'''                  <div class="faq-item">
                      <div class="faq-question"><h4>{faq["q"]}</h4><span class="faq-toggle"><i class="fas fa-plus"></i></span></div>
                      <div class="faq-answer"><p>{faq["a"]}</p></div>
                  </div>\n'''
                  
    new_faq_section = f'''<section id="faq" class="faq section">
          <div class="container">
              <div class="section-header text-center fade-in-up"><h2 class="section-title">Frequently Asked <span>Questions</span></h2></div>
              <div class="faq-container fade-in-up">
{faq_html_items}              </div>
          </div>
      </section>'''
      
    new_content = re.sub(pattern, new_faq_section, content, flags=re.DOTALL)
    
    if new_content != content:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        updated_count += 1
        
print(f"Updated {updated_count} files with new specific FAQs.")
