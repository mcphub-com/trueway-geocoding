markdown
# TrueWay Geocoding MCP Server

## Overview

The TrueWay Geocoding MCP Server provides powerful tools to perform forward and reverse geocoding. It is designed to convert addresses into geographic coordinates (latitude and longitude) and vice versa. This server supports multiple languages and offers global coverage, making it an ideal solution for applications requiring precise location data.

### Key Features

- **Global Coverage**: Access to geocoding services worldwide.
- **Forward Geocoding**: Convert addresses into geographic coordinates.
- **Reverse Geocoding**: Convert geographic coordinates into human-readable addresses.
- **Multi-Language Support**: Return results in different languages using ISO 639-1 codes.

## Tools and Functions

### Geocoding (Geocode)

**Description**: This tool converts street addresses into geographic coordinates.

- **Required Parameters**:
  - `address`: The street address you want to geocode.

- **Optional Parameters**:
  - `language`: The two-letter language code to specify the result language.
  - `bounds`: Prefer results in a specified rectangular area (south, west, north, east).
  - `country`: The two-letter country code to bias the results.

### Reverse Geocoding (ReverseGeocode)

**Description**: This tool converts geographic coordinates into a human-readable address.

- **Required Parameters**:
  - `location`: The geographic coordinates for which you want the address.

- **Optional Parameters**:
  - `language`: The two-letter language code to specify the result language.

## Response Structure

A geocoding result includes various fields to provide comprehensive location information:

- `address`: The full address.
- `postal_code`: The postal code.
- `country`: The country name.
- `region`: The region or state.
- `area`: The area or city.
- `locality`: The locality or district.
- `neighborhood`: The neighborhood.
- `street`: The street name.
- `house`: The house or building number.
- `location`: The geographic coordinates (latitude/longitude).
- `location_type`: Indicates the precision of the location (e.g., exact, approximate, centroid).
- `type`: The type of location (e.g., street_address, route, admin_area, country, region, etc.).

This MCP server is designed to facilitate seamless integration of geocoding capabilities into applications, providing reliable and efficient location-based services.