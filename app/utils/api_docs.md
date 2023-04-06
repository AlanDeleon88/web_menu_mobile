# E to Z menu API Documentation

## All endpoints that require authentication

All endpoints require a current user to be logged in.

- Request: endpoints that require authentication
- Error Response: Require authentication

  - Status Code: 401
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "message": "Authentication required",
      "statusCode": 401
    }
    ```

## All endpoints that require proper authorization

All endpoints that require authentication and the current user does not have the
correct role(s) or permission(s).

- Request: endpoints that require proper authorization
- Error Response: Require proper authorization

  - Status Code: 403
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "message": "Forbidden",
      "statusCode": 403
    }
    ```
## Sign Up a User

Creates a new user, logs them in as the current user, and returns the current
user's information.

- Require Authentication: false
- Request

  - Method: Post
  - URL: /users/signup
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "firstName": "John",
      "lastName": "Smith",
      "username": "jsmith",
      "email": "john.smith@gmail.com",
      "password": "secret password"
    }
    ```

- Successful Response
  - Status Code: 200
  - Headers:
    - Content-Type: application/json
  - Body:
      ```json
    {
      "id" : 1
      "firstName": "John",
      "lastName": "Smith",
      "username": "jsmith",
      "email": "john.smith@gmail.com",
      "menus" : [],
    }
    ```

- Error response: User already exists with the specified email

  - Status Code: 403
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "message": "User already exists",
      "statusCode": 403,
      "errors": {
        "email": "User with that email already exists"
      }
    }
    ```

- Error response: Body validation errors

  - Status Code: 400
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "message": "Validation error",
      "statusCode": 400,
      "errors": {
        "credential": "Invalid credential",
        "firstName": "First Name is required",
        "lastName": "Last Name is required"
      }
    }
    ```

## User Authorization
### Login a user
- Request
  -Method: Post
  -URL : /auth/login
  - Body:
  - Body:
      ```json
    {
      "email" : "john.smith@gmail.com",
      "password" : "password"
    }
    ```
- Successful Response
  -Status Code: 201
  - Headers:
    -Content-Type : application/json
  - Body:
    ```json
            "user" : {
                    "id" : 1
                    "first_name" : "John"
                    "last_name"  : "Smith"
                    "username" : "Jsmhiz"
                    "email" : "Jsmix@gmail.com"
                    "menus" : [
                                 {
                                     "id" : 1
                                     "name" : "huku"
                                     "user_id" : 1
                                 }
                              ]

      }
    ```

- Error Response: Invalid credentials

  - Status Code: 401
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "message": "Invalid credentials",
      "statusCode": 401
    }
    ```

- Error response: Body validation errors

  - Status Code: 400
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "message": "Validation error",
      "statusCode": 400,
      "errors": {
        "Credential": "Credential is required",
        "password": "Password is required"
      }
    }
    ```
### Logout a user
- logs a user out of the session

- Require Authentication: true
- Request
  - Method: Delete
  - URL : /auth/logout
  - Body: none
- Successful Response:
  - Body :
       ```json
          {
             "msg" : "logout successful"
          }
      ```
## Users
### Get all registered users
Returns all users.
- Require Authentication : true
- Request
  - Method : GET
  - URL: /users
  - Body: none
- Successful Response
  - Status code: 200
  - Headers:
    - Content-Type: application/json
  -Body:
    ```json
     {
       "users": [
                {
                  "id" : 1,
                  "first_name" : "John",
                  "last_name" : "Smith",
                  "username"  : "jshimizle",
                  "email" : "jshmiz@gmail.com",
                }
              ]
     }

    ```
### get user by id
- Get a user by id
- Require Authentication: true
- Request
  - Method : GET
  - URL : /users/:id
  - Body : none
- Successful Response
  - Status Code : 200
  - Headers:
    - Content-Type: application/json
  - Body:
    ```json
            "user" : {
                    "id" : 1
                    "first_name" : "John"
                    "last_name"  : "Smith"
                    "username" : "Jsmhiz"
                    "email" : "Jsmix@gmail.com"
                    "menus" : [
                                 {
                                     "id" : 1
                                     "name" : "huku"
                                     "user_id" : 1
                                 }
                              ]

      }
    ```
- Error Response: Can't find user
  - Status Code : 404
  ```json
    {"error" : "unable to find a user with that id"}
  ```
## Menus
### Get all menus
Returns all menus.
- Require Authentication : true
- Request
  - Method : GET
  - URL: /menus
  - Body: none
- Successful Response
  - Status code: 200
  - Headers:
    - Content-Type: application/json
  -Body:
    ```json
     {
       "menus": [
                {
                  "id" : 1,
                  "name" : "huku",
                  "user_id" : 1
                },
                 {"..."}
              ]
     }

    ```
### Get menu by Id
Returns all menus.
- Require Authentication : true
- Request
  - Method : GET
  - URL: /menus/:id
  - Body: none
- Successful Response
  - Status code: 200
  - Headers:
    - Content-Type: application/json
  -Body:
    ```json
     {
       "menu":
                {
                  "id" : 1,
                  "name" : "huku",
                  "user_id" : 1
                }
     }

    ```
- Error response: menu not found

  - Status Code: 404
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "message": "not found",
      "statusCode": 404,
      "errors": {
        "name": "Menu not found with that id"
      }
    }
### Create a new menu

- Require Authentication : true
- Require Authorization: true
- Request
  - Method : POST
  - URL: /menus
    -Body:
```
{
    user_id : 1,
    name : "huku"
    description : "optional"
}

