import json
import copy

def assign_validate(hub_data):
    original_data = copy.deepcopy(hub_data)  #to make a deep copy of the original hub data

    first_serial_number = "C25CTW000000000014"
    serial_number_range = range(1470, 1479) #the last 4 digits as specified

    hubs = hub_data['Internet_hubs']
    sorted_hubs = sorted(hubs, key=lambda hub: hub['id'][-1], reverse=True)

    for i, hub in enumerate(sorted_hubs):
        if hub['id'] != "men1": #leave the first since it already has a serial no
            four_last_digit = str(serial_number_range[len(serial_number_range) - 1 - i])
            hub['serial_number'] = first_serial_number + four_last_digit
    

    # return the original and updated data
    return original_data, hub_data


# sample input data
hub_data = {
    "comment": "Do NOT commit local changes to this file to source control",
    "Internet_hubs": [
   {"id": "men1", "serial_number": "C25CTW00000000001470"},
   {"id": "mn1", "serial_number": "<serial number here>"},
   {"id": "mn2", "serial_number": "<serial number here>"},
   {"id": "mn3", "serial_number": "<serial number here>"},
   {"id": "mn4", "serial_number": "<serial number here>"},
   {"id": "mn5", "serial_number": "<serial number here>"},
   {"id": "mn6", "serial_number": "<serial number here>"},
   {"id": "mn7", "serial_number": "<serial number here>"},
   {"id": "mn8", "serial_number": "<serial number here>"},
   {"id": "mn9", "serial_number": "<serial number here>"}
 ]
}

# Validate and assign serial numbers
original_hub_data, updated_hub_data = assign_validate(hub_data)

# Print both the original and updated JSON objects
print("Original Data:")
print(json.dumps(original_hub_data, indent=2))

print("\nUpdated Data:")
print(json.dumps(updated_hub_data, indent=2))

