class User:

    previous_posts = []

    def __init__(self, name, email_address, dl, phone_number):
        self.name = name
        self.email_address = email_address
        self.dl = dl
        self.phone_number = phone_number

    def post(self, post):
        self.previous_posts.append([f'{self.name} posted {post}'])
        return f'{self.name} posted {post}'
    
radd = User('Radd', 'Gr8BitHero@email.com', 9899100, '4042777373')
alta = User('Alta', 'redgirl9@email.com', 9293381, '4425998021')
shyren = User('Shyren', 'shyrenstars95@email.com', 1203948, '0809924421')

radd.post('I think I got it!')
alta.post('Good going Radd! It works!')
shyren.post('')

print(User.previous_posts)