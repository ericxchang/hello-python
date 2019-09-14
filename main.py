import repo.userDefiniton as api  # import but not execute
import util.email as email

api.fetch_user_definition()

print("before initialize email=", email, "\n")
# email.initialize_email()
# print("after initialize ", email)
