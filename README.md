# TestAppFAPI_GQL_STB
# Проект на Python для работы с GraphQL

Данный проект представляет собой сервис FastAPI для работы с GraphQL. Он использует базу данных SQL, которая работает с помощью SQLAlchemy, а методы GraphQL реализованы с помощью библиотеки strawberry-graphql. С помощью этого сервиса можно выполнять запросы и мутации к базе данных, используя язык GraphQL. Он может быть использован для различных приложений, которые требуют быстрого и удобного доступа к базе данных.

## Примеры запросов

### Создание пользователя
```
mutation ($username: String!, $email: String!, $passwordHash: String!) { 
  createUser(
    username: $username, 
    email: $email, 
    passwordHash: $passwordHash
  ) { 
    data { 
      id 
      username 
      email 
    } 
    error 
  } 
}

{
  "variables": {
    "username": "2testuser",
    "email": "2testuser@example.com",
    "passwordHash": "2TestPassword"
  }
}
```

### Удаление пользователя
\```
mutation ($id: String!) { 
  deleteUser(id: $id) { 
    msg 
    error 
  } 
}

{
  "variables": {
    "id": "123456"
  }
}
\```

### Обновление пользователя
\```
mutation ($id: String!, $username: String!, $email: String!, $passwordHash: String!) { 
  updateUser(
    id: $id, 
    username: $username, 
    email: $email, 
    passwordHash: $passwordHash
  ) { 
    data { 
      id 
      username 
      email 
    } 
    error 
  } 
}

{
  "variables": {
    "id": "123456",
    "username": "newusername",
    "email": "newemail@example.com",
    "passwordHash": "newpasswordhash"
  }
}
\```

### Получение списка пользователей
\```
query { 
  users { 
    id 
    username 
    email 
  } 
}
\```

### Получение пользователя по имени пользователя

\```
query GetUser($username: String!) { 
  user(username: $username) { 
    id 
    username 
    email 
  } 
}

{
  "variables": {
    "username": "1testuser"
  }
}
\```
