import React, { Component } from 'react';
import './App.css';

class Footer extends Component {
  render () {
    return (
      <footer>
        <p>Posted by: Claudio</p>
        <p>Contact information: <a href="mailto:claudio.rdgz@gmail.com">
        claudio.rdgz@gmail.com</a>.</p>
      </footer>
    );
  }
}

class Header extends Component {
  render() {
    return (
      <header>
        <h1>
          Dogs Data
        </h1>
        <p>A set of tools to crawl data from dogs and save it to files </p>
      </header>
    );
  }
}

class Main extends Component {
  render() {
    return (
      <main>
        <section>
          <h2>
            Setup
          </h2>
          <p>
            This project uses Python 3, to use I recommend <code>pyvenv</code>
          </p>
          <pre>
          <code>
  {`
    $ sudo apt install python3-venv
    $ pyvenv env
    $ source env/bin/activate
  `}
          </code>
          </pre>
        </section>
      </main>
    );
  }
}

class App extends Component {
  render() {
    return (
      <div className="app">
        <Header />
        <Main />
        <Footer />
      </div>
    );
  }
}

export default App;
