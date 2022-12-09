
const Head = {
  x: 0,
  y: 0,
};
const Tail = {
  x: 0,
  y: 0,
};
const Board = {
  Top: 0,
  Right: 0,
  Bottom: 0,
  Left: 0,
}
const TailVisited = {
  0: { 0: true }
};

const Cmd = {
  U: Up,
  D: Down,
  L: Left,
  R: Right,
};

function Up(Knot) {
  Knot.x += 1;
  if (Board.Top < Knot.x) Board.Top += 1
}

function Down(Knot) {
  Knot.x -= 1;
  if (Board.Bottom > Knot.x) Board.Bottom -= 1
}

function Left(Knot) {
  Knot.y -= 1;
  if (Board.Left > Knot.y) Board.Left -= 1
}

function Right(Knot) {
  Knot.y += 1;
  if (Board.Right < Knot.y) Board.Right += 1
}

function MoveTail() {
  if (Tail.y - Head.y < -1) {
    Right(Tail);
    if (Tail.x !== Head.x) Tail.x = Head.x;
  }
  if (Tail.x - Head.x < -1) {
    Up(Tail);
    if (Tail.y !== Head.y) Tail.y = Head.y;
  }
  if (Tail.y - Head.y > 1) {
    Left(Tail);
    if (Tail.x !== Head.x) Tail.x = Head.x;
  }
  if (Tail.x - Head.x > 1) {
    Down(Tail);
    if (Tail.y !== Head.y) Tail.y = Head.y;
  }

  if (!TailVisited[Tail.x]) {
    TailVisited[Tail.x] = {};
  }
  TailVisited[Tail.x][Tail.y] = true;
}

function printBoard() {
  for (let x = Board.Top; x >= Board.Bottom; x--) {
    let line = '';
    for (let y = Board.Left; y <= Board.Right; y++) {
      if (x == Head.x && y == Head.y) {
        line += 'H';
      } else if (x == Tail.x && y == Tail.y) {
        line += 'T';
      } else if (TailVisited[x] && TailVisited[x][y]) {
        line += '#';
      } else {
        line += '.';
      }
    }
    console.log(line);
  }
  console.log('============')
}


var lineReader = require('readline').createInterface({
  input: require('fs').createReadStream('input.txt')
});

lineReader.on('line', function (line) {
  const [direction, times] = line.split(' ');
  // console.log(direction, times);
  for (let i = 0; i < parseInt(times); i++) {
    Cmd[direction](Head)
    MoveTail()
    // printBoard()
  }
});

lineReader.on('close', function () {
  console.log(Object.values(TailVisited).reduce((acc, v) => acc + Object.values(v).length, 0));
});
