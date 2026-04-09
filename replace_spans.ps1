$htmlFiles = Get-ChildItem -Path "src", "public" -Filter "*.html" -Recurse -ErrorAction SilentlyContinue

$totalReplacements = 0

foreach ($file in $htmlFiles) {
    $content = Get-Content $file.FullName -Raw
    $originalContent = $content
    
    # Pattern to find the problematic span
    $spanPattern = '<span class="material-symbols-outlined icon-neutral" style=" vertical-align: -2px; margin-right: 4px;">[^<]*</span>'
    
    # Find all matches
    $matches = [regex]::Matches($content, $spanPattern)
    
    # Process matches in reverse order to maintain string indices
    for ($i = $matches.Count - 1; $i -ge 0; $i--) {
        $match = $matches[$i]
        $spanText = $match.Value
        $spanEndIndex = $match.Index + $match.Length
        
        # Get text after the span (up to 200 characters or next HTML tag)
        $remaining = $content.Substring($spanEndIndex)
        $contextMatch = [regex]::Match($remaining, '^[^<]{0,200}')
        $context = $contextMatch.Value
        
        # Determine replacement icon based on following text
        $icon = $null
        
        if ($context -match "(Livrée|delivered)") {
            $icon = "done"
        } elseif ($context -match "(Active|active)") {
            $icon = "check_circle"
        } elseif ($context -match "(Suspendue|suspended)") {
            $icon = "block"
        } elseif ($context -match "(email|contact|@)") {
            $icon = "mail"
        } elseif ($context -match "(phone|tel|\+)") {
            $icon = "phone"
        }
        
        if ($icon) {
            $newSpan = '<span class="material-symbols-outlined icon-neutral" style=" vertical-align: -2px; margin-right: 4px;">' + $icon + '</span>'
            $content = $content.Substring(0, $match.Index) + $newSpan + $content.Substring($spanEndIndex)
            $totalReplacements++
            Write-Host "Replaced in $($file.FullName): found '$($context.Substring(0, [Math]::Min(40, $context.Length)))...' -> icon: $icon"
        }
    }
    
    # Write back if changed
    if ($content -ne $originalContent) {
        Set-Content $file.FullName $content
    }
}

Write-Host ""
Write-Host "========================================="
Write-Host "Total replacements made: $totalReplacements"
Write-Host "========================================="
