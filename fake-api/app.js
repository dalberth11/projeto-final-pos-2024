// Importando dependências
const express = require('express');
const faker = require('faker');

const app = express();
const port = 3000;

// Definindo a estrutura dos dados
let posts = [];
let users = [];
let comments = [];

// Gerando dados falsos para as entidades
for (let i = 1; i <= 10; i++) {
    posts.push({
        id: i,
        title: faker.lorem.sentence(),
        body: faker.lorem.paragraph(),
        userId: faker.random.number({ min: 1, max: 5 })
    });

    users.push({
        id: i,
        name: faker.name.findName(),
        email: faker.internet.email()
    });

    comments.push({
        id: i,
        postId: faker.random.number({ min: 1, max: 10 }),
        name: faker.name.findName(),
        email: faker.internet.email(),
        body: faker.lorem.sentence()
    });
}

// Middleware para habilitar o uso de JSON
app.use(express.json());

// Endpoints

// GET /posts
app.get('/posts', (req, res) => {
    res.json(posts);
});

// GET /posts/:id
app.get('/posts/:id', (req, res) => {
    const post = posts.find(p => p.id === parseInt(req.params.id));
    if (!post) {
        return res.status(404).json({ message: 'Post not found' });
    }
    res.json(post);
});

// POST /posts
app.post('/posts', (req, res) => {
    const { title, body, userId } = req.body;
    const newPost = {
        id: posts.length + 1,
        title,
        body,
        userId
    };
    posts.push(newPost);
    res.status(201).json(newPost);
});

// PUT /posts/:id
app.put('/posts/:id', (req, res) => {
    const { title, body, userId } = req.body;
    const postIndex = posts.findIndex(p => p.id === parseInt(req.params.id));
    if (postIndex === -1) {
        return res.status(404).json({ message: 'Post not found' });
    }

    posts[postIndex] = { id: parseInt(req.params.id), title, body, userId };
    res.json(posts[postIndex]);
});

// DELETE /posts/:id
app.delete('/posts/:id', (req, res) => {
    const postIndex = posts.findIndex(p => p.id === parseInt(req.params.id));
    if (postIndex === -1) {
        return res.status(404).json({ message: 'Post not found' });
    }

    posts.splice(postIndex, 1);
    res.status(204).send();
});

// GET /users
app.get('/users', (req, res) => {
    res.json(users);
});

// GET /users/:id
app.get('/users/:id', (req, res) => {
    const user = users.find(u => u.id === parseInt(req.params.id));
    if (!user) {
        return res.status(404).json({ message: 'User not found' });
    }
    res.json(user);
});

// GET /comments
app.get('/comments', (req, res) => {
    res.json(comments);
});

// GET /comments/:id
app.get('/comments/:id', (req, res) => {
    const comment = comments.find(c => c.id === parseInt(req.params.id));
    if (!comment) {
        return res.status(404).json({ message: 'Comment not found' });
    }
    res.json(comment);
});

// Iniciando o servidor
app.listen(port, () => {
    console.log(`Servidor rodando em http://localhost:${port}`);
});
