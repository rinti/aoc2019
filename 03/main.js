const fs = require('fs')

const lines = fs.readFileSync('./input.txt', {encoding: 'utf8'}).split('\n')

let board = {}
let currPos = [0,0]
let intersections = []

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

        if(!board[currPos[0]]) {
            board[currPos[0]] = {}
        }

        if (!board[currPos[0]][currPos[1]]) {
            board[currPos[0]][currPos[1]] = ident
        }

        if (board[currPos[0]][currPos[1]] !== ident) {
            intersections.push([currPos[0],currPos[1]])
        }
    }
}


lines[0].split(',').map((i) => fill(i, 'A'))
currPos = [0,0]
lines[1].split(',').map((i) => fill(i, 'B'))

intersections = intersections.map(i => Math.abs(0 - Math.abs(i[0]) + 0 - Math.abs(i[1])))

console.log(intersections.sort((a, b) => a - b)[0])
