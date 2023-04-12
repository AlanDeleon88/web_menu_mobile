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
  - URL: /api/users
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
                    "id" : 1,
                    "first_name" : "John",
                    "last_name"  : "Smith",
                    "username" : "Jsmhiz",
                    "email" : "Jsmix@gmail.com",
                    "menus" : [
                                 {
                                     "id" : 1,
                                     "name" : "huku",
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

### get all restaunts owned by user
- Require Authentication: true
- Request
  - Method : GET
  - URL : /users/:id/restaurants
  - Body : none
-Response

## Restaurants

### get restaurant by id

### add a new restaurant

### edit a restaurant

### delete a restaurant

## Menus
### Get all menus
Returns all menus.
- Require Authentication : true
- Request
  - Method : GET
  - URL: /api/menus
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
  - URL: /api/menus/:id
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
```json
{
    "id" : 1,
    "user_id" : 1,
    "name" : "huku",
    "description" : "optional"
}

```

- Successful Response
  - Status code: 201
  - Headers:
    - Content-Type: application/json
    -Body:
```json
{
    "id" : 1,
    "user_id" : 1,
    "name" : "huku",
    "description" : "optional"
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
  - URL: /api/menus/:id
    -Body:

```json
    {
        "user_id" : 1,
        "name" : "huku EDITED",
        "description" : "optional EDITED"
    }
```


- Successful Response
  - Status code: 201
  - Headers:
    - Content-Type: application/json
    -Body:
```json
    {
        "id" : 1,
        "user_id" : 1,
        "name" : "huku EDITED",
        "description" : "optional EDITED"
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
  - URL: /api/menus/:id
    -Body: None

- Successful Response
  - Status code: 201
  - Headers:
    - Content-Type: application/json
    -Body:
```json
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
  - URL: /api/menus/:id/sub_menus
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
  - URL: /api/menus/:id
  - Body:
    ```json
     {
       "sub_menu":
                {
                  "id" : 2,
                  "name" : "House Rolls_Edited",
                  "description" : "House Specialty rolls, bigger than classic rolls._EDITED",
                  "user_id" : 1,
                  "menu_id" : 1,
                }
     }

    ```
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
                  "description" : "House Specialty rolls, bigger than classic rolls._EDITED",
                  "user_id" : 1,
                  "menu_id" : 1
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
    ```

### Get all tags for a menu
Returns all tags a menu has.
- Require Authentication : true
- Request
  - Method : GET
  - URL: /api/menus/:id/tags
  - Body: none
- Successful Response
  - Status code: 200
  - Headers:
    - Content-Type: application/json
  -Body:
    ```json
     {
       "tags":
                [
                   {
                      "id" : 1,
                      "name" : "vegitarian",
                      "menu_id" : 1,
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

### Add a new tag to menu
Add a new tag to a menu
- Require Authentication : true
- Require Authorization : true
- Request
  - Method : POST
  - URL: /api/menus/:id/tags
  - Body:
    ```json
     {

                {

                      "name" : "vegitarian",

                }
     }

    ```
- Successful Response
  - Status code: 201
  - Headers:
    - Content-Type: application/json
  -Body:
    ```json
     {

                   {
                      "id" : 3,
                      "name" : "vegitarian",
                      "menu_id" : 1,
                  }
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
- Error response: Form validation

  - Status Code: 401
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "message": "Form validation Error",
      "statusCode": 404,
      "errors": {
        "message": "tag field required"
      }
    }
    ```
### Add a new modification to menu
Add new modification to menu
- Require Authentication : true
- Require Authorization : true
- Request
  - Method : POST
  - URL: /api/menus/:id/modifications
  - Body:
    ```json
     {

                {

                      "body" : "extra veggies",

                }
     }

    ```
- Successful Response
  - Status code: 201
  - Headers:
    - Content-Type: application/json
  -Body:
    ```json
     {

                   {
                      "id" : 3,
                      "body" : "extra veggies",
                      "menu_id" : 1,
                  }
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
- Error response: Form validation

  - Status Code: 401
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "message": "Form validation Error",
      "statusCode": 404,
      "errors": {
        "message": "body field required"
      }
    }
    ```

## Sub Menus

### Get sub_menu by id
Returns a specific sub menu through its id
- Require Authentication : true
- Request
  - Method : GET
  - URL: /api/sub_menus/:id
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
    ```
### Edit a sub menu
Updates a sub menu through its ID
- Require Authentication : true
- Rquires Authorization: true
- Request
  - Method : PUT
  - URL: /api/sub_menus/:id
  - Body:
    ```json
     {
       "sub_menu":
                {
                  "id" : 1,
                  "name" : "appetizers_edited",
                  "menu_id" : 1,
                  "description": "dishes to share_edited",
                  "user_id" : 1
                }
     }

    ```

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
                  "name" : "appetizers_edited",
                  "menu_id" : 1,
                  "description": "dishes to share_edited",
                  "user_id" : 1
                }
     }

    ```
- Error response: sub-menu not found

  - Status Code: 404
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "message": "not found",
      "statusCode": 404,
      "errors": {
        "message": "sub-menu not found with that id"
      }
    }
    ```
- Error response: Form validation errors

  - Status Code: 401
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "message": "Form validation errors",
      "statusCode": 404,
      "errors": {
        "name": "Name field is required"
      }
    }
    ```

### Delete a sub-menu
Delete a sub-menu
Delete a sub menu through its ID
- Require Authentication : true
- Rquires Authorization: true
- Request
  - Method : DELETE
  - URL: /api/sub_menus/:id
  - Body: none
- Successful Response
  - Status code: 200
  - Headers:
    - Content-Type: application/json
  -Body: can return the deleted sub-menu item to update redux store
    ```json
     {
       "sub_menu":
                {
                  "id" : 1,
                  "name" : "appetizers_edited",
                  "menu_id" : 1,
                  "description": "dishes to share_edited",
                  "user_id" : 1
                }
     }

    ```
- Error response: sub-menu not found

  - Status Code: 404
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "message": "not found",
      "statusCode": 404,
      "errors": {
        "message": "sub-menu not found with that id"
      }
    }
    ```

