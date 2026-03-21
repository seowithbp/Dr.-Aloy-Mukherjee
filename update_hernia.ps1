$html = [System.IO.File]::ReadAllText('hernia-surgery.html')

# 1. Meta Tags
$html = [regex]::Replace($html, '(?s)<title>.*?</title>', '<title>Best Hernia Surgeon in Delhi | Dr. Aloy Mukherjee</title>')
$html = [regex]::Replace($html, '(?s)<meta name="description" content=".*?" />', '<meta name="description" content="Seeking the Best Hernia Surgeon in Delhi? Dr. Aloy Mukherjee provides advanced hernia surgery with precision, minimal pain, faster recovery, and trusted care." />`r`n    <link rel="canonical" href="https://aloymukherjee.com/hernia-surgery.html" />')

# 2. Understanding Hernias
$understanding_html = '<h2 style="font-size: 2.8rem; font-weight: 800; color: #1a1a1a; margin-bottom: 25px;">Understanding Hernias</h2>
                      <p style="font-size: 1.1rem; color: #444; line-height: 1.7; margin-bottom: 20px;">Hernia surgery is a procedure performed to repair a hernia, which occurs when an internal organ pushes through a weak spot in the muscle or tissue. This condition can cause pain, discomfort, and visible swelling, especially during physical activity. Hernia surgery helps in repositioning the organ and strengthening the weakened area using advanced techniques. With modern advancements, Hernia Surgery in Delhi is now safer, more effective, and minimally invasive.</p>
                      <p style="font-size: 1.1rem; color: #444; line-height: 1.7;">The procedure can be performed using open surgery, laparoscopic methods, or robotic-assisted techniques, depending on the severity of the condition. Minimally invasive approaches result in smaller incisions, less pain, and quicker recovery. Patients undergoing Hernia Surgery in Delhi often experience improved quality of life with reduced risk of recurrence. Early treatment is essential to prevent complications and ensure long-term relief.</p>'

$html = [regex]::Replace($html, '(?s)<h2 style="font-size: 2\.8rem; font-weight: 800; color: #1a1a1a; margin-bottom: 25px;">Understanding Hernias</h2>.*?</div>', $understanding_html + "`r`n                  </div>")

# 3. Causes
$causes_html = '<div class="causes-grid">
                  <div class="cause-card">
                      <h4>Weak Abdominal Muscles</h4>
                      <p>A hernia often develops due to weakness in the abdominal wall, which may be present from birth or develop over time due to aging or previous surgeries.</p>
                  </div>
                  <div class="cause-card">
                      <h4>Heavy Lifting and Physical Strain</h4>
                      <p>Frequent heavy lifting or intense physical activity increases pressure on the abdominal muscles, making them more prone to developing a hernia.</p>
                  </div>
                  <div class="cause-card">
                      <h4>Chronic Cough or Constipation</h4>
                      <p>Conditions like persistent coughing or long-term constipation can strain the abdominal area, increasing the risk of hernia formation.</p>
                  </div>
                  <div class="cause-card">
                      <h4>Obesity and Lifestyle Factors</h4>
                      <p>Excess body weight puts added pressure on the abdomen, while lack of exercise and poor lifestyle habits can weaken muscles and raise the chances of a hernia.</p>
                  </div>
              </div>'

$html = [regex]::Replace($html, '(?s)<div class="causes-grid">.*?</div>\s*</div>\s*</section>', $causes_html + "`r`n          </div>`r`n      </section>")

