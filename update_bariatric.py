import sys

def main():
    file_path = 'bariatric-surgery.html'
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. META
    old_meta = '''    <title>Bariatric Surgery in Delhi | Dr. Aloy Mukherjee</title>
    <meta name="description" content="Advanced laparoscopic Bariatric Surgery in Delhi by Dr. Aloy Mukherjee. Get relief from Bariatrics with minimal pain and 1-day hospital stay." />
    <meta name="keywords" content="Bariatric Surgery Delhi, Laparoscopic cholecystectomy Delhi, Bariatric treatment Delhi, Best Bariatric surgeon Delhi, Bariatric removal" />'''
    new_meta = '''    <title>Bariatric Surgery in Delhi | Dr. Aloy Mukherjee</title>
    <meta name="description" content="Seeking Bariatric Surgery in Delhi? Dr. Aloy Mukherjee offers safe, minimally invasive weight loss procedures with faster recovery and long-term health benefits." />
    <link rel="canonical" href="https://aloymukherjee.com/bariatric-surgery.html" />
    <meta name="keywords" content="Bariatric Surgery Delhi, Laparoscopic cholecystectomy Delhi, Bariatric treatment Delhi, Best Bariatric surgeon Delhi, Bariatric removal" />'''
    content = content.replace(old_meta, new_meta)

    # 2. UNDERSTANDING
    old_und = '''                      <h2 style="font-size: 2.8rem; font-weight: 800; color: #1a1a1a; margin-bottom: 25px;">Understanding Weight Loss Surgery</h2>
                      <p style="font-size: 1.1rem; color: #444; line-height: 1.7; margin-bottom: 20px;">Bariatric surgery involves surgical changes to your stomach and/or digestive system to help you lose weight.</p>
                      <p style="font-size: 1.1rem; color: #444; line-height: 1.7;">It is designed for individuals suffering from severe obesity who have not been able to achieve sustained weight loss through diet and exercise alone, helping resolve conditions like diabetes and hypertension.</p>'''
    new_und = '''                      <h2 style="font-size: 2.8rem; font-weight: 800; color: #1a1a1a; margin-bottom: 25px;">Understanding Weight Loss Surgery</h2>
                      <p style="font-size: 1.1rem; color: #444; line-height: 1.7; margin-bottom: 20px;">Weight loss surgery, also known as bariatric surgery, is a medical procedure designed to help individuals lose excess weight by making changes to the digestive system. It is usually recommended for people who are severely overweight and have not achieved results through diet, exercise, or medications. These procedures work by limiting food intake, reducing nutrient absorption, or a combination of both. Today, weight loss surgery in delhi is considered a safe and effective solution for long-term weight management.</p>
                      <p style="font-size: 1.1rem; color: #444; line-height: 1.7;">Modern techniques such as laparoscopic and robotic surgery have made the procedure less invasive, resulting in smaller incisions, minimal pain, and faster recovery. In addition to weight loss, the surgery helps improve obesity-related conditions like diabetes, high blood pressure, and sleep apnea. Patients opting for Bariatric Surgery in Delhi benefit from advanced treatment options and expert care, ensuring better health outcomes and improved quality of life.</p>'''
    content = content.replace(old_und, new_und)

    # 3. CAUSES
    old_cause = '''                  <h2 style="font-size: 2.5rem; color: #1a1a1a; margin-bottom: 20px;">Common Causes & Risk Factors</h2>
                  <p style="font-size: 1.1rem; color: #666; max-width: 800px; margin: 0 auto;">Several factors contribute to this condition. Understanding these risks can aid in prevention and management.</p>
              </div>
              <div class="causes-grid">
                  <div class="cause-card">
                      <h4>Genetics & Hormones</h4>
                      <p>Metabolic rates and the way the body stores fat are heavily influenced by genetics and hormonal imbalances.</p>
                  </div>
                  <div class="cause-card">
                      <h4>Dietary Habits</h4>
                      <p>Long-term consumption of high-calorie, highly processed foods fundamentally alters the body's natural weight set point.</p>
                  </div>
                  <div class="cause-card">
                      <h4>Sedentary Lifestyle</h4>
                      <p>A lack of physical activity combined with modern technological convenience drastically reduces calorie expenditure.</p>
                  </div>
                  <div class="cause-card">
                      <h4>Certain Medications</h4>
                      <p>Some antidepressants, steroids, and diabetes medications can trigger severe, unmanageable weight gain.</p>
                  </div>
              </div>'''
    new_cause = '''                  <h2 style="font-size: 2.5rem; color: #1a1a1a; margin-bottom: 20px;">Common Causes & Risk Factors</h2>
              </div>
              <div class="causes-grid">
                  <div class="cause-card">
                      <h4>1. Unhealthy Eating Habits</h4>
                      <p>Frequent consumption of high-calorie, processed, and fatty foods can lead to excessive weight gain over time.</p>
                  </div>
                  <div class="cause-card">
                      <h4>2. Sedentary Lifestyle</h4>
                      <p>Lack of physical activity and prolonged sitting contribute significantly to obesity and related health issues.</p>
                  </div>
                  <div class="cause-card">
                      <h4>3. Genetic Factors</h4>
                      <p>Family history can play a role in obesity, making some individuals more prone to weight gain.</p>
                  </div>
                  <div class="cause-card">
                      <h4>4. Hormonal Imbalance</h4>
                      <p>Certain medical conditions and hormonal disorders can affect metabolism and lead to weight gain.</p>
                  </div>
              </div>'''
    content = content.replace(old_cause, new_cause)

    # 4. SYMPTOMS
    old_symp = '''              <div class="symptoms-grid">
                  <div class="symptom-card text-left"><div class="symptom-icon-box"><i class="fas fa-exclamation-circle"></i></div><h4>Severe Obesity</h4><p>Having a BMI over 40, or a BMI over 35 with severe obesity-related comorbidities.</p></div>
                  <div class="symptom-card text-left"><div class="symptom-icon-box"><i class="fas fa-exclamation-triangle"></i></div><h4>Type 2 Diabetes</h4><p>Struggling with unmanaged diabetes that may be reversed via metabolic surgery.</p></div>
                  <div class="symptom-card text-left"><div class="symptom-icon-box"><i class="fas fa-notes-medical"></i></div><h4>Sleep Apnea</h4><p>Experiencing severe breathing interruptions during sleep due to excess weight.</p></div>
                  <div class="symptom-card text-left"><div class="symptom-icon-box"><i class="fas fa-procedures"></i></div><h4>Joint Pain</h4><p>Chronic joint pain and osteoarthritis exacerbated by excessive body weight.</p></div>
              </div>'''
    new_symp = '''              <div class="symptoms-grid">
                  <div class="symptom-card text-left"><div class="symptom-icon-box"><i class="fas fa-exclamation-circle"></i></div><h4>1. Excess Body Weight</h4><p>A high body mass index (BMI) is the primary indicator for considering bariatric surgery.</p></div>
                  <div class="symptom-card text-left"><div class="symptom-icon-box"><i class="fas fa-notes-medical"></i></div><h4>2. Difficulty in Daily Activities</h4><p>Simple tasks like walking, climbing stairs, or exercising become challenging.</p></div>
                  <div class="symptom-card text-left"><div class="symptom-icon-box"><i class="fas fa-exclamation-triangle"></i></div><h4>3. Obesity-Related Health Issues</h4><p>Conditions like diabetes, high blood pressure, and joint pain are common in obese individuals.</p></div>
                  <div class="symptom-card text-left"><div class="symptom-icon-box"><i class="fas fa-procedures"></i></div><h4>4. Low Energy and Fatigue</h4><p>Carrying excess weight often leads to reduced stamina and constant tiredness.</p></div>
              </div>'''
    content = content.replace(old_symp, new_symp)

    # 5. DIAGNOSIS
    old_diag = '''              <h2 class="section-title">Diagnosis <span>Process</span></h2>
              <p style="max-width: 800px; margin: 0 auto 40px; font-size: 1.1rem;">To definitively diagnose Weight Loss Surgery and rule out other causes, our clinic utilizes comprehensive testing.</p>
              <div class="grid-3">
                  <div class="info-box"><i class="fas fa-user-md" style="font-size: 3rem; color: var(--secondary-teal); margin-bottom: 20px;"></i><h4>Physical Examination</h4><p>Dr. Aloy will review your complete weight history, diet attempts, and existing medical conditions.</p></div>
                  <div class="info-box"><i class="fas fa-wave-square" style="font-size: 3rem; color: var(--secondary-teal); margin-bottom: 20px;"></i><h4>Imaging Tests</h4><p>Cardiology and pulmonology clearances are obtained to ensure you can safely undergo general anesthesia.</p></div>
                  <div class="info-box"><i class="fas fa-vial" style="font-size: 3rem; color: var(--secondary-teal); margin-bottom: 20px;"></i><h4>Laboratory Analysis</h4><p>Comprehensive metabolic blood panels are evaluated to customize your specific bariatric pathway.</p></div>
              </div>'''
    new_diag = '''              <h2 class="section-title" style="margin-bottom: 40px;">Diagnosis <span>Process</span></h2>
              <div class="grid-3">
                  <div class="info-box"><i class="fas fa-user-md" style="font-size: 3rem; color: var(--secondary-teal); margin-bottom: 20px;"></i><h4>1. Medical Evaluation</h4><p>The doctor assesses overall health, BMI, and obesity-related conditions to determine eligibility.</p></div>
                  <div class="info-box"><i class="fas fa-hand-holding-medical" style="font-size: 3rem; color: var(--secondary-teal); margin-bottom: 20px;"></i><h4>2. Diagnostic Tests</h4><p>Blood tests and imaging may be recommended to evaluate metabolic health and organ function.</p></div>
                  <div class="info-box"><i class="fas fa-microscope" style="font-size: 3rem; color: var(--secondary-teal); margin-bottom: 20px;"></i><h4>3. Lifestyle Assessment</h4><p>Diet, physical activity, and previous weight loss efforts are reviewed before planning surgery.</p></div>
              </div>'''
    content = content.replace(old_diag, new_diag)

    # 6. TREATMENTS
    old_treat = '''              <div class="section-heading text-center fade-in-up">
                  <h2 style="font-size: 2.5rem; color: #1a1a1a; margin-bottom: 20px;">Our Advanced Treatments</h2>
              </div>
              <div class="advanced-treatments-grid fade-in-up">
                  <div class="treatment-item"><div class="treatment-icon blue"><i class="fas fa-laptop-medical"></i></div><div class="treatment-content"><h4>Sleeve Gastrectomy</h4><p>Removing approximately 80% of the stomach to restrict food intake and reduce hunger-inducing hormones.</p></div></div>
                  <div class="treatment-item"><div class="treatment-icon teal"><i class="fas fa-procedures"></i></div><div class="treatment-content"><h4>Gastric Bypass</h4><p>Creating a small stomach pouch and bypassing a section of the intestine to reduce calorie absorption.</p></div></div>
              </div>'''
    new_treat = '''              <div class="section-heading text-center fade-in-up">
                  <h2 style="font-size: 2.5rem; color: #1a1a1a; margin-bottom: 20px;">Our Advanced Treatments</h2>
              </div>
              <div class="advanced-treatments-grid fade-in-up">
                  <div class="treatment-item"><div class="treatment-icon blue"><i class="fas fa-procedures"></i></div><div class="treatment-content"><h4>1. Gastric Bypass (Roux-en-Y Gastric Bypass)</h4><p>This procedure involves creating a small stomach pouch and rerouting the small intestine, which helps reduce food intake and calorie absorption. It is highly effective for significant and long-term weight loss.</p></div></div>
                  <div class="treatment-item"><div class="treatment-icon teal"><i class="fas fa-laptop-medical"></i></div><div class="treatment-content"><h4>2. Sleeve Gastrectomy</h4><p>In this surgery, a large portion of the stomach is removed, leaving a smaller, tube-shaped stomach. It limits food intake and reduces hunger by affecting hormone levels.</p></div></div>
                  <div class="treatment-item"><div class="treatment-icon cyan"><i class="fas fa-band-aid"></i></div><div class="treatment-content"><h4>3. Adjustable Gastric Band</h4><p>This involves placing an adjustable band around the upper part of the stomach to create a small pouch. It helps control portion size and promotes gradual weight loss.</p></div></div>
                  <div class="treatment-item"><div class="treatment-icon blue"><i class="fas fa-user-md"></i></div><div class="treatment-content"><h4>4. Biliopancreatic Diversion with Duodenal Switch (BPD/DS)</h4><p>This complex procedure combines sleeve gastrectomy with intestinal bypass, significantly reducing calorie absorption. It is usually recommended for patients with severe obesity and provides substantial weight loss results.</p></div></div>
              </div>'''
    content = content.replace(old_treat, new_treat)

    # 7. ABOUT
    old_about = '''            <h2 class="section-title">Why Dr. Aloy Mukherjee is the Best <span>Bariatric Surgeon</span> in Delhi?</h2>
            <p class="about-bio">Dr. Aloy Mukherjee is an internationally renowned Senior Consultant Surgeon with an exceptional track record of over 25 years. Specializing in Advanced Minimal Access Surgery, he is a pioneer in Laparoscopic, Bariatric, and Gastrointestinal procedures in India.</p>
            <p class="about-bio" style="margin-top: 15px;">His comprehensive approach integrates multidisciplinary expertise to ensure the best possible outcomes, prioritizing rapid recovery and minimal discomfort for every patient.</p>'''
    new_about = '''            <h2 class="section-title">Why Choose Dr. Aloy Mukherjee for <span>Bariatric Surgery?</span></h2>
            <p class="about-bio">Dr. Aloy Mukherjee is a highly experienced specialist known for delivering advanced and effective weight loss solutions. With expertise in minimally invasive and robotic techniques, he ensures safe procedures with faster recovery and long-term success. His patient-focused approach and use of modern technology make him a trusted choice for Bariatric Surgery in Delhi.</p>
            <p class="about-bio" style="margin-top: 15px;">His commitment to personalized care, accurate evaluation, and comprehensive support sets him apart. Dr. Mukherjee carefully designs treatment plans based on each patient’s needs and health conditions. Recognized as the Best Bariatric Surgeon in Delhi, he is dedicated to helping patients achieve sustainable weight loss and improved quality of life.</p>'''
    content = content.replace(old_about, new_about)

    # 8. FAQS
    old_faq = '''              <div class="faq-container fade-in-up">
                  <div class="faq-item">
                      <div class="faq-question"><h4>Who is considered a candidate for Bariatric Surgery?</h4><span class="faq-toggle"><i class="fas fa-plus"></i></span></div>
                      <div class="faq-answer"><p>Generally, individuals with a BMI over 35 with obesity-related conditions (like diabetes), or a BMI over 40. Dr. Aloy performs a thorough evaluation to determine the optimal approach.</p></div>
                  </div>                  <div class="faq-item">
                      <div class="faq-question"><h4>How much weight will I lose?</h4><span class="faq-toggle"><i class="fas fa-plus"></i></span></div>
                      <div class="faq-answer"><p>Weight loss varies by the specific procedure (Gastric Bypass vs Sleeve), but patients typically lose 60% to 80% of their excess body weight within the first 12-18 months.</p></div>
                  </div>                  <div class="faq-item">
                      <div class="faq-question"><h4>Does Bariatric Surgery cure Type 2 Diabetes?</h4><span class="faq-toggle"><i class="fas fa-plus"></i></span></div>
                      <div class="faq-answer"><p>It can lead to long-term remission of Type 2 Diabetes in up to 80% of patients. Many patients are able to stop insulin and oral medications shortly after surgery.</p></div>
                  </div>                  <div class="faq-item">
                      <div class="faq-question"><h4>Is Bariatric Surgery reversible?</h4><span class="faq-toggle"><i class="fas fa-plus"></i></span></div>
                      <div class="faq-answer"><p>Procedures like Gastric Bypass and Sleeve Gastrectomy are generally considered permanent. They involve restructuring the digestive system to enact lasting metabolic changes.</p></div>
                  </div>                  <div class="faq-item">
                      <div class="faq-question"><h4>Will I need to take vitamins forever?</h4><span class="faq-toggle"><i class="fas fa-plus"></i></span></div>
                      <div class="faq-answer"><p>Yes, bariatric surgery alters nutrient absorption. You will need to take designated daily bariatric multivitamins and possibly calcium, iron, and B12 for the rest of your life.</p></div>
                  </div>                  <div class="faq-item">
                      <div class="faq-question"><h4>What is the recovery timeline?</h4><span class="faq-toggle"><i class="fas fa-plus"></i></span></div>
                      <div class="faq-answer"><p>Patients typically spend 2-3 days in the hospital. Most can return to desk jobs in two weeks and resume more vigorous activities within 4-6 weeks.</p></div>
                  </div>
              </div>'''
    new_faq = '''              <div class="faq-container fade-in-up">
                  <div class="faq-item">
                      <div class="faq-question"><h4>1. What is bariatric surgery?</h4><span class="faq-toggle"><i class="fas fa-plus"></i></span></div>
                      <div class="faq-answer"><p>Bariatric surgery is a weight loss procedure that helps reduce excess body weight by modifying the digestive system.</p></div>
                  </div>
                  <div class="faq-item">
                      <div class="faq-question"><h4>2. Who is eligible for bariatric surgery?</h4><span class="faq-toggle"><i class="fas fa-plus"></i></span></div>
                      <div class="faq-answer"><p>Individuals with a high BMI or obesity-related health conditions who have not succeeded with diet and exercise may be eligible.</p></div>
                  </div>
                  <div class="faq-item">
                      <div class="faq-question"><h4>3. Is bariatric surgery safe?</h4><span class="faq-toggle"><i class="fas fa-plus"></i></span></div>
                      <div class="faq-answer"><p>Yes, it is a safe procedure when performed by an experienced surgeon using advanced techniques.</p></div>
                  </div>
                  <div class="faq-item">
                      <div class="faq-question"><h4>4. How much weight can I lose after surgery?</h4><span class="faq-toggle"><i class="fas fa-plus"></i></span></div>
                      <div class="faq-answer"><p>Weight loss varies, but most patients lose a significant amount of excess weight within the first year.</p></div>
                  </div>
                  <div class="faq-item">
                      <div class="faq-question"><h4>5. Who is the Best Bariatric Surgeon in Delhi?</h4><span class="faq-toggle"><i class="fas fa-plus"></i></span></div>
                      <div class="faq-answer"><p>Dr. Aloy Mukherjee is widely recognized as the Best Bariatric Surgeon in Delhi, known for his expertise and successful outcomes.</p></div>
                  </div>
                  <div class="faq-item">
                      <div class="faq-question"><h4>6. How long does recovery take?</h4><span class="faq-toggle"><i class="fas fa-plus"></i></span></div>
                      <div class="faq-answer"><p>Most patients recover within a few weeks and can return to normal activities with proper guidance.</p></div>
                  </div>
              </div>'''
    content = content.replace(old_faq, new_faq)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print("Done applying python replacement for Bariatric page.")

if __name__ == '__main__':
    main()
