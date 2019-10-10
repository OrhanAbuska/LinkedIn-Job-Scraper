search_query = 'site:linkedin.com/in/ AND "python developer" AND "Istanbul"'


username = input('LinkedIn Kullanıcı Adınız: ')
password = input('LinkedIn Kullanıcı Şifreniz: ')
desired_job = input('Aramak istediğiniz iş: ')
desired_location = input('Aramak istediğiniz şehir: ')

linkedin_username = 'Kullanıcı Adınızı Buraya Yazabilirsiniz.'
linkedin_password = 'Şifrenizi Buraya Yazabilirsiniz.'

csv_file = str.strip(desired_job)
file_name = csv_file+'.csv'