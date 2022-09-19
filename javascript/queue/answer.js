/**
 * @param {number[][]} mat
 * @return {number[][]}
 */
var updateMatrix = function (mat) {
  // Normally this is a undirected, however, due to the way im putting in all my vertex, i'm adding them all anyway.
  let g = new Graph(mat.length * mat[0].length, false);
  let y = mat.length;
  let x = mat[0].length;
  
  // Which of our nodes are zeroes.
  let zeroes = [];
 
  // Answer array.
  let ans = new Array(y);
  for (let i = 0; i < y; i++) {
    ans[i] = new Array(x).fill(null)
  }

  // Put all vertices into our graph. O(N) operations, O(N) storage.
  let start = new Date();
  console.time("ADD_VERTICES")
  let count = 0;
  for (let i = 0; i < y; i++) {
    for (let j = 0; j < x; j++) {
      g.addVertex(new Vertex(count, j, i, mat[i][j]));
      if (mat[i][j] === 0 ) {
        zeroes.push(count)
      }
      count += 1;
    }
  }
  console.timeEnd('ADD_VERTICES');

  // Populate adjacency list O(N) Operations.
  console.time('POPULATE_ADJLIST')
  count = 0;
  for (let i = 0; i < y; i++) {
    for (let j = 0; j < x; j++) {
      getAdjacentItems(j, i, mat).forEach((n) => g.addEdge(count, n));
      count += 1;
    }
  }
  console.timeEnd('POPULATE_ADJLIST')

  console.time("SEARCH")
  count = 0;
  for (let i = 0; i < y; i++) {
    for (let j = 0; j < x; j++) {
      if (mat[i][j] === 0) {
        ans[i][j] = 0;
      } 
      else {
        let distanceToZeroes = zeroes.map(z => g.bfs(count, z).length - 1)
        let minDistance = Math.min(...distanceToZeroes)
        ans[i][j] = minDistance; 
      }
      count += 1;
    }
  }
  console.timeEnd("SEARCH")

  return ans;

};

// Store our graph for later computation.
function Graph(noOfVertices, undirected = true) {
  this.AdjList = new Map();
  this.undirected = undirected;
  this.vertices = new Array(noOfVertices);

  // Add a vertex. 
  this.addVertex = (v) => {
    // console.log(`Vertice: ${v}`);
    this.vertices[v.name] = v;
    this.AdjList.set(v.name, []);
  };

  // Add an edge.
  this.addEdge = (v, w) => {
    this.AdjList.get(v).push(w);
    // console.log(`Added edge (${v}, ${w})`);
    if (undirected) {
      this.AdjList.get(w).push(v);
    }
  };

  // Returns previous nodes info.
  this.helper = (starting_node) => {
    console.log('CALLING HELPER at starting node: ', starting_node)
    let visited = new Array(noOfVertices).fill(false);
    let prev = new Array(noOfVertices).fill(null);
    let q = new Queue();
    q.enqueue(starting_node);
    console.log(`enqueued: ${starting_node}`)
    console.log(q.getItems())
    visited[starting_node] = true;
    
    while (!q.isEmpty()) {
      let node = q.dequeue();
      console.log(`while: dequeue: ${node}`)
      console.log(q.getItems())
      let aList = this.AdjList.get(node);
      // Process our list.
      for (let i = 0; i < aList.length; i++) {
        let nNode = aList[i];
        if (!visited[nNode]) {
          q.enqueue(nNode)
          console.log(`while: enqueued: ${nNode}`)
          console.log(q.getItems())
          visited[nNode] = true;
          prev[nNode] = node;  
        }
      }
    }

    return prev
  };

  const getPath = (prev, start, end) => {
    let path = [];
    for (let at = end; at != null; at = prev[at]){
      // console.log('Pushing: ', at)
      // path.push(prev[at])
      path.push(at)
    }

    path.reverse();

    if (path[0] === start) {
      return path;
    }
    return [];
  }

  // bfs from start to end.
  this.bfs = (start, end) => {
    console.log(`CALLING HELPER ${start} to ${end}`)
    return getPath(this.helper(start), start, end)
  }
}

