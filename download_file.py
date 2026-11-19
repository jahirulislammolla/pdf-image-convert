import geopandas as gpd
import requests
import time

# GBIF API endpoint
GBIF_DOWNLOAD_API = "https://api.gbif.org/v1/occurrence/download/request"

# GBIF login credentials
USERNAME = "jahirju1995"
PASSWORD = "jahirju1995"

# Path to your shapefile
SHAPEFILE_PATH = "bgd/bgd.shp"



def shapefile_to_wkt(shapefile_path):
    """Convert the shapefile geometry to WKT format."""
    gdf = gpd.read_file(shapefile_path)
    # Assuming the shapefile has multiple geometries, combine them into one
    geometry = gdf.geometry.union_all()  # Replace deprecated unary_union with union_all
    return geometry.wkt


def create_download_request(wkt_geometry):
    """Create a download request for GBIF data filtered by country and geometry."""
    # Filter: Country (Canada) and Geometry (shapefile area)
    filter_data = {
        "creator": USERNAME,
        "format": "DWCA",  # Changed format to DWCA (Darwin Core Archive)
        "predicate": {
            "type": "and",
            "predicates": [
                {"type": "equals", "key": "COUNTRY", "value": "CA"},  # Country filter
                {"type": "within", "geometry": wkt_geometry},  # Geometry filter
            ]
        }
    }

    # Debug: Print the JSON payload
    print("JSON Payload Sent:", filter_data)

    # Send the request
    response = requests.post(GBIF_DOWNLOAD_API, json=filter_data, auth=(USERNAME, PASSWORD))

    # Debug: Print the raw response
    print("Response Status Code:", response.status_code)
    print("Response Text:", response.text)

    if response.status_code == 201:
        print("Download request created successfully!")
        download_key = response.text.strip()
        print(f"Download Key: {download_key}")
        return download_key
    else:
        print(f"Failed to create download request: {response.status_code}")
        try:
            print("Response JSON:", response.json())
        except Exception as e:
            print(f"Error decoding response: {e}")
        return None

def check_download_status(download_key):
    """Check the status of the GBIF download request."""
    status_url = f"https://api.gbif.org/v1/occurrence/download/{download_key}"
    while True:
        response = requests.get(status_url, auth=(USERNAME, PASSWORD))
        try:
            status = response.json().get("status", "UNKNOWN")
        except Exception as e:
            print(f"Error decoding status response: {e}")
            break

        print(f"Download status: {status}")
        if status == "SUCCEEDED":
            print(f"Download ready at: https://www.gbif.org/occurrence/download/{download_key}")
            break
        elif status in {"FAILED", "CANCELLED"}:
            print("Download failed or was cancelled.")
            break
        time.sleep(30)  # Wait 30 seconds before checking again


def main():
    try:
        # Convert the shapefile to WKT
        wkt_geometry = shapefile_to_wkt(SHAPEFILE_PATH)
        print(f"WKT Geometry: {wkt_geometry[:100]}...")  # Print the first 100 characters of the WKT for verification

        # Create the download request
        download_key = create_download_request(wkt_geometry)
        if download_key:
            check_download_status(download_key)
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()