# == INSTRUCTIONS ==
#
# Purpose: Manage a user's (valid) passwords
#
# Methods:
#   1. Name: __init__
#      Arguments: none
#   2. Name: add
#      Purpose: add a password for a service IF it is valid, otherwise do nothing
#      Arguments: one string representing a service name,
#                 one string representing a password
#      Returns: None
#   3. Name: remove
#      Purpose: remove a password for a service
#      Arguments: one string representing a service name
#      Returns: None
#   4. Name: update
#      Purpose: update a password for a service IF it is valid, otherwise do nothing
#      Arguments: one string reprting a service name,
#                 one string representing a password
#      Returns: None
#   5. Name: list_services
#      Arguments: none
#      Returns: a list of all the services for which the user has a password
#   6. Name: sort_services_by
#      Arguments: A string, either 'service' or 'added_on',
#                 (Optional) A string 'reverse' to reverse the order
#      Returns: a list of all the services for which the user has a password
#               in the order specified
#   7. Name: get_for_service
#      Arguments: one string representing a service name
#      Returns: the password for the given service, or None if none exists
#
# A reminder of the validity rules:
#   1. A password must be at least 8 characters long
#   2. A password must contain at least one of the following special characters:
#      `!`, `@`, `$`, `%` or `&`
#
# And a new rule: passwords must be unique (not reused in other services).
#
# Example usage:
#   > password_manager = PasswordManager2()
#   > password_manager.add('gmail', '12ab5!678')   # Valid password
#   > password_manager.add('facebook', '$abc1234') # Valid password
#   > password_manager.add('youtube', '3@245256')  # Valid password
#   > password_manager.add('twitter', '12345678')  # Invalid password, so ignored
#   > password_manager.get_for_service('facebook')
#   '$abc1234'
#   > password_manager.list_services()
#   ['gmail', 'facebook', 'youtube']
#   > password_manager.remove('facebook')
#   > password_manager.list_services()
#   ['gmail', 'youtube']
#   > password_manager.update('gmail', '12345678')  # Invalid password, so ignored
#   > password_manager.get_for_service('gmail')
#   '12ab5!678'
#   > password_manager.update('gmail', '%21321415')  # Valid password
#   > password_manager.get_for_service('gmail')
#   '%21321415'
#   > password_manager.sort_services_by('service')
#   ['gmail', 'youtube']
#   > password_manager.sort_services_by('added_on', 'reverse')
#   ['youtube', 'gmail']

# There are many more examples possible but the above should give you a good
# idea.

# == YOUR CODE ==

from datetime import datetime
class PasswordManager2():
    def __init__(self):
        self.service_list = []
        self.service_password_list = []
    def add(self,service, password):
        
        required_length = 8
        special_characters ="!@$%&"
        service_password_dictionary = {}
        
        checked_char_length =  len(password) >= required_length and any(char for char in password if char in special_characters)
        
        # list of dictionaries containing a service and a password
            # iterate over the accepted service_list 
            # if the value for the key "password" == password
        
        unique_check = 0

        for service_item in self.service_password_list:
            for key in service_item:
                if service_item[key] == password or key == service:
                    unique_check += 1

        if checked_char_length and unique_check == 0:
            service_password_dictionary[service] = password
            service_password_dictionary["added_on"] = datetime.now()
            self.service_password_list.append(service_password_dictionary)
            print(self.service_password_list)
            self.service_list.append(service)

        return None
    def remove(self,service):
        for service_item in self.service_password_list:
            for key in service_item:
                if key == service:
                    del service_item[key]
                    break
        self.service_list.remove(service)

        return None
    def update(self,service,password):
        # update the password for a service, if it is valid
        required_length = 8
        special_characters ="!@$%&"
        
        checked_char_length =  len(password) >= required_length and any(char for char in password if char in special_characters)
        
        # list of dictionaries containing a service and a password
            # iterate over the accepted service_list 
            # if the value for the key "password" == password
        
        unique_check = 0

        for service_item in self.service_password_list:
            for key in service_item:
                if service_item[key] == password :
                    unique_check += 1

        if checked_char_length and unique_check == 0:  
            for service_item in self.service_password_list: # iterating across the list of dictionaries 
                for key in service_item: # iterating across the key value pairs
                    if key == service:
                        service_item[key] = password
                        
        return None
    def list_services(self):
        
        return self.service_list
    
    def sort_services_by(self, sort_method, method_reverse):
        pass
        #   6. Name: sort_services_by
#      Arguments: A string, either 'service' or 'added_on',
#                 (Optional) A string 'reverse' to reverse the order
#      Returns: a list of all the services for which the user has a password
#               in the order specified
    

        # pass

    def get_for_service(self, service):
        #   7. Name: get_for_service
#      Arguments: one string representing a service name
#      Returns: the password for the given service, or None if none exists
        if service in self.service_list:
            print("service is in list of services")
            for service_item in self.service_password_list: # iterating across the services in the list  
                for key in service_item: #now I am iterating across the dictionary of the element within the services list, that cotains the password
                    if key == service: # if key is the name of the service being passed as an argument:
                        print("service key found")
                        return service_item[key] # return the password
        else:
            print("not in services list") 

            return None

# password_manager = PasswordManager2()

# password_manager.add('youtube', '3@245256')


# password_manager.add('twitter', '12345678') # invalid password

# password_manager.update("youtube", "12345678" ) # also invalid, because it doesnt satisfy
# password_manager.update("youtube", "$abc1234" )# should be invalid because it has been used before 
# password_manager.update("youtube", "Uniwusd&" )
# password_manager.update("facebook", "Uniwusd!" )
password_manager= PasswordManager2()
# password_manager.add('youtube', '3@24ddsd')
# password_manager.add('facebook', '$abc1234')
print(password_manager.add('twitter', '1234%678'))
# password_manager.update("twitter", "Uniwusd&"  )


# print(password_manager.list_services())
# print(password_manager.get_for_service())
    

print(password_manager.add('acebook', '$12345678'))
print(password_manager.add('makersbnb', '@12345678'))
print(password_manager.update('acebook', '!12345678'))

print(password_manager.list_services())
print(password_manager.get_for_service("acebloov"))

