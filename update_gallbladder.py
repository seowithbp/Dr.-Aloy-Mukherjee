import sys

def main():
    file_path = 'gallbladder-surgery.html'
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. META
    old_meta = '''    <title>Gallbladder Stone Surgery in Delhi | Dr. Aloy Mukherjee</title>
    <meta name="description" content="Advanced laparoscopic gallbladder surgery in Delhi by Dr. Aloy Mukherjee. Get relief from gallstones with minimal pain and 1-day hospital stay." />
    <meta name="keywords" content="Gallbladder surgery Delhi, Laparoscopic cholecystectomy Delhi, Gallstone treatment Delhi, Best gallbladder surgeon Delhi, Gallbladder removal" />'''
    new_meta = '''    <title>Gallbladder Stone Surgeon in Delhi | Dr. Aloy Mukherjee</title>
    <meta name="description" content="Seeking the best gallbladder surgeon in delhi? Dr. Aloy Mukherjee offers advanced, minimally invasive surgery with faster recovery, less pain, and excellent patient outcomes." />
    <link rel="canonical" href="https://aloymukherjee.com/gallbladder-surgery.html" />
    <meta name="keywords" content="Gallbladder surgery Delhi, Laparoscopic cholecystectomy Delhi, Gallstone treatment Delhi, Best gallbladder surgeon Delhi, Gallbladder removal" />'''
    content = content.replace(old_meta, new_meta)
    
    # 2. UNDERSTANDING
    old_und = '''                      <h2 style="font-size: 2.8rem; font-weight: 800; color: #1a1a1a; margin-bottom: 25px;">Understanding Gallbladder</h2>
                      <p style="font-size: 1.1rem; color: #444; line-height: 1.7; margin-bottom: 20px;">The gallbladder is a small, hollow organ situated beneath the liver on the upper right side of the abdomen. It acts as a reservoir for bile, a digestive fluid produced by the liver that helps in the breakdown and absorption of dietary fats.</p>
                      <p style="font-size: 1.1rem; color: #444; line-height: 1.7;">When you eat, especially fatty foods, your gallbladder contracts and releases bile into the small intestine via the bile ducts. This release helps emulsify fats, making them easier for digestive enzymes to process.</p>'''
    new_und = '''                      <h2 style="font-size: 2.8rem; font-weight: 800; color: #1a1a1a; margin-bottom: 25px;">Understanding Gallbladder Surgery</h2>
                      <p style="font-size: 1.1rem; color: #444; line-height: 1.7; margin-bottom: 20px;">Gallbladder surgery, also known as cholecystectomy, is a procedure performed to remove the gallbladder when it develops stones or becomes inflamed. Gallstones can cause severe abdominal pain, nausea, and digestive issues, especially after eating fatty foods. This surgery helps relieve symptoms and prevents serious complications. Today, gallbladder surgery in delhi is commonly performed using advanced minimally invasive techniques for safer outcomes.</p>
                      <p style="font-size: 1.1rem; color: #444; line-height: 1.7;">Modern approaches like laparoscopic and robotic surgery allow smaller incisions, less pain, and faster recovery compared to traditional open surgery. Early diagnosis and timely treatment are essential to avoid complications such as infection or blockage of bile ducts. Patients opting for gallbladder surgery in delhi benefit from expert care, reduced hospital stay, and quicker return to normal life.</p>'''
    content = content.replace(old_und, new_und)
    
    # 3. CAUSES
    old_cause = '''                  <h2 style="font-size: 2.5rem; color: #1a1a1a; margin-bottom: 20px;">Common Causes & Risk Factors</h2>
                  <p style="font-size: 1.1rem; color: #666; max-width: 800px; margin: 0 auto;">Several factors contribute to the formation of gallstones. Understanding these risks can aid in prevention and management.</p>
              </div>
              <div class="causes-grid">
                  <!-- Cause Card 1 -->
                  <div class="cause-card">
                      <h4>High Cholesterol Diet</h4>
                      <p>Consuming a diet excessively high in fat and cholesterol, but low in fiber, can lead to bile that is too concentrated with cholesterol, ultimately forming stones.</p>
                      <div class="cause-treatment-box">
                          <strong>Management:</strong>
                          <p>Adopting a balanced, high-fiber, low-fat diet can help regulate cholesterol levels and promote healthy digestion.</p>
                      </div>
                  </div>
                  <!-- Cause Card 2 -->
                  <div class="cause-card">
                      <h4>Overweight or Obesity</h4>
                      <p>Being overweight is one of the most significant risk factors for gallstones. It can negatively impact the body's cholesterol metabolism and gallbladder emptying.</p>
                      <div class="cause-treatment-box">
                          <strong>Management:</strong>
                          <p>Gradual, sustained weight loss through diet and exercise is recommended to reduce gallstone formation risks.</p>
                      </div>
                  </div>
                  <!-- Cause Card 3 -->
                  <div class="cause-card">
                      <h4>Rapid Weight Loss</h4>
                      <p>When the body breaks down fat during rapid weight loss or fasting, the liver can secrete extra cholesterol into bile, which may lead to gallstones.</p>
                      <div class="cause-treatment-box">
                          <strong>Management:</strong>
                          <p>Safe, supervised weight loss plans aim for a steady loss of 1 to 2 pounds per week to minimize this risk.</p>
                      </div>
                  </div>
                  <!-- Cause Card 4 -->
                  <div class="cause-card">
                      <h4>Demographic Factors</h4>
                      <p>Age and biological sex play a role. Being over 40, being female (due to estrogen from pregnancy or hormone therapy), and having a family history increase risks.</p>
                      <div class="cause-treatment-box">
                          <strong>Management:</strong>
                          <p>While these factors can't be changed, awareness helps in early detection. Regular check-ups are advised for high-risk individuals.</p>
                      </div>
                  </div>
              </div>'''
    new_cause = '''                  <h2 style="font-size: 2.5rem; color: #1a1a1a; margin-bottom: 20px;">Common Causes & Risk Factors</h2>
              </div>
              <div class="causes-grid">
                  <div class="cause-card">
                      <h4>1. Gallstones Formation</h4>
                      <p>The most common cause is the formation of gallstones due to an imbalance in bile components like cholesterol and bilirubin.</p>
                  </div>
                  <div class="cause-card">
                      <h4>2. Poor Diet and Lifestyle</h4>
                      <p>High-fat, low-fiber diets and sedentary lifestyle increase the risk of developing gallstones.</p>
                  </div>
                  <div class="cause-card">
                      <h4>3. Obesity and Rapid Weight Loss</h4>
                      <p>Excess weight or sudden weight loss can disrupt bile balance, leading to stone formation.</p>
                  </div>
                  <div class="cause-card">
                      <h4>4. Age and Gender Factors</h4>
                      <p>Gallstones are more common in women and individuals over the age of 40.</p>
                  </div>
              </div>'''
    content = content.replace(old_cause, new_cause)
    
    # 4. SYMPTOMS
    old_symp = '''              <div class="symptoms-grid">
                  <div class="symptom-card text-left">
                      <div class="symptom-icon-box">
                          <i class="fas fa-procedures"></i>
                      </div>
                      <h4>Sudden Right-Side Pain</h4>
                      <p>Rapidly intensifying pain in the upper right portion of your abdomen, often after meals.</p>
                  </div>
                  <div class="symptom-card text-left">
                      <div class="symptom-icon-box">
                          <i class="fas fa-procedures"></i>
                      </div>
                      <h4>Center Abdominal Pain</h4>
                      <p>Intense, steadily worsening pain in the center of your abdomen, just below your breastbone.</p>
                  </div>
                  <div class="symptom-card text-left">
                      <div class="symptom-icon-box">
                          <i class="fas fa-procedures"></i>
                      </div>
                      <h4>Radiating Back Pain</h4>
                      <p>Uncomfortable, sharp pain that radiates between your shoulder blades or deeply into your right shoulder.</p>
                  </div>
                  <div class="symptom-card text-left">
                      <div class="symptom-icon-box">
                          <i class="fas fa-procedures"></i>
                      </div>
                      <h4>Severe Nausea</h4>
                      <p>Persistent nausea or active vomiting accompanied by extreme bloating and digestive discomfort.</p>
                  </div>
              </div>'''
    new_symp = '''              <div class="symptoms-grid">
                  <div class="symptom-card text-left"><div class="symptom-icon-box"><i class="fas fa-exclamation-circle"></i></div><h4>1. Severe Abdominal Pain</h4><p>Sharp pain in the upper right abdomen, especially after meals, is a common symptom.</p></div>
                  <div class="symptom-card text-left"><div class="symptom-icon-box"><i class="fas fa-notes-medical"></i></div><h4>2. Nausea and Vomiting</h4><p>Patients may experience frequent nausea and vomiting due to digestive issues.</p></div>
                  <div class="symptom-card text-left"><div class="symptom-icon-box"><i class="fas fa-exclamation-triangle"></i></div><h4>3. Indigestion and Bloating</h4><p>Difficulty digesting fatty foods and feeling bloated are common signs.</p></div>
                  <div class="symptom-card text-left"><div class="symptom-icon-box"><i class="fas fa-procedures"></i></div><h4>4. Fever and Jaundice</h4><p>In severe cases, infection may cause fever or yellowing of the skin and eyes.</p></div>
              </div>'''
    content = content.replace(old_symp, new_symp)

    # 5. DIAGNOSIS
    old_diag = '''              <h2 class="section-title">Diagnosis <span>Process</span></h2>
              <p style="max-width: 800px; margin: 0 auto 40px; font-size: 1.1rem;">To definitively diagnose gallstones and rule out other causes of abdominal pain, our clinic utilizes comprehensive testing.</p>
              <div class="grid-3">
                  <div class="info-box">
                      <i class="fas fa-user-md" style="font-size: 3rem; color: var(--secondary-teal); margin-bottom: 20px;"></i>
                      <h4>Physical Examination</h4>
                      <p>Dr. Aloy will check for abdominal tenderness and perform specific clinical tests (like Murphy's sign) to assess gallbladder inflammation.</p>
                  </div>
                  <div class="info-box">
                      <i class="fas fa-wave-square" style="font-size: 3rem; color: var(--secondary-teal); margin-bottom: 20px;"></i>
                      <h4>Abdominal Ultrasound</h4>
                      <p>The safest and most common test. It uses sound waves to quickly and painlessly visualize exactly where and how large the gallstones are.</p>
                  </div>
                  <div class="info-box">
                      <i class="fas fa-vial" style="font-size: 3rem; color: var(--secondary-teal); margin-bottom: 20px;"></i>
                      <h4>Blood Tests</h4>
                      <p>Used to check for signs of severe infection, jaundice, pancreatitis, or other complications caused by gallstones blocking bile ducts.</p>
                  </div>
              </div>'''
    new_diag = '''              <h2 class="section-title" style="margin-bottom: 40px;">Diagnosis <span>Process</span></h2>
              <div class="grid-3">
                  <div class="info-box"><i class="fas fa-user-md" style="font-size: 3rem; color: var(--secondary-teal); margin-bottom: 20px;"></i><h4>1. Physical Examination</h4><p>The doctor evaluates symptoms and checks for tenderness in the abdominal area.</p></div>
                  <div class="info-box"><i class="fas fa-hand-holding-medical" style="font-size: 3rem; color: var(--secondary-teal); margin-bottom: 20px;"></i><h4>2. Imaging Tests</h4><p>Ultrasound is the most common test to detect gallstones, along with CT scan if needed.</p></div>
                  <div class="info-box"><i class="fas fa-microscope" style="font-size: 3rem; color: var(--secondary-teal); margin-bottom: 20px;"></i><h4>3. Blood Tests</h4><p>Blood tests help identify infection, inflammation, or bile duct blockage.</p></div>
              </div>'''
    content = content.replace(old_diag, new_diag)

    # 6. TREATMENTS
    old_treat = '''              <div class="advanced-treatments-grid fade-in-up">
                  <div class="treatment-item">
                      <div class="treatment-icon blue">
                          <i class="fas fa-apple-alt"></i>
                      </div>
                      <div class="treatment-content">
                          <h4>Lifestyle Modifications</h4>
                          <p>A "watchful waiting" approach with a strict low-fat diet and pain management medications. Primarily advised for asymptomatic cases to prevent flare-ups.</p>
                      </div>
                  </div>
                  <div class="treatment-item">
                      <div class="treatment-icon teal">
                          <i class="fas fa-pills"></i>
                      </div>
                      <div class="treatment-content">
                          <h4>Medication Therapy</h4>
                          <p>In selective, non-surgical cases, medications may be prescribed to help dissolve small cholesterol stones, although they can take considerable time to work.</p>
                      </div>
                  </div>
                  <div class="treatment-item">
                      <div class="treatment-icon cyan">
                          <i class="fas fa-laptop-medical"></i>
                      </div>
                      <div class="treatment-content">
                          <h4>Laparoscopic Cholecystectomy</h4>
                          <p>The gold standard surgical treatment. A minimally invasive procedure to remove the gallbladder with tiny incisions, resulting in minimal pain and fast recovery.</p>
                      </div>
                  </div>
                  <div class="treatment-item">
                      <div class="treatment-icon blue">
                          <i class="fas fa-procedures"></i>
                      </div>
                      <div class="treatment-content">
                          <h4>Open Cholecystectomy</h4>
                          <p>A traditional surgical approach to remove the gallbladder. This is typically reserved for complex cases with severe infection or scarring that prevents laparoscopy.</p>
                      </div>
                  </div>
              </div>'''
    new_treat = '''              <div class="advanced-treatments-grid fade-in-up">
                  <div class="treatment-item"><div class="treatment-icon blue"><i class="fas fa-laptop-medical"></i></div><div class="treatment-content"><h4>1. Laparoscopic Gallbladder Surgery</h4><p>This minimally invasive procedure uses small incisions and a camera to remove the gallbladder with precision. It ensures faster recovery and minimal discomfort, making it a preferred option for best gallbladder stone surgery in delhi.</p></div></div>
                  <div class="treatment-item"><div class="treatment-icon teal"><i class="fas fa-procedures"></i></div><div class="treatment-content"><h4>2. Robotic Gallbladder Surgery</h4><p>Robotic-assisted surgery offers enhanced precision and control, resulting in better outcomes, minimal complications, and quicker healing.</p></div></div>
              </div>'''
    content = content.replace(old_treat, new_treat)

    # 7. ABOUT
    old_about = '''            <h2 class="section-title">Why Dr. Aloy Mukherjee is the Best <span>Gallbladder Surgeon</span> in Delhi?</h2>
            <p class="about-bio">
              Dr. Aloy Mukherjee is an internationally renowned Senior
              Consultant Surgeon with an exceptional track record of over 25
              years. Specializing in Advanced Minimal Access Surgery, he is a
              pioneer in Laparoscopic, Bariatric, and Gastrointestinal
              procedures in India.
            </p>
            <p class="about-bio">
              Currently practicing at the prestigious
              <strong>2nd floor, Indraprastha Apollo Hospital, Room No. 1265, Gate No. 10, Jasola Vihar, New Delhi, Delhi 110076</strong>, Dr.
              Mukherjee focuses on providing patient-centered, ethical, and
              world-class surgical care utilizing the latest technological
              advancements including Robotic Surgery.
            </p>
            <div class="highlight-cards">
              <div class="highlight-card">
                <div class="hc-icon"><i class="fas fa-user-md"></i></div>
                <div class="hc-text">25+ Years Experience</div>
              </div>
              <div class="highlight-card">
                <div class="hc-icon"><i class="fas fa-procedures"></i></div>
                <div class="hc-text">22,000+ Surgeries</div>
              </div>
              <div class="highlight-card">
                <div class="hc-icon"><i class="fas fa-microscope"></i></div>
                <div class="hc-text">Advanced Minimally Invasive Expert</div>
              </div>
              <div class="highlight-card">
                <div class="hc-icon"><i class="fas fa-heartbeat"></i></div>
                <div class="hc-text">Patient-Centered Care</div>
              </div>
            </div>'''
    new_about = '''            <h2 class="section-title">Why Choose Dr. Aloy Mukherjee for <span>Gallbladder Surgery?</span></h2>
            <p class="about-bio">Dr. Aloy Mukherjee is a highly experienced surgeon known for performing advanced gallbladder procedures with precision and care. His expertise in minimally invasive techniques ensures safe surgery, less pain, and faster recovery. Patients trust his approach for accurate diagnosis and effective treatment, making him a preferred choice for gallbladder surgery in delhi.</p>
            <p class="about-bio" style="margin-top: 15px;">His commitment to excellence, use of modern technology, and patient-focused care set him apart. Dr. Mukherjee provides personalized treatment plans based on each patient’s condition. Recognized as the Best Gallbladder surgeon in delhi, he delivers consistent results and high patient satisfaction.</p>
            <a href="about.html" class="btn btn-primary" style="margin-top: 20px;">Read More</a>'''
    content = content.replace(old_about, new_about)

    # 8. FAQS
    old_faq = '''              <div class="faq-container fade-in-up">
                  <div class="faq-item">
                      <div class="faq-question"><h4>Are gallbladder stones dangerous if left untreated?</h4><span class="faq-toggle"><i class="fas fa-plus"></i></span></div>
                      <div class="faq-answer"><p>Yes, they can slip into the bile duct, causing severe jaundice, pancreatitis, or acute infection. Prompt removal of the gallbladder (cholecystectomy) is the safest approach.</p></div>
                  </div>                  <div class="faq-item">
                      <div class="faq-question"><h4>Will my digestion be affected without a gallbladder?</h4><span class="faq-toggle"><i class="fas fa-plus"></i></span></div>
                      <div class="faq-answer"><p>The gallbladder stores bile, but your liver will continuously drip bile into the intestines. Most patients experience perfectly normal digestion within a few weeks of surgery.</p></div>
                  </div>                  <div class="faq-item">
                      <div class="faq-question"><h4>What diet should I follow after gallbladder removal?</h4><span class="faq-toggle"><i class="fas fa-plus"></i></span></div>
                      <div class="faq-answer"><p>In the initial weeks, a low-fat diet is recommended to prevent bloating or diarrhea. Gradually, you can reintroduce normal healthy fats into your diet as your body adapts.</p></div>
                  </div>                  <div class="faq-item">
                      <div class="faq-question"><h4>Why is Laparoscopic Cholecystectomy the standard?</h4><span class="faq-toggle"><i class="fas fa-plus"></i></span></div>
                      <div class="faq-answer"><p>It offers significantly less pain, a shorter 24-hour hospital stay, minimal scarring, and much faster return to normal activities compared to traditional open surgery.</p></div>
                  </div>                  <div class="faq-item">
                      <div class="faq-question"><h4>Can gallstones be removed without removing the gallbladder?</h4><span class="faq-toggle"><i class="fas fa-plus"></i></span></div>
                      <div class="faq-answer"><p>No, the medical standard is to remove the diseased gallbladder entirely. Simply removing stones guarantees they will reform because the gallbladder itself is functionally impaired.</p></div>
                  </div>                  <div class="faq-item">
                      <div class="faq-question"><h4>How soon can I return to work?</h4><span class="faq-toggle"><i class="fas fa-plus"></i></span></div>
                      <div class="faq-answer"><p>Most patients recovering from a laparoscopic gallbladder surgery can comfortably return to office or desk jobs within 5 to 7 days.</p></div>
                  </div>
              </div>'''
    new_faq = '''              <div class="faq-container fade-in-up">
                  <div class="faq-item">
                      <div class="faq-question"><h4>1. What is gallbladder surgery?</h4><span class="faq-toggle"><i class="fas fa-plus"></i></span></div>
                      <div class="faq-answer"><p>Gallbladder surgery is a procedure to remove the gallbladder, usually due to gallstones or inflammation.</p></div>
                  </div>
                  <div class="faq-item">
                      <div class="faq-question"><h4>2. Is gallbladder surgery safe?</h4><span class="faq-toggle"><i class="fas fa-plus"></i></span></div>
                      <div class="faq-answer"><p>Yes, it is a safe and commonly performed procedure, especially with minimally invasive techniques.</p></div>
                  </div>
                  <div class="faq-item">
                      <div class="faq-question"><h4>3. What are the benefits of this surgery?</h4><span class="faq-toggle"><i class="fas fa-plus"></i></span></div>
                      <div class="faq-answer"><p>Gallbladder surgery in delhi provides relief from pain, prevents complications, and improves digestion.</p></div>
                  </div>
                  <div class="faq-item">
                      <div class="faq-question"><h4>4. How long does recovery take?</h4><span class="faq-toggle"><i class="fas fa-plus"></i></span></div>
                      <div class="faq-answer"><p>Most patients recover within 1–2 weeks after laparoscopic surgery.</p></div>
                  </div>
                  <div class="faq-item">
                      <div class="faq-question"><h4>5. Who is the best doctor for gallbladder surgery in Delhi?</h4><span class="faq-toggle"><i class="fas fa-plus"></i></span></div>
                      <div class="faq-answer"><p>Dr. Aloy Mukherjee is considered the Best Gallbladder surgeon in delhi, known for his expertise and successful outcomes.</p></div>
                  </div>
                  <div class="faq-item">
                      <div class="faq-question"><h4>6. Can I live normally without a gallbladder?</h4><span class="faq-toggle"><i class="fas fa-plus"></i></span></div>
                      <div class="faq-answer"><p>Yes, most people live a normal life without a gallbladder, with minor dietary adjustments.</p></div>
                  </div>
              </div>'''
    content = content.replace(old_faq, new_faq)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Done applying python replacement.")

if __name__ == '__main__':
    main()
