class MyQueue {
  constructor() {
    /*
    Initialize your data structure here.
    */
    this.stack1 = [];
    this.stack2 = [];
  }

  push(x) {
    /*
    Push element x to the back of queue.
    */
    this.stack1.push(x);
  }

  pop() {
    /*
    Removes the element from in front of queue and returns that element.
    */
    var n, res;
    n = this.stack1.length - 1;

    for (var i = 0, _pj_a = n; i < _pj_a; i += 1) {
      this.stack2.push(this.stack1.pop());
    }

    res = this.stack1.pop();

    for (var i = 0, _pj_a = n; i < _pj_a; i += 1) {
      this.stack1.push(this.stack2.pop());
    }

    return res;
  }

  peek() {
    /*
    Get the front element.
    */
    var n, res;
    n = this.stack1.length - 1;

    for (var i = 0, _pj_a = n; i < _pj_a; i += 1) {
      this.stack2.push(this.stack1.pop());
    }

    res = this.stack1[0];

    for (var i = 0, _pj_a = n; i < _pj_a; i += 1) {
      this.stack1.push(this.stack2.pop());
    }

    return res;
  }

  empty() {
    /*
    Returns whether the queue is empty.
    */
    return this.stack1.length === 0;
  }

}