# 4. Symptoms
$symptoms_html = '<div class="symptoms-grid">
                  <div class="symptom-card text-left"><div class="symptom-icon-box"><i class="fas fa-exclamation-circle"></i></div><h4>Visible Bulge or Swelling</h4><p>One of the most common signs of a hernia is a noticeable bulge or lump in the affected area, especially when standing, coughing, or straining.</p></div>
                  <div class="symptom-card text-left"><div class="symptom-icon-box"><i class="fas fa-exclamation-triangle"></i></div><h4>Pain or Discomfort</h4><p>Patients may experience pain or a dragging sensation at the site of the hernia, which often worsens during physical activity or lifting.</p></div>
                  <div class="symptom-card text-left"><div class="symptom-icon-box"><i class="fas fa-notes-medical"></i></div><h4>Heaviness or Pressure</h4><p>A feeling of heaviness, pressure, or weakness in the abdomen or groin is a common symptom, particularly after prolonged standing or exertion.</p></div>
                  <div class="symptom-card text-left"><div class="symptom-icon-box"><i class="fas fa-procedures"></i></div><h4>Burning or Aching Sensation</h4><p>Some individuals may feel a burning or aching sensation around the bulge, indicating irritation of surrounding tissues.</p></div>
              </div>'

$rgxObj = [regex] '(?s)<div class="symptoms-grid">.*?</div>\s*</div>\s*</section>'
$html = $rgxObj.Replace($html, $symptoms_html + "`r`n          </div>`r`n      </section>", 1)

# 5. Diagnosis
$diagnosis_html = '<div class="grid-3">
                  <div class="info-box"><i class="fas fa-user-md" style="font-size: 3rem; color: var(--secondary-teal); margin-bottom: 20px;"></i><h4>Physical Examination</h4><p>The doctor begins with a detailed physical examination to check for visible bulges or swelling. Patients may be asked to cough or strain to make the hernia more noticeable.</p></div>
                  <div class="info-box"><i class="fas fa-wave-square" style="font-size: 3rem; color: var(--secondary-teal); margin-bottom: 20px;"></i><h4>Imaging Tests</h4><p>In some cases, imaging tests such as ultrasound, CT scan, or MRI are recommended to confirm the diagnosis and assess the size and type of hernia.</p></div>
                  <div class="info-box"><i class="fas fa-vial" style="font-size: 3rem; color: var(--secondary-teal); margin-bottom: 20px;"></i><h4>Medical History Evaluation</h4><p>The doctor reviews the patient’s medical history, symptoms, and lifestyle factors to determine the severity of the condition and plan the most suitable treatment.</p></div>
              </div>'

$rgxObj2 = [regex] '(?s)<div class="grid-3">.*?</div>\s*</div>\s*</section>'
$html = $rgxObj2.Replace($html, $diagnosis_html + "`r`n          </div>`r`n      </section>", 1)

# 6. Treatments
$treatments_html = '<div class="advanced-treatments-grid fade-in-up">
                  <div class="treatment-item"><div class="treatment-icon blue"><i class="fas fa-laptop-medical"></i></div><div class="treatment-content"><h4>Robotic Hernia Repair</h4><p>Robotic hernia repair is an advanced, minimally invasive technique that uses robotic-assisted technology for greater precision and control. This approach allows the surgeon to perform complex repairs with smaller incisions, reduced pain, and minimal scarring.</p></div></div>
                  <div class="treatment-item"><div class="treatment-icon teal"><i class="fas fa-procedures"></i></div><div class="treatment-content"><h4>Laparoscopic Hernia Repair</h4><p>Laparoscopic hernia repair is a widely used minimally invasive procedure performed using small incisions and a camera-guided system. It provides a clear view of the affected area, allowing accurate repair of the hernia with less tissue damage.</p></div></div>
              </div>'

$rgxObj3 = [regex] '(?s)<div class="advanced-treatments-grid fade-in-up">.*?</div>\s*</div>\s*</section>'
$html = $rgxObj3.Replace($html, $treatments_html + "`r`n          </div>`r`n      </section>", 1)

