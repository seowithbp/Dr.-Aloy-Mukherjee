$htmlFiles = Get-ChildItem -Path $PWD -Filter "*.html"
$utf8NoBom = New-Object System.Text.UTF8Encoding $false

foreach ($file in $htmlFiles) {
    # Check if file has BOM by reading bytes
    $bytes = [System.IO.File]::ReadAllBytes($file.FullName)
    if ($bytes.Length -ge 3 -and $bytes[0] -eq 0xEF -and $bytes[1] -eq 0xBB -and $bytes[2] -eq 0xBF) {
        # Read the file as string
        $content = [System.IO.File]::ReadAllText($file.FullName)
        
        # Write back without BOM
        [System.IO.File]::WriteAllText($file.FullName, $content, $utf8NoBom)
        Write-Host "Removed UTF-8 BOM from $($file.Name)"
    }
}
Write-Host "Finished BOM removal."
