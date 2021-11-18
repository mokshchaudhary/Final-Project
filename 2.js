const express = require("express");
const app = express();
const port = process.env.PORT || 8080;

ServerList = ['http://localhost:3000', 'http://localhost:3001', 'http://localhost:3002', 'http://localhost:3003', 'http://localhost:3004']

app.get("/", (req, res) => {
    sleep(1000).then(() => {
        res.send(ServerList.toString());
    });
});

app.listen(port, () => { });


function sleep(ms) {
    return new Promise((resolve) => {
        setTimeout(resolve, ms);
    });
}
