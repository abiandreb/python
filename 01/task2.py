capital_dict = dict(

    Germany='Berlin',
    Spain='Madrid',
    France='Paris',
    Poland='Warsaw'
)

country_list = ['Poland', 'Ukraine', 'Belarus', 'Germany']

for i in country_list:
    if i in capital_dict.keys():
        print(capital_dict.get(i))
