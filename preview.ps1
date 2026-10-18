Write-Host "Rendering Manim slides..." -ForegroundColor Cyan

manim-slides render presentation.py DigiFest

if ($LASTEXITCODE -ne 0) {
    Write-Host "Rendering failed!" -ForegroundColor Red
    exit 1
}

Write-Host "Converting to HTML..." -ForegroundColor Cyan

manim-slides convert --to html DigiFest DigiFest.html

if ($LASTEXITCODE -ne 0) {
    Write-Host "HTML conversion failed!" -ForegroundColor Red
    exit 1
}

Write-Host "Opening presentation..." -ForegroundColor Green

Start-Process ".\DigiFest.html"