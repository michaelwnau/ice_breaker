import os
import requests

def scrape_linkedin_profile(linkedin_profile_url: str):
    """scrape information from linkedin profiles, 
    manually scrape the information from the LinkedIn profile
    """
    api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
    
    # Initialize the header dictionary as an empty dictionary
    header_dic = {}
    # Now add the API key to it
    header_dic.update({"Authorization": f'Bearer {os.environ.get("PROXYCURL_API_KEY")}'})

    response = requests.get(
        api_endpoint, params={"url": linkedin_profile_url}, headers=header_dic
    )
    
    print(response.text)
    
    return response 