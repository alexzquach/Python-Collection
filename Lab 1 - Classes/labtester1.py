# Constants for the speed categorys
UNDER20 = 'under 20 minutes'
UNDER30 = 'under 30 minutes'
UNDER40 = 'under 40 minutes'
OVEROR40 = '40 minutes or over'

if __name__ == '__main__':
    import lab1
    r1 = lab1.RaceRegistry()
    r1.add_runner('gerhard@mail.utoronto.ca', UNDER40)
    r1.add_runner('toni@mail.utoronto.ca', UNDER20)
    r1.add_runner('margot@mail.utoronto.ca', UNDER30)
    r1.add_runner('gerhard@mail.utoronto.ca', UNDER30)
    print(r1)
