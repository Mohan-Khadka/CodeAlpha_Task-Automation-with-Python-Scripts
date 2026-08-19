import os
import sys

from image_file_organizer import organize_images
from email_extractor import extract_emails
from webpage_title_scraper import scrape_webpage_title

def show_menu():
    print("=" * 50)
    print("       AUTOMATIC TASK AUTOMATION")
    print("=" * 50)
    print("1. Image File Organizer")
    print("2. Email Address Extractor")
    print("3. Webpage Title Scraper")
    print("4. Run All Tasks")
    print("5. Exit")
    print("=" * 50)

def run_all():
    print("\n" + "=" * 50)
    print("RUNNING ALL TASKS...")
    print("=" * 50)
    organize_images()
    extract_emails()
    scrape_webpage_title()
    print("\n" + "=" * 50)
    print("ALL TASKS COMPLETED SUCCESSFULLY!")
    print("=" * 50)

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            organize_images()
        elif choice == "2":
            extract_emails()
        elif choice == "3":
            scrape_webpage_title()
        elif choice == "4":
            run_all()
        elif choice == "5":
            print("\nThank you for using Automatic Task Automation!")
            print("Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()