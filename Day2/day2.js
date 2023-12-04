const fs = require("fs");
const path = require("path");
const readline = require("readline");

filePath = path.join(__dirname, "day2.txt");


let maxByColor = {"blue": 14, "green": 13, "red": 12}
let cumulativeTotal = 0
let cumulativeTotalPart2 = 0

fs.readFile(filePath, { encoding: "utf-8" }, function (err, data) {
  if (!err) {

    
    const lines = data.split("Game");

    for (let i = 0; i < lines.length; i++) {
      let line = lines[i];
      line = line.trim()

      // parse each game and get game ID, and max of red/green/blue
      let gameIsValid = true;
      let draws = line.split(":")[1];
      let gameId = line.split(":")[0]
      gameId = Number(gameId)

      let minGameCounts = {"red": 0, "green": 0, "blue": 0}
      if (draws != undefined) {
        draws = draws.split(";");
        for (let draw of draws) {
            draw.trim()

            let cubeDraws = draw.split(",")
            for (let cubeValue of cubeDraws) {
                cubeValue = cubeValue.trim()

                let drawData = cubeValue.split(" ")
                let color = drawData[1]
                let amount = Number(drawData[0])

                // part 1
                if (amount > maxByColor[color]) {
                    // console.log("amount" + amount +" color:" + color)
                    gameIsValid = false;
                } 

                // part 2
                if (amount > minGameCounts[color]) {
                    minGameCounts[color] = amount
                }
            }

        }
      }
      if (gameIsValid) {
        console.log("gameId" + gameId + " idx" + i)
        console.log(line)
        cumulativeTotal = cumulativeTotal + gameId
      }

      let power = minGameCounts["red"] * minGameCounts["green"] * minGameCounts["blue"]
      cumulativeTotalPart2 = cumulativeTotalPart2 + power
    }
    console.log(cumulativeTotal)
    console.log(cumulativeTotalPart2)

  }
});

