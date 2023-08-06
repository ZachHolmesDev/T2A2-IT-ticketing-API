# T2A2 - API Webserver Project README

This document describes the various aspects of the My IT Ticket System Web Server. This includes its purpose, database system choice, API endpoints, entity-relationship diagram (ERD), third-party services, model relationships, database relations, and task tracking.

**link to my github repo: [T2A2_API_src](https://github.com/zholmes430/T2A2_API_src)**

- [T2A2 - API Webserver Project README](#t2a2---api-webserver-project-readme)
  - [1-2 Problem Statement](#1-2-problem-statement)
    - [Identification of the Problem](#identification-of-the-problem)
    - [Why is it a Problem?](#why-is-it-a-problem)
    - [Solution](#solution)
  - [3 Database System](#3-database-system)
    - [Choice and Drawbacks of This Database System](#choice-and-drawbacks-of-this-database-system)
      - [Justification for Using PostgreSQL in the IT Ticket System API:](#justification-for-using-postgresql-in-the-it-ticket-system-api)
      - [Benefits of PostgreSQL for this Application:](#benefits-of-postgresql-for-this-application)
      - [Drawbacks of PostgreSQL for this Application:](#drawbacks-of-postgresql-for-this-application)
  - [4 ORM and Its Key Functionalities](#4-orm-and-its-key-functionalities)
    - [ORM  Benefits and Functionalities](#orm--benefits-and-functionalities)
      - [Justification for Using SQLAlchemy in the IT Ticket System API](#justification-for-using-sqlalchemy-in-the-it-ticket-system-api)
      - [Key Functionalities of SQLAlchemy](#key-functionalities-of-sqlalchemy)
      - [Benefits of SQLAlchemy for this Application](#benefits-of-sqlalchemy-for-this-application)
  - [5 API Endpoints](#5-api-endpoints)
    - [Endpoints List](#endpoints-list)
    - [Auth](#auth)
      - [POST /auth/register](#post-authregister)
      - [POST /auth/register/admin](#post-authregisteradmin)
      - [POST /auth/login](#post-authlogin)
    - [Users](#users)
      - [GET /users](#get-users)
      - [GET /users/{id}](#get-usersid)
      - [PATCH /users/{id}](#patch-usersid)
      - [PUT /users/{id}](#put-usersid)
      - [DELETE /users/{id}](#delete-usersid)
    - [Tickets](#tickets)
      - [GET: list all tickets](#get-list-all-tickets)
      - [GET /tickets/{id}](#get-ticketsid)
      - [POST /tickets/{id}](#post-ticketsid)
      - [PATCH /tickets/{id}](#patch-ticketsid)
      - [PUT /tickets/{id}](#put-ticketsid)
      - [DELETE /tickets/{id}](#delete-ticketsid)
    - [Comments](#comments)
      - [GET /comments](#get-comments)
      - [GET /comments/{id}](#get-commentsid)
      - [POST /comments/{id}](#post-commentsid)
      - [PATCH /comments/{id}](#patch-commentsid)
      - [PUT /comments/{id}](#put-commentsid)
      - [DELETE /comments/{id}](#delete-commentsid)
  - [6 Entity-Relationship Diagram](#6-entity-relationship-diagram)
    - [ERD: DBML](#erd-dbml)
  - [7 Third-Party Services](#7-third-party-services)
    - [Third-Party Services Used](#third-party-services-used)
  - [8 Model Relationships](#8-model-relationships)
    - [SQLalcemy Models and Their Relationships](#sqlalcemy-models-and-their-relationships)
      - [Users Model:](#users-model)
      - [Role Model:](#role-model)
      - [Tickets Model:](#tickets-model)
      - [Comment Model:](#comment-model)
      - [Summary:](#summary)
  - [9 Database Relations](#9-database-relations)
    - [Database Relations in the Application](#database-relations-in-the-application)
  - [10 Task Allocation and Tracking](#10-task-allocation-and-tracking)
    - [Notion's Kanban And Gnatt Chart](#notions-kanban-and-gnatt-chart)


## 1-2 Problem Statement 

### Identification of the Problem

Throughout my tenure as the sole IT technician for a small business housing approximately ten staff, I've observed the limitations of our current IT issue management methods. When relying on direct communication channels, including emails and chat applications, my workload spirals into disarray. A problematic aspect of this methodology is the veil it casts over the users, blurring their vision into the current operations of the IT department. They need to be more informed about the number of active issues, possible duplications in the tickets they are submitting, and the progression status of their prior submissions.

While seeking solutions to streamline these processes, I've been met with off-the-shelf software that introduces an additional layer of complexity. Not only are they cumbersome to integrate, but their setup consumes a disproportionate amount of time.

### Why is it a Problem? 


The absence of a structured system to monitor and manage IT tickets breeds chaos. Tickets can easily be neglected, misclassified, or entirely forgotten. This systemic inefficiency manifests as prolonged response and resolution times, amplifying system downtimes and, by extension, user dissatisfaction. 

Our current system, somewhat ironically, while aiming for efficiency, paves the way for redundant communication, subsequently leading to misallocated resources. The constant direct communication, especially for recurring trivial concerns, casts a shadow over significant issues, sometimes leading to them being inadvertently disregarded.

### Solution


The IT Ticket API I propose is geared towards rectifying these prevalent issues. At its core, it aims to bring order to the chaotic realm of IT issue management. Not only does it seek to organise and manage IT challenges optimally, but it also strives to bolster transparency for the staff. Through this API, users can gain insights into ticket statuses, potential issue duplications, and the overall workload of the IT department, fostering an environment of clarity and efficiency. By simplifying the user experience and centralising ticket management, the IT Ticket API heralds a new era of effective IT issue resolution tailored to the specific needs of small businesses.

## 3 Database System 


###  Choice and Drawbacks of This Database System


PostgreSQL was selected as the IT ticket system API database system, a choice grounded in an informed evaluation detailed in my workbook T2A1-A - Workbook Question 2.

#### Justification for Using PostgreSQL in the IT Ticket System API:


An IT ticket system demands a reliable, adaptable, and expandable database foundation. With varied ticket types, diverse user inputs, and potential business growth, the database must support a myriad of data types and scale efficiently.

#### Benefits of PostgreSQL for this Application:


1. **Reliability and Integrity:** PostgreSQL's unwavering commitment to the ACID (Atomicity, Consistency, Isolation, Durability) principles is a testament to its dedication to data reliability. The slightest error can be catastrophic in an IT ticket system where numerous tickets are generated, processed, and closed daily. However, with PostgreSQL, each transaction, whether creating a new ticket or updating an existing one, is executed with the highest reliability standard, ensuring minimal discrepancies.

2. **Adaptability:** The IT landscape is constantly in flux, with new challenges regularly emerging. PostgreSQL is designed to handle an extensive range of data types, including custom ones, thus providing the flexibility to incorporate unforeseen data types or structures in the future without cumbersome migrations or modifications.

3. **Extensibility:** PostgreSQL's extensible nature isn't limited to data types. Its support for potent extensions like PostGIS could be leveraged for novel functionalities. For instance, if the IT ticket system needs to incorporate location-based ticketing in the future, PostgreSQL already has the groundwork in place.

4. **Data Protection and Confidentiality:** In the digital era, safeguarding information assets is paramount, especially in systems that deal with proprietary or personal data. Its comprehensive suite of security tools distinguishes PostgreSQL. Beyond the inherent SSL support that encrypts data during transit, its role-based authentication provides granular control over who can access what data and to what extent. For an IT ticket system, which often captures and retains details about users, infrastructure vulnerabilities, or proprietary configurations, ensuring data confidentiality is non-negotiable. PostgreSQL's commitment to security provisions directly addresses this critical requirement.

5. **Active Community & Support:** Being open-source, PostgreSQL boasts a dynamic and responsive community. This translates to regular feature updates, prompt resolution of vulnerabilities, and a plethora of auxiliary tools to streamline and enhance database operations.

#### Drawbacks of PostgreSQL for this Application:

1. **Complexity:** PostgreSQL's sheer breadth of features, while a strength, can also be its Achilles heel. For someone new to database management, the system's multifaceted nature might prove daunting, extending the initial phase of setup and familiarisation.

2. **Performance Trade-offs:** While PostgreSQL offers commendable write speed, scenarios with an overwhelming number of read requests might experience a marginal performance dip, a trade-off stemming from its emphasis on data integrity.

3. **Resource Requirements:** As the scale of the ticket database increases, there is a proportional increase in PostgreSQL's hunger for resources. This could necessitate more powerful hardware, incurring higher operational costs.

4. **Operational Overheads:** Dedicated administrative expertise is pivotal to truly harnessing PostgreSQL's advanced functionalities. This could mean extensive training or hiring specialised personnel, which entail time and cost implications.

5. **Lack of Built-in Sharding:** While PostgreSQL is adept at handling voluminous data, it lacks native support for sharding. If the ticket system's database grows exponentially, one might have to rely on third-party tools for sharding, introducing another layer of complexity.

In summary, while PostgreSQL presents particular challenges, its robust suite of benefits tailored to the needs of an IT ticket system makes it a compelling choice. It is paramount to understand and prepare for its potential complexity. However, its virtues undeniably make a strong case for its selection when viewed broadly, especially regarding long-term scalability and adaptability.


## 4 ORM and Its Key Functionalities 


###  ORM  Benefits and Functionalities 


SQLAlchemy, a leading ORM in Python web applications, was chosen for the IT ticket system API. The underlying motivations for this selection have been assessed meticulously.

#### Justification for Using SQLAlchemy in the IT Ticket System API

An efficient IT ticket system requires a seamless interface between the application and the database. ORM tools like SQLAlchemy bridge this gap, making interactions more intuitive and less error-prone.

#### Key Functionalities of SQLAlchemy

1. **Expression Language**: SQLAlchemy employs a SQL expression language that is both comprehensive and neutral, offering a direct SQL-like way to interact with the database, but with the advantages of being DBMS-agnostic and more secure.

2. **Two-fold API Layers**: SQLAlchemy operates with two distinct layers:
   - **Core**: This is a low-level SQL abstraction layer. It provides a more explicit way to build SQL statements, catering to those who prefer to have finer control over their queries.
   - **ORM**: A high-level, object-oriented querying API that lets developers interact with the database in a way that is more akin to manipulating Python objects.

3. **Automatic Schema Creation**: With SQLAlchemy, the database schema can be created directly from Python classes. This facilitates rapid prototyping and ensures the database structure remains synchronised with the application's data models.

#### Benefits of SQLAlchemy for this Application

1. **Data Consistency**: SQLAlchemy's Unit of Work pattern ensures that all operations are bundled into a single transaction, meaning that all operations are executed successfully, or none are. This translates to consistency, especially in an IT ticket system where many concurrent database operations might occur.

2. **Abstraction**: One of SQLAlchemy's strongest suits is the abstraction it offers. By mediating interactions with the database, it shields developers from the intricacies of raw SQL, making development faster and more intuitive.

3. Adaptability: SQLAlchemy is designed to accommodate various database interaction preferences. From those who wish to have granular control with handcrafted SQL statements to those who lean towards the object-oriented ease of ORMs, its dual Core and ORM layers ensure every developer's approach is supported.

4. **Database Agnostic**: Should there ever be a need to switch the underlying database, SQLAlchemy's database-agnostic nature ensures that such a migration would be significantly smoother. Most of the application code would remain unchanged.

5. **Robust Security**: By utilising parameterised queries, SQLAlchemy effectively counters SQL injection attacks, bolstering the security of the IT ticket system.

6. **Active Community**: Being a popular choice in the Python community, SQLAlchemy enjoys extensive documentation, regular updates, and a large user base, ensuring that any challenges faced during development can be swiftly addressed.

In conclusion, SQLAlchemy's diverse functionalities and myriad benefits make it an optimal choice for the IT ticket system API. It streamlines the development process and introduces robustness and scalability to the application.

## 5 API Endpoints 

###  Endpoints List

  - [Auth](#auth)
    - [POST /auth/register](#post-authregister)
    - [POST /auth/register/admin](#post-authregisteradmin)
    - [POST /auth/login](#post-authlogin)
  - [Users](#users)
    - [GET /users](#get-users)
    - [GET /users/{id}](#get-usersid)
    - [PATCH /users/{id}](#patch-usersid)
    - [PUT /users/{id}](#put-usersid)
    - [DELETE /users/{id}](#delete-usersid)
  - [Tickets](#tickets)
    - [GET: list all tickets](#get-list-all-tickets)
    - [GET /tickets/{id}](#get-ticketsid)
    - [POST /tickets/{id}](#post-ticketsid)
    - [PATCH /tickets/{id}](#patch-ticketsid)
    - [PUT /tickets/{id}](#put-ticketsid)
    - [DELETE /tickets/{id}](#delete-ticketsid)
  - [Comments](#comments)
    - [GET /comments](#get-comments)
    - [GET /comments/{id}](#get-commentsid)
    - [POST /comments/{id}](#post-commentsid)
    - [PATCH /comments/{id}](#patch-commentsid)
    - [PUT /comments/{id}](#put-commentsid)
    - [DELETE /comments/{id}](#delete-commentsid)

### Auth

---

#### POST /auth/register

http://127.0.0.1:5000/auth/register

Register a new standard user account.

**Authentication:** Nill

**Request body:**

```json
{
  "name": "New User JOHN",
  "email": "john.doe@example.com",
  "password": "secret_password",
  "role": "user"
}
```

**Successful response:**

- Status code: 201
- Content:

```json
{
  "id": 7,
  "name": "New User JOHN",
  "email": "john.doe@example.com",
  "user_role": {
    "role_name": "user"
  },
  "created_tickets": [],
  "assigned_tickets": [],
  "created_comments": []
}
```

**Failed response:**

- Status code: 409
- Content:

```json
{
  "error": "Email address already in use"
}
```

---

#### POST /auth/register/admin

Register a new user account as a user with administrative privileges.

**Authentication:** Required. Token must match a valid user.

**Request body:** http://127.0.0.1:5000/auth/register/admin

```json
{
  "name": "POST Test ADMIN 2",
  "email": "ADMIN2@example.com",
  "password": "secret_password",
  "role": "admin"
}
```

**Successful response:**

- Status code: 201
- Content:

```json
{
  "id": 6,
  "name": "POST Test ADMIN 2",
  "email": "ADMIN2@example.com",
  "user_role": {
    "role_name": "admin"
  },
  "created_tickets": [],
  "assigned_tickets": [],
  "created_comments": []
}
```

**Failed response:**

- Status code: **400**
- Content:

```json
{
  "error": {
    "name": ["Missing data for required field."]
  }
}
```

---

#### POST /auth/login

http://127.0.0.1:5000/auth/login

Authenticate a user and retrieve a session token.

**Request body:**

**Authentication:** Required. Token must match a valid user.

```json
{
  "email": "john.doe@example.com",
  "password": "secret_password"
}
```

**Successful response:**

- Status code: 200
- Content:

```json
{
  "message": "welcome New User JOHN here is your token",
  "token": "JWT token string here"
}
```

**Failed response:**

- Status code: 400
- Content:

```json
{
  "message": "Invalid email or password"
}
```

---

### Users

---

#### GET /users

http://127.0.0.1:5000/users

Gets a list of all users

**Authentication:** Required. Token must match a valid user.

**Request body:**

```json
none
```

**Successful response:**

- Status code: 200 OK
- Content:

```json
[
  {
    "id": 1,
    "name": "Admin_id_1",
    "email": "admin@admin.com",
    "user_role": {
      "role_name": "admin"
    }
  },
  {
    "id": 2,
    "name": "Tech Zach_id_2",
    "email": "tech_Zach@email.com",
    "user_role": {
      "role_name": "tech"
    }
  },
  {
    "id": 3,
    "name": "User Meg_id_3",
    "email": "MEG@email.com",
    "user_role": {
      "role_name": "user"
    }
  }
]
```

**Failed response:**

- Status code: 404
- Content:

```json
{
  "message": "Route not found on this app"
}
```

---

#### GET /users/{id}

http://127.0.0.1:5000/users/1

Get a specific user's details.

**Authentication:** Required. Token must match a valid user.

**Successful response:**

- Status code: 200
- Content:

```json
{
  "id": 7,
  "name": "New User JOHN",
  "email": "john.doe@example.com",
  "user_role": {
    "role_name": "user"
  },
  "created_tickets": [],
  "assigned_tickets": [],
  "created_comments": []
}
```

**Failed response:**

- Status code: 404
- Content:

```json
{
  "message": "User not found"
}
```

---

#### PATCH /users/{id}

http://127.0.0.1:5000/users/1

Update a user by id

**Request body:**

**Authentication:** Required. Token must match a valid user and the user must be the object's owner or have relevant permissions.

```json
{
  "password": "YVJW@9#&npZ%"
}
```

**Successful response:**

- Status code: 200
- Content:

```json
{
  "id": 1,
  "name": "Admin_id_1",
  "email": "admin@admin.com",
  "user_role": {
    "role_name": "admin"
  },
  "created_tickets": [],
  "assigned_tickets": [
    {
      "id": 1,
      "title": "Issue 1",
      "description": "This is issue 1",
      "priority": "High",
      "status": "Open",
      "created_at": "2023-08-05T13:17:34.791383",
      "updated_at": null,
      "created_by_user": {
        "id": 2,
        "name": "Tech Zach_id_2",
        "email": "tech_Zach@email.com",
        "user_role": {
          "role_name": "tech"
        }
      }
    },
    {
      "id": 6,
      "title": "Issue 6",
      "description": "This is issue 6",
      "priority": "Medium",
      "status": "Closed",
      "created_at": "2023-08-05T13:17:34.794566",
      "updated_at": null,
      "created_by_user": {
        "id": 5,
        "name": "User Caleb_id_5",
        "email": "CALEB@email.com",
        "user_role": {
          "role_name": "user"
        }
      }
    }
  ],
  "created_comments": [
    {
      "id": 1,
      "content": "This is a comment on issue 1 by the user Admin1",
      "user_id": 1,
      "ticket_id": 1,
      "created_at": "2023-08-05T13:17:34.794573",
      "ticket": {
        "title": "Issue 1",
        "description": "This is issue 1"
      }
    },
    {
      "id": 6,
      "content": "This is a comment on issue 6 by the user Admin1",
      "user_id": 1,
      "ticket_id": 6,
      "created_at": "2023-08-05T13:17:34.794609",
      "ticket": {
        "title": "Issue 6",
        "description": "This is issue 6"
      }
    }
  ]
}
```

**Failed response:**

- Status code: 400
- Content:

```json
{
  "error": "Role \"minister for propaganda\" not found"
}
```

---

#### PUT /users/{id}

http://127.0.0.1:5000/users/4

Update a specific user's details.

**Authentication:** Required. Token must match a valid user and the user must be the object's owner or have relevant permissions.

**Request body:**

```json
{
  "name": "was caleb now bazza",
  "email": "bazza@example.com",
  "password": "new_password",
  "role": "user"
}
```

**Successful response:**

- Status code: 200
- Content:

```json
{
  {
    "id": 4,
    "name": "was caleb now bazza",
    "email": "bazza@example.com",
    "user_role": {
        "role_name": "user"
    },
    "created_tickets": [
        {
            "id": 4,
            "title": "Issue 4",
            "description": "This is issue 4",
            "priority": "High",
            "status": "Closed",
            "created_at": "2023-08-05T13:17:34.794240",
            "updated_at": null,
            "assigned_to_user": {
                "id": 5,
                "name": "User Caleb_id_5",
                "email": "CALEB@email.com",
                "user_role": {
                    "role_name": "user"
                }
            }
        }
    ],
    "assigned_tickets": [],
    "created_comments": [
        {
            "id": 4,
            "content": "This is a comment on issue 4 by the user Caleb4",
            "user_id": 4,
            "ticket_id": 4,
            "created_at": "2023-08-05T13:17:34.794598",
            "ticket": {
                "title": "Issue 4",
                "description": "This is issue 4"
            }
        }
    ]
}
}
```

**Failed response:**

- Status code: 404
- Content:

```json
{
  "message": "User not found!"
}
```

---

#### DELETE /users/{id}

http://127.0.0.1:5000/users/3

Delete a specific user.

**Authentication:** Required. Token must match a valid user and the user must be the object's owner or have relevant permissions.

**Successful response:**

- Status code: 200
- Content:

```json
{
  "message": "User successfully deleted"
}
```

**Failed response:**

- Status code: 404
- Content:

```json
{
  "error": "User not found with id 117"
}
```

---

### Tickets

#### GET: list all tickets

http://127.0.0.1:5000/tickets

**Authentication:** Required. Token must match a valid user.

**Request body:**

```json
 none
```

**Successful response:**

- Status code: 200
- Content:

```json
[
  {
    "id": 1,
    "title": "Issue 1",
    "description": "This is issue 1",
    "priority": "High",
    "status": "Open",
    "created_at": "2023-08-05T13:17:34.791383",
    "updated_at": null,
    "created_by_user": {
      "id": 2,
      "name": "Tech Zach_id_2",
      "email": "tech_Zach@email.com",
      "user_role": {
        "role_name": "tech"
      }
    },
    "assigned_to_user": {
      "id": 1,
      "name": "Admin_id_1",
      "email": "admin@admin.com",
      "user_role": {
        "role_name": "admin"
      }
    },
    "comments": [
      {
        "id": 1,
        "content": "This is a comment on issue 1 by the user Admin1",
        "user": {
          "name": "Admin_id_1",
          "email": "admin@admin.com"
        },
        "user_id": 1,
        "created_at": "2023-08-05T13:17:34.794573"
      }
    ]
  },
  {
    "id": 2,
    "title": "Issue 2",
    "description": "This is issue 2",
    "priority": "Low",
    "status": "Closed",
    "created_at": "2023-08-05T13:17:34.793139",
    "updated_at": null,
    "created_by_user": {
      "id": 2,
      "name": "Tech Zach_id_2",
      "email": "tech_Zach@email.com",
      "user_role": {
        "role_name": "tech"
      }
    },
    "assigned_to_user": {
      "id": 5,
      "name": "User Caleb_id_5",
      "email": "CALEB@email.com",
      "user_role": {
        "role_name": "user"
      }
    },
    "comments": [
      {
        "id": 2,
        "content": "This is a comment on issue 2 by the user Meg2",
        "user": {
          "name": "Tech Zach_id_2",
          "email": "tech_Zach@email.com"
        },
        "user_id": 2,
        "created_at": "2023-08-05T13:17:34.794588"
      }
    ]
  }
]
```

**Failed response:**

- Status code: 400
- Content:

```json
{
  "error": "404 Not Found: The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again."
}
```

#### GET /tickets/{id}

http://127.0.0.1:5000/tickets/1

Get a specific ticket.

**Authentication:** Required. Token must match a valid user.

**Successful response:**

- Status code: 200
- Content:

```json
{
  "id": 1,
  "title": "Issue 1",
  "description": "This is issue 1",
  "priority": "High",
  "status": "Open",
  "created_at": "2023-08-06T17:14:06.292240",
  "updated_at": null,
  "created_by_user": {
    "id": 2,
    "name": "Tech Zach_id_2",
    "email": "tech_Zach@email.com",
    "user_role": {
      "role_name": "tech"
    }
  },
  "assigned_to_user": {
    "id": 1,
    "name": "Admin_id_1",
    "email": "admin@admin.com",
    "user_role": {
      "role_name": "admin"
    }
  },
  "comments": [
    {
      "id": 1,
      "content": "This is a comment on issue 1 by the user Admin1",
      "user": {
        "name": "Admin_id_1",
        "email": "admin@admin.com"
      },
      "user_id": 1,
      "created_at": "2023-08-06T17:14:06.295953"
    }
  ]
}
```

**Failed response:**

- Status code: 404
- Content:

```json
{
  "message": "message": "ticket with id: 7 not found"
}
```

---

#### POST /tickets/{id}

http://127.0.0.1:5000/tickets

Create a new ticket

**Request body:**

**Authentication:** Required. Token must match a valid user.

```json
{
  "title": "New Ticket",
  "description": "This is a description of the new ticket.",
  "priority": "High",
  "status": "Open"
}
```

**Successful response:**

- Status code: 201
- Content:

```json
{ {
    "id": 8,
    "title": "New Ticket",
    "description": "This is a description of the new ticket.",
    "priority": "high",
    "status": "open",
    "created_at": "2023-08-05T14:56:27.212755",
    "updated_at": null,
    "created_by_user": {
        "id": 1,
        "name": "Admin_id_1",
        "email": "admin@admin.com",
        "user_role": {
            "role_name": "admin"
        }
    },
    "assigned_to_user": null,
    "comments": []
}

}
```

**Failed response:**

- Status code: 400
- Content:

```json
{
  "message": "Validation Error",
  "errors": {
    "priority": [
      "Priority must be one of the following : low, medium, high, emergency"
    ]
  }
}
```

---

#### PATCH /tickets/{id}

http://127.0.0.1:5000/tickets/4

update specific ticket

**Request body:**

**Authentication:** Required. Token must match a valid user and the user must be the object's owner or have relevant permissions.

```json
{
  "title": "Updated Ticket Title",
  "status": "In Progress"
}
```

**Successful response:**

- Status code: 200
- Content:

```json
{ {
    "id": 4,
    "title": "Updated Ticket Title",
    "description": "This is issue 4",
    "priority": "High",
    "status": "in progress",
    "created_at": "2023-08-05T13:17:34.794240",
    "updated_at": "2023-08-05T14:56:44.263098",
    "created_by_user": {
        "id": 4,
        "name": "bazza",
        "email": "bazza@example.com",
        "user_role": {
            "role_name": "user"
        }
    },
    "assigned_to_user": {
        "id": 5,
        "name": "Caleb",
        "email": "CALEB@email.com",
        "user_role": {
            "role_name": "tech"
        }
    },
    "comments": [
        {
            "id": 4,
            "content": "This is a comment on issue 4 by the user Caleb",
            "user": {
                "name": "Caleb",
                "email": "CALEB@email.com"
            },
            "user_id": 5,
            "created_at": "2023-08-05T13:17:34.794598"
        }
    ]
}
}
```

**Failed response:**

- Status code: 404
- Content:

```json
{
  "message": "Validation Error",
  "errors": {
    "title": ["Title cannot be empty"]
  }
}
```

---

#### PUT /tickets/{id}

http://127.0.0.1:5000/tickets/4

Update a specific ticket.

**Authentication:** Required. Token must match a valid user and the user must be the object's owner or have relevant permissions.

**Request body:**

```json
{
  "title": "Updated Ticket Title",
  "status": "In Progress"
}
```

**Successful response:**

- Status code: 200
- Content:

```json
{
  {
    "id": 4,
    "title": "Updated Ticket Title",
    "description": "This is issue 4",
    "priority": "High",
    "status": "in progress",
    "created_at": "2023-08-05T13:17:34.794240",
    "updated_at": "2023-08-05T14:56:44.263098",
    "created_by_user": {
        "id": 4,
        "name": "was caleb now bazza",
        "email": "bazza@example.com",
        "user_role": {
            "role_name": "user"
        }
    },
    "assigned_to_user": {
        "id": 5,
        "name": "User Caleb_id_5",
        "email": "CALEB@email.com",
        "user_role": {
            "role_name": "user"
        }
    },
    "comments": [
        {
            "id": 4,
            "content": "This is a comment on issue 4 by the user Caleb4",
            "user": {
                "name": "was caleb now bazza",
                "email": "bazza@example.com"
            },
            "user_id": 4,
            "created_at": "2023-08-05T13:17:34.794598"
        }
    ]
}
}
```

**Failed response:**

- Status code: 404
- Content:

```json
{
  "error": "Ticket not found with id 32"
}
```

---

#### DELETE /tickets/{id}

http://127.0.0.1:5000/tickets/5

Delete a specific ticket.

**Authentication:** Required. Token must match a valid user and the user must be the object's owner or have relevant permissions.

**Successful response:**

- Status code: 200
- Content:

```json
{
  "message": "Ticket deleted"
}
```

**Failed response:**

- Status code: 404
- Content:

```json
{
  "message": "Ticket not found"
}
```

---

### Comments

#### GET /comments

http://127.0.0.1:5000/comments

Gets a list of all comments on all tickets

**Authentication:** Required. Token must match a valid user.

**Request body:**

```json
 none
```

**Successful response:**

- Status code: 200
- Content:

```json
{  "id": 1,
        "content": "This is a comment on issue 1 by the user Admin1",
        "user": {
            "name": "Admin_id_1",
            "email": "admin@admin.com"
        },
        "user_id": 1,
        "ticket_id": 1,
        "created_at": "2023-08-05T13:17:34.794573",
        "ticket": {
            "title": "Issue 1",
            "description": "This is issue 1"
        }
    },
    {
        "id": 2,
        "content": "This is a comment on issue 2 by the user Meg2",
        "user": {
            "name": "Tech Zach_id_2",
            "email": "tech_Zach@email.com"
        },
        "user_id": 2,
        "ticket_id": 2,
        "created_at": "2023-08-05T13:17:34.794588",
        "ticket": {
            "title": "Issue 2",
            "description": "This is issue 2"
        }
    },
    {
        "id": 4,
        "content": "This is a comment on issue 4 by the user Caleb4",
        "user": {
            "name": "was caleb now bazza",
            "email": "bazza@example.com"
        },
        "user_id": 4,
        "ticket_id": 4,
        "created_at": "2023-08-05T13:17:34.794598",
        "ticket": {
            "title": "Updated Ticket Title",
            "description": "This is issue 4"
        }

}
```

**Failed response:**

- Status code: 404
- Content:

```json
{
  "message": "Route not found on this app"
}
```

---

#### GET /comments/{id}

http://127.0.0.1:5000/comments/1

Get a specific comment.

**Authentication:** Required. Token must match a valid user.

**Successful response:**

- Status code: 200
- Content:

```json
{
  "id": 1,
  "content": "This is a comment on issue 1 by the user Admin1",
  "user": {
    "name": "Admin_id_1",
    "email": "admin@admin.com"
  },
  "user_id": 1,
  "ticket_id": 1,
  "created_at": "2023-08-06T17:14:06.295953",
  "ticket": {
    "title": "Issue 1",
    "description": "This is issue 1"
  }
}
```

**Failed response:**

- Status code: 404
- Content:

```json
{
  "error": "Comment not found with id 69"
}
```

---

#### POST /comments/{id}

http://127.0.0.1:5000/comments

Create a new comment on a ticket.

**Authentication:** Required. Token must match a valid user.

**Request body:**

```json
{
  "ticket_id": 7,
  "content": "This is a new comment on ticket 7."
}
```

**Successful response:**

- Status code: 201
- Content:

```json
{
  {
    "id": 9,
    "content": "This is a new comment on ticket 7.",
    "user": {
        "name": "Admin_id_1",
        "email": "admin@admin.com"
    },
    "user_id": 1,
    "ticket_id": 7,
    "created_at": "2023-08-05T14:57:07.039020",
    "ticket": {
        "title": "Updated Ticket Title",
        "description": "This is issue 4"
    }
 }
}

```

**Failed response:**

- Status code: 400
- Content:

```json
{
  "message": "IntegrityError make sure you include a VALID ticket id that EXISTS and content",
  "errors": "insert or update on table \"comment\" violates foreign key constraint \"comment_ticket_id_fkey\"\nDETAIL:  Key (ticket_id)=(4) is not present in table \"tickets\".\n"
}
```

---

#### PATCH /comments/{id}

http://127.0.0.1:5000/comments/1

patch update comment

**Authentication:** Required. Token must match a valid user and the user must be the object's owner or have relevant permissions.

**Request body:**

```json
{
  "content": "Updated comment made by admin1 on ticket 1."
}
```

**Successful response:**

- Status code: 200
- Content:

```json
{
  "id": 1,
  "content": "Updated comment made by admin1 on ticket 1.",
  "user": {
    "name": "Admin_id_1",
    "email": "admin@admin.com"
  },
  "user_id": 1,
  "ticket_id": 1,
  "created_at": "2023-08-06T17:14:06.295953",
  "ticket": {
    "title": "Issue 1",
    "description": "This is issue 1"
  }
}
```

**Failed response:**

- Status code: 400
- Content:

```json
{
  "error": "Comment not found with id 42"
}
```

---

#### PUT /comments/{id}

http://127.0.0.1:5000/comments/1

Update a specific comment.

**Authentication:** Required. Token must match a valid user and the user must be the object's owner or have relevant permissions.

**Request body:**

```json
{
  "content": "Updated comment made by admin1 on ticket 1."
}
```

**Successful response:**

- Status code: 200
- Content:

```json
{
  "id": 1,
  "content": "Updated comment made by admin1 on ticket 1.",
  "user": {
    "name": "Admin_id_1",
    "email": "admin@admin.com"
  },
  "user_id": 1,
  "ticket_id": 1,
  "created_at": "2023-08-05T13:17:34.794573",
  "ticket": {
    "title": "Issue 1",
    "description": "This is issue 1"
  }
}
```

**Failed response:**

- Status code: 404
- Content:

```json
{
  "message": "IntegrityError make sure you include a VALID ticket id that EXISTS and content",
  "errors": "insert or update on table \"comment\" violates foreign key constraint \"comment_ticket_id_fkey\"\nDETAIL:  Key (ticket_id)=(4) is not present in table \"tickets\".\n"
}
```

---

#### DELETE /comments/{id}

http://127.0.0.1:5000/comments/6

Delete a specific comment.

**Authentication:** Required. Token must match a valid user and the user must be the object's owner or have relevant permissions.

**Successful response:**

- Status code: 200
- Content:

```json
{
  "message": "Comment deleted"
}
```

**Failed response:**

- Status code: 404
- Content:

```json
{
  "error": "Comment not found with id 256"
}
```

---


## 6 Entity-Relationship Diagram 


The following ERD was written in DBML and displayed using dbdiagram.io, and the DBML is provided below, as well as an explanation of how it relates to the models and associations in answers 8 and 9.

![image-20230805174215335](/docs/ERD.png)


### ERD: DBML

```dbml
Table comment {
  id integer [pk, increment]
  content text [not null]
  created_at timestamp [not null]
  user_id integer [not null]
  ticket_id integer [not null]
}

Table role {
  id integer [pk, increment]
  role_name varchar [not null]
  can_view_all boolean [not null]
  can_delete_all boolean [not null]
  can_edit_all boolean [not null]
  can_manage_users boolean [not null]
  can_manage_tickets boolean [not null]
  can_assign_tickets boolean [not null]
}

Table tickets {
  id integer [pk, increment]
  title varchar [not null]
  description text [not null]
  created_at timestamp [not null]
  updated_at timestamp
  priority varchar
  status varchar
  created_by_id integer [not null]
  assigned_to_id integer
}

Table users {
  id integer [pk, increment]
  name varchar
  email varchar [not null, unique]
  password_hash varchar
  role_id integer [not null]
}

Ref: comment.user_id > users.id
Ref: comment.ticket_id > tickets.id
Ref: tickets.created_by_id > users.id
Ref: tickets.assigned_to_id > users.id
Ref: users.role_id > role.id
```



## 7 Third-Party Services 

### Third-Party Services Used


1. **Flask**:
   - Flask operates as the core of the IT ticket system API. As a micro-framework, it is responsible for routing, processing, and responding to web requests. Flask manages API endpoints in this project such as ticket creation and user data retrieval.
   - Flask's lightweight and modular nature means it's fast and efficient. Its flexibility allows for easy integration with other libraries and tools. With Flask, developers can quickly prototype, making it ideal for iterative development and rapid deployment.

2. **Psycopg2**:
   - Psycopg2 forms the conduit between the Flask application and the PostgreSQL database. In the IT ticket system, it ensures SQLAlchemy's interactions with the Postgres database are smooth, handling database operations seamlessly.
   - Psycopg2 supports multiple PostgreSQL-specific features, ensuring the fullest utilisation of the database's capabilities. It provides efficient and secure communication, supports transactions, and handles concurrent database sessions effectively.

3. **Postgres**:
   - PostgreSQL stands as the reliable data repository for the IT ticket system. It's where all the data—from ticket information to user profiles—is stored and managed.
   - Postgres offers advanced data integrity and reliability. Its support for both relational and non-relational data models ensures flexibility. Additionally, it provides robustness with features like transactional integrity and concurrency control.

4. **SQLAlchemy**:
   - SQLAlchemy is the translator, converting Python code into database-friendly SQL queries. The IT ticket system defines and manages data models and relationships.
   - Beyond mere translation, SQLAlchemy provides an Object-Relational Mapping (ORM) layer, allowing developers to work with high-level objects instead of raw SQL queries. This abstraction promotes cleaner code, reduces the risk of SQL injection attacks, and enhances portability across different database systems.

5. **Marshmallow**:
   - Marshmallow acts as the system's data gatekeeper, ensuring incoming and outgoing data adheres to set structures and formats. It validates, serialises, and deserialises data for the IT ticket system.
   - Marshmallow safeguards the system against malformed or malicious input by validating data. Its serialisation capabilities ensure data consistency and integrity, fostering reliable communication between the server and clients.

6. **Bcrypt**:
   - Bcrypt is the guardian of user password confidentiality. Before any user password reaches the Postgres database, Bcrypt hashes it, and during authentication, it checks submitted passwords against stored hashes.
   - Bcrypt's adaptive nature means it remains secure even as hardware improves. It's resistant to rainbow table attacks due to its salting mechanism. Its deliberate computational intensity ensures brute-force attacks are time-consuming and impractical.

7. **JSON Web Tokens (JWT)**:
   - JWT operates as the system's Ticketmaster, granting authenticated users tokens as proof of identity. Every interaction post-authentication requires the user's token, which the Flask API verifies.
   - JWT allows for stateless authentication, reducing the need for repeated database queries. The tokens can embed user roles and permissions, enabling fine-grained access control. They are also compact, ensuring efficient data transfer.


## 8 Model Relationships 

###  SQLalcemy Models and Their Relationships


This section will explore the key models utilised in the IT ticket system API and their associations, which provide the foundation for organising and managing data. Additionally, we will discuss the check_permissions_wrap function, acting as a wrapper on API endpoints, to retrieve and pass user permissions for effective access control. Understanding these models and their associations will highlight how the API maintains data integrity and enforces permission checks, contributing to a seamless and secure ticketing system experience.

#### Users Model:

```python
class User(db.Model):
   __tablename__ = 'users'
   id            = db.Column(db.Integer, primary_key=True, autoincrement=True)
   name          = db.Column(db.String)
   email         = db.Column(db.String, nullable=False, unique=True )
   password_hash = db.Column(db.String)
   # foreign keys
   role_id       = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)

   # relationship
   created_tickets  = db.relationship("Ticket",
                                    foreign_keys   = 'Ticket.created_by_id',
                                    back_populates = "created_by_user",
                                    cascade        = 'all, delete')
   assigned_tickets = db.relationship("Ticket",
                                    foreign_keys   = 'Ticket.assigned_to_id',
                                    back_populates = "assigned_to_user",
                                    cascade        = 'all, delete')
   created_comments = db.relationship('Comment', 
                                       back_populates = 'user',
                                       cascade        = 'all, delete')
   ```
 
The Users model represents individuals using the IT ticket system. It contains fields such as `id`, `name`, `email`, and `password_hash` to store user information. One of the key features of the Users model is its association with the Role model through the `role_id` field. This association establishes a relationship between users and their respective roles, determining their permissions within the system. The API can effectively enforce access controls and restrict users to authorised actions by linking each user to a specific role.

#### Role Model:
 
```python
   class Role(db.Model): 
   __tablename__ = 'role'
   id            = db.Column(db.Integer, primary_key=True, autoincrement=True)
   role_name     = db.Column(db.String, nullable=False)
   # permissions
   can_view_all       = db.Column(db.Boolean, nullable=False)
   can_delete_all     = db.Column(db.Boolean, nullable=False)
   can_edit_all       = db.Column(db.Boolean, nullable=False)
   can_manage_users   = db.Column(db.Boolean, nullable=False)
   can_manage_tickets = db.Column(db.Boolean, nullable=False)
   can_assign_tickets = db.Column(db.Boolean, nullable=False)

   # relationship
   users = db.relationship("User", backref="user_role")
```

Role Model and Permissions Wrapper:
The Role model defines various user permissions within the system. It contains fields such as `id, role_name, can_view_all, can_edit_all, can_manage_users, can_manage_tickets, and can_assign_tickets` to specify a user's operations. The Role model is associated with the Users model through the role_id field, establishing a relationship between users and their respective roles.

To leverage these permissions effectively, the API utilises the check_permissions_wrap function as a decorator on endpoints. This function acts as a wrapper and checks a user's permissions before executing the endpoint's main logic.

The `check_permissions_wrap` decorator extracts the user's identity from the JSON Web Token (JWT) and retrieves the associated role from the database. This role includes all the permissions relevant to the user.

Bypassing the user_role containing the permissions as a keyword argument `(kwargs['user_role'])` to the wrapped function, the business logic can effortlessly access and utilise the user's permissions. This enables the API to enforce access controls effectively and restrict users to actions they are authorised for.



#### Tickets Model:

```python
class Ticket(db.Model):
   __tablename__ = 'tickets'
   id          = db.Column(db.Integer, primary_key=True, autoincrement=True)
   title       = db.Column(db.String, nullable=False)
   description = db.Column(db.Text, nullable=False)
   created_at  = db.Column(db.DateTime, nullable=False)
   updated_at  = db.Column(db.DateTime)
   priority    = db.Column(db.String)
   status      = db.Column(db.String)
   # foreign keys
   created_by_id  = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
   assigned_to_id = db.Column(db.Integer, db.ForeignKey('users.id'))

   # relationship
   created_by_user = db.relationship('User',
                                    foreign_keys   = 'Ticket.created_by_id',
                                    back_populates = 'created_tickets')
   assigned_to_user= db.relationship("User", 
                                    foreign_keys   = 'Ticket.assigned_to_id',
                                    back_populates = "assigned_tickets")
   comments        = db.relationship("Comment", 
                                    back_populates = "ticket",
                                    cascade        = 'all, delete')
```
 
The Tickets model represents IT-related issues or tasks within the system. It contains fields like `id`, `title`, `description`, `priority`, `status`, `created_at`, and `updated_at` to capture ticket-related information. Notably, the Tickets model has two foreign key fields: `created_by_id` and `assigned_to_id`, which are associated with the Users model. The `created_by_id` field links each ticket to the user who created it, while the `assigned_to_id` field associates a ticket with the user to whom it is potentially assigned.

The associations between the Tickets and Users models enable a direct relationship between tickets and the users who interact with them. This linkage ensures that each ticket has a creator and, if assigned, an assignee, making tracking and managing ticket ownership and status easier.

#### Comment Model:

```python
class Comment(db.Model):
   __tablename__ = 'comment'
   id         = db.Column(db.Integer, primary_key=True, autoincrement=True)
   content    = db.Column(db.Text, nullable=False)
   created_at = db.Column(db.DateTime, nullable=False)
   # foreign keys
   user_id   = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
   ticket_id = db.Column(db.Integer, db.ForeignKey('tickets.id'), nullable=False)

   # relationship
   ticket = db.relationship("Ticket", 
                           back_populates="comments")
   user   = db.relationship('User', 
                           back_populates='created_comments')
    
```
 
The Comment model represents additional information or updates users provide about specific tickets. It contains fields like `id`, `content`, and `created_at` to store the comment's details. Importantly, the Comment model is associated with the Users model (via `user_id`) and the Tickets model (via `ticket_id`). These foreign key fields enable a many-to-one relationship, allowing multiple comments to be associated with individual users and tickets.

The associations between the Comment, Users, and Tickets models facilitate ongoing communication and updates related to each ticket. When users submit comments, the system can identify which ticket the comment is referencing and which user made the comment. This seamless connection enables efficient tracking of ticket updates and user interactions.

#### Summary:

In summary, the SQLAlchemy models and their associations are pivotal in structuring the database and enabling seamless data management within the IT ticket system API. The models and their relationships provide a clear roadmap for implementing functionalities, fetching related data, and enforcing access controls, ensuring an efficient and secure ticketing system for users.

## 9 Database Relations 

### Database Relations in the Application


1. **Users Model**:
   - **Purpose**: This model is pivotal, representing individual users or stakeholders in the ticketing system. In any ticket system, understanding user entities and their attributes is essential.
   - **Attributes**: Each user has an ID, name, email, encrypted password, and role ID.
   - **Relationship**: The user model has an integral connection to the `Role` model via the `role_id`. This association allows the system to determine the capabilities and permissions of each user. 
   
2. **Tickets Model**:
   - **Purpose**: The ticket itself is at the heart of any ticket system. It is a record of an IT-related issue or task that requires attention.
   - **Attributes**: Tickets have an ID, title, description, creation timestamp, update timestamp, priority, status, creator's ID (`created_by_id`), and assignee's ID (`assigned_to_id`).
   - **Relationship**: Tickets have two key foreign references tied to the `Users` model. The `created_by_id` denotes who logged the ticket, and the `assigned_to_id` designates who resolves it. This dual reference reinforces the inherent relationship between tickets and the users they concern, both from a creation and resolution standpoint.

3. **Comment Model**:
   - **Purpose**: Comments provide updates, feedback, or additional information on a specific ticket. They enable chronological tracking of actions, decisions, or updates related to a ticket.
   - **Attributes**: Comments consist of an ID, content, timestamp, user ID (`user_id`), and ticket ID (`ticket_id`).
   - **Relationship**: The Comment model is intricately linked to `Users` and `Tickets`. The `user_id` denotes which user has left the comment, allowing for accountability and transparency. Meanwhile, `ticket_id` ties the comment to a specific ticket, ensuring every feedback or update can be traced back to the ticket it pertains to.

4. **Role Model**:
   - **Purpose**: This model encapsulates user permissions, a critical aspect in systems that require differentiated access levels.
   - **Attributes**: Each role has an ID and a set of permission flags (e.g., `can_view_all`, `can_delete_all`, etc.).
   - **Relationship**: The role does not directly relate to other models via foreign keys but is indirectly tied to `Users` through the `role_id` in the `Users` model. This connection implies that each user has a defined role in determining their operational permissions within the system.

**Reflecting on the ERD**:

This system's Entity Relationship Diagram (ERD) will showcase four main entities (or tables): Users, Tickets, Comments, and Roles. The interrelations between them will be denoted by lines connecting these entities, indicating foreign key references.

- **Users & Comments**: A one-to-many line will connect `Users` to `Comments`, signifying that a single user can make multiple comments.
- **Tickets & Comments**: Another one-to-many relationship from `Tickets` to `Comments`, suggesting multiple comments can be related to one ticket.
- **Users & Tickets (Creation)**: A one-to-many line from `Users` to `Tickets` representing the `created_by_id` relationship.
- **Users & Tickets (Assignment)**: Another one-to-many line from `Users` to `Tickets`, this time for the `assigned_to_id`.
- **Users & Roles**: A many-to-one connection from `Users` to `Roles`, indicating that multiple users can share the same role, but each user has only one role.

The ERD thus serves as a visual guide, reflecting the structure, relationships, and data flow within the ticket system's database. This visual representation can assist developers, stakeholders, and other team members understand how data is organised, related, and accessed, informing API development, feature planning, and system enhancements.

## 10 Task Allocation and Tracking 


### Notion's Kanban And Gnatt Chart


I utilised Notion's Kanban board, and Gantt chart features for task management in my project. The choice of Notion was influenced by its similarity to Trello, coupled with my familiarity with its interface. Notion’s board system stands out due to its simplicity, flexibility, and capacity for extension. This makes it a favoured choice among both individual developers and larger teams.

You can view and browse through the Notion board [here](https://fan-enquiry-91b.notion.site/2524eb517f0b484d9dec4d7d841ce72e?v=da8ae1d1f28c43f3b62d1f3abfcdfee5&pvs=4).

The initial integration of a Kanban board was beneficial for its capacity to outline individual tasks and establish parent/subtask hierarchies. Each task or subtask could be attributed to its unique status, with the added provision to append notes where necessary. Below is an illustration of the primary draft of the Kanban board, demonstrating the tracking mechanics:

![Initial Kanban Board View](/docs/Screenshot%202023-08-02%20121021.png)

As the project evolved, the board underwent refinements to accommodate sub-statuses. These were integrated to facilitate a more nuanced tracking of task progression, especially for detailed subtask evaluations:

![Extended Board - Detailed View 1](/docs/Screenshot%202023-08-03%20141115.png)
![Extended Board - Detailed View 2](/docs/Screenshot%202023-08-03%20184410.png)

With most project components in place, the board's architecture was further refined to emulate a Gantt chart. Achieved merely by incorporating a new viewing mode in Notion, this transformation ensured a broad project overview, minimising the likelihood of over-planning at the expense of actual task execution. The Gantt chart was instrumental in prioritising tasks. Through the use of blocking arrows, it highlighted the sequencing of tasks, guiding my efforts efficiently:

![Gantt Chart Overview 1](/docs/Screenshot%202023-08-03%20185405.png)
![Gantt Chart Overview 2](/docs/Screenshot%202023-08-04%20160458.png)
![Gantt Chart Overview 3](/docs/Screenshot%202023-08-04%201900171.png)
![Gantt Chart Overview 4](/docs/Screenshot%202023-08-06%20120023.png)

In summary, the dynamic adaptability of Notion, transitioning from a Kanban board to a Gantt chart, proved instrumental in tracking, prioritising, and executing tasks throughout the project's lifecycle.