# 7. Why Dr. Aloy
$why_dr_aloy_html = '<h2 class="section-title">Why Dr. Aloy Mukherjee is the Best <span>Hernia Surgeon</span> in Delhi?</h2>
            <p class="about-bio">Dr. Aloy Mukherjee is highly regarded for his expertise in treating all types of hernias using advanced and minimally invasive techniques. With years of surgical experience and a strong focus on precision, he ensures effective treatment with minimal discomfort and faster recovery. His ability to handle both simple and complex cases with confidence has earned him a reputation as a trusted specialist. This excellence makes him a preferred choice for patients seeking reliable hernia care.</p>
            <p class="about-bio" style="margin-top: 15px;">What truly sets Dr. Aloy Mukherjee apart is his patient-first approach and commitment to delivering personalized treatment plans. He carefully evaluates each case and recommends the most suitable surgical method, whether laparoscopic or robotic. His use of modern technology, combined with compassionate care, ensures safe procedures and long-term results. Known for consistent success rates and patient satisfaction, he is widely recognized as a leading hernia surgeon in Delhi.</p>
            <a href="about.html" class="btn btn-primary" style="margin-top: 20px;">Read More</a>'

$rgxObj4 = [regex] '(?s)<h2 class="section-title">Why Dr. Aloy Mukherjee is the Best <span>Hernia Surgeon</span> in Delhi\?</h2>.*?<a href="about.html" class="btn btn-primary".*?</a>'
$html = $rgxObj4.Replace($html, $why_dr_aloy_html, 1)

# 8. FAQ
$faq_html = '<div class="faq-container fade-in-up">
                  <div class="faq-item">
                      <div class="faq-question">
                          <h4>What is a hernia?</h4>
                          <span class="faq-toggle"><i class="fas fa-plus"></i></span>
                      </div>
                      <div class="faq-answer">
                          <p>A hernia occurs when an internal organ pushes through a weak spot in the muscle or tissue, often causing a visible bulge and discomfort.</p>
                      </div>
                  </div>

                  <div class="faq-item">
                      <div class="faq-question">
                          <h4>Is hernia surgery the only treatment?</h4>
                          <span class="faq-toggle"><i class="fas fa-plus"></i></span>
                      </div>
                      <div class="faq-answer">
                          <p>Yes, surgery is the only permanent solution for a hernia. Non-surgical methods may provide temporary relief but do not fix the underlying issue.</p>
                      </div>
                  </div>

                  <div class="faq-item">
                      <div class="faq-question">
                          <h4>Is hernia surgery painful?</h4>
                          <span class="faq-toggle"><i class="fas fa-plus"></i></span>
                      </div>
                      <div class="faq-answer">
                          <p>Modern techniques like laparoscopic and robotic surgery involve minimal pain. Most patients experience mild discomfort that improves quickly during recovery.</p>
                      </div>
                  </div>

                  <div class="faq-item">
                      <div class="faq-question">
                          <h4>How long does it take to recover after surgery?</h4>
                          <span class="faq-toggle"><i class="fas fa-plus"></i></span>
                      </div>
                      <div class="faq-answer">
                          <p>Recovery time depends on the type of surgery, but most patients can return to normal activities within a few days to a couple of weeks.</p>
                      </div>
                  </div>

                  <div class="faq-item">
                      <div class="faq-question">
                          <h4>Who is the top hernia surgeon in Delhi?</h4>
                          <span class="faq-toggle"><i class="fas fa-plus"></i></span>
                      </div>
                      <div class="faq-answer">
                          <p>Dr. Aloy Mukherjee is considered one of the top hernia surgeons in Delhi, known for his expertise and successful treatment outcomes.</p>
                      </div>
                  </div>

                  <div class="faq-item">
                      <div class="faq-question">
                          <h4>Can a hernia come back after surgery?</h4>
                          <span class="faq-toggle"><i class="fas fa-plus"></i></span>
                      </div>
                      <div class="faq-answer">
                          <p>While recurrence is rare, it can happen in some cases. Following post-surgery guidelines and maintaining a healthy lifestyle can help reduce the risk.</p>
                      </div>
                  </div>
              </div>'

$rgxObj5 = [regex] '(?s)<div class="faq-container fade-in-up">.*?</div>\s*</div>\s*</section>'
$html = $rgxObj5.Replace($html, $faq_html + "`r`n          </div>`r`n      </section>", 1)

$utf8NoBom = New-Object System.Text.UTF8Encoding $false
[System.IO.File]::WriteAllText('hernia-surgery.html', $html, $utf8NoBom)
Write-Host "Update completed successfully."
