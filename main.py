# Lauren Ward
# This program is designed for General Contractor Admins with the intention of
# compiling individual expenses for a New Home Build as well as stsy on track
# with the job budget.

# Resources used: w3schools.com (to review 'def' and 'if..else' functions),
# HomeGuide.com (to get a better idea of new home construction cost)
# I used mostly past HackerRank exercises to work out the rest


print("Welcome to", end=' ')
print("C", "I", "N", "D", "E", "R", sep=' ')
print("\n")


# The following lines are used to allow user to input number of hours worked &
# wage rate.
# The 'if' statements and get_valid functions are used to keep entries within
# probable parameters and
# return a custom error message for anticipated values out of range.

print("To Calculate the Pay of One Employee ")


def get_valid_float(prompt):
    while True:
        try:
            num = float(input(prompt))
            return num
        except ValueError:
            print("Invalid Input")
def get_valid_int(prompt):
    while True:
        try:
            num = int(input(prompt))
            return num
        except ValueError:
            print("Invalid Input")

def labor_main():
    hour_prompt = str("Enter total hours worked by this employee: ")
    hour_error = str("ERROR Hours must be between 1 and 100")
    num_hours = get_valid_float(hour_prompt)
    while True:
        if num_hours < 1 or num_hours > 100:
            print(hour_error)
            num_hours = get_valid_float(hour_prompt)
        else:
            break
    wage_prompt = str("Enter this employee's wage rate: ")
    wage_error = str("ERROR Wage must be between $8.00 and $50.00")
    wage_rate = get_valid_float(wage_prompt)
    while True:
        if wage_rate < 8 or wage_rate > 50:
            print(wage_error)
            wage_rate = get_valid_float(wage_prompt)
        else:
            break
    print("\n")
    payroll_no_ot(num_hours, wage_rate)
    payroll_ot(num_hours, wage_rate)

# The following function is used to define payroll as a function of 'hours'
# and 'wage' in the case that hours worked is less than (or equal to) 40.
# The Lunch breaks variable is used to deduct one 30 min. lunch break for
# every 6 hours worked and round down to the nearest whole number.
# Payroll is calculated based in net hours worked after lunch breaks are
# deducted.

def payroll_no_ot(num_hours, wage_rate):
    lunch_breaks = num_hours // 6
    num_hours -= (lunch_breaks * 0.5)
    if num_hours <= 40:
        print("Payroll for Employee with NO OVERTIME\n")
        print("Paid Hours deducting lunch breaks", num_hours)
        print("Overtime Hours: 0")
        print("Overtime Paid: $0.00")
        print("Total Paid to Employee: $", format(num_hours * wage_rate, '.2f'))


# The following function is used to define payroll as a function of 'hours'
# and 'wage' in the case that hours worked is greater than 40.
# The OT_hours variable is defined under the assumption that OT is time
# and a half i.e. (wage*1.5).

def payroll_ot(num_hours, wage_rate):
    lunch_breaks = num_hours // 6
    num_hours -= (lunch_breaks * 0.5)
    ot_hours = num_hours - 40
    ot_wage1 = (ot_hours * (wage_rate * 1.5))
    ot_wage2 = (40 * wage_rate)
    if num_hours > 40:
        print("Payroll for Employee\n")
        print("Total Site Hours Worked", num_hours)
        print("Paid Hours deducting lunch breaks", ot_hours)
        print("Overtime Hours: ", ot_hours)
        print("Overtime Paid: $", format(ot_hours * wage_rate * 1.5, '.2f'))
        print("Total Paid to Employee: $", format(ot_wage1 and ot_wage2, '.2f'))

labor_main()


print("To track the budget of this job")
job_budget = get_valid_float("Enter Budget: ")
print("Select cost codes from the menu below to calculate total job cost")

# To allow the user to select the cost code and enter the vendor cost
# I created a menu of the most common cost codes for new home builds and a while
# loop to continuously take inputs and save each input to a list.
# The for loop with range() prints the menu as a vertical list.
# The list is used so that not all cost codes need to be used it only sums up the
# cost of each specific selection. Once the user enters zero the loop breaks and
# the program calculates the total vendor cost of only the selections returned to
# the cost_list.

