/**
 * @param {number[][]} mat
 * @return {number[][]}
 */
 var updateMatrix = function(mat) {
  let g = new Graph(mat.length * mat[0].length)
  
  let y = mat.length;
  let x = mat[0].length;

  // Put all vertices into our graph. O(N) operations, O(N) storage.
  let count = 0;
  for (let i = 0; i < y; i++) {
    for (let j = 0; j < x; j++) {
      g.addVertex(new Vertex(count, j, i, mat[i][j]))
      count += 1;
    }
  }
  console.log('done populating our vertices.')

  // Populate adjacency list O(N) Operations.
  count = 0;
  for (let i = 0; i < y; i++) {
    for (let j = 0; j < x; j++) {
      getAdjacentItems(j, i, mat).forEach(n => g.addEdge(count, n));
      count += 1;
    }
  }
  console.log('We are done building our adjacency list')
  
};


// Store our graph for later computation.
function Graph(noOfVertices, undirected = true) {
  console.log(`Creating a new graph with ${noOfVertices} vertices.`)
  this.noOfVertices = noOfVertices;
  this.AdjList = new Map();
  this.undirected = undirected;
 
  this.vertices = new Array(noOfVertices); 
  
  this.addVertex = (v) => {
    console.log(`Vertice: ${v}`)
    this.vertices[v.name] = v
    this.AdjList.set(v.name, []);  
  }
  
  this.addEdge = (v, w) => {
    this.AdjList.get(v).push(w); 
    console.log(`Added edge (${v}, ${w})`)
    // If we are undirected then add (w,v) as well.
    if (undirected) {
      // this.AdjList.get(w).push(v);
      // console.log(`Added edge (${w}, ${v})`)
    }
  }

  this.bfs = (starting_node) => {
    let visited = {};
    // TODO: WTF I have to implement my own queue? 
    let q = new Queue();
    q.enqueue(starting_node.name);
    let visited = {};
    
    while (!q.isEmpty) {
      let node = q.dequeue();
      let aList = this.AdjList.get(node);
      visited[node] = true;
      
      // Process our list.
      for (let i = 0; i < aList.length; i++) {
        let neighborName = aList[i];
        let neighborNode = this.vertices[neighborName];
        
        if (!visited[neighborName]) {
          
        }
      }
    }
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
function getAdjacentItems(x,y,mat) {
  const minY = 0;
  const maxY = mat.length - 1;
  
  const minX = 0;
  const maxX = mat[0].length - 1;  
  
  const isValidCoords = (coords) => {
    let validX = (coords.x >= minX && coords.x <= maxX)  
    let validY = (coords.y >= minY && coords.y <= maxY)  
    return (validX && validY)
  }
  
  // Check [U, D, L, R]
  const movements = [{x: x, y: y - 1}, {x: x, y: y + 1}, {x: x - 1, y: y}, {x: x + 1, y: y}];
  const validMovements = movements.filter(movement => isValidCoords(movement)).map(movement => (mat.length * movement.y + movement.x));
  console.log('Have valid movements.'); 
  return validMovements
}

function Queue() {
  let items = [];
  let head = 0;
  let tail = 0;

  this.enqueue = (i) => {
    items[tail] = i; 
    tail += 1;
  };
 
  this.dequeue = () => {
    let i = items[head];
    items.shift(); 
    tail = (tail -1 < 0) ? 0: tail - 1;
    return i;
  };

  this.isEmpty = () => {
    return items.length === 0;
  }

  this.getItems = () => {
    return items;
  }
}


// Test with the following...
// [[0,0,0],[0,1,0],[0,0,0]]