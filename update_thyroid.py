import sys

with open('thyroid-surgery.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Meta updates
html = html.replace('<title>Thyroid Surgery in Delhi | Dr. Aloy Mukherjee</title>', '<title>Thyroid Surgery in Delhi | Dr. Aloy Mukherjee</title>\n    <meta name="description" content="Seeking expert thyroid surgery in Delhi? Dr. Aloy Mukherjee offers advanced treatment, precise care, and faster recovery for safe and effective thyroid management." />\n    <link rel="canonical" href="https://aloymukherjee.com/thyroid-surgery.html" />')
# Need to remove the old meta description
html = html.replace('<meta name="description" content="Expert thyroid surgery in Delhi by Dr. Aloy Mukherjee. Advanced minimally invasive treatment for goiter, thyroid nodules, and thyroid cancer." />\n    ', '')

# Understanding thyroid
old_understanding = """                      <h2 style="font-size: 2.8rem; font-weight: 800; color: #1a1a1a; margin-bottom: 25px;">Understanding Thyroid Disorders</h2>
                      <p style="font-size: 1.1rem; color: #444; line-height: 1.7; margin-bottom: 20px;">Thyroid surgery (thyroidectomy) involves removing all or part of the thyroid gland located in your neck.</p>
                      <p style="font-size: 1.1rem; color: #444; line-height: 1.7;">It is commonly performed to treat thyroid cancer, noncancerous enlargement of the thyroid (goiter), or overactive thyroid (hyperthyroidism) that has not responded to medication.</p>
                  </div>
                  <div style="flex: 1; min-width: 300px;" class="fade-in-right">
                      <img src="https://images.unsplash.com/photo-1582719508461-905c673771fd?auto=format&fit=crop&w=800&q=80" alt="Understanding Thyroid Disorders" style="width: 100%; border-radius: 12px; box-shadow: 0 10px 30px rgba(0,0,0,0.15);" />"""

new_understanding = """                      <h2 style="font-size: 2.8rem; font-weight: 800; color: #1a1a1a; margin-bottom: 25px;">Understanding Thyroid Surgery</h2>
                      <p style="font-size: 1.1rem; color: #444; line-height: 1.7; margin-bottom: 20px;">Thyroid surgery is a procedure performed to treat disorders of the thyroid gland, such as thyroid nodules, goiter, hyperthyroidism, or thyroid cancer. The thyroid is a small gland located in the neck that plays a crucial role in regulating metabolism and hormone levels. When medications are not effective, surgery may be recommended to remove part or all of the thyroid gland. Consulting a thyroid specialist in delhi is essential for accurate diagnosis and proper treatment planning.</p>
                      <p style="font-size: 1.1rem; color: #444; line-height: 1.7;">With advancements in surgical techniques, thyroid procedures are now safer and more precise. Minimally invasive and advanced approaches help reduce complications, scarring, and recovery time. Patients seeking care from the best thyroid surgeon in delhi benefit from expert treatment, improved outcomes, and faster healing, ensuring better overall health.</p>
                  </div>
                  <div style="flex: 1; min-width: 300px;" class="fade-in-right">
                      <img src="assets/thyroid-img.jpg" alt="Understanding Thyroid Surgery" style="width: 100%; border-radius: 12px; box-shadow: 0 10px 30px rgba(0,0,0,0.15);" />"""
html = html.replace(old_understanding, new_understanding)

# Causes
old_causes = """                  <h2 style="font-size: 2.5rem; color: #1a1a1a; margin-bottom: 20px;">Common Causes & Risk Factors</h2>
                  <p style="font-size: 1.1rem; color: #666; max-width: 800px; margin: 0 auto;">Several factors contribute to this condition. Understanding these risks can aid in prevention and management.</p>
              </div>
              <div class="causes-grid">
                  <div class="cause-card">
                      <h4>Iodine Deficiency</h4>
                      <p>Globally, a lack of dietary iodine is a major cause of thyroid enlargement, known as a goiter.</p>
                  </div>
                  <div class="cause-card">
                      <h4>Autoimmune Disease</h4>
                      <p>Conditions like Hashimoto's or Graves' disease prompt the immune system to attack the thyroid.</p>
                  </div>
                  <div class="cause-card">
                      <h4>Radiation Exposure</h4>
                      <p>Prior intense radiation treatments to the head and neck significantly increase the risk of thyroid tumors.</p>
                  </div>
                  <div class="cause-card">
                      <h4>Genetics</h4>
                      <p>A strong family history of thyroid cancers or endocrine disorders elevates personal risk.</p>
                  </div>
              </div>"""

new_causes = """                  <h2 style="font-size: 2.5rem; color: #1a1a1a; margin-bottom: 20px;">Common Causes & Risk Factors</h2>
              </div>
              <div class="causes-grid">
                  <div class="cause-card">
                      <h4>1. Thyroid Nodules</h4>
                      <p>Abnormal growths in the thyroid gland can lead to discomfort and may require surgical removal if they are large or suspicious.</p>
                  </div>
                  <div class="cause-card">
                      <h4>2. Hyperthyroidism</h4>
                      <p>Overactive thyroid conditions that do not respond to medication may require surgery for effective management.</p>
                  </div>
                  <div class="cause-card">
                      <h4>3. Thyroid Cancer</h4>
                      <p>Cancerous growth in the thyroid gland is a major reason for recommending thyroid surgery.</p>
                  </div>
                  <div class="cause-card">
                      <h4>4. Goiter (Enlarged Thyroid)</h4>
                      <p>An enlarged thyroid can cause difficulty in breathing or swallowing, making surgery necessary.</p>
                  </div>
              </div>"""
html = html.replace(old_causes, new_causes)

# Symptoms
old_symptoms = """              <div class="symptoms-grid">
                  <div class="symptom-card text-left"><div class="symptom-icon-box"><i class="fas fa-exclamation-circle"></i></div><h4>Neck Swelling</h4><p>A visible lump or generalized swelling in the lower front of your neck.</p></div>
                  <div class="symptom-card text-left"><div class="symptom-icon-box"><i class="fas fa-exclamation-triangle"></i></div><h4>Swallowing Difficulty</h4><p>A feeling of a lump in your throat making swallowing difficult or uncomfortable.</p></div>
                  <div class="symptom-card text-left"><div class="symptom-icon-box"><i class="fas fa-notes-medical"></i></div><h4>Voice Changes</h4><p>Unexplained hoarseness or changes in your voice quality.</p></div>
                  <div class="symptom-card text-left"><div class="symptom-icon-box"><i class="fas fa-procedures"></i></div><h4>Breathing Problems</h4><p>A sensation of restricted breathing, especially when lying flat.</p></div>
              </div>"""

new_symptoms = """              <div class="symptoms-grid">
                  <div class="symptom-card text-left"><div class="symptom-icon-box"><i class="fas fa-exclamation-circle"></i></div><h4>1. Swelling in the Neck</h4><p>A visible lump or swelling in the neck is a common sign of thyroid issues.</p></div>
                  <div class="symptom-card text-left"><div class="symptom-icon-box"><i class="fas fa-exclamation-triangle"></i></div><h4>2. Difficulty in Swallowing or Breathing</h4><p>An enlarged thyroid may press on nearby structures, causing discomfort.</p></div>
                  <div class="symptom-card text-left"><div class="symptom-icon-box"><i class="fas fa-notes-medical"></i></div><h4>3. Hormonal Imbalance Symptoms</h4><p>Weight changes, fatigue, anxiety, or irregular heartbeat may indicate thyroid dysfunction.</p></div>
                  <div class="symptom-card text-left"><div class="symptom-icon-box"><i class="fas fa-procedures"></i></div><h4>4. Voice Changes</h4><p>Hoarseness or changes in voice can occur if the thyroid affects nearby nerves.</p></div>
              </div>"""
html = html.replace(old_symptoms, new_symptoms)

# Diagnosis
old_diagnosis = """              <p style="max-width: 800px; margin: 0 auto 40px; font-size: 1.1rem;">To definitively diagnose Thyroid Disorders and rule out other causes, our clinic utilizes comprehensive testing.</p>
              <div class="grid-3">
                  <div class="info-box"><i class="fas fa-user-md" style="font-size: 3rem; color: var(--secondary-teal); margin-bottom: 20px;"></i><h4>Physical Examination</h4><p>A gentle palpation of the neck to examine the size, shape, and firmness of the thyroid gland.</p></div>
                  <div class="info-box"><i class="fas fa-wave-square" style="font-size: 3rem; color: var(--secondary-teal); margin-bottom: 20px;"></i><h4>Imaging Tests</h4><p>A high-resolution thyroid ultrasound is crucial to identify nodule characteristics and exact location.</p></div>
                  <div class="info-box"><i class="fas fa-vial" style="font-size: 3rem; color: var(--secondary-teal); margin-bottom: 20px;"></i><h4>Laboratory Analysis</h4><p>Fine Needle Aspiration (FNA) biopsy to determine if the abnormal cells are benign or malignant.</p></div>
              </div>"""

new_diagnosis = """              <div class="grid-3" style="margin-top: 40px;">
                  <div class="info-box"><i class="fas fa-user-md" style="font-size: 3rem; color: var(--secondary-teal); margin-bottom: 20px;"></i><h4>1. Physical Examination</h4><p>The doctor examines the neck for swelling or lumps in the thyroid region.</p></div>
                  <div class="info-box"><i class="fas fa-wave-square" style="font-size: 3rem; color: var(--secondary-teal); margin-bottom: 20px;"></i><h4>2. Blood Tests</h4><p>Thyroid function tests help assess hormone levels and detect abnormalities.</p></div>
                  <div class="info-box"><i class="fas fa-vial" style="font-size: 3rem; color: var(--secondary-teal); margin-bottom: 20px;"></i><h4>3. Imaging and Biopsy</h4><p>Ultrasound and fine-needle aspiration biopsy are used to evaluate nodules and confirm diagnosis.</p></div>
              </div>"""
html = html.replace(old_diagnosis, new_diagnosis)

# Treatments
old_treatments = """              <div class="advanced-treatments-grid fade-in-up">
                  <div class="treatment-item"><div class="treatment-icon blue"><i class="fas fa-laptop-medical"></i></div><div class="treatment-content"><h4>Total Thyroidectomy</h4><p>Complete removal of the thyroid gland, typically performed for cancer or severe hyperthyroidism.</p></div></div>
                  <div class="treatment-item"><div class="treatment-icon teal"><i class="fas fa-procedures"></i></div><div class="treatment-content"><h4>Hemithyroidectomy</h4><p>Removal of one lobe of the thyroid, often used for isolated benign nodules.</p></div></div>
              </div>"""

new_treatments = """              <div class="advanced-treatments-grid fade-in-up">
                  <div class="treatment-item"><div class="treatment-icon blue"><i class="fas fa-laptop-medical"></i></div><div class="treatment-content"><h4>1. Partial Thyroidectomy</h4><p>Removal of a portion of the thyroid gland, usually recommended for localized nodules or small growths.</p></div></div>
                  <div class="treatment-item"><div class="treatment-icon teal"><i class="fas fa-procedures"></i></div><div class="treatment-content"><h4>2. Total Thyroidectomy</h4><p>Complete removal of the thyroid gland, often required in cases of cancer or severe thyroid disease.</p></div></div>
              </div>"""
html = html.replace(old_treatments, new_treatments)

# About Doctor
old_about = """            <h2 class="section-title">Why Dr. Aloy Mukherjee is the Best <span>Thyroid Surgeon</span> in Delhi?</h2>
            <p class="about-bio">Dr. Aloy Mukherjee is an internationally renowned Senior Consultant Surgeon with an exceptional track record of over 25 years. Specializing in Advanced Minimal Access Surgery, he is a pioneer in Laparoscopic, Bariatric, and Gastrointestinal procedures in India.</p>
            <p class="about-bio" style="margin-top: 15px;">His comprehensive approach integrates multidisciplinary expertise to ensure the best possible outcomes, prioritizing rapid recovery and minimal discomfort for every patient.</p>"""

new_about = """            <h2 class="section-title">Why Choose Dr. Aloy Mukherjee for <span>Thyroid Surgery?</span></h2>
            <p class="about-bio">Dr. Aloy Mukherjee is a highly experienced thyroid doctor in delhi known for providing advanced and effective thyroid treatments. His expertise in minimally invasive techniques ensures safe procedures with minimal discomfort and faster recovery. Patients trust his approach for accurate diagnosis and successful outcomes, making him a preferred thyroid specialist in delhi.</p>
            <p class="about-bio" style="margin-top: 15px;">His commitment to personalized care, use of modern technology, and focus on patient safety set him apart. Dr. Mukherjee carefully evaluates each case and offers the most suitable treatment plan. Recognized as the best thyroid surgeon in delhi, he delivers excellent results with high patient satisfaction.</p>"""
html = html.replace(old_about, new_about)

# FAQs
old_faqs = """              <div class="faq-container fade-in-up">
                  <div class="faq-item">
                      <div class="faq-question"><h4>When is thyroid surgery recommended?</h4><span class="faq-toggle"><i class="fas fa-plus"></i></span></div>
                      <div class="faq-answer"><p>It is typically recommended for thyroid cancer, large goiters causing swallowing or breathing difficulties, or overactive thyroids (hyperthyroidism) that don't respond to medication.</p></div>
                  </div>                  <div class="faq-item">
                      <div class="faq-question"><h4>Will I need to take thyroid medication forever?</h4><span class="faq-toggle"><i class="fas fa-plus"></i></span></div>
                      <div class="faq-answer"><p>If the entire thyroid is removed (total thyroidectomy), you will need daily thyroid hormone replacement pills for life. If only a portion is removed, you may still produce enough naturally.</p></div>
                  </div>                  <div class="faq-item">
                      <div class="faq-question"><h4>Is there a risk to my vocal cords?</h4><span class="faq-toggle"><i class="fas fa-plus"></i></span></div>
                      <div class="faq-answer"><p>The nerves controlling your vocal cords run very close to the thyroid. In expert hands like Dr. Aloy's, nerve monitors are often used to minimize this risk to less than 1%.</p></div>
                  </div>                  <div class="faq-item">
                      <div class="faq-question"><h4>Can you do Robotic Thyroid Surgery?</h4><span class="faq-toggle"><i class="fas fa-plus"></i></span></div>
                      <div class="faq-answer"><p>Yes, select patients are eligible for Robotic/Endoscopic approaches, completely avoiding a visible neck scar by making hidden incisions under the arm or inside the mouth.</p></div>
                  </div>                  <div class="faq-item">
                      <div class="faq-question"><h4>How visible will the scar be if done openly?</h4><span class="faq-toggle"><i class="fas fa-plus"></i></span></div>
                      <div class="faq-answer"><p>Incisions are made in the natural skin creases of the neck and meticulously closed. They typically fade to a barely noticeable thin line over several months.</p></div>
                  </div>                  <div class="faq-item">
                      <div class="faq-question"><h4>What is the recovery like?</h4><span class="faq-toggle"><i class="fas fa-plus"></i></span></div>
                      <div class="faq-answer"><p>Patients usually stay overnight. Neck stiffness and a mild sore throat are common for a few days, but most return to normal activities within 1-2 weeks.</p></div>
                  </div>
              </div>"""

new_faqs = """              <div class="faq-container fade-in-up">
                  <div class="faq-item">
                      <div class="faq-question"><h4>1. What is thyroid surgery?</h4><span class="faq-toggle"><i class="fas fa-plus"></i></span></div>
                      <div class="faq-answer"><p>Thyroid surgery involves removing part or all of the thyroid gland to treat conditions like nodules, goiter, or cancer.</p></div>
                  </div>
                  <div class="faq-item">
                      <div class="faq-question"><h4>2. Is thyroid surgery safe?</h4><span class="faq-toggle"><i class="fas fa-plus"></i></span></div>
                      <div class="faq-answer"><p>Yes, it is a safe procedure when performed by an experienced thyroid specialist in delhi using advanced techniques.</p></div>
                  </div>
                  <div class="faq-item">
                      <div class="faq-question"><h4>3. When is thyroid surgery required?</h4><span class="faq-toggle"><i class="fas fa-plus"></i></span></div>
                      <div class="faq-answer"><p>Surgery is recommended when medications are not effective or in cases of large nodules, cancer, or severe thyroid disorders.</p></div>
                  </div>
                  <div class="faq-item">
                      <div class="faq-question"><h4>4. How long does recovery take?</h4><span class="faq-toggle"><i class="fas fa-plus"></i></span></div>
                      <div class="faq-answer"><p>Most patients recover within a few weeks, depending on the type of surgery and overall health.</p></div>
                  </div>
                  <div class="faq-item">
                      <div class="faq-question"><h4>5. Who is the best doctor for thyroid surgery in Delhi?</h4><span class="faq-toggle"><i class="fas fa-plus"></i></span></div>
                      <div class="faq-answer"><p>Dr. Aloy Mukherjee is considered the best thyroid surgeon in delhi, known for his expertise and successful outcomes.</p></div>
                  </div>
                  <div class="faq-item">
                      <div class="faq-question"><h4>6. Will I need lifelong medication after surgery?</h4><span class="faq-toggle"><i class="fas fa-plus"></i></span></div>
                      <div class="faq-answer"><p>In some cases, especially after total thyroidectomy, patients may require thyroid hormone replacement therapy.</p></div>
                  </div>
              </div>"""
html = html.replace(old_faqs, new_faqs)

with open('thyroid-surgery.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Done!")
