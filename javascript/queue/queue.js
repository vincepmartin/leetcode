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

console.log('Queue test')
let q = new Queue();
console.log(q);
q.enqueue('a');
q.enqueue('b');
q.enqueue('c');
let nachos = q.dequeue();
console.log(q.getItems());
console.log(nachos);
q.enqueue('d');
console.log(q.getItems());
q.dequeue();
q.dequeue();
q.dequeue();
q.dequeue();
console.log(q.dequeue());
console.log(q.dequeue());
console.log(q.dequeue());
console.log(q.getItems());
q.enqueue('z');
console.log(q.getItems());