// Vertex object.
function Vertex(name, x, y, value) {
  this.name = name;
  this.x = x;
  this.y = y;
  this.value = value;
}

// Get all immediately adjacent items in our matrix.
function getAdjacentItems(x, y, mat) {
  const minY = 0;
  const maxY = mat.length - 1;

  const minX = 0;
  const maxX = mat[0].length - 1;

  const isValidCoords = (coords) => {
    let validX = coords.x >= minX && coords.x <= maxX;
    let validY = coords.y >= minY && coords.y <= maxY;
    return validX && validY;
  };

  // const convertCoordsToNodeNumber = (x,y) => {
  //   console.log(`converting: ${x}, ${y}`)
  //   return (mat.length) * movement.y + movement.x
  // }

  // Check [U, D, L, R]
  const movements = [
    { x: x, y: y - 1 },
    { x: x, y: y + 1 },
    { x: x - 1, y: y },
    { x: x + 1, y: y },
  ];


  // .map((movement) => ((mat.length * movement.y) + movement.x));  Before adding - 1 to take into account out of bounds.
  const validMovements = movements.filter((movement) => isValidCoords(movement))
  const validDestinations = validMovements.map((movement) => ((movement.x + mat[0].length * movement.y)) );

  return validDestinations;
}

function Node(val = null, next = null) {
  this.val = val;
  this.next = next;  
}

function Queue() {
  let head = null;
  let tail = null;

  this.enqueue = (i) => {
    let temp = new Node(i);
    if (!tail) {
      head = temp;
      tail = head;
      return
    }
    
    tail.next = temp;
  };

  // OPTIMIZE: What is the run time of items.shift()?
  // Returns Node.val or null if our queue is empty. 
  this.dequeue = () => {
    console.log('Dequeue')
    if (!head) {
      return 
    }

    let temp = head;
    head = head.next;
    
    // If our head is null, make the rear null as well.
    if (!head) {
      tail = null;
    }
  
    // Return temp value
    return temp.val;
  };

  this.isEmpty = () => {
    return (!head);
  };

  this.getItems = () => {
    let p = head;
    let items = []
    while (p) {
      items.push(p.val)
      p = p.next
    }
    return items
  };
}

// TESTS FOR QUEUE
 let q = new Queue;
 console.log('Queue TEST: enque 0, dequeue 0, enqueue 1')

 q.enqueue(0);
console.log('after enque 0: ')
console.log(q.getItems())

console.log('dequeue hopefully the 0:')
console.log(q.dequeue());
console.log(q.getItems())

console.log('enqueue the 1, then 2:')
q.enqueue(1);
q.enqueue(2);

console.log(q.getItems())
console.log('dequeue 2 times')
q.dequeue();
q.dequeue();
console.log('is empty?: ', q.isEmpty())

console.log('dequeue 1 more, should be empty already though.')
q.dequeue();
console.log('is empty?: ', q.isEmpty())

// 
// console.log('DeQueue TEST: remove 1')
// console.log(q.dequeue())
// console.log('Items after dequeue.')
// console.log(q.getItems());
// 
// console.log('Queue TEST: add items [5,8]')
// q.enqueue(5);
// q.enqueue(6);
// q.enqueue(7);
// q.enqueue(8);
// console.log('Items after enqueue.')
// console.log(q.getItems());
// 
// 
// console.log('DeQueue a bunch TEST')
// console.log(q.dequeue());
// console.log(q.dequeue());
// console.log(q.dequeue());
// console.log(q.dequeue());
// console.log(q.dequeue());
// console.log(q.dequeue());
// console.log(q.dequeue());
// console.log(q.dequeue());
// console.log(q.dequeue());
// console.log(q.dequeue());
// console.log(q.dequeue());
// console.log(q.dequeue());
// console.log(q.dequeue());
// console.log(q.dequeue());
// console.log(q.dequeue());
// console.log(q.dequeue());
// console.log(q.dequeue());
// console.log(q.dequeue());
// console.log(q.dequeue());
// 
// console.log('Items after dequeue.')
// console.log(q.getItems());


