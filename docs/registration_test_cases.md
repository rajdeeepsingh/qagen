# Test Cases: Registration

**Registration Format: Gherkin for Mobile App**

**Feature: User Registration**

**Background:**
- Mobile app is installed and launched.
- User has a valid internet connection.

**Scenario: Happy Path**

| Step | Description | Expected Result |
| --- | --- | --- |
| 1 | User taps on "Register" button | Registration form appears |
| 2 | User enters valid email address | Email address is validated |
| 3 | User enters valid password | Password is validated |
| 4 | User confirms password | Password confirmation is validated |
| 5 | User enters valid name | Name is validated |
| 6 | User taps on "Register" button | User is successfully registered |
| 7 | User receives confirmation email | Email is sent to user's email address |

**Scenario: Negative Cases**

| Step | Description | Expected Result |
| --- | --- | --- |
| 1 | User enters invalid email address | Error message appears |
| 2 | User enters weak password | Error message appears |
| 3 | User enters mismatched passwords | Error message appears |
| 4 | User enters empty name | Error message appears |
| 5 | User taps on "Register" button without filling any fields | Error message appears |
| 6 | User enters email address already in use | Error message appears |

**Scenario: Edge Cases**

| Step | Description | Expected Result |
| --- | --- | --- |
| 1 | User enters email address with special characters | Email address is validated |
| 2 | User enters password with special characters | Password is validated |
| 3 | User enters name with special characters | Name is validated |
| 4 | User taps on "Register" button multiple times | Registration form remains unchanged |
| 5 | User navigates away from registration form and returns | Registration form remains unchanged |

**Scenario: Boundary Conditions**

| Step | Description | Expected Result |
| --- | --- | --- |
| 1 | User enters email address with maximum allowed length | Email address is validated |
| 2 | User enters password with maximum allowed length | Password is validated |
| 3 | User enters name with maximum allowed length | Name is validated |
| 4 | User enters email address with minimum allowed length | Error message appears |
| 5 | User enters password with minimum allowed length | Error message appears |
| 6 | User enters name with minimum allowed length | Error message appears |

**Scenario: Error Handling**

| Step | Description | Expected Result |
| --- | --- | --- |
| 1 | Network connection is lost during registration | Error message appears |
| 2 | Server is down during registration | Error message appears |
| 3 | User taps on "Register" button during server maintenance | Error message appears |
| 4 | User enters invalid characters in email address | Error message appears |
| 5 | User enters invalid characters in password | Error message appears |
| 6 | User enters invalid characters in name | Error message appears |