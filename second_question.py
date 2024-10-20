import requests
import csv
import os
import pandas as pd

# Function to fetch customer numbers from the API
def fetch_total_customer_numbers(api_key):
    url = "https://pysoftware.com/v1/customer_numbers"
    headers = {"X-API-KEY": api_key}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return int(response.text)  # Assuming the response contains the customer count as plain text
    else:
        raise Exception(f"Failed to fetch customer numbers. Status code: {response.status_code}")

# Function to fetch customer address by customer number
def fetch_customer_address(customer_number, api_key):
    url = f"https://pysoftware.com/v1/address_inventory/{customer_number}"
    headers = {"X-API-KEY": api_key}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()  # Returns the address in JSON format
    else:
        raise Exception(f"Failed to fetch address for customer {customer_number}. Status code: {response.status_code}")

# Function to validate and clean address data
def validate_address_data(address):
    required_fields = ["first_name", "last_name", "street", "postcode", "state", "country", "lat", "lon"]
    
    for field in required_fields:
        if field not in address or not address[field]:
            return False  # Return False if a required field is missing or empty
    
    # Additional validation (e.g., correct lat/lon range, postcode format, etc.) can be added here
    return True

# Function to fetch, validate, and write all customer addresses to CSV
def get_all_customer_addresses(api_key, csv_file_name):
    total_customers = fetch_total_customer_numbers(api_key)
    addresses = []
    
    # Fetch each customer's address
    for customer_number in range(1, total_customers + 1):
        try:
            address = fetch_customer_address(customer_number, api_key)
            
            if validate_address_data(address):
                addresses.append(address)
            else:
                print(f"Invalid address for customer {customer_number}. Skipping.")
                
        except Exception as e:
            print(e)
    
    # Write addresses to CSV
    keys = addresses[0].keys()  # Assuming all addresses have the same fields
    csv_file_path = os.path.join(os.getcwd(), csv_file_name)
    
    with open(csv_file_path, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=keys)
        writer.writeheader()
        writer.writerows(addresses)
    
    # Return file path and addresses in tabular form
    print(f"CSV file saved at: {csv_file_path}")
    return addresses, pd.DataFrame(addresses)

# Main function to execute the functionality
def main():
    # The API key for authorization
    api_key = "ssfdsjfksjdhfgjfgvjdshgvshgkjsdlgvkjsdgjkl"
    
    # Name of the CSV file to be created
    csv_file_name = "customer_addresses.csv"
    
    # Fetch all addresses and save them to CSV
    try:
        addresses, addresses_df = get_all_customer_addresses(api_key, csv_file_name)
        
        # Output: CSV file path and table of addresses
        print("\nCustomer Addresses in Tabular Form:")
        print(addresses_df)
        
    except Exception as e:
        print(f"An error occurred: {e}")

# Execute the main function
if __name__ == "__main__":
    main()
