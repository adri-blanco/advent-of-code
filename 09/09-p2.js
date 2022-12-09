const KnotsLength = 9;
const Head = {
  x: 0,
  y: 0,
};
const Knot = {
  x: 0,
  y: 0,
};
const Knots = [];
const Board = {
  Top: 0,
  Right: 0,
  Bottom: 0,
  Left: 0,
};
const TailVisited = {
  0: { 0: true }
};

const Cmd = {
  U: Up,
  D: Down,
  L: Left,
  R: Right,
}

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

function MoveTail(tail, head) {
  if (tail.y - head.y < -1) {
    Right(tail);
    // if (tail.x !== head.x) tail.x = head.x;
    if(tail.x - head.x < 0) Up(tail);
    if(tail.x - head.x > 0) Down(tail);
  }
  if (tail.x - head.x < -1) {
    Up(tail);

    if(tail.y - head.y < 0) Right(tail);
    if(tail.y - head.y > 0) Left(tail);
    // if (tail.y !== head.y) tail.y = head.y;
  }
  if (tail.y - head.y > 1) {
    Left(tail);

    if(tail.x - head.x < 0) Up(tail);
    if(tail.x - head.x > 0) Down(tail);
    // if (tail.x !== head.x) tail.x = head.x;
  }
  if (tail.x - head.x > 1) {
    Down(tail);

    if(tail.y - head.y < 0) Right(tail);
    if(tail.y - head.y > 0) Left(tail);
    // if (tail.y !== head.y) tail.y = head.y;
  }
}

function printBoard() {
  for (let x = Board.Top; x >= Board.Bottom; x--) {
    let line = '';
    for (let y = Board.Left; y <= Board.Right; y++) {
      isTale = false;
      if (x == Head.x && y == Head.y) {
        line += 'H';
        isTale = true;
      }
      for (let i = 0; i < Knots.length; i++) {
        const knot = Knots[i];
        if (!isTale && x == knot.x && y == knot.y) {
          line += i + 1;
          isTale = true;
          break;
        }
      }
      // } else if (TailVisited[x] && TailVisited[x][y]) {
      //   line += '#';
      if (!isTale) {
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

for (let k = 0; k < KnotsLength; k++) {
  Knots.push({ ...Knot });
}

lineReader.on('line', function (line) {
  const [direction, times] = line.split(' ');
  // console.log('+++++', direction, times, '+++++');
  for (let i = 0; i < parseInt(times); i++) {
    Cmd[direction](Head)
    Knots.forEach((knot, ki) => {
      head = ki === 0 ? Head : Knots[ki - 1];
      MoveTail(knot, head);
      // console.log('==== Knot ', ki + 1, ' ====');
      // printBoard()
    })
    // printBoard()

    const RopeTail = Knots[KnotsLength - 1];
    if (!TailVisited[RopeTail.x]) {
      TailVisited[RopeTail.x] = {};
    }
    TailVisited[RopeTail.x][RopeTail.y] = true;
  }
  // printBoard();
});

lineReader.on('close', function () {
  console.log(Object.values(TailVisited).reduce((acc, v) => acc + Object.values(v).length, 0));
});
