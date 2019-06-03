const client = require('./client')
client.list({}, (error, notes) => {
    if (!error) {
        console.log('successfully fetch List notes')
        console.log(notes)
    } else {
        console.log('Error al conectarse con el servidor')
        console.error(error)
    }
})