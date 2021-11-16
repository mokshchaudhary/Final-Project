const { JsonStorage, config } = require("json-storage-fs");
const express = require("express");
const app = express();
const port = process.env.PORT || 8080;
app.use(express.json());
app.get("/", (req, res) => {
    console.log(req.query['filename']);
    res.send(findrecord(req.query['filename']));
});

app.get("/verify", (req, res) => {
    // console.log(req.query['filename'] + " " + req.query['signature']);
    console.log('Verification Report Received');
    verifysignature(req.query['filename'], req.query['signature']).then((value) => {
        res.send(value);
    })
});


app.post("/", function (req, res) {
    res.send(req.body);
    saverecord(req.body[0], req.body[1]);
});

app.listen(port, () => { });

// Save Records ===================================
function saverecord(filename, signature) {
    console.log("Filename : \t" + filename);
    console.log("Signature : \t" + signature);
    JsonStorage.set(filename, signature);
    console.log(JsonStorage.get(filename));
}

// Find Records ====================================
function findrecord(filename) {
    return JsonStorage.get(filename);
}

// Verify Signature ================================
async function verifysignature(filename, signature) {
    await sleep(getRandomInt(2) * 1000);
    var storedsignature = JsonStorage.get(filename);
    if (storedsignature == signature) {
        return 'True'
    } else {
        return 'False'
    }
}


// Experimenal =====================================

function sleep(ms) {
    return new Promise((resolve) => {
        setTimeout(resolve, ms);
    });
}

function getRandomInt(max) {
    return Math.floor(Math.random() * max);
}