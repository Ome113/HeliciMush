from flask import Flask, request, jsonify
from flask_mail import Mail, Message

app = Flask(__name__)

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465  # SSL Port
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'juniorale947@gmail.com'  # Your email
app.config['MAIL_PASSWORD'] = 'ghana1234'  # Your email password or app-specific password
app.config['MAIL_DEFAULT_SENDER'] = 'juniorale947@gmail.com'  # Default sender address

# Initialize Flask-Mail
mail = Mail(app)

# Route to handle new order
@app.route('/', methods=['POST'])
def place_order():
    data = request.get_json()

    # Extract order details from the request
    customer_name = data.get('customerName')
    customer_email = data.get('customerEmail')
    order_details = data.get('orderDetails')

    # Create the email message
    msg = Message(
        subject='New Order Notification',
        recipients=['juniorale947@gmail.com'],  # Replace with the owner's email
        body=f"You have received a new order from {customer_name} ({customer_email}).\n\nOrder Details:\n{order_details}"
    )

    try:
        # Send the email
        mail.send(msg)
        return jsonify({'message': 'Order received and email sent successfully!'}), 200
    except Exception as e:
        return jsonify({'message': f'Error sending email: {str(e)}'}), 500


# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)