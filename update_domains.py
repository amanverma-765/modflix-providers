import requests
import json

JSON_PATH = 'modflix.json'

def load_domains():
    with open(JSON_PATH, 'r') as f:
        return json.load(f)

def save_domains(data):
    with open(JSON_PATH, 'w') as f:
        json.dump(data, f, indent=4)

def get_final_url(start_url):
    try:
        response = requests.get(start_url, timeout=60, allow_redirects=True)
        final_url = response.url
        # Remove trailing slash if present
        if final_url.endswith('/'):
            final_url = final_url[:-1]
        return final_url
    except requests.RequestException as e:
        print(f"Error fetching {start_url}: {e}")
        return start_url


def update_domains():
    print("🔄 Checking and updating domains...")
    domains = load_domains()
    updated = []

    for entry in domains:
        old_url = entry['url']
        new_url = get_final_url(old_url)
        if new_url != old_url:
            print(f"✅ {entry['name']} updated: {old_url} → {new_url}")
        else:
            print(f"ℹ️  {entry['name']} unchanged.")
        entry['url'] = new_url
        updated.append(entry)

    save_domains(updated)
    print("✅ Update completed.\n")

if __name__ == '__main__':
    update_domains()

