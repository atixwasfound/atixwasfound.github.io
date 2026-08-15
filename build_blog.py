import os
import glob
import re
import markdown
import frontmatter

def calculate_read_time(text):
    words = len(re.findall(r'\w+', text))
    minutes = max(1, round(words / 200))
    return f"{minutes} min read"

def build_blogs():
    print("Building blogs...")

    os.makedirs('blogs', exist_ok=True)

    with open('blog_template.html', 'r', encoding='utf-8') as f:
        template = f.read()
        
    md = markdown.Markdown(extensions=['fenced_code', 'tables', 'nl2br'])
    
    posts = []

    for filepath in glob.glob('content/blogs/*.md'):
        filename = os.path.basename(filepath)
        slug = filename[:-3]
        
        with open(filepath, 'r', encoding='utf-8') as f:
            post = frontmatter.load(f)
            
        title = post.get('title', 'Untitled')
        date = post.get('date', 'Unknown Date')
        desc = post.get('description', '')
        
        html_content = md.convert(post.content)
        read_time = calculate_read_time(post.content)

        page_html = template
        page_html = page_html.replace('{{title}}', title)
        page_html = page_html.replace('{{date}}', date)
        page_html = page_html.replace('{{read_time}}', read_time)
        page_html = page_html.replace('{{content}}', html_content)

        out_path = f"blogs/{slug}.html"
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(page_html)
            
        print(f"Generated {out_path}")
        
        posts.append({
            'title': title,
            'date': date,
            'desc': desc,
            'url': f"/{out_path}"
        })

    update_blog_index(posts)

def update_blog_index(posts):

    posts.reverse()
    
    cards_html = ""
    for p in posts:
        cards_html += f"""
            <a href="{p['url']}" class="bento-card group">
                <div class="flex flex-col h-full justify-between">
                    <div>
                        <h2 class="font-display text-2xl font-bold mb-3 text-gruvbox-fg group-hover:text-gruvbox-orange transition-colors">{p['title']}</h2>
                        <p class="text-gruvbox-fg2 mb-6 leading-relaxed">{p['desc']}</p>
                    </div>
                    <div class="flex items-center justify-between mt-4">
                        <span class="text-sm font-medium text-gruvbox-fg3">{p['date']}</span>
                        <i class="fas fa-arrow-right text-gruvbox-fg3 group-hover:text-gruvbox-orange transition-colors"></i>
                    </div>
                </div>
            </a>
"""

    with open('blog.html', 'r', encoding='utf-8') as f:
        content = f.read()
        
    pattern = r'(<!-- BLOG_CARDS_START -->)(.*?)(<!-- BLOG_CARDS_END -->)'
    new_content = re.sub(pattern, r'\1\n' + cards_html + r'            \3', content, flags=re.DOTALL)
    
    with open('blog.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print("Updated blog.html index.")

if __name__ == "__main__":
    build_blogs()
