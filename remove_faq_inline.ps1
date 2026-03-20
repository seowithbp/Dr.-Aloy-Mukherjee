$htmlFiles = Get-ChildItem -Path $PWD -Filter "*.html"

# This regex matches the exact inline script found on service pages.
# It makes sure we only match a <script> block starting with the querySelector for '.faq-question'
$regex = '(?s)<script>\s*document\.addEventListener\(''DOMContentLoaded'', \(\) => \{\s*const faqs = document\.querySelectorAll\(''\.faq-question''\);.*?</script>'

foreach ($file in $htmlFiles) {
    $content = [System.IO.File]::ReadAllText($file.FullName)
    if ($content -match $regex) {
        $content = [regex]::Replace($content, $regex, "")
        [System.IO.File]::WriteAllText($file.FullName, $content, [System.Text.Encoding]::UTF8)
        Write-Host "Removed inline script from $($file.Name)"
    }
}
Write-Host "Script removal complete."
