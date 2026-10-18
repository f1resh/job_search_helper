#!/usr/bin/env python3
"""
Markdown to PDF Converter for CVs and Reports.
Uses Python Markdown with clean ATS-friendly CSS and Google Chrome Headless.
"""

import sys
import os
import argparse
import subprocess
import tempfile
import markdown

DEFAULT_CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

CV_CSS = """
@page {
    size: A4;
    margin: 12mm 13mm 12mm 13mm;
}

@media print {
    body {
        -webkit-print-color-adjust: exact;
        print-color-adjust: exact;
    }
    .page-break {
        page-break-before: always;
    }
    h1, h2, h3, .job-header {
        page-break-after: avoid;
    }
    ul, ol, p {
        page-break-inside: auto;
    }
    li {
        page-break-inside: avoid;
    }
}

* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    color: #1a202c;
    background: #ffffff;
    line-height: 1.38;
    font-size: 9.5pt;
    padding: 0;
}

h1 {
    font-size: 20pt;
    font-weight: 700;
    color: #0f172a;
    letter-spacing: -0.02em;
    margin-bottom: 4px;
    text-transform: uppercase;
}

h2 {
    font-size: 11pt;
    font-weight: 700;
    color: #0f172a;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    border-bottom: 1.5px solid #0f172a;
    padding-bottom: 2px;
    margin-top: 11px;
    margin-bottom: 6px;
}

h3 {
    font-size: 10pt;
    font-weight: 600;
    color: #1e293b;
    margin-top: 7px;
    margin-bottom: 2px;
}

p {
    margin-bottom: 5px;
    color: #334155;
}

a {
    color: #0369a1;
    text-decoration: none;
}

a:hover {
    text-decoration: underline;
}

strong {
    color: #0f172a;
    font-weight: 600;
}

em {
    color: #475569;
    font-style: italic;
}

hr {
    border: 0;
    height: 1px;
    background: #e2e8f0;
    margin: 8px 0;
}

ul {
    margin-left: 18px;
    margin-bottom: 6px;
}

li {
    margin-bottom: 2px;
    color: #334155;
    line-height: 1.38;
}

li::marker {
    color: #0284c7;
}

/* Contact bar */
p:first-of-type strong {
    color: #475569;
}

/* Tables for skills */
table {
    width: 100%;
    border-collapse: collapse;
    margin: 8px 0 12px 0;
    font-size: 9.5pt;
}

th, td {
    padding: 5px 8px;
    text-align: left;
    border-bottom: 1px solid #e2e8f0;
}

th {
    background-color: #f8fafc;
    color: #0f172a;
    font-weight: 600;
    font-size: 9pt;
    text-transform: uppercase;
    letter-spacing: 0.04em;
}

tr:nth-child(even) td {
    background-color: #fcfcfd;
}

/* Code / Tech tags */
code {
    background-color: #f1f5f9;
    color: #0369a1;
    padding: 1px 4px;
    border-radius: 3px;
    font-size: 9pt;
    font-family: Consolas, "Liberation Mono", Menlo, Courier, monospace;
}

blockquote {
    border-left: 3px solid #0284c7;
    background: #f8fafc;
    padding: 6px 12px;
    margin: 8px 0;
    color: #475569;
    font-size: 9pt;
}
"""

def convert_md_to_html(md_content: str, title: str = "Curriculum Vitae") -> str:
    extensions = [
        "extra",
        "tables",
        "sane_lists",
        "smarty"
    ]
    html_body = markdown.markdown(md_content, extensions=extensions)
    
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
{CV_CSS}
    </style>
</head>
<body>
{html_body}
</body>
</html>
"""
    return html

def print_to_pdf_chrome(html_path: str, output_pdf_path: str, chrome_path: str = DEFAULT_CHROME_PATH):
    if not os.path.exists(chrome_path):
        raise FileNotFoundError(
            f"Google Chrome executable not found at: {chrome_path}\n"
            "Please verify Chrome is installed or specify the path via --chrome argument."
        )

    abs_html_path = os.path.abspath(html_path)
    abs_pdf_path = os.path.abspath(output_pdf_path)

    cmd = [
        chrome_path,
        "--headless=new",
        "--disable-gpu",
        "--no-pdf-header-footer",
        "--run-all-compositor-stages-before-draw",
        f"--print-to-pdf={abs_pdf_path}",
        f"file:///{abs_html_path.replace(os.sep, '/')}"
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"Chrome failed to generate PDF. Return code: {result.returncode}\nStderr: {result.stderr}")
    
    if not os.path.exists(abs_pdf_path):
        raise RuntimeError(f"PDF file was not created at expected path: {abs_pdf_path}")

    return abs_pdf_path

def convert_file(input_md_path: str, output_pdf_path: str = None, chrome_path: str = DEFAULT_CHROME_PATH) -> str:
    if not os.path.exists(input_md_path):
        raise FileNotFoundError(f"Input markdown file not found: {input_md_path}")

    with open(input_md_path, "r", encoding="utf-8") as f:
        md_text = f.read()

    # Determine title from first heading if present
    title = "Document"
    for line in md_text.splitlines():
        if line.startswith("# "):
            title = line[2:].strip()
            break

    html_content = convert_md_to_html(md_text, title=title)

    if not output_pdf_path:
        base, _ = os.path.splitext(input_md_path)
        output_pdf_path = f"{base}.pdf"

    # Save temp HTML file in the same folder or tempdir
    temp_html_path = os.path.splitext(output_pdf_path)[0] + "_temp_render.html"
    try:
        with open(temp_html_path, "w", encoding="utf-8") as f:
            f.write(html_content)

        pdf_path = print_to_pdf_chrome(temp_html_path, output_pdf_path, chrome_path)
    finally:
        if os.path.exists(temp_html_path):
            try:
                os.remove(temp_html_path)
            except OSError:
                pass

    return pdf_path

def main():
    parser = argparse.ArgumentParser(description="Convert Markdown CV / document to PDF using Chrome Headless.")
    parser.add_argument("input", help="Path to input .md file")
    parser.add_argument("output", nargs="?", default=None, help="Path to output .pdf file (optional)")
    parser.add_argument("--chrome", default=DEFAULT_CHROME_PATH, help=f"Path to Chrome executable (default: {DEFAULT_CHROME_PATH})")

    args = parser.parse_args()

    try:
        pdf_path = convert_file(args.input, args.output, args.chrome)
        print(f"[SUCCESS] PDF successfully generated: {pdf_path}")
    except Exception as e:
        print(f"[ERROR] {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
