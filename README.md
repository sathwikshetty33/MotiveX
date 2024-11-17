# MotiveX

MotiveX is a Django-based web application designed to inspire users with motivational quotes. Registered users receive motivational quotes via email every Monday, and an API endpoint allows easy access to the weekly quote.

## Features
- **Email Notifications**: Sends motivational quotes to registered users every Monday.
- **API Endpoint**: Accessible via a GET request without parameters to fetch the current week's quote.
- **User-Friendly Interface**: Designed with HTML, CSS, and JavaScript.
- **Automated Deployment**: Hosted on [PythonAnywhere](https://www.pythonanywhere.com/).

## Technologies Used
- **Backend**: Django, Django REST Framework
- **Database**: MySQL
- **Frontend**: HTML, CSS, JavaScript
- **Utilities**: smtplib, datetime, time
- **Deployment**: PythonAnywhere

## API Usage
### Endpoint
`https://sathwik33.pythonanywhere.com/api/`

### Response
The API returns the motivational quote for the current week in JSON format.

#### Example Response:
```json
{
  "quote": "Your limitation—it’s only your imagination."
}
