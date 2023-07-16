const express = require("express")
const app = express()

app.set('view engine', 'ejs');

app.get('/', async (req,res) => {
    res.render("index.ejs");
})


app.listen(
    3000, () =>
    console.log("Server is running", "url: http://localhost:3000")
)