```

- Successful Response
  - Status code: 201
  - Headers:
    - Content-Type: application/json
    -Body:
```
{
    id : 1,
    user_id : 1,
    name : "huku"
    description : "optional"
}

```
- Error response: Form validation errors

  - Status Code: 403
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "message": "Form validation error",
      "statusCode": 403,
      "errors": {
        "name": "Name is required"
      }
    }
    ```
### Editing an existing menu
- Require Authentication : true
- Require Authorization: true, User must own the menu to be edited. IE User.id === Menu.user_id
- Request
  - Method : Put
  - URL: /menus/:id
    -Body:
```
{
    user_id : 1,
    name : "huku EDITED"
    description : "optional EDITED"
}

```

- Successful Response
  - Status code: 201
  - Headers:
    - Content-Type: application/json
    -Body:
```
{
    id : 1,
    user_id : 1,
    name : "huku EDITED"
    description : "optional EDITED"
}

```
- Error response: Form validation errors

  - Status Code: 403
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "message": "Form validation error",
      "statusCode": 403,
      "errors": {
        "name": "Name is required"
      }
    }
    ```
### Delete an existing menu
- Require Authentication : true
- Require Authorization: true, User must own the menu to be deleted. IE User.id === Menu.user_id
- Request
  - Method : DELETE
  - URL: /menus/:id
    -Body: None

- Successful Response
  - Status code: 201
  - Headers:
    - Content-Type: application/json
    -Body:
```
{
    "message" : "menu successfully deleted"
}

```
- Error response: not found

  - Status Code: 404
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "message": "menu not found",
      "statusCode": 404,
      "errors": {
        "message": "menu not found"
      }
    }
    ```
### get all menu's sub-menus
Returns all sub menus of a menu.
- Require Authentication : true
- Request
  - Method : GET
  - URL: /menus/:id/sub_menus
  - Body: none
- Successful Response
  - Status code: 200
  - Headers:
    - Content-Type: application/json
  -Body:
    ```json
     {
       "sub_menus":
                [
                   {
                      "id" : 1,
                      "name" : "appetizers",
                      "menu_id" : 1,
                      "description" : "Small bites to be share"
                  },
                  {"..."}
                ]
     }

    ```
- Error response: not found

  - Status Code: 404
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "message": "menu not found",
      "statusCode": 404,
      "errors": {
        "message": "menu not found"
      }
    }
    ```
### Add a sub-menu to menu
- Require Authentication : true
- Require Authorization : true
- Request
  - Method : POST
  - URL: /menus/:id
  - Body: none
- Successful Response
  - Status code: 200
  - Headers:
    - Content-Type: application/json
  -Body:
    ```json
     {
       "sub_menu":
                {
                  "id" : 2,
                  "name" : "House Rolls",
                  "description" : "House Specialty rolls, bigger than classic rolls."
                  "user_id" : 1
                }
     }

    ```
- Error response: Form validation errors

  - Status Code: 404
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "message": "Form validation errors",
      "statusCode": 404,
      "errors": {
        "name": "Name required"
      }
    }
## Sub Menus

### Get sub_menu by id
Returns a specific sub menu through its id
- Require Authentication : true
- Request
  - Method : GET
  - URL: /sub_menus/:id
  - Body: none
- Successful Response
  - Status code: 200
  - Headers:
    - Content-Type: application/json
  -Body:
    ```json
     {
       "sub_menu":
                {
                  "id" : 1,
                  "name" : "appetizers",
                  "menu_id" : 1,
                  "description": "dishes to share",
                  "user_id" : 1
                }
     }

    ```
- Error response: menu not found

  - Status Code: 404
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "message": "not found",
      "statusCode": 404,
      "errors": {
        "name": "sub-menu not found with that id"
      }
    }
### Edit a sub menu

## Sub Menu Items

## Tags

## Modifications
