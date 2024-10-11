import random
import ipaddress

def generate_random_ip():
    """Generates a random IP address."""
    """ From 1.0.0.0 to 223.0.0.0.0"""
    return str(ipaddress.IPv4Address(random.randint(0x01000000, 0xDF000000)))

def generate_random_subnet_mask(difficulty):
    """Generates a random subnet mask based on difficulty level."""
    if difficulty == 'easy':
        return random.randint(24, 30)
    elif difficulty == 'medium':
        return random.randint(12, 30)
    elif difficulty == 'hard':
        return random.randint(1, 30)
    else:
        raise ValueError("Invalid difficulty level")

def calculate_network_info(ip, subnet_mask):
    """Calculates network ID, first usable, last usable, and broadcast address."""
    network = ipaddress.IPv4Network(f"{ip}/{subnet_mask}", strict=False)
    network_id = str(network.network_address)
    broadcast_address = str(network.broadcast_address)
    first_usable = str(list(network.hosts())[0])
    last_usable = str(list(network.hosts())[-1])
    return network_id, first_usable, last_usable, broadcast_address

def get_user_input(prompt, valid_options):
    """Handles user input with basic validation."""
    while True:
        user_input = input(prompt).lower()
        if user_input in valid_options:
            return user_input
        else:
            print("Invalid input. Please try again.")

def get_user_input_numbered(prompt, valid_options):
    """Handles user input with numbered validation."""
    while True:
        try:
            user_input = int(input(prompt))
            if user_input in valid_options:
                return user_input
            else:
                print("Invalid input. Please pick a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def ask_questions(ip, subnet_mask):
    """Asks the user subnetting questions and checks their answers."""
    network_id, first_usable, last_usable, broadcast_address = calculate_network_info(ip, subnet_mask)
    
    print(f"\nYou are given IP: {ip} /{subnet_mask}")
    
    user_network_id = input("What is the network ID? ").strip()
    user_first_usable = input("What is the first usable IP address? ").strip()
    user_last_usable = input("What is the last usable IP address? ").strip()
    user_broadcast = input("What is the broadcast address? ").strip()
    
    correct = True
    
    if user_network_id == network_id:
        print("Good job on the network ID!\n")
    else:
        print(f"Nice try! The correct network ID is: {network_id}\n")
        correct = False
        
    if user_first_usable == first_usable:
        print("Good job on the first usable IP address!\n")
    else:
        print(f"Nice try! The correct first usable IP address is: {first_usable}\n")
        correct = False
    
    if user_last_usable == last_usable:
        print("Good job on the last usable IP address!\n")
    else:
        print(f"Nice try! The correct last usable IP address is: {last_usable}\n")
        correct = False
    
    if user_broadcast == broadcast_address:
        print("Good job on the broadcast address!\n")
    else:
        print(f"Nice try! The correct broadcast address is: {broadcast_address}\n")
        correct = False

    return correct

def main():
    print("\nWelcome to the subnetting quiz!\n")
    
    while True:
        difficulty_choice = get_user_input_numbered("Choose a difficulty:\n  1) Easy\n  2) Medium\n  3) Hard\nPick a number: ", [1, 2, 3])
        
        if difficulty_choice == 1:
            difficulty = 'easy'
        elif difficulty_choice == 2:
            difficulty = 'medium'
        elif difficulty_choice == 3:
            difficulty = 'hard'
        
        ip = generate_random_ip()
        subnet_mask = generate_random_subnet_mask(difficulty)
        
        ask_questions(ip, subnet_mask)
        
        play_again = get_user_input("\nWould you like to try again? (yes/no): ", ["yes", "no"])
        if play_again == 'no':
            print("Thanks for playing! Goodbye!")
            break



main()