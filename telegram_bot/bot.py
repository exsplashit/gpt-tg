from .business.interactions import handle_business_approval, send_approval_message
from .customer.interactions import handle_customer_message
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the chat ID of the business support member
BUSINESS_SUPPORT_MEMBER_CHAT_ID = int(
    os.getenv('BUSINESS_SUPPORT_MEMBER_CHAT_ID'))


# Rest of the code...


def collect_user_ids(self):
    # Get the list of customer user IDs from the dispatcher
    user_ids = self.dispatcher.user_data.keys()

    # Save the user IDs to a file
    with open('user_ids.txt', 'w') as file:
        for user_id in user_ids:
            file.write(str(user_id) + os.linesep)
