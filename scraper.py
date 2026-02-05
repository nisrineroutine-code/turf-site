import requests
from bs4 import BeautifulSoup

def get_real_pronos():
    url = "https://www.coin-turf.com/"
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Hna l-bot kayقلب 3la l-khil f l-site
        # Coin-turf kista3mlo souvent des tableaux (td)
        cells = soup.find_all('td')
        prono_list = []
        
        for cell in cells:
            text = cell.get_text().strip()
            # Kan-قلبوا 3la l-khayl li fihom 2 arqam (mital: 04, 12...)
            if text.isdigit() and len(text) <= 2:
                prono_list.append(text)
        
        # Kan-akhdou awel 8 d-l-khil lqina f l-pronostic
        final_prono = " - ".join(prono_list[:8])
        return final_prono if final_prono else "00 - 00 - 00 - 00 - 00 - 00 - 00 - 00"
    
    except Exception as e:
        print(f"Erreur: {e}")
        return "Service Indisponible"

def update_html(new_numbers):
    with open("index.html", "r", encoding="utf-8") as f:
        html_content = f.read()

    # Hna l-bot ghadi i-qleb 3la ay 8 d-l-arkam f l-blassa d-l-prono w i-badalhom
    # Khass t-koun l-joumla tamaman bhal li f index.html
    import re
    pattern = r"\d{2} - \d{2} - \d{2} - \d{2} - \d{2} - \d{2} - \d{2} - \d{2}"
    new_html = re.sub(pattern, new_numbers, html_content)

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(new_html)

# Khaddam l-khidma
arkam = get_real_pronos()
update_html(arkam)
print(f"تم تحديث الأرقام بنجاح: {arkam}")