### Get all items of a sub-menu
Get all items that belong to the sub-menu through its ID
- Require Authentication : true
- Rquires Authorization: true
- Request
  - Method : GET
  - URL: /api/sub_menus/:id/items
  - Body: none
- Successful Response
  - Status code: 200
  - Headers:
    - Content-Type: application/json
  -Body:
    ```json
     {
       "sub_menu_items":
                [
                    {
                        "id" : 1,
                        "name" : "gyoza",
                        "sub_menu_id" : 1,
                        "description": "essentially pot stickers",
                        "user_id" : 1,
                        "image" : "url" --> in the future could be its own table so an item can have multiple images.

                    },
                ]

     }

    ```
- Error response: sub-menu not found

  - Status Code: 404
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "message": "not found",
      "statusCode": 404,
      "errors": {
        "message": "sub-menu not found with that id"
      }
    }
    ```

## Sub Menu Items

### Get sub-menu item by id
Updates a sub menu through its ID
- Require Authentication : true
- Rquires Authorization: true
- Request
  - Method : GET
  - URL: /api/sub_menu_items/:id
  - Body: none
- Successful Response
  - Status code: 200
  - Headers:
    - Content-Type: application/json
  -Body:
    ```json
     {
       "sub_menu_item":
                {
                  "id" : 1,
                  "name" : "gyoza",
                  "sub_menu_id" : 1,
                  "description": "essentially pot stickers",
                  "user_id" : 1,
                  "price" : 8.50,
                  "image" : url,
                  "tags" : [
                              {
                                "id" : 1,
                                "tag" : "appetizer",
                                "menu_id" : 1,
                                "user_id" : 1
                              },
                              {
                                "id" : 2,
                                "tag" : "hot food",
                                "menu_id" : 1,
                                "user_id" : 1
                              }

                           ],
                  "ingredients" : [
                                    {
                                        "id" : 1,
                                        "menu_id" : 1,
                                        "user_id" : 1,
                                        "name" : "pork"
                                    },
                                    {
                                        "id" : 2,
                                        "menu_id" : 1,
                                        "user_id" : 1,
                                        "name" : "onions"
                                    }
                                  ],
                    "modifications" : [
                                        {
                                            "id" : 1,
                                            "menu_id" : 1,
                                            "body" : "extra sauce",
                                            "price" : 1.50
                                        },
                                      ],
                }
     }

    ```
- Error response: sub-menu-item not found

  - Status Code: 404
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "message": "not found",
      "statusCode": 404,
      "errors": {
        "message": "sub-menu not found with that id"
      }
    }
    ```

