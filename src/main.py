import os
import shutil
from block_to_html import markdown_to_html_node
from textnode import TextNode

def main():
    
    copy_to_path('static', 'public')
    generate_pages_recursive('content', 'template.html', 'public')

      
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
    
    if os.path.exists(from_path) and os.path.exists(template_path):
        file = open(from_path)
        mdtext = file.read()
        file.close()
        
        file = open(template_path)
        template = file.read()
        file.close()

        content = markdown_to_html_node(mdtext).to_html()
        title = extract_title(mdtext)
        
        template = template.replace(f'{{{{ Title }}}}', title)
        template = template.replace(f'{{{{ Content }}}}', content)
        
        dirname = os.path.dirname(dest_path)
        
        if not os.path.exists(dirname):
            os.makedirs(dirname)
        
        file = open(dest_path, 'x')
        file.write(template)
        file.close()
           
        
        
    else:
        raise Exception('Path error, check inputs')

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    contents = os.listdir(dir_path_content)
    for item in contents:
        if item[-3:] == '.md':
            item_name = item[:-3]+'.html'
            generate_page(dir_path_content+'/'+item, template_path, dest_dir_path+'/'+item_name)
        if os.path.isdir(dir_path_content+'/'+item):
            generate_pages_recursive(dir_path_content+'/'+item, template_path, dest_dir_path+'/'+item)
        else:
            continue
        
    print('done')
if __name__== "__main__":
    main()

 