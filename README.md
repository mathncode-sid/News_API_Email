# News_API_Email

A simple Python project to fetch the latest news articles on a topic of your choice and email them to you using Gmail's SMTP service.

## Features

- Fetches the latest news articles based on your chosen topic using the NewsAPI.
- Sends a summary email with article titles, descriptions, and URLs.
- Uses your Gmail account for sending emails.

## Requirements

- Python 3.x
- [requests](https://pypi.org/project/requests/) library

## Setup

1. **Clone the repository**
   ```
   git clone https://github.com/mathncode-sid/News_API_Email.git
   cd News_API_Email
   ```

2. **Install dependencies**
   ```
   pip install requests
   ```

3. **Configure your credentials**
   - Edit `send_mail.py` and replace:
     - `username` with your Gmail address
     - `password` with your [App Password](https://support.google.com/accounts/answer/185833)
     - `receiver` with the recipient's email address
   - Edit `main.py` and replace the `api_key` with your [News API key](https://newsapi.org/).

## Usage

Run the main script:
```
python main.py
```
- You’ll be prompted to enter a topic.  
- The script fetches the latest news and sends an email with the articles.

## File Overview

- **main.py**  
  Fetches news from NewsAPI and sends results via email.
- **send_mail.py**  
  Contains the function for sending emails using Gmail’s SMTP.

## Security Notes

- Use a Gmail App Password, not your main password.
- Never share your credentials or API keys publicly.

## Example

```
Enter your topic: technology
# (An email will be sent to the configured recipient with the latest news on "technology")
```

---

Feel free to copy, modify, and enhance this README as needed!