### Edit a sub-menu item
Updates a sub_menu_item through its ID
- Require Authentication : true
- Rquires Authorization: true
- Request
  - Method : PUT
  - URL: /api/sub_menu_items/:id
  - Body:
  ```json
    {
        {
            "id": 1,
            "name": "gyoza_super",
            "description" : "new description",
        }
    }
  ```
- Successful Response
  - Status code: 201
  - Headers:
    - Content-Type: application/json
  -Body:
    ```json
     {
       "sub_menu_item":
                {
                  "id" : 1,
                  "name" : "gyoza_super",
                  "sub_menu_id" : 1,
                  "description": "new description",
                  "user_id" : 1,
                  "price" : 8.50,
                  "image" : url,
                  "tags" : [
                              {
                                "id" : 1,
                                "tag" : "appetizer",
                                "menu_id" : 1,
                                "user_id" : 1
                              },
                              {
                                "id" : 2,
                                "tag" : "hot food",
                                "menu_id" : 1,
                                "user_id" : 1
                              }

                           ],
                  "ingredients" : [
                                    {
                                        "id" : 1,
                                        "menu_id" : 1,
                                        "user_id" : 1,
                                        "name" : "pork"
                                    },
                                    {
                                        "id" : 2,
                                        "menu_id" : 1,
                                        "user_id" : 1,
                                        "name" : "onions"
                                    }
                                  ],
                    "modifications" : [
                                        {
                                            "id" : 1,
                                            "menu_id" : 1,
                                            "body" : "extra sauce",
                                            "price" : 1.50
                                        },
                                      ],
                }
     }

    ```
- Error response: sub-menu-item not found

  - Status Code: 404
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "message": "not found",
      "statusCode": 404,
      "errors": {
        "message": "sub-menu not found with that id"
      }
    }
    ```

- Error response: Form Validations Error

  - Status Code: 404
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "message": "Form validation error",
      "statusCode": 404,
      "errors": {
        "name": "name field required"
      }
    }
    ```


### Delete a sub-menu item
Delete a sub-menu item
- Require Authentication : true
- Rquires Authorization: true
- Request
  - Method : DELETE
  - URL: /api/sub_menu_items/:id
  - Body: none
- Successful Response
  - Status code: 201
  - Headers:
    - Content-Type: application/json
  -Body:
    ```json
     {
       "sub_menu_item":
                {
                  "id" : 1,
                  "name" : "gyoza_super",
                  "sub_menu_id" : 1,
                  "description": "new description",
                  "user_id" : 1,
                  "price" : 8.50,
                  "image" : url,
                  "tags" : [
                              {
                                "id" : 1,
                                "tag" : "appetizer",
                                "menu_id" : 1,
                                "user_id" : 1
                              },
                              {
                                "id" : 2,
                                "tag" : "hot food",
                                "menu_id" : 1,
                                "user_id" : 1
                              }

                           ],
                  "ingredients" : [
                                    {
                                        "id" : 1,
                                        "menu_id" : 1,
                                        "user_id" : 1,
                                        "name" : "pork"
                                    },
                                    {
                                        "id" : 2,
                                        "menu_id" : 1,
                                        "user_id" : 1,
                                        "name" : "onions"
                                    }
                                  ],
                    "modifications" : [
                                        {
                                            "id" : 1,
                                            "menu_id" : 1,
                                            "body" : "extra sauce",
                                            "price" : 1.50
                                        },
                                      ],
                },
     }

    ```
