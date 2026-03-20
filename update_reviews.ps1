$servicePages = @(
    @("achalasia-cardia-treatment.html", "Achalasia Cardia Treatment", "Best Surgeon for Achalasia Cardia Treatment in Delhi", "Achalasia Cardia Treatment in Delhi"),
    @("adrenal-gland-removal.html", "Adrenal Gland Removal", "Best Surgeon for Adrenal Gland Removal in Delhi", "Adrenal Gland Removal in Delhi"),
    @("appendix-surgery.html", "Appendix Surgery", "Best Appendix Surgeon in Delhi", "Appendix Surgery in Delhi"),
    @("colorectal-surgery.html", "Colorectal Surgery", "Best Colorectal Surgeon in Delhi", "Colorectal Surgery in Delhi"),
    @("bariatric-surgery.html", "Bariatric Surgery", "Best Bariatric Surgeon in Delhi", "Bariatric Surgery in Delhi"),
    @("endoscopic-anorectal-surgery.html", "Endoscopic Anorectal Surgery", "Best Surgeon for Endoscopic Anorectal Surgery in Delhi", "Endoscopic Anorectal Surgery in Delhi"),
    @("gallbladder-surgery.html", "Gallbladder Surgery", "Best Gallbladder Surgeon in Delhi", "Gallbladder Surgery in Delhi"),
    @("gastric-bypass-surgery.html", "Gastric Bypass Surgery", "Best Surgeon for Gastric Bypass Surgery in Delhi", "Gastric Bypass Surgery in Delhi"),
    @("hernia-surgery.html", "Hernia Surgery", "Best Hernia Surgeon in Delhi", "Hernia Surgery in Delhi"),
    @("hiatus-hernia.html", "Hiatus Hernia", "Best Surgeon for Hiatus Hernia in Delhi", "Hiatus Hernia Treatment in Delhi"),
    @("laser-piles-treatment.html", "Laser Piles Treatment", "Best Doctor for Laser Piles Treatment in Delhi", "Laser Piles Treatment in Delhi"),
    @("myasthenia-gravis-surgery.html", "Myasthenia Gravis Surgery", "Best Surgeon for Myasthenia Gravis in Delhi", "Myasthenia Gravis Surgery in Delhi"),
    @("pilonidal-sinus-treatment.html", "Pilonidal Sinus Treatment", "Best Doctor for Pilonidal Sinus in Delhi", "Pilonidal Sinus Treatment in Delhi"),
    @("robotic-surgery.html", "Robotic Surgery", "Best Robotic Surgeon in Delhi", "Robotic Surgery in Delhi"),
    @("test-hernia.html", "Hernia Surgery", "Best Hernia Surgeon in Delhi", "Hernia Surgery in Delhi"),
    @("thyroid-surgery.html", "Thyroid Surgery", "Best Thyroid Surgeon in Delhi", "Thyroid Surgery in Delhi"),
    @("varicocelectomy-surgery.html", "Varicocelectomy Surgery", "Best Varicocelectomy Surgeon in Delhi", "Varicocelectomy Surgery in Delhi")
)

foreach ($page in $servicePages) {
    $filename = $page[0]
    $name = $page[1]
    $kw1 = $page[2]
    $kw2 = $page[3]

    $filepath = Join-Path (Get-Location) $filename
    if (-Not (Test-Path $filepath)) { continue }

    $content = Get-Content -Raw -Encoding UTF8 $filepath

    # Standard reviews
    $rev1_pattern = '<p class="review-text">"He gave me one of the best medical experiences I''ve had[^<]*</p>'
    $rev1_repl = '<p class="review-text">"He gave me one of the best medical experiences I''ve had. For anyone looking for the ' + $kw1 + ', Dr. Aloy is the one. The staff was supportive and he explained everything in detail."</p>'
    
    $rev2_pattern = '<p class="review-text">"The facility is clean and modern, with advanced tools[^<]*</p>'
    $rev2_repl = '<p class="review-text">"The facility is clean and modern, with advanced tools. I would strongly recommend Dr. Mukherjee for ' + $kw2 + '. The recovery was very fast."</p>'
    
    $rev3_pattern = '<p class="review-text">"Doctor was very patient in explaining everything before the surgery[^<]*</p>'
    $rev3_repl = '<p class="review-text">"Doctor was very patient in explaining everything before the surgery. The entire process here for ' + $name.ToLower() + ' is seamless and the recovery is much faster than I expected."</p>'
    
    $rev4_pattern = '<p class="review-text">"His 25 years of experience really show[^<]*</p>'
    $rev4_repl = '<p class="review-text">"His 25 years of experience really show. Very professional and calming demeanor while discussing my operation. If you need a top specialist in Delhi, he is extremely helpful."</p>'

    $content = [regex]::Replace($content, $rev1_pattern, $rev1_repl)
    $content = [regex]::Replace($content, $rev2_pattern, $rev2_repl)
    $content = [regex]::Replace($content, $rev3_pattern, $rev3_repl)
    $content = [regex]::Replace($content, $rev4_pattern, $rev4_repl)

    # Bariatric specific handling
    if ($filename -eq "bariatric-surgery.html") {
        # Fix bariatric specific text
        # But wait, did Bariatric Surgery get the "standard" reviews? 
        # In `bariatric-surgery.html` the review patient is `Priya J.`
        
        # Original bariatric specific patterns:
        $bar1_pattern = '<p class="review-text">"My weight has always been a struggle[^<]*</p>'
        $bar1_repl = '<p class="review-text">"My weight has always been a struggle, but finding the ' + $kw1 + ' changed my life. Dr. Aloy is truly a lifesaver."</p>'
        
        $bar2_pattern = '<p class="review-text">"The decision to get bariatric surgery was terrifying[^<]*</p>'
        $bar2_repl = '<p class="review-text">"The decision to undergo this was terrifying, but getting ' + $kw2 + ' with Dr. Mukherjee was my best decision ever."</p>'
        
        $bar3_pattern = '<p class="review-text">"After years of trying everything[^<]*</p>'
        $bar3_repl = '<p class="review-text">"After years of trying everything, Dr. Mukherjee''s expertise made all the difference. I wish I had done it sooner with the top specialist!"</p>'

        $content = [regex]::Replace($content, $bar1_pattern, $bar1_repl)
        $content = [regex]::Replace($content, $bar2_pattern, $bar2_repl)
        $content = [regex]::Replace($content, $bar3_pattern, $bar3_repl)
    }

    Set-Content -Path $filepath -Value $content -Encoding UTF8
}

Write-Output "Reviews updated successfully"
