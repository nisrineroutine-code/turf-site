import os

# Hna tkhayel l-bot ghadi i-jbed had l-arkam (ghadi n-bedloha mn ba3d)
arkam_jdid = "10 - 02 - 14 - 05 - 08 - 11 - 03"

with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Had l-bot kital9a l-joumla dial l-arkam w i-badalha
old_numbers = "04 - 07 - 12 - 03 - 09 - 15 - 08 - 01"
new_html = html_content.replace(old_numbers, arkam_jdid)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(new_html)