- Error response: sub-menu not found

  - Status Code: 404
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "message": "not found",
      "statusCode": 404,
      "errors": {
        "message": "sub-menu not found with that id"
      }
    }
    ```

### Add a tag to a sub_menu_item
Add a new tag to a sub_menu_item
- Require Authentication : true
- Rquires Authorization: true
- Request
  - Method : POST
  - URL: /api/sub_menu_item/:id/tag
  - Body:
    ```json
     {
                {
                    tag_id: 2,
                },
     }

    ```
- Successful Response
  - Status code: 201
  - Headers:
    - Content-Type: application/json
  -Body:
    ```json
     {
       "sub_menu_item_tags":
                [
                    {
                        "id" : 1,
                        "menu_id" : 1,
                        "tag" : "Raw Food",
                        "tag_item":
                        {
                            "id" : 1,
                            "sub_menu_item_id" : 1,
                            "tag_id" :2
                        }
                    }

                ]


     }

    ```
- Error response: tag not found

  - Status Code: 404
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "message": "not found",
      "statusCode": 404,
      "errors": {
        "message": "tag not found with that id"
      }
    }
    ```
- Error response: sub_menu_item not found

  - Status Code: 404
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "message": "not found",
      "statusCode": 404,
      "errors": {
        "message": "sub_menu_item not found with that id"
      }
    }
    ```

### Add a modification to a sub_menu_item
Add a new modification to a sub_menu_item
- Require Authentication : true
- Rquires Authorization: true
- Request
  - Method : POST
  - URL: /api/sub_menu_item/:id/modification
  - Body:
    ```json
     {
                {
                    mod_id: 2,
                },
     }

    ```
- Successful Response
  - Status code: 201
  - Headers:
    - Content-Type: application/json
  -Body:
    ```json
     {
       "sub_menu_item_modifications":
                [
                    {
                        "id" : 1,
                        "menu_id" : 1,
                        "body" : "Add salmon",
                        "mod_item":
                        {
                            "id" : 1,
                            "sub_menu_item_id" : 1,
                            "mod_id" :2
                        }
                    }

                ]


     }

    ```
- Error response: mod not found

  - Status Code: 404
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "message": "not found",
      "statusCode": 404,
      "errors": {
        "message": "mod not found with that id"
      }
    }
    ```
- Error response: sub_menu_item not found

  - Status Code: 404
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "message": "not found",
      "statusCode": 404,
      "errors": {
        "message": "sub_menu_item not found with that id"
      }
    }
    ```

### remove a tag from a sub_menu_item
remove a tag to a sub_menu_item
- Require Authentication : true
- Rquires Authorization: true
- Request
  - Method : DELETE
  - URL: /api/sub_menu_item/:id/tag
  - Body:
    ```json
     {
                {
                    tag_id: 2,
                    sub_menu_id: 1
                },
     }

    ```
- Successful Response
  - Status code: 201
  - Headers:
    - Content-Type: application/json
  -Body:
    ```json
     {
       "sub_menu_item_tag":
                                        {
                                            "id": 1,
                                            "tag_id" : 2,
                                            "sub_menu_id": 1
                                        }

     }

    ```
- Error response: tag not found

  - Status Code: 404
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "message": "not found",
      "statusCode": 404,
      "errors": {
        "message": "tag not found with that id"
      }
    }
    ```
