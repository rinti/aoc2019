const fs = require('fs')

const lines = fs.readFileSync('./input.txt', {encoding: 'utf8'}).split('\n')

let board = {}
let currPos = [0,0]
let intersections = []
let steps = 0;

const fill = (item, ident) => {
    const dir = item[0]
    const size = parseInt(item.slice(1), 10)

    for (let i=0; i <  size; i++) {
        if(dir === 'R') {
            currPos = [currPos[0]+1, currPos[1]]
        } else if (dir === 'U') {
            currPos = [currPos[0], currPos[1]+1]
        } else if (dir === 'D') {
            currPos = [currPos[0], currPos[1]-1]
        } else if (dir === 'L') {
            currPos = [currPos[0]-1, currPos[1]]
        }

        steps++;

        if(!board[currPos[0]]) {
            board[currPos[0]] = {}
        }

        if (!board[currPos[0]][currPos[1]]) {
            board[currPos[0]][currPos[1]] = {ident, steps}
        }

        if (board[currPos[0]][currPos[1]]["ident"] !== ident) {
            intersections.push([currPos[0],currPos[1], board[currPos[0]][currPos[1]]["steps"]+steps])
        }
    }
}


lines[0].split(',').map((i) => fill(i, 'A'))
currPos = [0,0]
steps = 0
lines[1].split(',').map((i) => fill(i, 'B'))

intersections = intersections.map(
    i => {
        return {"distance": Math.abs(0 - Math.abs(i[0]) + 0 - Math.abs(i[1])), "steps": i[2]}
    }
)

console.log("Part 1", intersections.sort((a, b) => a["distance"] - b["distance"])[0])
console.log("Part 2", intersections.sort((a, b) => a["steps"] - b["steps"])[0])
