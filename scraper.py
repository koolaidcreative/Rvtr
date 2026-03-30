from pywebcopy import save_website
import sys

def scrape():
    print("Starting site scrape for rvtr.com...")
    try:
        save_website(
            url="https://rvtr.com/",
            project_folder="/Users/sashasandler/AI Folder/rvtr-static-site/output",
            project_name="website",
            bypass_robots=True,
            debug=True,
            open_in_browser=False,
            delay=0.1,
            threaded=True,
        )
        print("Scrape completed successfully!")
    except Exception as e:
        print(f"Error during scrape: {e}")
        sys.exit(1)

if __name__ == "__main__":
    scrape()
