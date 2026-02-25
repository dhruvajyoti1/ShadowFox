import requests
from bs4 import BeautifulSoup
import csv
import time

# STEP 1 — Fetch RandomUser.me homepage (for BS4 usage)
def fetch_html(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print("HTML Fetch Error:", e)
        return None

# STEP 2 — Parse HTML title using BeautifulSoup
def parse_html_title(html):
    soup = BeautifulSoup(html, "html.parser")
    return soup.title.text if soup.title else "No Title Found"

# STEP 3 — Fetch JSON User Data from RandomUser API
def fetch_randomuser_json():
    url = "https://randomuser.me/api/"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print("JSON Fetch Error:", e)
        return None

# STEP 4 — Extract important fields from JSON
def extract_user_details(data):
    user = data["results"][0]

    return {
        "Full Name": f"{user['name']['title']} {user['name']['first']} {user['name']['last']}",
        "Gender": user["gender"],
        "Email": user["email"],
        "Phone": user["phone"],
        "Age": user["dob"]["age"],
        "City": user["location"]["city"],
        "State": user["location"]["state"],
        "Country": user["location"]["country"],
        "Postcode": user["location"]["postcode"],
        "Profile Picture": user["picture"]["large"]
    }

# STEP 5 — Save extracted data to CSV
def save_csv(filename, data):
    if not data:
        print("Warning: No data to save.")
        return

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

    print(f"Data saved in clean tabular format into {filename}")


# STEP 6 — Main Scraper Class
class RandomUserScraper:
    def __init__(self, total_users=10):
        self.total_users = total_users
        self.html_url = "https://randomuser.me/"
        self.data = []

    def run(self):
        print("\nStarting RandomUser Web Scraper...\n")

        # Step 1: Fetch homepage HTML
        html = fetch_html(self.html_url)
        if html:
            title = parse_html_title(html)
            print("HTML Page Title:", title)
        else:
            print("Could not fetch homepage HTML.")

        # Step 2: Fetch multiple user profiles
        print("\nFetching user profiles from RandomUser API...\n")

        for i in range(1, self.total_users + 1):
            print(f"Fetching user {i}/{self.total_users}...")
            user_json = fetch_randomuser_json()

            if not user_json:
                print("Error fetching JSON data.")
                continue

            details = extract_user_details(user_json)
            self.data.append(details)

            print("User extracted:", details["Full Name"])

            time.sleep(1)  # Polite delay

        # Step 3: Save results to CSV
        save_csv("randomuser_users.csv", self.data)

        print("\nScraping Completed Successfully.\n")


# EXECUTE SCRAPER
if __name__ == "__main__":
    scraper = RandomUserScraper(total_users=10)
    scraper.run()