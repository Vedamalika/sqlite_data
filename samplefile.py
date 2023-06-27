import bcrypt
  
password = 'passwordabc'
  

bytes = password.encode('utf-8')
  
salt = bcrypt.gensalt()
  
# Hashing the password
hash = bcrypt.hashpw(bytes, salt)

userPassword =  'password000'
  
userBytes = userPassword.encode('utf-8')
  
result = bcrypt.checkpw(userBytes, hash)
  
print(result)

