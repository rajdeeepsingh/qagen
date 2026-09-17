# Test Cases: Login

**Login API Test Cases**

**Happy Path**

1. **Valid Credentials**
   - Given the API endpoint for login
   - When I send a POST request with valid username and password
   - Then the response status code is 200
   - And the response contains the user's details

2. **Valid Credentials with Empty Password**
   - Given the API endpoint for login
   - When I send a POST request with valid username and empty password
   - Then the response status code is 200
   - And the response contains the user's details

3. **Valid Credentials with Empty Username**
   - Given the API endpoint for login
   - When I send a POST request with empty username and valid password
   - Then the response status code is 200
   - And the response contains the user's details

**Negative Cases**

1. **Invalid Username**
   - Given the API endpoint for login
   - When I send a POST request with invalid username and valid password
   - Then the response status code is 401
   - And the response contains an error message

2. **Invalid Password**
   - Given the API endpoint for login
   - When I send a POST request with valid username and invalid password
   - Then the response status code is 401
   - And the response contains an error message

3. **Empty Username and Password**
   - Given the API endpoint for login
   - When I send a POST request with empty username and password
   - Then the response status code is 400
   - And the response contains an error message

4. **Invalid Request Method**
   - Given the API endpoint for login
   - When I send a GET request with valid username and password
   - Then the response status code is 405
   - And the response contains an error message

5. **Invalid Request Body**
   - Given the API endpoint for login
   - When I send a POST request with invalid request body
   - Then the response status code is 400
   - And the response contains an error message

**Edge Cases**

1. **Username with Special Characters**
   - Given the API endpoint for login
   - When I send a POST request with username containing special characters and valid password
   - Then the response status code is 401
   - And the response contains an error message

2. **Password with Special Characters**
   - Given the API endpoint for login
   - When I send a POST request with valid username and password containing special characters
   - Then the response status code is 401
   - And the response contains an error message

3. **Username with Non-ASCII Characters**
   - Given the API endpoint for login
   - When I send a POST request with username containing non-ASCII characters and valid password
   - Then the response status code is 401
   - And the response contains an error message

4. **Password with Non-ASCII Characters**
   - Given the API endpoint for login
   - When I send a POST request with valid username and password containing non-ASCII characters
   - Then the response status code is 401
   - And the response contains an error message

**Boundary Conditions**

1. **Username Length Limit**
   - Given the API endpoint for login
   - When I send a POST request with username at the maximum length and valid password
   - Then the response status code is 200
   - And the response contains the user's details

2. **Password Length Limit**
   - Given the API endpoint for login
   - When I send a POST request with valid username and password at the maximum length
   - Then the response status code is 200
   - And the response contains the user's details

3. **Username Length Min**
   - Given the API endpoint for login
   - When I send a POST request with username at the minimum length and valid password
   - Then the response status code is 200
   - And the response contains the user's details

4. **Password Length Min**
   - Given the API endpoint for login
   - When I send a POST request with valid username and password at the minimum length
   - Then the response status code is 200
   - And the response contains the user's details