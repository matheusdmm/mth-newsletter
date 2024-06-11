import json
import re
from datetime import datetime

now = datetime.now()
dateToday = now.strftime("%Y-%m-%d")
week = now.strftime("%U")

with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

with open('templates/template.html', 'r', encoding='utf-8') as f:
    template = f.read()

base64Pattern = re.compile(
    r'^([A-Za-z0-9+/]{4})*([A-Za-z0-9+/]{3}=|[A-Za-z0-9+/]{2}==)?$')

htmlContent = ""
for item in data['bullet_points']:
    htmlContent += f"<p style='padding-left: 60px;'><strong>&bull; {
        item['title']}</strong></p>\n"
    if item.get('description') and item['description'].strip():
        htmlContent += f"<p style='padding-left: 120px;'>{
            item['description']}</p>\n"
    if item['image']:
        if base64Pattern.fullmatch(item['image']):
            htmlContent += f"<p><strong><img style='display: block; margin-left: auto; margin-right: auto; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); border: 1px solid #ddd; max-width: 600px; max-height: 400px;' src='data:image/png;base64,{
                item['image']}' alt='{item['title']}' /></strong></p>\n <br/>"
        else:
            htmlContent += f"<p><strong><img style='display: block; margin-left: auto; margin-right: auto; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); border: 1px solid #ddd; max-width: 600px; max-height: 400px;' src='{
                item['image']}' alt='{item['title']}' /></strong></p>\n <br/>"


newsletterTitle = f'DigiCast newsletter - week {week}'
html_content = template.replace(
    '{bullet_points}', htmlContent).replace('{newsletter_title}', newsletterTitle)


newsletterName = f'newsletter-{dateToday}.html'

with open(f'output/{newsletterName}', 'w', encoding='utf-8') as f:
    f.write(html_content)
