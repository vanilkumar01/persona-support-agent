# API Authentication Guide

## Bearer Token Authentication

All API requests must include:

Authorization: Bearer YOUR_API_KEY

Required Headers:

Content-Type: application/json
Authorization: Bearer YOUR_API_KEY

Common Errors

401 Unauthorized

* Invalid API key
* Expired token
* Missing Authorization header

403 Forbidden

* Insufficient permissions

Example Request

curl -H "Authorization: Bearer YOUR_API_KEY" https://api.company.com/v1/users

## Generating an API Key

1. Log in to your account.
2. Open Developer Settings.
3. Click Generate API Key.
4. Copy and store the key securely.

## Using the API Key

Include the key in the Authorization header:

Authorization: Bearer YOUR_API_KEY

## Common Errors

401 Unauthorized:

* Invalid API key
* Expired API key

403 Forbidden:

* Insufficient permissions
