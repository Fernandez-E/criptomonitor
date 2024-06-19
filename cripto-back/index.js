const express = require('express')
const app = express()
const port = 3000

// ROTAS PARA STATIC
app.use(express.static('assets'))


// METODOS HTTP
app.get('/hello', (req, res) => {
    res.send("hello world")
})

app.post('/', function(req, res) {
    res.send('Post')
})

app.put('/user', function(req, res) {
    res.send('put')
})

app.delete('/user', function(req, res){
    res.send('delete')
})

app.listen(port, () => {
    console.log(`listening ${port}`)
})

