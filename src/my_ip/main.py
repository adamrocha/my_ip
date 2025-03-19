import requests

def get_ip():
    try:
        #response = requests.get("https://api64.ipify.org?format=json")
        response = requests.get("https://ident.me/json")
        response.raise_for_status()
        ip_data = response.json()
        print(f"Your public IP address is: {ip_data['ip']}")
    except requests.RequestException as e:
        print(f"Error fetching IP: {e}")

if __name__ == "__main__":
    get_ip()

