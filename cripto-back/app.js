const express = require('express')
const app = express()
const port = 3000

async function btcPrice(){
    try{
        const response = await fetch('https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT')
        const data = await response.json()
        console.log(data)
        return data.price
    } catch (error) {
        console.error('Error', error)
    }
}

app.get('/', async (req, res) => {
    try {
        const value = await btcPrice();
        res.send(value.toString());
    } catch (error) {
        res.status(500).send('Error fetching BTC price');
    }
})

app.listen(port, () => {
    console.log(`PORT: ${port}`)
})