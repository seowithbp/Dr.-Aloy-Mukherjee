$servicePages = @{
    "achalasia-cardia-treatment.html" = @{ name = "Achalasia Cardia Treatment"; keywords = @("Best Surgeon for Achalasia Cardia Treatment in Delhi", "Achalasia Cardia Treatment in Delhi") }
    "adrenal-gland-removal.html" = @{ name = "Adrenal Gland Removal"; keywords = @("Best Surgeon for Adrenal Gland Removal in Delhi", "Adrenal Gland Removal in Delhi") }
    "appendix-surgery.html" = @{ name = "Appendix Surgery"; keywords = @("Best Appendix Surgeon in Delhi", "Appendix Surgery in Delhi") }
    "colorectal-surgery.html" = @{ name = "Colorectal Surgery"; keywords = @("Best Colorectal Surgeon in Delhi", "Colorectal Surgery in Delhi") }
    "bariatric-surgery.html" = @{ name = "Bariatric Surgery"; keywords = @("Best Bariatric Surgeon in Delhi", "Bariatric Surgery in Delhi") }
    "endoscopic-anorectal-surgery.html" = @{ name = "Endoscopic Anorectal Surgery"; keywords = @("Best Surgeon for Endoscopic Anorectal Surgery in Delhi", "Endoscopic Anorectal Surgery in Delhi") }
    "gallbladder-surgery.html" = @{ name = "Gallbladder Surgery"; keywords = @("Best Gallbladder Surgeon in Delhi", "Gallbladder Surgery in Delhi") }
    "gastric-bypass-surgery.html" = @{ name = "Gastric Bypass Surgery"; keywords = @("Best Surgeon for Gastric Bypass Surgery in Delhi", "Gastric Bypass Surgery in Delhi") }
    "hernia-surgery.html" = @{ name = "Hernia Surgery"; keywords = @("Best Hernia Surgeon in Delhi", "Hernia Surgery in Delhi") }
    "hiatus-hernia.html" = @{ name = "Hiatus Hernia"; keywords = @("Best Surgeon for Hiatus Hernia in Delhi", "Hiatus Hernia in Delhi") }
    "laser-piles-treatment.html" = @{ name = "Laser Piles Treatment"; keywords = @("Best Doctor for Laser Piles Treatment in Delhi", "Laser Piles Treatment in Delhi") }
    "myasthenia-gravis-surgery.html" = @{ name = "Myasthenia Gravis Surgery"; keywords = @("Best Surgeon for Myasthenia Gravis in Delhi", "Myasthenia Gravis Surgery in Delhi") }
    "pilonidal-sinus-treatment.html" = @{ name = "Pilonidal Sinus Treatment"; keywords = @("Best Doctor for Pilonidal Sinus in Delhi", "Pilonidal Sinus Treatment in Delhi") }
    "robotic-surgery.html" = @{ name = "Robotic Surgery"; keywords = @("Best Robotic Surgeon in Delhi", "Robotic Surgery in Delhi") }
    "test-hernia.html" = @{ name = "Hernia Surgery"; keywords = @("Best Hernia Surgeon in Delhi", "Hernia Surgery in Delhi") }
    "thyroid-surgery.html" = @{ name = "Thyroid Surgery"; keywords = @("Best Thyroid Surgeon in Delhi", "Thyroid Surgery in Delhi") }
    "varicocelectomy-surgery.html" = @{ name = "Varicocelectomy Surgery"; keywords = @("Best Varicocelectomy Surgeon in Delhi", "Varicocelectomy Surgery in Delhi") }
}

foreach ($item in $servicePages.GetEnumerator()) {
    $filename = $item.Key
    $data = $item.Value
    
    $filePath = Join-Path -Path $PWD -ChildPath $filename
    if (-Not (Test-Path $filePath)) {
        Write-Host "Skipping $filename"
        continue
    }

    $content = [System.IO.File]::ReadAllText($filePath)
    
    $kw1 = $data.keywords[0]
    $kw2 = $data.keywords[1]
    
    $singleReviewHtml = @"
<div class="reviews-track" id="reviews-track">
                      <div class="review-card">
                          <div class="review-stars"><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i></div>
                          <p class="review-text">"He gave me one of the best medical experiences I've had. For anyone looking for the $kw1, Dr. Aloy is the one. I strongly recommend him for $kw2. The entire process was seamless."</p>
                          <h5 class="review-patient-name">Rajesh Kumar</h5>
                      </div>
                  </div>
              </div>
              
"@

    # Use regex to match the entire reviews-track block
    $regex = '(?s)<div class="reviews-track" id="reviews-track">.*?(?=<div class="text-center mt-4 fade-in-up")'
    $newContent = [regex]::Replace($content, $regex, $singleReviewHtml)

    [System.IO.File]::WriteAllText($filePath, $newContent, [System.Text.Encoding]::UTF8)
    Write-Host "Updated $filename"
}

Write-Host "Done"
