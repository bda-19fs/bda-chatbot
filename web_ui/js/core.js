let ask = function(question, config) {
  return postData('//localhost:7001/api/v1/run', {
      question: question,
      config: config
    })
    .then(response => response.json());
}

let pipelines = function() {
  return fetch('//localhost:7001/api/v1/pipelines')
    .then(response => response.json());
}

let postData = function(url = '', data = {}) {
    return fetch(url, {
        method: 'POST',
        mode: 'cors',
        cache: 'no-cache',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data),
    });
}

let ask_question = function() {
  question = document.querySelector('#question').value;
  ask(question, '').then(data => console.log(JSON.stringify(data)));
}

// demo
pipelines().then(data => console.log(JSON.stringify(data)));
ask('How old am I?', 0).then(data => console.log(JSON.stringify(data)));
