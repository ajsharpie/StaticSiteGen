import os
import shutil
from block_to_html import markdown_to_html_node
from textnode import TextNode

def main():
    file = open('content/index.md')
    mdtext = file.read()
    file.close()

    
    os.mknod('publictest/test1.py')
    file = open('publictest/test1.py')
    file.write('thisisthetext')
    file.close()
    
    # copy_to_path('static', 'public')
    # generate_page('content/index.md', 'template.html', 'public/index.html')
    pass
        
def copy_to_path(src, dest):
    shutil.rmtree(dest, ignore_errors=True)
    os.mkdir(dest)
    if os.path.exists(src) and os.path.exists(dest):
        contents = os.listdir(src)
        for p in contents:
            if not os.path.isfile(os.path.join(src, p)):
                copy_to_path(os.path.join(src, p), os.path.join(dest, p))
            else:
                shutil.copy(os.path.join(src, p), os.path.join(dest, p))
                
def extract_title(markdown):
    for line in markdown.splitlines():
        if line.startswith('# '):
            return line[2:].strip()
        
def generate_page(from_path, template_path, dest_path):
    print(f'generating page: from {from_path}, to {dest_path}, using {template_path}')
    
    if os.file.exists(from_path) and os.file.exists(template_path) and os.file.exists(dest_path):
        file = open(from_path)
        mdtext = file.read()
        file.close()
        
        file = open(template_path)
        template = file.read()
        file.close()

        content = markdown_to_html_node(mdtext).to_html()
        title = extract_title(mdtext)
        
        template.replace('{{ Title }}', title)
        template.replace('{{ Content }}', content)
        
        dirname = os.path.dirname(dest_path)
        
        if not os.path.exists(dirname):
            os.makedirs(dirname)
        
        file = open()
        
        
        
        
        
        
        
        
        
        
    else:
        raise Exception('Path error, check inputs')

if __name__== "__main__":
    main()

 