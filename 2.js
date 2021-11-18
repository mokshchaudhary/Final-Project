const express = require("express");
const app = express();
const port = process.env.PORT || 8080;

ServerList = ['http://52.66.27.131:8080', 'http://13.127.166.232:8080', 'http://13.234.10.227:8080', 'http://localhost:3003', 'http://localhost:3004']

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
