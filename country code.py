country_code = {'india':91, 
                'usa':1, 
                'uk':44, 
                'australia':61, 
                'canada':1,
                'thailand':66,
                'china':86,
                'japan':81
                }
print("Country Code for India is: ", country_code.get('india', 'not found'))
print("Country Code for USA is: ", country_code.get('usa', 'not found'))
print("Country Code for UK is: ", country_code.get('uk', 'not found'))
print("Country Code for Australia is: ", country_code.get('australia', 'not found'))
print("Country Code for Canada is: ", country_code.get('canada', 'not found'))
print("Country Code for Thailand is: ", country_code.get('thailand', 'not found'))
print("Country Code for China is: ", country_code.get('china', 'not found'))
print("Country Code for Japan is: ", country_code.get('japan', 'not found'))

print("Country Code for Germany is: ", country_code.get('germany', 'not found'))
print("Country Code for France is: ", country_code.get('france', 'not found'))
print("Country Code for Italy is: ", country_code.get('italy', 'not found'))