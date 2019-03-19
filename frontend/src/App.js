import React, { Component } from 'react';
import './App.css';

class App extends Component {
  componentDidMount() {
    fetch('http://10.0.1.13:8000/api/cat/')
      .then(res=>res.json())
      .then(json=>console.log(json))
  }

  render() {
    return (
      <div className="App">
        hi
      </div>
    );
  }
}

export default App;
