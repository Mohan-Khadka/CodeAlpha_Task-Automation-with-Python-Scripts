import os
import re

def create_sample_contacts():
    """Create sample contacts file if it doesn't exist"""
    email_folder = "email_data"
    contacts_file = os.path.join(email_folder, "contacts.txt")
    
    if not os.path.exists(email_folder):
        os.makedirs(email_folder)
        print("Created 'email_data' folder")
    
    if not os.path.exists(contacts_file):
        sample_content = """Hello, my name is Ram.
My email is ram@gmail.com.

You can contact Sita at sita@gmail.com.
Another email is ram@gmail.com.

Company contact: info@company.org
Support: support@helpdesk.net
Manager: manager@project.io
Inquiries: inquiries@business.com
Emergency: emergency@emergency.org
Contact: contact@example.com
Tech team: tech@company.org
Sales: sales@company.org

Duplicate email: ram@gmail.com
Another duplicate: SITA@GMAIL.COM
"""
        with open(contacts_file, "w", encoding="utf-8") as file:
            file.write(sample_content)
        print("Created sample contacts.txt with email addresses")

def extract_emails():
    print("\n[Task 2] Email Address Extractor")
    print("-" * 40)
    
    # Define files
    input_file = "email_data/contacts.txt"
    output_folder = "output"
    output_file = "output/extracted_emails.txt"
    
    # Create sample contacts if missing
    if not os.path.exists(input_file):
        create_sample_contacts()
    
    # Check if input exists
    if not os.path.exists(input_file):
        print("Error: Could not create contacts.txt file")
        return
    
    # Create output folder
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print("Created folder: " + output_folder)
    
    # Read file
    print("Reading from: " + input_file)
    with open(input_file, "r", encoding="utf-8") as file:
        content = file.read()
    
    # Check if file is empty
    if not content.strip():
        print("Error: contacts.txt is empty!")
        print("Please add some text with email addresses")
        return
    
    # Find emails using regex
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(email_pattern, content)
    
    # Remove duplicates (keep order)
    unique_emails = []
    seen = set()
    for email in emails:
        email_lower = email.lower()
        if email_lower not in seen:
            seen.add(email_lower)
            unique_emails.append(email)
    
    # Check if any emails found
    if len(unique_emails) == 0:
        print("No email addresses found in the file.")
        return
    
    # Save to file
    with open(output_file, "w", encoding="utf-8") as file:
        for email in unique_emails:
            file.write(email + "\n")
    
    # Summary
    print("-" * 40)
    print("SUMMARY:")
    print("  Emails found: " + str(len(unique_emails)))
    print("  Output file: " + output_file)
    print("-" * 40)
    
    # Print emails
    print("\nExtracted emails:")
    for i, email in enumerate(unique_emails, 1):
        print("  " + str(i) + ". " + email)

if __name__ == "__main__":
    extract_emails()