#Module 5 Lab
#Michael Miao
#10/24


def get_bottles():
    nbr_of_days = 7
    total_bottles = 0  
    counter = 1  

    while counter <= nbr_of_days:
        today_bottles = int(input(f"Enter number of bottles returned for day #{counter}:"))
        total_bottles += today_bottles  
        counter += 1 
    return total_bottles  

def calc_payout(total_bottles):
    payout_per_bottle = 0.10 
    total_payout = total_bottles * payout_per_bottle  
    return total_payout  

def print_info(total_bottles, total_payout):
    print(f"Total number of bottles collected: {total_bottles}")
    print(f"Total payout for the week: ${total_payout:.2f}")


if __name__ == "__main__":
    keep_going = "y" 

   
    while keep_going.lower() == "y":

        total_bottles = get_bottles()  
        total_payout = calc_payout(total_bottles)  
        print_info(total_bottles, total_payout)  
        print("Do you want to enter another week’s worth of data?")
        keep_going = input("(Enter y or n):")
        