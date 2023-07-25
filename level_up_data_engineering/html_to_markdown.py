
import re

html = "<p>This is a paragraph.</p><p>This is another\nparagraph.</p>"

def to_markdown(html):
    markdown = re.sub("<em>(.*?)</em>", r"*\1*", html)
    markdown = markdown.split()
    markdown = ' '.join(markdown)
    markdown = re.sub("<p>(.*?)</p>",r"\1\\n\\n", markdown)
    return markdown

print(to_markdown(html))