// Test with the following...
// let t1 = [
//   [0, 0, 0],
//   [0, 1, 0],
//   [0, 0, 0],
// ];
// 
// let t2 = [[0],[0],[0],[0],[0]];
// let t3 = [[0], [1]]
// let t4 = [[1,1,1,1,1,0,1,0,1,0,1,0,1,1,0,1,1,1,0,1,1,1,0,1,1,1,1,0,1,1],[1,1,1,0,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,0,1,0,0,1],[1,1,1,1,0,1,0,0,1,1,0,1,1,0,1,1,1,0,1,0,1,0,0,1,0,1,0,1,1,1],[1,1,1,1,1,0,1,1,1,1,1,0,1,1,0,0,0,0,1,0,0,0,0,1,1,1,1,0,0,1],[0,1,0,0,1,0,0,1,1,1,0,1,1,1,1,1,0,1,0,1,1,1,1,1,0,1,1,1,0,1],[1,0,1,1,1,1,0,1,0,1,0,1,1,1,0,1,1,1,1,0,1,1,0,1,0,1,0,0,1,0],[1,1,0,1,1,0,0,0,1,1,0,0,0,1,0,1,1,1,1,1,0,1,0,1,1,0,1,1,1,1],[1,1,1,0,0,0,1,0,0,1,1,1,1,1,1,1,1,0,1,0,1,0,0,1,0,0,1,0,0,1],[0,1,1,0,1,1,1,0,1,0,1,1,0,1,1,1,1,0,1,0,1,1,1,1,1,0,0,1,0,1],[1,1,0,0,1,1,1,0,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,0,0,0,0,1,1],[1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,0,1,1,0,1,0,1,1,1,0],[1,1,1,1,0,1,0,0,0,1,1,1,0,1,1,1,0,1,0,1,1,1,0,1,0,1,1,1,1,1],[0,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,1,0,1,1,1,1,0,1,0,0,0,1],[0,1,1,0,0,0,1,1,0,0,0,0,1,1,0,1,1,1,1,1,1,1,0,1,0,0,1,1,1,1],[1,1,1,1,0,0,1,1,1,0,0,1,1,0,1,1,1,0,0,1,1,0,1,0,0,0,0,1,1,1],[1,1,1,1,0,1,1,0,1,1,0,1,1,1,1,1,1,1,0,0,0,0,1,1,0,0,1,0,0,0],[1,1,0,1,1,0,0,1,1,0,0,1,0,1,1,1,1,0,1,1,1,0,1,1,0,1,0,1,0,1],[1,0,0,0,1,1,1,0,1,1,1,1,0,0,1,1,1,0,1,1,0,1,0,0,1,1,1,1,1,0],[1,1,0,1,0,1,1,0,0,1,1,0,0,1,0,1,1,1,1,1,1,0,1,0,0,0,0,1,1,1],[1,1,1,0,1,0,1,0,1,0,1,0,1,1,0,1,0,0,1,1,1,0,1,1,0,1,0,1,1,0],[1,0,0,1,1,1,1,0,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,1,1,0,1,1],[0,1,1,1,1,0,1,1,0,1,1,1,1,1,1,0,1,0,0,1,0,1,1,0,1,1,0,1,0,1],[1,1,1,0,1,1,1,0,0,1,0,0,0,1,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1,1],[1,1,0,0,1,1,1,1,0,0,1,0,0,1,1,0,0,1,1,1,1,0,1,1,0,1,1,1,1,1],[0,0,0,1,1,1,1,1,1,0,1,1,1,0,0,1,1,1,1,1,1,1,0,1,0,0,0,1,1,0],[1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,0,1,1,1,1,0,1,0,0,0,0,0,1,1,1],[1,0,1,1,0,1,1,0,1,0,1,1,1,0,1,1,1,1,1,0,1,0,0,1,1,0,0,1,1,0],[1,1,1,0,0,1,1,1,1,0,1,0,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,0,0,1,1,1],[0,1,1,0,1,1,0,0,1,0,1,1,1,1,0,0,1,1,1,1,1,1,0,0,0,1,1,0,1,0]]
// 
// console.log('Running update matrix: ')
// console.log(updateMatrix(t1));
// console.log(updateMatrix(t4));
