import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/trueway/api/trueway-geocoding'

mcp = FastMCP('trueway-geocoding')

@mcp.tool()
def reverse_geocode(location: Annotated[str, Field(description='The location for which you wish to obtain the human-readable address')],
                    language: Annotated[Union[str, None], Field(description='The language in which to return results')] = None) -> dict: 
    '''Obtain address for location'''
    url = 'https://trueway-geocoding.p.rapidapi.com/ReverseGeocode'
    headers = {'x-rapidapi-host': 'trueway-geocoding.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'location': location,
        'language': language,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def geocode(address: Annotated[str, Field(description='The address that you want to geocode')],
            language: Annotated[Union[str, None], Field(description='The language in which to return results')] = None,
            bounds: Annotated[Union[str, None], Field(description='The bounding box')] = None,
            country: Annotated[Union[str, None], Field(description='The country code')] = None) -> dict: 
    '''Obtain geocoordinates for address'''
    url = 'https://trueway-geocoding.p.rapidapi.com/Geocode'
    headers = {'x-rapidapi-host': 'trueway-geocoding.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'address': address,
        'language': language,
        'bounds': bounds,
        'country': country,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
