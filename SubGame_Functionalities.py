import ipaddress, random

def user_actions():
    
    while True:

        user_choice = input("Try again? or restart (0 for try again, 1 for restart, 2 to exit): ")
        if user_choice == '0':
            return "reguess"
        elif user_choice == '1':
            print("Restarting the game...")
            return "restart"
        elif user_choice == '2':
            print("Exiting the game...")
            exit()
        else:
            print("Invalid choice, please enter 0 or 1 or 2.")


    
def genereate_ip_info():

    first_octet = random.randrange(0,256,1)
    second_octet = random.randrange(0,256,1)
    third_octet = random.randrange(0,256,1)
    fourth_octet = random.randrange(0,256,1)
    CIDR = random.randrange(9,31,1)
    ip_address_generated = ipaddress.IPv4Interface(f"{first_octet}.{second_octet}.{third_octet}.{fourth_octet}/{CIDR}")
    
    host_rage = list(ip_address_generated.network.hosts())

    #Calculating magic number
    cird_ip_notation =  ip_address_generated.network.netmask
    cidr_list = str(cird_ip_notation).split(".")
    interesting_octet = 0
    k = 0
    for i in range(4):
        if cidr_list[k] == '255' or cidr_list[k] == '0':
            k = k+1
        else:
            interesting_octet = cidr_list[k]
            k = k+1
            
    magic_number = 256 - int(interesting_octet)

    cidr_ip_notation_solution =  cird_ip_notation
    magic_number_solution= magic_number
    subnet_ip_solution =  host_rage[0]-1
    first_host_solution = host_rage[0]
    last_host_guess_solution = host_rage[-1]
    broadcast_ip_solution = ip_address_generated.network.broadcast_address
    ip_list_info = [ip_address_generated, cidr_ip_notation_solution, magic_number_solution, subnet_ip_solution, first_host_solution, last_host_guess_solution, broadcast_ip_solution]
    return ip_list_info



while True:
    action = "guess"
    restart = "no"
    while restart == "no": 
        if action != "reguess":

            #Generates random ip address and information about it
            ip_list_info = genereate_ip_info()
            user_questions = ["Ip notation for CIDR mask: ",
                            "Magic number: ",
                            "Subnet IP: ",
                            "First host in our network: ",
                            "Last host in our network: ",
                            "Broadcast IP: "]

            cidr_ip_notation_guess = magic_number_guess = subnet_ip_guess = first_host_guess = last_host_guess = broadcast_ip_guess = "0"
            user_guesses = [cidr_ip_notation_guess, magic_number_guess, subnet_ip_guess, first_host_guess, last_host_guess, broadcast_ip_guess]

            print(f"Here is the ip address: {ip_list_info[0]}")
            question_length = len(user_questions)
            question_num = 0
        else: 
            action = "guess"
            question_num = last_question_num

        while action == "guess" and restart == "no":

            for i in range(question_num, question_length) :

                last_question_num = i
                user_guesses[i] = input(user_questions[i]) 

                if user_guesses[i] == str(ip_list_info[i+1]):
                    print("Correct!")
                else:
                    state = user_actions()
                    if state == "reguess":
                        action = "reguess"
                        break
                    elif state == "restart":
                        restart = "yes"
                        break        