- Error response: sub_menu_item not found

  - Status Code: 404
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "message": "not found",
      "statusCode": 404,
      "errors": {
        "message": "sub_menu_item not found with that id"
      }
    }
    ```

### Remove a modification from a sub_menu_item
remove a tag to a sub_menu_item
- Require Authentication : true
- Rquires Authorization: true
- Request
  - Method : DELETE
  - URL: /api/sub_menu_item/:id/modifications
  - Body:
    ```json
     {
                {
                    mod_id: 2,
                    sub_menu_id: 1
                },
     }

    ```
- Successful Response
  - Status code: 201
  - Headers:
    - Content-Type: application/json
  -Body:
    ```json
     {
       "sub_menu_item_modification":
                                        {
                                            "id": 1,
                                            "mod_id" : 2,
                                            "sub_menu_id": 1
                                        }

     }

    ```
- Error response: modification not found

  - Status Code: 404
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "message": "not found",
      "statusCode": 404,
      "errors": {
        "message": "modification not found with that id"
      }
    }
    ```
- Error response: sub_menu_item not found

  - Status Code: 404
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "message": "not found",
      "statusCode": 404,
      "errors": {
        "message": "sub_menu_item not found with that id"
      }
    }
    ```




## Tags
### Edit a Tag
Edit a tag
- Require Authentication : true
- Rquires Authorization: true
- Request
  - Method : PUT
  - URL: /api/tags/:id
  - Body:
    ```json
     {
                {
                    "tag": "Raw Food",
                },
     }

    ```
- Successful Response
  - Status code: 201
  - Headers:
    - Content-Type: application/json
  -Body:
    ```json
     {
       "tag":
                {
                    "id" : 1,
                    "menu_id" : 1,
                    "tag" : "Raw Food"

                },
     }

    ```
- Error response: tag not found

  - Status Code: 404
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "message": "not found",
      "statusCode": 404,
      "errors": {
        "message": "tag not found with that id"
      }
    }
    ```
- Error response: Form validation

  - Status Code: 404
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "message": "Form validation error",
      "statusCode": 401,
      "errors": {
        "message": "tag field required."
      }
    }
    ```

### Delete a tag
Delete a tag by id
- Require Authentication : true
- Rquires Authorization: true
- Request
  - Method : DELETE
  - URL: /api/tags/:id
  - Body: none
- Successful Response
  - Status code: 201
  - Headers:
    - Content-Type: application/json
  -Body:
    ```json
     {
       "tag":
                {
                    "id" : 1,
                    "menu_id" : 1,
                    "tag" : "Raw Food"

                },
     }

    ```
- Error response: tag not found

  - Status Code: 404
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "message": "not found",
      "statusCode": 404,
      "errors": {
        "message": "tag not found with that id"
      }
    }
    ```

## Modifications

### Edit a modification
Edit a modification
- Require Authentication : true
- Rquires Authorization: true
- Request
  - Method : PUT
  - URL: /api/modifications/:id
  - Body:
    ```json
     {
                    {
                        "body" : "Add Tunas"
                    },
     }

    ```
- Successful Response
  - Status code: 201
  - Headers:
    - Content-Type: application/json
  -Body:
    ```json
     {
                    {
                        "id" : 1,
                        "menu_id" : 1,
                        "body" : "Add Tunas"
                    },
     }

    ```
    ```
- Error response: modification not found

  - Status Code: 404
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "message": "not found",
      "statusCode": 404,
      "errors": {
        "message": "modification not found with that id"
      }
    }
    ```

### delete a modification
Delete a modification
- Require Authentication : true
- Rquires Authorization: true
- Request
  - Method : DELETE
  - URL: /api/modifications/:id
  - Body: none
- Successful Response
  - Status code: 201
  - Headers:
    - Content-Type: application/json
  -Body:
    ```json
     {
                    {
                        "id" : 1,
                        "menu_id" : 1,
                        "body" : "Add Tunas"
                    },
     }

    ```
    ```
- Error response: modification not found

  - Status Code: 404
  - Headers:
    - Content-Type: application/json
  - Body:

    ```json
    {
      "message": "not found",
      "statusCode": 404,
      "errors": {
        "message": "modification not found with that id"
      }
    }
    ```
