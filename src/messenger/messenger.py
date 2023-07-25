import requests


def send_message(access_token, recipient_id, message_text):
    try:
        api_url = 'https://graph.facebook.com/v13.0/me/messages'
        headers = {
            'Content-Type': 'application/json',
        }
        params = {
            'access_token': access_token,
        }
        message_data = {
            'messaging_type': 'RESPONSE',
            'recipient': {
                'id': recipient_id,
            },
            'message': {
                'text': message_text,
            }
        }
        response = requests.post(api_url, headers=headers, params=params, json=message_data)
        response_data = response.json()

        if response.status_code == 200 and 'message_id' in response_data:
            print("Message sent successfully!")
        else:
            print("Failed to send the message. Response:", response_data)
    except Exception as error:
        raise error
