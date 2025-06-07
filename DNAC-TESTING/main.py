from dnac_client import get_token, get_devices

def display_devices(devices):
    print(f"{'Hostname':<20} {'Type':<20} {'IP Address':<20} {'Platform'}")
    print("="*80)
    for dev in devices:
        print(f"{dev.get('hostname', 'N/A'):<20} {dev.get('type', 'N/A'):<20} "
              f"{dev.get('managementIpAddress', 'N/A'):<20} {dev.get('platformId', 'N/A')}")

def main():
    token = get_token()
    devices = get_devices(token)
    display_devices(devices)

if __name__ == "__main__":
    main()
