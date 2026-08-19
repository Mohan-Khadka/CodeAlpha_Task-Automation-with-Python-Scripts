import os
import requests

def scrape_webpage_title():
    print("\n[Task 3] Webpage Title Scraper")
    print("-" * 40)
    
    # Define URL and output
    url = "https://example.com"
    output_folder = "output"
    output_file = "output/webpage_title.txt"
    
    # Create output folder
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print("Created folder: " + output_folder)
    
    print("Connecting to: " + url)
    
    try:
        # Send HTTP GET request
        response = requests.get(url, timeout=10)
        
        # Check if successful
        if response.status_code == 200:
            html = response.text
            
            # Extract title
            start = html.find("<title>")
            end = html.find("</title>")
            
            if start != -1 and end != -1:
                title = html[start+7:end]
                title = title.strip()
                
                # Save title
                with open(output_file, "w", encoding="utf-8") as file:
                    file.write(title)
                
                # Summary
                print("-" * 40)
                print("SUMMARY:")
                print("  Webpage: " + url)
                print("  Title: " + title)
                print("  Saved to: " + output_file)
                print("-" * 40)
            else:
                print("Error: Could not find title tag in HTML")
        else:
            print("Error: HTTP status code " + str(response.status_code))
            
    except requests.exceptions.ConnectionError:
        print("Error: No internet connection. Please check your network.")
    except requests.exceptions.Timeout:
        print("Error: Connection timeout. Please try again.")
    except requests.exceptions.RequestException as e:
        print("Error: " + str(e))
    except Exception as e:
        print("Unexpected error: " + str(e))

if __name__ == "__main__":
    scrape_webpage_title()