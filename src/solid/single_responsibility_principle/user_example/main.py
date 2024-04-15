from user import User
from user_manager import UserManager
from message_sender import EmailSender, SMSSender

if __name__ == "__main__":
    user1 = User(username="JohnDoe", email="john@example.com", phone_number="xxxxx")
    user2 = User(username="JaneDoe", email="jane@example.com", phone_number="xxxxx")

    user_manager = UserManager()
    user_manager.add_user(user1)
    user_manager.add_user(user2)

    print(user_manager.usernames)
    # send an email and a sms message to all users
    user_manager.send_message_to_all_users(sender=EmailSender(), message="Welcome to our emailing platform!")
    user_manager.send_message_to_all_users(sender=SMSSender(), message="Welcome to our SMS platform!")


"""Note on the design
Where the design from break_srp.py clearly breaks the Single Responsibility Principle (SRP), this design utilises a 
couple of different classes to properly create, store and contact users of a platform. This separating of concerns
neatly illustrates the SRP. However, it should be noted that this design is not without its flaws. For example, the 
SenderInterface is closely coupled with the User class to extract the required recipient information when sending a 
message. Though it suffices in demonstrating the SRP, which this example is meant to do.
"""