def cost_code_menu():
    list_codes = ["[1] Framing", "[2] Concrete", "[3] Masonry",
                  "[4] Cabinets/Countertops", "[5] Tile/Flooring",
                  "[6] Trusses", "[7] Electrical", "[8] Paint",
                  "[9] HVAC", "[10] Architects/Engineers", "[11] Landscape",
                  "[12] Equipment/Vehicles", "[13] Permitting",
                  "[14] Miscellaneous","[0] Exit program"]
    for i in range(0, len(list_codes)):
        print(list_codes[i])

cost_code_menu()

print("\n")
print("After all vendor costs have been entered select 0 for total cost of job")
print("Cost Codes may only be entered once")
print("\n")

cost_code = get_valid_int("Enter the Cost Code Number Option: ")

# The vendor_cost function takes each input for labor and materials for each menu
# selection and returns the sum to the specific vendor variable.

def vendor_cost(num1,num2):
    sum = num1 + num2
    return sum

while cost_code != 0:
    cost_list = []
    labor_cost = get_valid_float("Enter cost of labor: ")
    mat_cost = get_valid_float("Enter cost of materials: ")
    v_funct = vendor_cost(labor_cost,mat_cost)
    if cost_code == 1:
        framing_cost = v_funct
        cost_list.append(framing_cost)
    elif cost_code == 2:
        concrete_cost = v_funct
        cost_list.append(concrete_cost)
    elif cost_code == 3:
        masonry_cost = v_funct
        cost_list.append(masonry_cost)
    elif cost_code == 4:
        cab_cost = v_funct
        cost_list.append(cab_cost)
    elif cost_code == 5:
        tile_cost = v_funct
        cost_list.append(tile_cost)
    elif cost_code == 6:
        trus_cost = v_funct
        cost_list.append(trus_cost)
    elif cost_code == 7:
        elec_cost = v_funct
        cost_list.append(elec_cost)
    elif cost_code == 8:
        paint_cost = v_funct
        cost_list.append(paint_cost)
    elif cost_code == 9:
        hvac_cost = v_funct
        cost_list.append(hvac_cost)
    elif cost_code == 10:
        eng_cost = v_funct
        cost_list.append(eng_cost)
    elif cost_code == 11:
        land_cost = v_funct
        cost_list.append(land_cost)
    elif cost_code == 12:
        equip_cost = v_funct
        cost_list.append(equip_cost)
    elif cost_code == 13:
        perm_cost = v_funct
        cost_list.append(perm_cost)
    elif cost_code == 14:
        misc_cost = v_funct
        cost_list.append(misc_cost)
    else:
        print("Invalid Selection")
    cost_code = get_valid_int("Enter the Cost Code Number Option: ")

# This for loop totals the sums in cost_list

total = 0
for i in cost_list:
    total += i

print("\n")
print("The total cost of this job is: $",format(total,'.2f'))
print("\n")

# The if statement here determines if the user is on/over/under budget

if not total > job_budget:
    total_diff = job_budget - total
    print("Your job is projected to stay under budget: $",format(total_diff,'.2f'))
elif total == job_budget:
    print("Your job is projected to stay exactly on budget")
else:
    total_over = total - job_budget
    print("Your job is projected to go over budget: $",format(total_over,'.2f'))

# The following code is used to calculate how many site workers is allowable
# under the user entered budget.
# The modulus operator is used to calculate the remaining amount left in the
# budget after the amount of affordable workers is rounded down to the nearest
# whole number.
# Sample inputs - avg_wage = 20, weeks = 24-30, budget = 68 - 70,000.

print("To calculate how many site workers affordable on the job per day")
num_weeks = get_valid_int("Enter desired number of weeks to job completion: ")
avg_wage = get_valid_float("Enter the average wage of site workers: ")
job_hours = num_weeks * 18
num_work = job_budget // (job_hours * avg_wage)
labor_surplus = job_budget % (job_hours * avg_wage)

print("The number of workers affordable on this job per day is: ", num_work)
print("Surplus left in Budget: $", format(labor_surplus, '.2f'))

# The following code is used to test out different numbers of workers
# on site and how that will affect the budget.

print("\n")
print("To test how your budget will be affected by adding site workers")
add_workers = get_valid_int("Enter number of site workers here: ")
int_labor_cost = add_workers * avg_wage * job_hours
if int_labor_cost <= job_budget:
    print("Your project is projected to stay on/under budget")
    print("Woo hoo!")
else:
    print("Your project will go over budget $",
           format(int_labor_cost - job_budget, '.2f'))
print("\n")
print("Thank You")
