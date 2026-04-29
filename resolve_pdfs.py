import os
import re
import urllib.parse
import requests
import hashlib

DIRECTORY = '/Users/sashasandler/AI Folder/rvtr-static-site'
PDF_DIR = os.path.join(DIRECTORY, 'assets', 'pdfs')

def get_relative_depth(filepath):
    rel_path = os.path.relpath(filepath, DIRECTORY)
    depth = rel_path.count(os.sep)
    return '../' * depth if depth > 0 else './'

def resolve_pdfs():
    os.makedirs(PDF_DIR, exist_ok=True)
    success = 0
    modified_files = 0
    
    # Regex to find <a href="...">
    link_pattern = re.compile(r'(<a\s+[^>]*href=["\'])([^"\']+)(["\'][^>]*>)', re.IGNORECASE)

    for root, dirs, files in os.walk(DIRECTORY):
        if 'node_modules' in root or '.git' in root or 'assets' in root or 'monograph-media' in root:
            continue
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        html_content = f.read()
                        
                    depth_prefix = get_relative_depth(filepath)
                    modified = False
                    
                    def repl_func(match):
                        nonlocal modified
                        prefix = match.group(1)
                        href = match.group(2)
                        suffix = match.group(3)
                        
                        href_lower = href.lower()
                        is_pdf = False
                        
                        if href_lower.endswith('.pdf') or '.pdf?' in href_lower:
                            is_pdf = True
                        elif 'dropbox.com' in href_lower:
                            is_pdf = True
                        elif 's3.amazonaws.com' in href_lower and 'pdf' in href_lower:
                            is_pdf = True
                        elif 'drive.google.com' in href_lower:
                            is_pdf = True
                            
                        if is_pdf:
                            orig_href = href
                            if 'dropbox.com' in href_lower:
                                if 'dl=0' in href:
                                    href = href.replace('dl=0', 'dl=1')
                                elif 'dl=' not in href:
                                    href += '&dl=1' if '?' in href else '?dl=1'
                            
                            parsed_url = urllib.parse.urlparse(href)
                            filename = os.path.basename(parsed_url.path)
                            if not filename or filename == '' or filename == 'view':
                                url_hash = hashlib.md5(href.encode()).hexdigest()[:8]
                                filename = f"document_{url_hash}.pdf"
                            if not filename.lower().endswith('.pdf'):
                                filename += '.pdf'
                                
                            pdf_path = os.path.join(PDF_DIR, filename)
                            
                            if not os.path.exists(pdf_path):
                                print(f"Downloading PDF: {href}")
                                try:
                                    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'}
                                    response = requests.get(href, stream=True, timeout=15, headers=headers)
                                    if response.status_code == 200:
                                        with open(pdf_path, 'wb') as pdf_file:
                                            for chunk in response.iter_content(chunk_size=8192):
                                                pdf_file.write(chunk)
                                    else:
                                        print(f"Failed to download {href}: Status {response.status_code}")
                                except Exception as e:
                                    print(f"Failed to download {href}: {e}")
                                    
                            new_href = f"{depth_prefix}assets/pdfs/{filename}"
                            modified = True
                            return f"{prefix}{new_href}{suffix}"
                        
                        return match.group(0)

                    new_content = link_pattern.sub(repl_func, html_content)

                    if modified:
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        modified_files += 1
                    success += 1

                except Exception as e:
                    print(f"Failed processing {filepath}: {e}")
                    
    print(f"Successfully processed {success} HTML files. {modified_files} files were modified with new PDF links.")

if __name__ == "__main__":
    resolve_pdfs()
