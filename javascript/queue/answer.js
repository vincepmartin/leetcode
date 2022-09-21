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
  // console.log(`Creating a new graph with ${noOfVertices} vertices.`);
  // TODO: REMOVE ME...this.noOfVertices = noOfVertices;
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
    let visited = new Array(noOfVertices).fill(false);
    let prev = new Array(noOfVertices).fill(null);
    let q = new Queue();
    q.enqueue(starting_node);
    visited[starting_node] = true;
    
    while (!q.isEmpty()) {
      let node = q.dequeue();
      let aList = this.AdjList.get(node);
      // Process our list.
      for (let i = 0; i < aList.length; i++) {
        let nNode = aList[i];
        if (!visited[nNode]) {
          q.enqueue(nNode)
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
  this.bfs = (start, end) => getPath(this.helper(start), start, end)
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
  // console.log("Have valid movements.");
  // return validMovements 

  return validDestinations;
}

function Queue() {
  let items = [];
  let head = 0;
  let tail = 0;

  this.enqueue = (i) => {
    items[tail] = i;
    tail += 1;
  };

  // OPTIMIZE: What is the run time of items.shift()?
  this.dequeue = () => {
    let i = items[head];
    items.shift();
    tail = tail - 1 < 0 ? 0 : tail - 1;
    return i;
  };

  this.isEmpty = () => {
    return items.length === 0;
  };

  this.getItems = () => {
    return items;
  };
}

// Test with the following...
let t1 = [
  [0, 0, 0],
  [0, 1, 0],
  [0, 0, 0],
];

let t2 = [[0],[0],[0],[0],[0]];

let t3 = [[0], [1]]
let t4 = [[1,1,1,1,1,0,1,0,1,0,1,0,1,1,0,1,1,1,0,1,1,1,0,1,1,1,1,0,1,1],[1,1,1,0,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,0,1,0,0,1],[1,1,1,1,0,1,0,0,1,1,0,1,1,0,1,1,1,0,1,0,1,0,0,1,0,1,0,1,1,1],[1,1,1,1,1,0,1,1,1,1,1,0,1,1,0,0,0,0,1,0,0,0,0,1,1,1,1,0,0,1],[0,1,0,0,1,0,0,1,1,1,0,1,1,1,1,1,0,1,0,1,1,1,1,1,0,1,1,1,0,1],[1,0,1,1,1,1,0,1,0,1,0,1,1,1,0,1,1,1,1,0,1,1,0,1,0,1,0,0,1,0],[1,1,0,1,1,0,0,0,1,1,0,0,0,1,0,1,1,1,1,1,0,1,0,1,1,0,1,1,1,1],[1,1,1,0,0,0,1,0,0,1,1,1,1,1,1,1,1,0,1,0,1,0,0,1,0,0,1,0,0,1],[0,1,1,0,1,1,1,0,1,0,1,1,0,1,1,1,1,0,1,0,1,1,1,1,1,0,0,1,0,1],[1,1,0,0,1,1,1,0,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,0,0,0,0,1,1],[1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,0,1,1,0,1,0,1,1,1,0],[1,1,1,1,0,1,0,0,0,1,1,1,0,1,1,1,0,1,0,1,1,1,0,1,0,1,1,1,1,1],[0,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,1,0,1,1,1,1,0,1,0,0,0,1],[0,1,1,0,0,0,1,1,0,0,0,0,1,1,0,1,1,1,1,1,1,1,0,1,0,0,1,1,1,1],[1,1,1,1,0,0,1,1,1,0,0,1,1,0,1,1,1,0,0,1,1,0,1,0,0,0,0,1,1,1],[1,1,1,1,0,1,1,0,1,1,0,1,1,1,1,1,1,1,0,0,0,0,1,1,0,0,1,0,0,0],[1,1,0,1,1,0,0,1,1,0,0,1,0,1,1,1,1,0,1,1,1,0,1,1,0,1,0,1,0,1],[1,0,0,0,1,1,1,0,1,1,1,1,0,0,1,1,1,0,1,1,0,1,0,0,1,1,1,1,1,0],[1,1,0,1,0,1,1,0,0,1,1,0,0,1,0,1,1,1,1,1,1,0,1,0,0,0,0,1,1,1],[1,1,1,0,1,0,1,0,1,0,1,0,1,1,0,1,0,0,1,1,1,0,1,1,0,1,0,1,1,0],[1,0,0,1,1,1,1,0,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,1,1,0,1,1],[0,1,1,1,1,0,1,1,0,1,1,1,1,1,1,0,1,0,0,1,0,1,1,0,1,1,0,1,0,1],[1,1,1,0,1,1,1,0,0,1,0,0,0,1,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1,1],[1,1,0,0,1,1,1,1,0,0,1,0,0,1,1,0,0,1,1,1,1,0,1,1,0,1,1,1,1,1],[0,0,0,1,1,1,1,1,1,0,1,1,1,0,0,1,1,1,1,1,1,1,0,1,0,0,0,1,1,0],[1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,0,1,1,1,1,0,1,0,0,0,0,0,1,1,1],[1,0,1,1,0,1,1,0,1,0,1,1,1,0,1,1,1,1,1,0,1,0,0,1,1,0,0,1,1,0],[1,1,1,0,0,1,1,1,1,0,1,0,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,0,0,1,1,1],[0,1,1,0,1,1,0,0,1,0,1,1,1,1,0,0,1,1,1,1,1,1,0,0,0,1,1,0,1,0]]

console.log('Running update matrix: ')
// console.log(updateMatrix(t1));
console.log(updateMatrix(t1));
