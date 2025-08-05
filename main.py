from flask import Flask, request
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

app = Flask(__name__)

#SendGrid API Key

SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY')

owner_email = 'juniorale947@gmail.com'

@app.route('/purchase', method=['POST'])
def send_email_notification():
    customer_name = request.json['customer_name']
    order_total = request.json['order_total']
    product_info = request.json['product_info']

    email_content = f'Customer {customer_name} has made a purchase of ghc{order_total} for {product_info}

    message = Mail(
        from email="helicimush@gmail.com", to_emails=owner_email,
        subject={'New Purchase'},
        plain_text_content=email_content)
    try:
        sg= SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e)
    return "Email notification sent successfully!'

if __name__=='__main__':
    app.run(debug=True)        