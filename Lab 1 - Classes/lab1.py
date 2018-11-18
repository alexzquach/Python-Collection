"""
Registry module
"""

from typing import List, Dict, Any

# Constants for the speed categorys
UNDER20 = 'under 20 minutes'
UNDER30 = 'under 30 minutes'
UNDER40 = 'under 40 minutes'
OVEROR40 = '40 minutes or over'


class RaceRegistry:
    """ Represent a runner registry system for a race

    registry - Database (stored in a dictionary) of runners registered by email
    """
    registry: Dict[str, List[str]]

    def __init__(self) -> None:
        """ Initializes a new race registry
        """

        # Intializes the registry with appropriate default values
        self.registry = {UNDER20: [], UNDER30: [], UNDER40: [], OVEROR40: []}

    def __str__(self) -> str:
        """ String representation of RaceRegistry """

        st = ''
        for key in self.registry:
            st = st + 'People ' + key + ': ' + str(self.registry[key]) + '\n'
        # Returns the complete string representation of registry
        return st

    def __eq__(self, other: Any) -> bool:
        """ Return whether self is equivalent to other

        >>> r1 = RaceRegistry()
        >>> r2 = RaceRegistry()
        >>> r1 == r2
        True
        >>> r1 = RaceRegistry()
        >>> r2 = RaceRegistry()
        >>> r2.add_runner('jimmy_tan@gmail.com', UNDER20)
        >>> r1 == r2
        False
        """

        # Returns true iff the registry of self is the same as other
        return type(self) == type(other) and self.registry == other.registry

    def get_speed_category(self, speed_category: str) -> List[str]:
        """ Returns a list of emails of all people in the under 20 minutes
        speed category

        >>> r1 = RaceRegistry()
        >>> r1.add_runner('jimmy_tan@gmail.com', UNDER20)
        >>> r1.add_runner('alex.quach@gmail.com', UNDER20)
        >>> r1.add_runner('keith@outlook.com', UNDER20)
        >>> r1.get_speed_category(UNDER20)
        ['jimmy_tan@gmail.com', 'alex.quach@gmail.com', 'keith@outlook.com']
        """

        # Returns the list of the certain speed category
        return self.registry[speed_category]

    def add_runner(self, runner_email: str, runner_category: str) -> None:
        """ Adds a new runner to the current runner registry

        >>> r1 = RaceRegistry()
        >>> r1.registry
        {'under 20 minutes': [], 'under 30 minutes': [], 'under 40 minutes': [], '40 minutes or over': []}
        >>> r1.add_runner("al_q@gmail.com", UNDER20)
        >>> r1.registry
        {'under 20 minutes': ['al_q@gmail.com'], 'under 30 minutes': [], 'under 40 minutes': [], '40 minutes or over': []}
        """

        # Searchs the registry to see if the user has already registered that
        # email
        for category in self.registry:
            for email in self.registry[category]:
                if email == runner_email:
                    # Removes the email if it already exists
                    # to avoid duplicate emails
                    self.registry[category].remove(email)
                    # Breaks out of the loop since we have found the first
                    # and only occurrence of email
                    break
        # Adds the email to the registry
        self.registry[runner_category].append(runner_email)

    def look_up(self, runner_email: str) -> str:
        """ Returns the speed category of email.  Returns User Not Found if the user
        is not in the registry.

        >>> r1 = RaceRegistry()
        >>> r1.add_runner('al_q@gmail.com', UNDER20)
        >>> r1.add_runner('jimmy@gmail.com', UNDER20)
        >>> r1.look_up('al_q@gmail.com')
        'Their speed category is: under 20 minutes'
        """

        st = ''
        # Searchs the registry for the email
        for category in self.registry:
            for email in self.registry[category]:
                if email == runner_email:
                    st = st + 'Their speed category is: ' + category
                    return st
        return 'User Not Found'


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    # Test Code
    r1 = RaceRegistry()
    # Introduction to program message
    print("Welcome to Race Registry!")
    print("Please enter a name to to register or enter \'Exit\' to exit.")
    print("Avaliable speed categories:", end=' ')
    # Avaliable speed categories based on constants
    print(UNDER20, UNDER30, UNDER40, OVEROR40, sep=', ')
    # User email that is being registered
    user_email = ''
    user_email = input("Enter an email to register: ").strip()
    # While the user does not want to exit, keep prompting them to register
    while user_email.upper() != 'EXIT':
        # Makes sure the email is actually ann email
        while '@' not in user_email:
            user_email = input("Please enter a valid email!: ").strip()
        # Prompts the user for a speed category
        user_category = input("Enter a category: ").strip()
        # If the user does not enter a proper email, prompt them until
        # they enter a valid email
        while (user_category != UNDER20 and user_category != UNDER30 and
                user_category != UNDER40 and user_category != OVEROR40):
            # Checks to see if the user mistyped
            if user_category.upper() == 'EXIT':
                choice = input('Are you sure you want to exit? Y/N: ')
                if choice.upper() == 'Y':
                    print('Thank you for registering!')
                    exit()
            user_category = input("Please enter a valid category!: ")
        # Let the user know they have successfully registered their email
        r1.add_runner(user_email, user_category)
        print('Registration sucessful!')
        print(r1)
        # Prompt the user again to see if they would like to stay or exit
        user_email = input("Enter an email to register or Exit: ").strip()
    print('Thank you for registering!')
