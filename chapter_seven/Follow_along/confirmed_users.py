# Start with users that need to be vierfied,
# and an empty list to hold confirmed users.

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# Verify each user until there are no more cuncofiremd users.
# Move each verified user into the list of confirmed users.

while unconfirmed_users:
    current_users = unconfirmed_users.pop()

    print(f"Verifiying user: {current_users.title()}")
    confirmed_users.append(current_users)
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())