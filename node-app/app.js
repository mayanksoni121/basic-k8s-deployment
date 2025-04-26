require('dotenv').config();

const express = require('express')
const app = express()
const port = 3000
const message1 = process.env.MESSAGE1 || "";
const message2 = process.env.MESSAGE2 || "";
const username = process.env.USERNAME || "";
const password = process.env.PASSWORD || "";

app.get('/', (req, res) => {
  res.send(`<h1>Hello Developers! </h1>`)
})

app.get('/message1', (req, res) => {
  res.send(`<h1>Hello Developers! ${message1}</h1>`)
})

app.get('/message2', (req, res) => {
  res.send(`<h1>Hello Developers! ${message2}</h1>`)
})

app.get('/secrets', (req, res) => {
  res.send(`
    <h1>Username: ${username} </h1>
    <h1>Password: ${password} </h1>
    `)
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})