#!/usr/bin/node
// finding characters of a movie
const request = require('request');
const myUrl = 'https://swapi-api.alx-tools.com/api/films/';
const myInputs = process.argv[2];
function myRequster () {
  return new Promise((resolve, reject) => {
    request.get(myUrl + myInputs, async (err, req, res) => {
      if (err) {
        reject(err);
      }
      if (req.statusCode === 200) {
        const users = await JSON.parse(res).characters;
        resolve(characters(users, 0));
      }
    });
  });
}

function characters (info, j) {
  if (j < info.length) {
    request.get(info[j], async (err1, req1, res1) => {
      if (err1) console.log(err1);
      if (req1.statusCode === 200) {
        console.log(await JSON.parse(res1).name);
        characters(info, j + 1);
      }
    });
  }
}
myRequster();
